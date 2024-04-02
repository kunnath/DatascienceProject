# DatascienceProject


## Scan nutrition information from product image and anaysis the data with AI programme

 Utilize computer vision techniques to extract text data from images of product components. This process involves capturing frames from a camera feed, converting them to text using optical character recognition (OCR) with pytesseract, and storing the extracted information in text and CSV files. This functionality allows for automated data extraction and analysis from product images.



# run pip to install requirement
 pip install -r requirements.txt


##  Activity to be Plan:

To implement a solution using Qdrant and Python, you can follow these general steps:

1. Set Up Qdrant: First, you need to set up Qdrant, an open-source vector search engine, on your system. You can install Qdrant by following the instructions provided in the Qdrant documentation.

2. Prepare Data: Prepare your dataset of product images and their corresponding nutrition information. This could involve extracting text from the images using OCR (Optical Character Recognition) techniques.

3. Vectorize Nutrition Information: Convert the extracted nutrition information into numerical vectors that can be understood by Qdrant. You may use techniques like TF-IDF (Term Frequency-Inverse Document Frequency) or word embeddings to represent the text data as vectors.

4. Index Data in Qdrant: Upload the vectorized data into Qdrant's index. Qdrant provides APIs for indexing data, allowing you to upload vectors along with their corresponding metadata.

5. Querying with Python: Use the Qdrant Python SDK to query the indexed data. You can perform similarity searches to find products with similar nutrition information based on a given query.

