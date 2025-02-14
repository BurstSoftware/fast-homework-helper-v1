import streamlit as st
from fpdf import FPDF
import os

def save_to_pdf(class_name, book_name, chapter, page, homework_text, image, domain_knowledge, concepts, activities, school_function, school_requirements, learning_aspects):
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    
    pdf.cell(200, 10, "Student Homework & Learning Tracker", ln=True, align='C')
    pdf.ln(10)
    pdf.cell(200, 10, f"Class: {class_name}", ln=True)
    pdf.cell(200, 10, f"Book: {book_name}", ln=True)
    pdf.cell(200, 10, f"Chapter: {chapter}", ln=True)
    pdf.cell(200, 10, f"Page: {page}", ln=True)
    pdf.ln(5)
    pdf.multi_cell(0, 10, f"Homework: {homework_text}")
    
    pdf.ln(10)
    pdf.cell(200, 10, "Educational Insights", ln=True, align='C')
    pdf.ln(5)
    pdf.multi_cell(0, 10, f"Domain Knowledge: {domain_knowledge}")
    pdf.multi_cell(0, 10, f"Concepts: {concepts}")
    pdf.multi_cell(0, 10, f"Activities: {activities}")
    pdf.multi_cell(0, 10, f"Function of School: {school_function}")
    pdf.multi_cell(0, 10, f"Requirements of School: {school_requirements}")
    pdf.multi_cell(0, 10, f"Aspects of Learning: {learning_aspects}")
    
    if image:
        image_path = "uploaded_image.png"
        with open(image_path, "wb") as f:
            f.write(image.getbuffer())
        pdf.image(image_path, x=10, w=100)
        os.remove(image_path)
    
    pdf_output = "homework_learning.pdf"
    pdf.output(pdf_output)
    return pdf_output

def main():
    st.title("Student Homework & Learning Tracker")

    class_name = st.text_input("Class Name")
    book_name = st.text_input("Book Name")
    chapter = st.text_input("Chapter")
    page = st.text_input("Page")
    homework_text = st.text_area("Homework Assignment")
    image = st.file_uploader("Upload Image (optional)", type=["png", "jpg", "jpeg"])
    
    domain_knowledge = st.text_area("Describe Domain Knowledge")
    concepts = st.text_area("Describe Concepts")
    activities = st.text_area("Describe Activities")
    school_function = st.text_area("Describe Function of School")
    school_requirements = st.text_area("Describe Requirements of School")
    learning_aspects = st.text_area("Describe Aspects of Learning")
    
    if st.button("Save and Download PDF"):
        if all([class_name, book_name, chapter, page, homework_text, domain_knowledge, concepts, activities, school_function, school_requirements, learning_aspects]):
            pdf_file = save_to_pdf(class_name, book_name, chapter, page, homework_text, image, domain_knowledge, concepts, activities, school_function, school_requirements, learning_aspects)
            with open(pdf_file, "rb") as file:
                st.download_button("Download PDF", file, file_name=pdf_file, mime="application/pdf")
        else:
            st.error("Please fill all the fields except the image (optional).")

if __name__ == "__main__":
    main()
