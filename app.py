import streamlit as st
import re

def extract_ids(text):
    return set(re.findall(r'#\d{5}', text))

st.title("Find Differences Between Sets of IDs")

# Use session state to store the text inputs
if 'text_a' not in st.session_state:
    st.session_state.text_a = ''
if 'text_b' not in st.session_state:
    st.session_state.text_b = ''

# Update session state when text changes
text_a = st.text_area("Paste Text for A:", height=200, key='text_a')
text_b = st.text_area("Paste Text for B:", height=200, key='text_b')

if st.button("Find Differences"):
    ids_a = extract_ids(text_a)
    ids_b = extract_ids(text_b)

    only_in_a = sorted(ids_a - ids_b)  # Convert to sorted list
    only_in_b = sorted(ids_b - ids_a)  # Convert to sorted list

    st.subheader("In A but not in B:")
    if only_in_a:
        for id in only_in_a:
            st.markdown(f"* {id}")
    else:
        st.write("No unique IDs found")

    st.subheader("In B but not in A:")
    if only_in_b:
        for id in only_in_b:
            st.markdown(f"* {id}")
    else:
        st.write("No unique IDs found")