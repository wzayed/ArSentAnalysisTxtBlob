from textblob import TextBlob
from textblob_ar import TextBlobAR

# Sample Arabic text
arabic_text = "المطعم جيد"

# Create a TextBlobAR object
blob = TextBlobAR(arabic_text)

# Tokenization
tokens = blob.words
print("Tokens:", tokens)

# Sentiment Analysis
sentiment = blob.sentiment
print("Sentiment:", sentiment)