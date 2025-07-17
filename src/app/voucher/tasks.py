from src.worker.celery_config import celery_app
import os
import base64
import requests
from dotenv import load_dotenv
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from msal import ConfidentialClientApplication
from src.configuration.env_settings import setting

load_dotenv()

@celery_app.task()
def voucher_task_test():
    """A simple task to add two numbers."""
    return "Voucher Task executed successfully!"
# Gmail parsing task
@celery_app.task()
def parse_gmail_emails():
    SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']
    creds_path = os.getenv("GOOGLE_CLIENT_SECRET_PATH")

    flow = InstalledAppFlow.from_client_secrets_file(creds_path, SCOPES)
    creds = flow.run_local_server(port=0)
    service = build('gmail', 'v1', credentials=creds)

    results = service.users().messages().list(userId='me', maxResults=5).execute()
    messages = results.get('messages', [])

    parsed = []
    for msg in messages:
        full_msg = service.users().messages().get(userId='me', id=msg['id'], format='full').execute()
        payload = full_msg.get('payload', {})
        parts = payload.get('parts', [])

        for part in parts:
            mime = part.get("mimeType")
            data = part.get("body", {}).get("data", "")
            if data:
                decoded = base64.urlsafe_b64decode(data.encode()).decode()
                parsed.append({"mime": mime, "body": decoded})

    print("📧 Gmail Emails Parsed:", parsed)
    return parsed


# Outlook parsing task
@celery_app.task()
def parse_outlook_emails():
    CLIENT_ID = setting.OUTLOOK_CLIENT_ID 
    TENANT_ID = setting.OUTLOOK_TENANT_ID
    CLIENT_SECRET = setting.OUTLOOK_CLIENT_SECRET
    print(CLIENT_ID, TENANT_ID, CLIENT_SECRET)

    authority = f"https://login.microsoftonline.com/{TENANT_ID}"
    scope = ["https://graph.microsoft.com/.default"]

    app = ConfidentialClientApplication(
        CLIENT_ID, authority=authority, client_credential=CLIENT_SECRET
    )

    token = app.acquire_token_for_client(scopes=scope)
    access_token = token.get("access_token")

    if not access_token:
        raise Exception("Failed to acquire Outlook access token")

    headers = {"Authorization": f"Bearer {access_token}"}
    response = requests.get("https://graph.microsoft.com/v1.0/me/messages", headers=headers)
    print("📧 Outlook Response:", response.json())

    messages = response.json().get("value", [])
    print("📧 Outlook Messages:", messages)
    parsed = []

    for message in messages[:5]:
        subject = message.get("subject")
        body = message.get("body", {}).get("content", "")
        parsed.append({"subject": subject, "body": body})

    print("📧 Outlook Emails Parsed:", parsed)
    return parsed

