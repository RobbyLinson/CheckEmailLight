from google_auth_oauthlib.flow import InstalledAppFlow
import os
from dotenv import load_dotenv
load_dotenv() 

CLIENT_ID = os.getenv("GOOGLE_CLIENT_ID")
CLIENT_SECRET = os.getenv("GOOGLE_CLIENT_SECRET")

flow = InstalledAppFlow.from_client_config(
    {
        "installed": {
            "client_id": CLIENT_ID,
            "client_secret": CLIENT_SECRET,
            "auth_uri": "https://accounts.google.com/o/oauth2/auth",
            "token_uri": "https://oauth2.googleapis.com/token",
            "redirect_uris": ["http://localhost"],
        }
    },
    scopes=["https://www.googleapis.com/auth/gmail.readonly"],
)

creds = flow.run_local_server(port=0, access_type="offline", prompt="consent", open_browser=False,)
print("\nREFRESH TOKEN:\n")
print(creds.refresh_token)