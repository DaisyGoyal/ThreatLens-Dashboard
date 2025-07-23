import streamlit as st
import pandas as pd
from utils import fetch_tweets, analyze_with_gemini


st.set_page_config(page_title="ThreatLens AI", page_icon="🛡️")
st.title("🛡️ ThreatLens AI – Cyber Threat Dashboard")

keyword = st.text_input("Enter a keyword (e.g., ransomware, phishing):")

if st.button("Scan Now") and keyword:
    with st.spinner("Scanning tweets and analyzing..."):
        tweets = fetch_tweets(keyword)
        results = []
        for tweet in tweets:
            summary, severity = analyze_with_gemini(tweet)

            results.append({
                "Tweet": tweet,
                "Summary": summary,
                "Severity": severity
            })

        df = pd.DataFrame(results)
        st.success("Scan complete!")
        st.dataframe(df)

        # Optional chart
        st.subheader("Threat Severity Chart")
        chart = df['Severity'].value_counts()
        st.bar_chart(chart)
