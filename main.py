import streamlit as st
import pandas as pd

from maps_scraper import get_google_maps_leads
from justdial_scraper import get_justdial_leads
from email_extractor import extract_email
from lead_scoring import score_lead

SERP_API_KEY = "169a779d84a87247a81899a4adbf2255ee12ee614b5602dc411f9e416c9fb2f0"

st.set_page_config(
    page_title="AI Lead Generator",
    page_icon="🚀",
    layout="wide"
)

# Header
st.title("AI Powered MVP for Lead Generator🚀")
st.write("Generate business leads automatically based on a product keyword from Google Maps and JustDial")

# Sidebar
st.sidebar.header("Search Settings 🔎")

keyword = st.sidebar.text_input(
    "Product Keyword",
    placeholder="Example: Water Purifier Dealers Pune"
)

max_results = st.sidebar.slider(
    "Number of Leads",
    5,
    50,
    20
)

generate = st.sidebar.button("Generate Leads")

st.divider()

# Main Section
if generate:

    with st.spinner("🔎 Searching businesses..."):

        maps_leads = get_google_maps_leads(keyword, SERP_API_KEY)
        jd_leads = get_justdial_leads(keyword)

        all_leads = maps_leads + jd_leads

        results = []

        for lead in all_leads[:max_results]:

            email = extract_email(lead["website"])

            score = score_lead(
                lead["phone"],
                email,
                lead["website"]
            )

            results.append({
                "Company": lead["company"],
                "Phone": lead["phone"],
                "Email": email,
                "Location": lead["location"],
                "Source": lead["source"],
                "Lead Score": score
            })

        df = pd.DataFrame(results)

        df = df.sort_values(
            by="Lead Score",
            ascending=False
        )

    # Metrics
    col1, col2, col3 = st.columns(3)

    col1.metric("Total Leads", len(df))

    col2.metric(
        "Emails Found",
        (df["Email"] != "Not Found").sum()
    )

    col3.metric(
        "High Quality Leads",
        (df["Lead Score"] > 60).sum()
    )

    st.divider()

    # Table
    st.subheader("📊 Generated Leads")

    st.dataframe(
        df,
        use_container_width=True,
        height=500
    )

    st.download_button(
        "⬇ Download Leads CSV",
        df.to_csv(index=False),
        "leads.csv",
        "text/csv"
    )

else:

    st.info("👈 Enter a product keyword in the sidebar and click **Generate Leads**")

    st.image(
        "https://blog.aadidigital.com/wp-content/uploads/2025/11/lead_gen_company.webp.w720.webp",
        caption="AI Powered Lead Generation"
    )