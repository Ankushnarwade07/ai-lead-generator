import requests
from bs4 import BeautifulSoup

def get_justdial_leads(keyword):

    url = f"https://www.justdial.com/search?q={keyword}"

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, "html.parser")

    leads = []

    listings = soup.find_all("div", class_="resultbox")

    for item in listings[:10]:

        name = item.find("h2")
        phone = item.find("span", class_="callcontent")

        leads.append({
            "company": name.text if name else "",
            "phone": phone.text if phone else "",
            "website": None,
            "location": keyword,
            "source": "JustDial"
        })

    return leads