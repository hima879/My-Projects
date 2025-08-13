# Importing the TextBlob library for sentiment analysis
# TextBlob helps in understanding the sentiment (positive/negative/neutral) and subjectivity of a text.
from textblob import TextBlob

# Take a sentence from the user as input
text = input("Enter a sentence: ")

# Create a TextBlob object from the entered text
# This object can analyze the text's sentiment, detect language, correct spelling, etc.
blob = TextBlob(text)

# ---------------- SENTIMENT ANALYSIS ----------------

# First, check the "polarity" of the sentence:
# Polarity ranges from -1 (very negative) to +1 (very positive)
if blob.sentiment.polarity > 0:
    print("🌞 Yay! That sounds nice!")  # Positive message
elif blob.sentiment.polarity < 0:
    print("💔 Oh no, that sounds sad!")  # Negative message
else:
    # If polarity is exactly 0, we consider it "neutral"
    # But we will check for special neutral cases (like greetings, questions, thanks, yes/no)
    
    # Convert the text to lowercase for easier matching
    lowered = text.lower()
    
    # Check for greetings
    if any(greet in lowered for greet in ["hi", "hello", "hey"]):
        print("👋 Hey there!")
    
    # Check if the sentence is a question
    elif "?" in text:
        print("🤔 Sounds like you’re asking something.")
    
    # Check for gratitude words
    elif any(word in lowered for word in ["thanks", "thank you"]):
        print("🙏 You're welcome!")
    
    # Check if the reply is affirmative (yes)
    elif lowered in ["yes", "yep", "yeah"]:
        print("👍 Got it!")
    
    # Check if the reply is negative (no)
    elif lowered in ["no", "nope"]:
        print("🙅 Okay, no worries.")
    
    # If subjectivity is less than 0.2, it means the statement is more factual than opinion-based
    elif blob.sentiment.subjectivity < 0.2:
        print("📊 That seems like a fact.")
    
    # If none of the above match, we don't know the emotion
    else:
        print("🤷 Hmm, I can’t tell how you feel.")

#This program tells how the user is feeling 
