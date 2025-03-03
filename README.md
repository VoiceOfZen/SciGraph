# SciGraph

## Development of a Methodology and Software for Creating a Dataset to Train Neural Networks to Integrate Scientific Graphics

SciGraph is a project focused on developing a methodology and software for automatically creating a dataset of scientific graphs extracted from PDF documents. This dataset is designed to train neural networks for tasks related to the automatic analysis and recognition of scientific graphics.

**Goal**: To create an automated system for extracting, classifying, and annotating scientific graphs from PDFs to build a high-quality dataset for AI training.

## Challenges in Extracting Scientific Graphics

Extracting scientific graphs from PDFs is far from trivial. Here are the main challenges:

1. **Extracting Images from PDFs** – PDF documents are complex; images are stored in different formats and can be embedded in unpredictable ways.
2. **Identifying Graphs Among Extracted Images** – Not all extracted images are graphs. Logos, illustrations, and tables must be filtered out.
3. **Extracting Graph Descriptions** – Scientific graphs usually have captions, but retrieving them accurately requires advanced text processing techniques.

## Features

✅ **Automated Image Extraction** – Extracts images from PDFs while filtering out irrelevant content.  
✅ **Graph Identification** – Uses filtering techniques to isolate graphs from other images.  
✅ **Metadata Annotation** – Attempts to link extracted images with their descriptions.  
✅ **Flexible and Scalable** – Can be adapted to different types of research papers and scientific disciplines.  

##  Technologies Used

 **Programming:** Python  
 **PDF Processing:** PyMuPDF  
 **Image Processing:** OpenCV, PIL  
 **AI for Classification:** Machine Learning/Deep Learning  
 **Metadata Storage:** JSON/XML  

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/SciGraph.git
   cd SciGraph
   ```
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

## Usage

Run the extraction script:
```sh
python extract_graphs.py --pdf-folder path/to/pdfs --output-folder path/to/output
```

## Future Improvements

🔹 **Machine Learning-based Graph Identification** – Train a model to detect graphs automatically.  
🔹 **OCR for Captions** – Use Optical Character Recognition to extract embedded text.  
🔹 **Better Filtering Algorithms** – Improve the accuracy of identifying scientific graphs.  

## 🌍 Localization

🔹 English version (default)  
🔹 [Русская версия (README.ru.md)](README.ru.md)  

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
CHANGE THIS PART by me

**This project is part of a graduation thesis focused on AI-driven scientific data processing.** 
