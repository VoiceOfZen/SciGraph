import os
import fitz  # PyMuPDF
from PIL import Image

def extract_images_from_pdfs(pdf_folder, output_folder):
    # Check if the PDF folder exists
    if not os.path.exists(pdf_folder):
        print(f"The folder {pdf_folder} does not exist.")
        return

    # Iterate through all PDF files in the folder
    for pdf_index, pdf_file in enumerate(sorted(os.listdir(pdf_folder)), start=1):
        pdf_path = os.path.join(pdf_folder, pdf_file)
        if pdf_file.endswith(".pdf"):
            # Create a subfolder for each PDF's images
            pdf_output_folder = os.path.join(output_folder, str(pdf_index))
            os.makedirs(pdf_output_folder, exist_ok=True)

            # Open PDF
            pdf_document = fitz.open(pdf_path)
            for page_index in range(len(pdf_document)):
                page = pdf_document[page_index]
                images = page.get_images(full=True)
                for img_index, img in enumerate(images):
                    xref = img[0]
                    base_image = pdf_document.extract_image(xref)
                    image_bytes = base_image["image"]
                    image_ext = base_image["ext"]
                    image_output_path = os.path.join(
                        pdf_output_folder, f"page{page_index + 1}_img{img_index + 1}.{image_ext}"
                    )
                    with open(image_output_path, "wb") as image_file:
                        image_file.write(image_bytes)
            pdf_document.close()

# Paths
base_path = os.path.dirname(os.path.abspath(__file__))
pdf_folder = os.path.join(base_path, "pdfs")  # Adjusted to relative path
output_folder = os.path.join(base_path, "extracted_images")

# Run the function
extract_images_from_pdfs(pdf_folder, output_folder)
