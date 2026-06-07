import os
import resend
from dotenv import load_dotenv
from src.schema import InboxDigest

load_dotenv()
resend.api_key = os.environ["RESEND_API_KEY"]


def digest_to_html(digest: InboxDigest) -> str:
    def list_section(title, items) -> str:
        if not items:
            return f"<h3>{title}</h3><p><em>Nothing here.</em></p>"
        rows = "".join(f"<li>{item}</li>" for item in items)
        return f"<h3>{title}</h3><ul>{rows}</ul>"

    return (
        f"<h2>Inbox Digest</h2>"
        f"<p>{digest.overall_summary}</p>"
        f"{list_section('Needs attention', digest.needs_attention)}"
        f"{list_section('To-dos', digest.todos)}"
        f"{list_section('Can ignore', digest.can_ignore)}"
    )


def send_digest(digest: InboxDigest):
    params: resend.Emails.SendParams = {
        "from": "Check Email Light <CheckEmailLight@robbylinson.dev>",
        "to": ["robbylinson@gmail.com"],
        "subject": "Your inbox digest",
        "html": digest_to_html(digest),
    }
    try:
        email = resend.Emails.send(params)
        print(f"Digest sent to: {params['to'][0]}")
        return email
    except Exception as e:
        print(f"Failed to send digest: {e}")
        return None