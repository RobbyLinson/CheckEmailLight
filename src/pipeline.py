from src.briefing import generate_briefing
from src.sentiment import analyze_sentiment
from src.sender import send_digest
from src.notify import show_light
from src.gmail import get_emails


def pipeline():
    emails = get_emails()

    analyzed = []
    for email in emails:
        sentiment_result = analyze_sentiment(email["body"])
        analyzed.append({
            "sender": email["sender"],
            "subject": email["subject"],
            "body": email["body"],
            "sentiment": sentiment_result,
        })

    digest = generate_briefing(analyzed)
    show_light(digest)
    send_digest(digest)
