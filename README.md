# Sentiment-Analysis-Tool

This Python script provides a simple tool to analyze the sentiment of user-provided text using the Natural Language Toolkit (nltk). It utilizes the `SentimentIntensityAnalyzer` from the `nltk` library, which uses the VADER (Valence Aware Dictionary and sEntiment Reasoner) lexicon to perform sentiment analysis.

## Features
- Analyzes text sentiment and provides detailed scores for:
  - Positive
  - Neutral
  - Negative
  - Compound (overall sentiment score)
- Classifies the overall sentiment as **Positive**, **Neutral**, or **Negative** based on the compound score.
- User-friendly interactive command-line interface.

## Requirements
- Python 3.6 or higher
- The following Python packages:
  - `nltk`

## Setup

1. Clone this repository or download the script:
   ```bash
   git clone https://github.com/Real-J/sentiment-analysis-tool.git
   cd sentiment-analysis-tool
   ```

2. Install the required packages using `pip`:
   ```bash
   pip install nltk
   ```

3. Run the script to download the VADER lexicon:
   ```bash
   python sentiment_analysis.py
   ```
   The script will automatically download the required `vader_lexicon` resource.

## Usage

1. Run the script:
   ```bash
   python sentiment_analysis.py
   ```

2. Enter text when prompted. The script will return sentiment scores and classify the overall sentiment.

3. To exit the tool, type `exit`.

### Example

```bash
Sentiment Analysis Tool
Type 'exit' to quit.

Enter text: I love this product!

Sentiment Scores:
Positive: 0.669
Neutral: 0.331
Negative: 0.0
Compound: 0.7783

Overall Sentiment: Positive

Enter text: This is the worst experience ever.

Sentiment Scores:
Positive: 0.0
Neutral: 0.357
Negative: 0.643
Compound: -0.8074

Overall Sentiment: Negative

Enter text: exit
Goodbye!
```

### Results

Below are some example results of the sentiment analysis:

| Text                              | Positive | Neutral | Negative | Compound | Overall Sentiment |
|-----------------------------------|----------|---------|----------|----------|-------------------|
| I love this product!              | 0.669    | 0.331   | 0.0      | 0.7783   | Positive          |
| This is the worst experience ever.| 0.0      | 0.357   | 0.643    | -0.8074  | Negative          |
| The movie was okay, not great.    | 0.0      | 0.873   | 0.127    | -0.296   | Neutral           |
| Amazing performance by the team!  | 0.795    | 0.205   | 0.0      | 0.9243   | Positive          |
| I don’t like this at all.         | 0.0      | 0.643   | 0.357    | -0.4767  | Negative          |

## How It Works
The script:
1. Prompts the user to enter text input.
2. Analyzes the sentiment using `SentimentIntensityAnalyzer`.
3. Outputs the sentiment scores (positive, neutral, negative, compound).
4. Classifies the overall sentiment as Positive, Neutral, or Negative based on the compound score:
   - Compound ≥ 0.05: Positive
   - Compound ≤ -0.05: Negative
   - Otherwise: Neutral

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Contributing
Contributions are welcome! Feel free to open issues or submit pull requests to improve the functionality or fix bugs.

## Acknowledgments
- The VADER lexicon was developed by C.J. Hutto and Eric Gilbert. Read more about it in their [paper](https://ojs.aaai.org/index.php/ICWSM/article/view/14550).

---

Enjoy analyzing sentiments with this tool! 😊

