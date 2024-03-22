import csv
from qdrant_client import QdrantClient
from qdrant_client.http.models import PointStruct

# Create an instance of QdrantClient
client = QdrantClient("localhost", port=6333)

# Create a new collection (replace 'test_collection' with your desired collection name)
collection_name = "product_collection"
client.create_collection(
    collection_name=collection_name,
    vectors_config={
        "size": 4,  # Adjust vector size based on your data
        "distance": "Dot"
    }
)

# Path to the CSV file
csv_file = 'product.csv'  # Replace 'data.csv' with the path to your CSV file

# List to store PointStruct instances
points = []

# Read data from the CSV file
with open(csv_file, 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        # Extract data from CSV row
        point_id = int(row['id'])
        vector = [float(row['vector1']), float(row['vector2']), float(row['vector3']), float(row['vector4'])]
        payload = {"product": row['product']}
        
        # Create PointStruct instance and add it to the list
        points.append(PointStruct(id=point_id, vector=vector, payload=payload))

# Insert data into the collection
operation_info = client.upsert(
    collection_name=collection_name,
    wait=True,
    points=points,
)

print("Data uploaded successfully.")
