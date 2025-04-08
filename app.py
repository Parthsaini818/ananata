import av
import cv2
import streamlit as st
from streamlit_webrtc import webrtc_streamer, VideoProcessorBase, WebRtcMode
import mediapipe as mp
import numpy as np
from gesture_config import GESTURE_MAP, PHRASE_MAP, GESTURE_CONFIDENCE
import logging
import os
import time
from collections import deque

# Configure environment
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'
logging.getLogger('aioice').setLevel(logging.ERROR)

# Initialize MediaPipe
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles

class HandGestureProcessor(VideoProcessorBase):
    def __init__(self) -> None:
        super().__init__()
        self.hands = mp_hands.Hands(
            static_image_mode=False,
            max_num_hands=1,
            min_detection_confidence=GESTURE_CONFIDENCE['min_detection_confidence'],
            min_tracking_confidence=GESTURE_CONFIDENCE['min_tracking_confidence']
        )
        self.prev_gesture = None
        self.gesture_streak = 0
        self.sentence = []
        self.current_phrase = []
        self.last_update_time = time.time()
        self.debug_info = {}
        self.gesture_history = deque(maxlen=10)  # Track recent gestures
        self.phrase_mode = False
        self.phrase_in_progress = None

    def get_finger_states(self, landmarks):
        """Improved finger state detection"""
        finger_states = []
        
        # Thumb
        thumb_tip = landmarks[4]
        thumb_ip = landmarks[3]
        thumb_extended = thumb_tip.x < thumb_ip.x - 0.05
        finger_states.append(1 if thumb_extended else 0)
        
        # Other fingers
        tips_ids = [8, 12, 16, 20]  # Index, Middle, Ring, Pinky
        pip_ids = [6, 10, 14, 18]   # PIP joints
        
        for tip_id, pip_id in zip(tips_ids, pip_ids):
            tip = landmarks[tip_id]
            pip = landmarks[pip_id]
            finger_extended = tip.y < pip.y - 0.05
            finger_states.append(1 if finger_extended else 0)
            
        return tuple(finger_states)

    def update_display(self, img, gesture_data):
        """Enhanced visual feedback with phrase detection"""
        # Display current gesture
        cv2.putText(
            img, f"Gesture: {gesture_data['text']}", 
            (50, 80),
            cv2.FONT_HERSHEY_SIMPLEX, 0.8, 
            (0, 255, 255), 2, cv2.LINE_AA
        )
        
        # Display current phrase construction
        phrase_text = " ".join([g["text"] for g in self.current_phrase])
        cv2.putText(
            img, f"Phrase: {phrase_text}", 
            (50, 130),
            cv2.FONT_HERSHEY_SIMPLEX, 0.8, 
            (255, 255, 255), 2, cv2.LINE_AA
        )
        
        # Display full sentence
        sentence_text = " ".join(self.sentence)
        cv2.putText(
            img, f"Sentence: {sentence_text}", 
            (50, 180),
            cv2.FONT_HERSHEY_SIMPLEX, 0.7, 
            (200, 200, 255), 1, cv2.LINE_AA
        )
        
        # Display detected phrase if applicable
        if self.phrase_in_progress:
            cv2.putText(
                img, f"Detected Phrase: {self.phrase_in_progress}", 
                (50, 230),
                cv2.FONT_HERSHEY_SIMPLEX, 0.8, 
                (0, 255, 0), 2, cv2.LINE_AA
            )

    def detect_phrase(self):
        """Check if recent gestures match any predefined phrases"""
        gesture_sequence = [g["text"] for g in self.current_phrase]
        for phrase, sequence in PHRASE_MAP.items():
            if gesture_sequence == sequence:
                return phrase
        return None

    def process_gesture(self, gesture_data):
        """Handle gesture actions with phrase support"""
        current_time = time.time()
        
        # Ignore if too soon since last update
        if current_time - self.last_update_time < 0.3:
            return
            
        self.last_update_time = current_time
        
        # Handle control gestures
        if gesture_data["type"] == "control":
            if gesture_data["text"] == "Clear":
                self.sentence = []
                self.current_phrase = []
                self.phrase_in_progress = None
            elif gesture_data["text"] == "Enter":
                # Check for complete phrase first
                detected_phrase = self.detect_phrase()
                if detected_phrase:
                    self.sentence.append(detected_phrase)
                    self.current_phrase = []
                    self.phrase_in_progress = None
                elif self.current_phrase:
                    self.sentence.append(" ".join([g["text"] for g in self.current_phrase]))
                    self.current_phrase = []
        else:
            # Add to current phrase
            self.current_phrase.append(gesture_data)
            # Check for phrase completion after each gesture
            self.phrase_in_progress = self.detect_phrase()

# Streamlit UI
st.set_page_config(
    page_title="ASL Word Recognition",
    layout="wide"
)

st.title("👋 Sign Language Word & Phrase Recognition")
st.markdown("""
    <style>
    .gesture-card {
        padding: 15px;
        border-radius: 10px;
        background-color: #f0f2f6;
        margin: 10px 0;
    }
    </style>
""", unsafe_allow_html=True)

col1, col2 = st.columns([2, 1])

with col1:
    st.header("Live Recognition")
    st.write("Show gestures to your webcam to build sentences and phrases")

with col2:
    with st.expander("Available Words & Phrases"):
        st.markdown("""
        ### Single-Gesture Words:
        - Hello 👋
        - Hi
        - Thank You
        - Please
        - Good
        - Morning
        - Afternoon
        
        ### Multi-Gesture Phrases:
        - How are you
        - Good morning
        - Good afternoon
        - My name is
        """)

webrtc_ctx = webrtc_streamer(
    key="word-recognition",
    video_processor_factory=HandGestureProcessor,
    rtc_configuration={"iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]},
    media_stream_constraints={
        "video": {"width": 640, "height": 480, "facingMode": "user"},
        "audio": False
    },
    async_processing=True
)
    
if not webrtc_ctx.state.playing:
    st.info("Please allow camera access to begin")
    st.warning("For best results:")
    st.write("- Use consistent hand positioning")
    st.write("- Hold each gesture for 1 second")
    st.write("- Ensure good lighting conditions")