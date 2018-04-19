import os

# Customer Email Settings

EMAIL_ACCOUNT = os.getenv("EMAIL_ACCOUNT")

EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")

EMAIL_HOST = os.getenv("EMAIL_HOST")

EMAIL_PORT = int(os.getenv("SMTP_PORT", 465))

EMAIL_SSL = bool(int(os.getenv("EMAIL_SSL", 1)))

# Django Email Settings
DEFAULT_FROM_EMAIL = os.getenv("DEFAULT_FROM_EMAIL")

SERVER_EMAIL = os.getenv("SERVER_EMAIL")
