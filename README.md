# SciGraph

✅ **Development of Methodology and Software for Creating a Dataset to Train Neural Networks to Integrate Scientific Graphics** ✅

📌 **Goal**: To create an automated system for extracting, classifying, and annotating scientific graphs from PDFs to build a high-quality dataset for AI training.

---

## 🔹 Challenges in Dataset Creation

1️⃣ **Extracting images from PDFs** 📄➡️🖼️  
   Extracting images from PDFs is **not straightforward**, as scientific articles use different formats, encodings, and image embedding methods. Some images are **embedded as vectors**, while others are **rasterized**, making uniform extraction complex.

2️⃣ **Identifying and extracting graphs** 📊  
   Not every image in a scientific paper is a graph. **Diagrams, logos, and figures** can be mixed in. Developing **an automated filtering method** to extract only graphs is a major challenge.

3️⃣ **Extracting the graph's description** 📝  
   Descriptions of graphs may be **below, above, or on another page**. Some are labeled as `Figure X`, while others are embedded within text. Finding a **reliable way to match a graph with its description** is a key challenge.

---

## 🔹 Features

✅ **Automated Image Extraction**: Parses PDFs and extracts images related to scientific graphics.
✅ **Graph Filtering & Classification**: Filters irrelevant images (logos, schematics) and selects only graphs.
✅ **Text Extraction & Metadata Annotation**: Identifies and extracts relevant graph descriptions.
✅ **Flexible & Scalable**: Can be adapted to different scientific fields and publication types.

---

## 🔹 Technologies Used

🛠 **Programming:** Python  
📄 **PDF Processing:** PyMuPDF  
🖼 **Image Processing:** OpenCV, PIL  
🤖 **AI for Classification:** Machine Learning/Deep Learning  
📂 **Metadata Storage:** JSON/XML  

---

## 🔹 Installation & Usage

### 🔧 Installation
```bash
# Clone the repository
git clone https://github.com/yourusername/SciGraph.git
cd SciGraph

# Install dependencies
pip install -r requirements.txt
```

### 🚀 Usage
```bash
python extract_graphs.py --input_folder pdfs/ --output_folder extracted_images/
```

---

## 🌍 Localization

🔹 English version (default)  
🔹 [Русская версия (README.ru.md)](README.ru.md)  

---

## 📜 License
MIT License

---

✅ **This project is part of a graduation thesis focused on AI-driven scientific data processing.** 🚀
