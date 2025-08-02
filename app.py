import streamlit as st
import requests

st.title("Groq Synonym Generator")

word = st.text_input("Enter a word:")

if st.button("Generate"):
    if word:
        with st.spinner("Generating synonyms..."):
            try:
                response = requests.post(
                    "https://distributors-dekh-production.up.railway.app/generate-synonyms",
                    json={"word": word}
                )
                if response.status_code == 200:
                    data = response.json()
                    synonyms = data.get("synonyms", [])
                    if synonyms:
                        st.success("Synonyms: " + ", ".join(synonyms))
                    else:
                        st.info("No synonyms found.")
                else:
                    st.error(f"Error: {response.json().get('detail', 'Unknown error')}")
            except Exception as e:
                st.error(f"Exception: {e}")
    else:
        st.warning("Please enter a word above.")
