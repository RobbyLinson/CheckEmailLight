from transformers import pipeline

classifier = pipeline(
    "sentiment-analysis",
    model="cardiffnlp/twitter-roberta-base-sentiment-latest",
)


def analyze_sentiment(email_text: str):
    result = classifier(email_text, truncation=True, max_length=512)[0]
    return result
