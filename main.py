import streamlit as st
import requests

st.set_page_config(page_title="Quote App", layout="centered")
st.title("Random Quote Generator")

# Streamlit Secrets (if your API requires a key)
# Example: st.secrets["API_KEY"]

API_URL = "https://api.quotable.io/random"  # Example public API, change if needed

def fetch_quote():
    try:
        response = requests.get(API_URL, timeout=10)  # timeout added
        response.raise_for_status()  # Raise error if HTTP error
        data = response.json()
        # Adjust according to API response structure
        return data.get("content"), data.get("author")
    except requests.exceptions.RequestException as e:
        st.error(f"Failed to fetch quotes from the API: {e}")
        return None, None

if st.button("Get Random Quote"):
    quote, author = fetch_quote()
    if quote and author:
        st.markdown(f"> {quote}")
        st.markdown(f"**— {author}**")
