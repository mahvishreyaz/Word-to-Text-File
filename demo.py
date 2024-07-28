from docx import Document

def docx_to_text(docx_file, txt_file):
    # Load the .docx file
    doc = Document(docx_file)
    
    # Open the .txt file in write mode
    with open(txt_file, 'w', encoding='utf-8') as txt:
        # Iterate through each paragraph in the .docx file
        for para in doc.paragraphs:
            # Write the paragraph text to the .txt file
            txt.write(para.text + '\n')

docx_file = input("Enter the path to the .docx file: ")
txt_file = input("Enter the path for the output .txt file: ")

docx_to_text(docx_file, txt_file)
print(f"Converted {docx_file} to {txt_file}")
