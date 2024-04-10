from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

@app.route('/')
def index():
    # Load the dataset and preprocess
    data = pd.read_csv('house_data.csv')
    data = data.dropna()
    print(data)
    zipcodes = [{'zipcode': row['zipcode'], 'price': row['price']} for idx, row in data.iterrows()]
    print(data['zipcode'])
    # Render the HTML template and pass the zipcodes data
    return render_template('index.html', zipcodes=zipcodes)

if __name__ == '__main__':
    app.run(debug=True)
