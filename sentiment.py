from textblob import TextBlob

text = input("Enter a sentence to analyze: ")
blob = TextBlob(text)

print("\nSentiment Analysis:")
print("Polarity:", blob.sentiment.polarity)
print("Subjectivity:", blob.sentiment.subjectivity)

# Optional: basic interpretation
if blob.sentiment.polarity > 0:
    print("This is a positive sentence.")
elif blob.sentiment.polarity < 0:
    print("This is a negative sentence.")
else:
    print("This is a neutral sentence.")
