import os
import base64

USE_LIVE_GMAIL = True  # flip to True for real inbox, False for mock demo


def get_emails():
    if USE_LIVE_GMAIL:
        return _get_unread_primary_emails()
    else:
        from data.sample_emails import SAMPLE_EMAILS
        return SAMPLE_EMAILS


def _get_unread_primary_emails(max_results=20):
    from google.oauth2.credentials import Credentials
    from google.auth.transport.requests import Request
    from googleapiclient.discovery import build

    creds = Credentials(
        token=None,
        refresh_token=os.getenv("GOOGLE_REFRESH_TOKEN"),
        client_id=os.getenv("GOOGLE_CLIENT_ID"),
        client_secret=os.getenv("GOOGLE_CLIENT_SECRET"),
        token_uri="https://oauth2.googleapis.com/token",
        scopes=["https://www.googleapis.com/auth/gmail.readonly"],
    )
    creds.refresh(Request())

    service = build("gmail", "v1", credentials=creds)

    results = service.users().messages().list(
        userId="me",
        q="is:unread category:primary",
        maxResults=max_results,
    ).execute()

    messages = results.get("messages", [])
    emails = []

    for msg in messages:
        msg_data = service.users().messages().get(
            userId="me",
            id=msg["id"],
            format="full",
        ).execute()

        headers = msg_data["payload"]["headers"]
        sender = next((h["value"] for h in headers if h["name"] == "From"), "Unknown")
        subject = next((h["value"] for h in headers if h["name"] == "Subject"), "(no subject)")
        body = _extract_body(msg_data["payload"])

        emails.append({"sender": sender, "subject": subject, "body": body})

    return emails


def _extract_body(payload):
    """Recursively extract plain-text body from a Gmail message payload."""
    if "parts" in payload:
        for part in payload["parts"]:
            if part["mimeType"] == "text/plain":
                data = part.get("body", {}).get("data", "")
                if data:
                    return base64.urlsafe_b64decode(data).decode("utf-8", errors="replace")
            if "parts" in part:
                result = _extract_body(part)
                if result:
                    return result
    data = payload.get("body", {}).get("data", "")
    if data:
        return base64.urlsafe_b64decode(data).decode("utf-8", errors="replace")
    return ""
