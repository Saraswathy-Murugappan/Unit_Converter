import streamlit as st
import requests
import random

st.set_page_config(page_title="Mood-Based Quote Generator", page_icon="💭", layout="centered")

st.title("💭 Mood-Based Quote Generator")
st.write("Enter your mood and get a quote that matches your feelings!")

# User input
mood = st.text_input("How are you feeling today? (e.g., happy, sad, motivated, angry, tired)").lower()

# Function to fetch quotes from API
def get_quotes():
    url = "https://type.fit/api/quotes"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        st.error("Failed to fetch quotes from the API.")
        return []

# Display quote
if st.button("Get Quote"):
    quotes = get_quotes()
    if quotes:
        # Filter quotes based on mood word match
        filtered_quotes = [q for q in quotes if mood in (q['text'] or '').lower()]
        if filtered_quotes:
            q = random.choice(filtered_quotes)
        else:
            q = random.choice(quotes)
        st.success(f"💬 *{q['text']}* — {q['author'] or 'Unknown'}")
