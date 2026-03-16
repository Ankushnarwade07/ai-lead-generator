import requests
import re

def extract_email(website):

    if not website:
        return "Not Found"

    try:
        r = requests.get(website, timeout=5)

        emails = re.findall(
            r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}",
            r.text
        )

        return emails[0] if emails else "Not Found"

    except:
        return "Not Found"