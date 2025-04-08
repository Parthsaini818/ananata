
GESTURE_MAP = {
    
}

# Format: (thumb, index, middle, ring, pinky) : {"text": "Display Text", "speech": "Spoken Text", "type": "word/letter/punctuation"}
GESTURE_MAP = {
    # Letters (ASL inspired)
    (0, 0, 0, 0, 0): {"text": "Fist 👊", "speech": "Fist detected!"},
    (1, 1, 1, 1, 1): {"text": "Open Palm ✋", "speech": "Open palm visible"},
    (1, 0, 0, 0, 0): {"text": "Thumbs Up 👍", "speech": "Great job! Thumbs up!"},
    (0, 1, 1, 0, 0): {"text": "Victory ✌", "speech": "Victory!"},
    (0, 1, 0, 0, 0): {"text": "Pointing ☝", "speech": "You're pointing at something"},
    (1, 1, 0, 0, 1): {"text": "I Love You! ❤️", "speech": "I love you"},
    (0, 0, 0, 0, 1): {"text": "Pinky Promise 🤙", "speech": "I promise!"},
    (1, 0, 0, 0, 1): {"text": "Call Me! 📞", "speech": "Call me later"},
    (1, 1, 1, 0, 0): {"text": "Three! 3️⃣", "speech": "Number three"},
    (0, 1, 1, 1, 1): {"text": "Four! 4️⃣", "speech": "Number four"},
    (1, 0, 1, 0, 1): {"text": "Rock On! 🤘", "speech": "Rock and roll!"},
    (1, 1, 0, 0, 0): {"text": "A", "speech": "A", "type": "letter"},
    (0, 1, 1, 1, 1): {"text": "B", "speech": "B", "type": "letter"},
    (0, 1, 1, 0, 0): {"text": "C", "speech": "C", "type": "letter"},
    (0, 1, 0, 0, 0): {"text": "D", "speech": "D", "type": "letter"},
    (1, 1, 1, 1, 1): {"text": "E", "speech": "E", "type": "letter"},
    (0, 0, 0, 0, 1): {"text": "I", "speech": "I", "type": "letter"},
    (1, 0, 0, 0, 1): {"text": "K", "speech": "K", "type": "letter"},
    (1, 1, 1, 0, 0): {"text": "L", "speech": "L", "type": "letter"},
    (0, 0, 0, 0, 0): {"text": "M", "speech": "M", "type": "letter"},
    (1, 0, 0, 0, 0): {"text": "N", "speech": "N", "type": "letter"},
    (0, 1, 1, 1, 0): {"text": "O", "speech": "O", "type": "letter"},
    (1, 0, 1, 0, 1): {"text": "R", "speech": "R", "type": "letter"},
    (0, 0, 1, 1, 1): {"text": "U", "speech": "U", "type": "letter"},
    (0, 1, 0, 0, 1): {"text": "V", "speech": "V", "type": "letter"},
    (1, 1, 0, 0, 1): {"text": "W", "speech": "W", "type": "letter"},
    (1, 0, 1, 1, 1): {"text": "Y", "speech": "Y", "type": "letter"},

    # Common Words
    (1, 0, 0, 1, 1): {"text": "Hello", "speech": "Hello", "type": "word"},
    (0, 1, 1, 0, 1): {"text": "Class", "speech": "Class", "type": "word"},
    (1, 1, 0, 1, 0): {"text": "Name", "speech": "Name", "type": "word"},
    (0, 0, 1, 0, 0): {"text": "My", "speech": "My", "type": "word"},
    (1, 0, 1, 0, 0): {"text": "Is", "speech": "Is", "type": "word"},
    (0, 1, 0, 1, 0): {"text": "Thank You", "speech": "Thank you", "type": "word"},
    (1, 0, 0, 1, 0): {"text": "Please", "speech": "Please", "type": "word"},
    (0, 0, 1, 0, 1): {"text": "Good", "speech": "Good", "type": "word"},
    (1, 1, 1, 1, 0): {"text": "Morning", "speech": "Morning", "type": "word"},
    (0, 1, 1, 1, 1): {"text": "Afternoon", "speech": "Afternoon", "type": "word"},

    # Punctuation/Controls
    (1, 1, 0, 0, 0): {"text": ".", "speech": ".", "type": "punctuation"},
    (0, 0, 0, 1, 1): {"text": ",", "speech": ",", "type": "punctuation"},
    (1, 0, 1, 1, 0): {"text": "?", "speech": "?", "type": "punctuation"},
    (0, 1, 0, 1, 1): {"text": "Space", "speech": " ", "type": "punctuation"},
    (1, 1, 1, 0, 1): {"text": "Clear", "speech": "", "type": "control"},
    (0, 0, 1, 1, 0): {"text": "Enter", "speech": "\n", "type": "control"},
}

