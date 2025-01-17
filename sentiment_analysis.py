import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

# Download required resources
nltk.download('vader_lexicon')

def analyze_sentiment(text):
    """
    Analyze the sentiment of the given text.

    Parameters:
        text (str): The input text to analyze.

    Returns:
        dict: Sentiment scores (positive, neutral, negative, and compound).
    """
    sia = SentimentIntensityAnalyzer()
    sentiment_scores = sia.polarity_scores(text)
    return sentiment_scores

def main():
    print("Sentiment Analysis Tool")
    print("Type 'exit' to quit.")
    
    while True:
        user_input = input("\nEnter text: ")
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break

        # Analyze the sentiment of the input text
        scores = analyze_sentiment(user_input)
        
        # Display the results
        print("\nSentiment Scores:")
        for key, value in scores.items():
            print(f"{key.capitalize()}: {value}")

        # Overall sentiment label
        if scores['compound'] >= 0.05:
            print("\nOverall Sentiment: Positive")
        elif scores['compound'] <= -0.05:
            print("\nOverall Sentiment: Negative")
        else:
            print("\nOverall Sentiment: Neutral")

if __name__ == "__main__":
    main()
