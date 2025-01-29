import fitz  # PyMuPDF
import os
import csv
import re
from PIL import Image
import io

def extract_images_and_metadata(pdf_folder, output_folder, csv_path, keywords):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    with open(csv_path, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['PDF_Name', 'Image_Path', 'Figure_Description', 'Science_Field', 'Keywords_Found', 'Comments'])

        for pdf_index, pdf_file in enumerate(sorted(os.listdir(pdf_folder)), start=1):
            if pdf_file.endswith('.pdf'):
                pdf_path = os.path.join(pdf_folder, pdf_file)
                pdf_output_folder = os.path.join(output_folder, str(pdf_index))
                os.makedirs(pdf_output_folder, exist_ok=True)

                print(f"\nProcessing: {pdf_file}")
                doc = fitz.open(pdf_path)
                image_index = 1
                captured_any_images = False  

                for page_number in range(len(doc)):
                    page = doc[page_number]
                    print(f"  Page {page_number + 1}: Checking for images...")
                    
                    for img_index, img in enumerate(page.get_images(full=True), start=1):
                        xref = img[0]
                        base_image = doc.extract_image(xref)
                        image_bytes = base_image["image"]
                        image_ext = base_image["ext"]
                        
                        image = Image.open(io.BytesIO(image_bytes))
                        print(f"    Found image {img_index}: size={image.size}, format={image.format}")

                        if pdf_file == "12-alboschiy-dorokhov-hrabovskyi-naumenko.pdf":
                            print("      Special handling for first document: skipping filters.")
                        else:
                            if image.size[0] < 200 or image.size[1] < 200:
                                print("      Skipped: Image too small.")
                                continue
                            
                            image_data = image.getdata()
                            pixel_count = sum(1 for pixel in image_data if pixel == (255, 255, 255))
                            if pixel_count > 1000:
                                print("      Skipped: Too many white pixels.")
                                continue
                        
                        image_path = os.path.join(pdf_output_folder, f'image_{image_index}.{image_ext}')
                        with open(image_path, "wb") as image_file:
                            image_file.write(image_bytes)
                        print(f"      Saved: {image_path}")
                        image_index += 1
                        captured_any_images = True

                if not captured_any_images:
                    print(f"  No images were captured for {pdf_file}.")

                full_text = " ".join(page.get_text() for page in doc)
                science_field = 'Unknown'
                matched_keywords = []

                for field, field_keywords in keywords.items():
                    if any(keyword.lower() in full_text.lower() for keyword in field_keywords):
                        science_field = field
                        matched_keywords = [kw for kw in field_keywords if kw.lower() in full_text.lower()]
                        break

                captions = re.findall(r"(Figure\s\d+.*)", full_text)

                for i in range(1, image_index):
                    description = captions[i - 1] if i - 1 < len(captions) else "Doesn't seem to have a comment"
                    writer.writerow([pdf_file, os.path.join(str(pdf_index), f'image_{i}.{image_ext}'), description, science_field, ", ".join(matched_keywords), ""])

if __name__ == "__main__":
    pdf_folder = r"C:\\Users\\Master\\Desktop\\pypy\\onesci\\SciGraph\\pdfs"
    output_folder = r"C:\\Users\\Master\\Desktop\\pypy\\onesci\\SciGraph\\extracted_images"
    csv_path = r"C:\\Users\\Master\\Desktop\\pypy\\onesci\\SciGraph\\metadata.csv"

    keywords = {
        "Mathematics and Computer Science": ["algorithm", "computational", "vector", "graph", "math"],
        "Environmental Science": ["ecosphere", "habitat", "environment", "ecosystem"],
    }

    extract_images_and_metadata(pdf_folder, output_folder, csv_path, keywords)