# Common phrases that can be constructed from these gestures
COMMON_PHRASES = {
    "Hello Class": ["Hello", "Space", "Class"],
    "My name is": ["My", "Space", "Name", "Space", "Is", "Space"],
    "Thank you": ["Thank You"],
    "Good morning": ["Good", "Space", "Morning"],
    "Good afternoon": ["Good", "Space", "Afternoon"],
}
# Enhanced gesture configuration with words and phrases
GESTURE_MAP = {
    # Letters (ASL)
    (0, 0, 0, 0, 0): {"text": "A", "type": "letter"},
    (0, 1, 1, 1, 1): {"text": "B", "type": "letter"},
    (0, 1, 1, 0, 0): {"text": "C", "type": "letter"},
    (0, 1, 0, 0, 0): {"text": "D", "type": "letter"},
    (1, 1, 1, 1, 1): {"text": "E", "type": "letter"},
    (0, 0, 0, 0, 1): {"text": "I", "type": "letter"},
    (1, 0, 0, 0, 1): {"text": "K", "type": "letter"},
    (1, 1, 1, 0, 0): {"text": "L", "type": "letter"},
    (0, 1, 1, 1, 0): {"text": "O", "type": "letter"},
    (1, 0, 1, 0, 1): {"text": "R", "type": "letter"},
    (0, 0, 1, 1, 1): {"text": "U", "type": "letter"},
    (0, 1, 0, 0, 1): {"text": "V", "type": "letter"},
    (1, 1, 0, 0, 1): {"text": "W", "type": "letter"},
    (1, 0, 1, 1, 1): {"text": "Y", "type": "letter"},

    # Words (single-gesture words)
    (1, 0, 0, 1, 1): {"text": "Hello", "type": "word"},
    (0, 1, 1, 0, 1): {"text": "Hi", "type": "word"},
    (1, 1, 0, 1, 0): {"text": "Name", "type": "word"},
    (0, 0, 1, 0, 0): {"text": "My", "type": "word"},
    (1, 0, 1, 0, 0): {"text": "Is", "type": "word"},
    (0, 1, 0, 1, 0): {"text": "Thank You", "type": "word"},
    (1, 0, 0, 1, 0): {"text": "Please", "type": "word"},
    (0, 0, 1, 0, 1): {"text": "Good", "type": "word"},
    (1, 1, 1, 1, 0): {"text": "Morning", "type": "word"},
    (0, 1, 1, 1, 1): {"text": "Afternoon", "type": "word"},
    (1, 1, 0, 0, 0): {"text": "How", "type": "word"},
    (0, 0, 0, 1, 1): {"text": "Are", "type": "word"},
    (1, 0, 1, 1, 0): {"text": "You", "type": "word"},

    # Controls
    (1, 1, 1, 0, 1): {"text": "Clear", "type": "control"},
    (0, 0, 1, 1, 0): {"text": "Enter", "type": "control"},
    (0, 1, 0, 1, 1): {"text": "Space", "type": "punctuation"},
}

# Phrase construction mapping
PHRASE_MAP = {
    "How are you": ["How", "Space", "Are", "Space", "You"],
    "Good morning": ["Good", "Space", "Morning"],
    "Good afternoon": ["Good", "Space", "Afternoon"],
    "My name is": ["My", "Space", "Name", "Space", "Is"],
    "Thank you": ["Thank You"],
    "Hello": ["Hello"],
    "Hi": ["Hi"],
}

# Confidence thresholds
GESTURE_CONFIDENCE = {
    'min_detection_confidence': 0.8,
    'min_tracking_confidence': 0.5,
    'min_streak_for_recognition': 5,
    'phrase_delay_seconds': 1.5  # Time between gestures in a phrase
}