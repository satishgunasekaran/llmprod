import streamlit as st
from PIL import Image

# Set page title and favicon
st.set_page_config(
    page_title="CSV Analytics with LLM",
    page_icon=":chart_with_upwards_trend:"
)

# Set title at the top middle of the page
st.title("CSV Analytics with LLM")
# Function to connect to another .ipynb file
# Upload CSV file with size limit of 5 MB
uploaded_file = st.file_uploader("Upload CSV file (Max 5 MB)", type=["csv"])
def connection(question):
    # Call your function in the other .ipynb file here
    # For example, if the other file is named 'other_file.ipynb' and the function is 'other_function'
    # You can use: !jupyter nbconvert --to script other_file.ipynb
    # Then import and call the function in this script
    # from other_file import other_function
    # other_function(question)
    pass
if uploaded_file is not None:
    # Display file details
    st.success(f"File Uploaded: {uploaded_file.name}")

    # Buttons for chatcsv and visualize
    if st.button("Chat CSV"):
        questions = ["1. give me the top 5 students as per cgpa7?", "Question 2", "Question 3", "Question 4"]
        selected_question = st.selectbox("Sample:", questions)
        connection(selected_question)

    if st.button("Visualize"):
        questions = ["Question 1", "Question 2", "Question 3", "Question 4"]
        selected_question = st.selectbox("Select a question:", questions)
        connection(selected_question)


