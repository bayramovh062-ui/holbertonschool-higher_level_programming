from flask import Flask, render_template, request
import json
import csv
import sqlite3

app = Flask(__name__)

# JSON və CSV oxuma funksiyaları (Task 03-dən)
def read_json():
    with open('products.json', 'r') as f:
        return json.load(f)

def read_csv():
    products = []
    with open('products.csv', 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            row['id'] = int(row['id'])
            row['price'] = float(row['price'])
            products.append(row)
    return products

# Yeni SQL oxuma funksiyası
def read_sql(product_id=None):
    products = []
    try:
        conn = sqlite3.connect('products.db')
        conn.row_factory = sqlite3.Row  # Bu sətir nəticəni lüğət kimi qaytarır!
        cursor = conn.cursor()
        
        if product_id:
            cursor.execute('SELECT * FROM Products WHERE id = ?', (product_id,))
        else:
            cursor.execute('SELECT * FROM Products')
        
        rows = cursor.fetchall()
        # Row obyektlərini standart dict-ə çeviririk
        products = [dict(row) for row in rows]
        conn.close()
    except sqlite3.Error as e:
        print(f"Database error: {e}")
    return products

@app.route('/products')
def display_products():
    source = request.args.get('source')
    product_id = request.args.get('id', type=int)
    
    products = []
    error = None

    if source == 'json':
        products = read_json()
    elif source == 'csv':
        products = read_csv()
    elif source == 'sql':
        products = read_sql(product_id)
        # SQL-də filtrləməni funksiya daxilində etdiyimiz üçün 
        # əlavə filtrləməyə ehtiyac yoxdur, sadəcə tapılmama halını yoxlayaq
        if not products and product_id:
            error = "Product not found"
    else:
        error = "Wrong source"

    # JSON və CSV üçün köhnə filtrləmə məntiqi (əgər source düzgündürsə)
    if not error and source in ['json', 'csv'] and product_id:
        filtered = [p for p in products if p['id'] == product_id]
        if not filtered:
            error = "Product not found"
        else:
            products = filtered

    return render_template('product_display.html', products=products, error=error)

if __name__ == '__main__':
    app.run(debug=True, port=5000)

