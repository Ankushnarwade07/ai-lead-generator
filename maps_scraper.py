from serpapi import GoogleSearch

def get_google_maps_leads(keyword, api_key):

    params = {
        "engine": "google_maps",
        "q": keyword,
        "api_key": '169a779d84a87247a81899a4adbf2255ee12ee614b5602dc411f9e416c9fb2f0'
    }

    search = GoogleSearch(params)
    results = search.get_dict()

    leads = []

    for place in results.get("local_results", []):

        leads.append({
            "company": place.get("title"),
            "phone": place.get("phone"),
            "website": place.get("website"),
            "location": place.get("address"),
            "source": "Google Maps"
        })

    return leads