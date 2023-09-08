import streamlit as st
import PyPDF2
import os
import csv


# Parse the resume using the resume parser
def parsed_resume(file):
    reader = PyPDF2.PdfReader(file)
    text = ""
    for page_num in range(len(reader.pages)):
        current_txt = reader.pages[page_num].extract_text()

        # for every new line in the text, replace with a space
        current_txt = current_txt.replace("\n", " ")

        # for every "●" in the text, replace with a space
        current_txt = current_txt.replace("●", " ")

        text += current_txt
    return text

# 5. Build an app with streamlit
def main():
    # set the page title as Custom Write Assistant and page icon as a robot
    st.set_page_config(
        page_title="Easy ATS System", page_icon=":robot_face:")

    st.header("Easy ATS System")
    # a subheader for the app saying that it helps to check if your resume is ATS friendly
    st.subheader("This app helps to check if your resume is ATS friendly")

    # allow the user to upload their resume as a PDF file
    resume = st.file_uploader("Upload your resume as a PDF file")

    # Create an empty placeholder
    placeholder = st.empty()

    # During loading the file, display a message saying that the resume is being parsed
    if resume:
        placeholder.text("Generating your ATS parsed resume...")
        result = parsed_resume(resume)
        placeholder.text("Resume Text Parsed ✅")
        st.info(result)
    else:
        placeholder.info("Please upload a resume file")


if __name__ == '__main__':
    main()
