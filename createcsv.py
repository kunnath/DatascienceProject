import csv

# Given data
data = [
    {"id": 1, "vector": [0.05, 0.61, 0.76, 0.74], "payload": {"product": "Product1"}},
    {"id": 2, "vector": [0.19, 0.81, 0.75, 0.11], "payload": {"product": "Product2"}},
    {"id": 3, "vector": [0.36, 0.55, 0.47, 0.94], "payload": {"product": "Product3"}},
    {"id": 4, "vector": [0.18, 0.01, 0.85, 0.80], "payload": {"product": "Product4"}},
    {"id": 5, "vector": [0.24, 0.18, 0.22, 0.44], "payload": {"product": "Product5"}},
    {"id": 6, "vector": [0.35, 0.08, 0.11, 0.44], "payload": {"product": "Product6"}}
]

# Write data to CSV file
with open('product.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['id', 'vector1', 'vector2', 'vector3', 'vector4', 'product'])
    for item in data:
        writer.writerow([item['id'], *item['vector'], item['payload']['product']])
