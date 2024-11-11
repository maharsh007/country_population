import PyPDF2
from docx import Document

def pdf_to_doc(pdf_path, doc_path):
    # Create a PDF reader object
    pdf_reader = PyPDF2.PdfReader(pdf_path)
    
    # Create a Word document
    doc = Document()
    
    # Iterate through each page in the PDF
    for page_num in range(len(pdf_reader.pages)):
        page = pdf_reader.pages[page_num]
        text = page.extract_text()
        print(text)
        # Add the extracted text to the Word document
        doc.add_paragraph(text)
    
    # Save the Word document
    doc.save(doc_path)

if __name__ == "__main__":
    # Specify the paths to the input PDF and output DOCX files
    pdf_path = '../ECARDPDF_banasree_24-25.pdf'
    doc_path = '../output.docx'
    
    # Convert the PDF to DOCX
    pdf_to_doc(pdf_path, doc_path)
    print(f"Conversion completed. The output file is saved as {doc_path}")