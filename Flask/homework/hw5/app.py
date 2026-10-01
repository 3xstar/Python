from flask import Flask, render_template, redirect, url_for, session, request

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mini-shop-secret-key'

products = {
    1: {"name": "Laptop", "price": 899, "category": "Electronics"},
    2: {"name": "Wireless Headphones", "price": 99, "category": "Electronics"},
    3: {"name": "Coffee Maker", "price": 120, "category": "Home Appliances"},
    4: {"name": "Smartphone", "price": 699, "category": "Electronics"},
    5: {"name": "Electric Kettle", "price": 45, "category": "Home Appliances"},
    6: {"name": "Blender", "price": 60, "category": "Home Appliances"},
    7: {"name": "Running Shoes", "price": 85, "category": "Sports & Outdoors"},
    8: {"name": "Backpack", "price": 50, "category": "Sports & Outdoors"},
    9: {"name": "Water Bottle", "price": 15, "category": "Sports & Outdoors"},
    10: {"name": "Desk Lamp", "price": 30, "category": "Home & Office"},
    11: {"name": "Office Chair", "price": 180, "category": "Home & Office"},
    12: {"name": "Notebook", "price": 5, "category": "Home & Office"}
}

@app.route('/')
def index():
    if 'cart' not in session:
        session['cart'] = {}
    return render_template('index.html', products=products)

@app.route('/add/<int:product_id>')
def add_to_cart(product_id):
    pid = str(product_id)
    if pid in session['cart']:
        session['cart'][pid] += 1
    else:
        session['cart'][pid] = 1
    session.modified = True
    return redirect(url_for('index'))

@app.route('/cart')
def view_cart():
    cart_items = []
    total_sum = 0
    total_items = 0

    for pid, quantity in session.get('cart', {}).items():
        product = products.get(int(pid))
        if product:
            item_sum = product['price'] * quantity
            total_sum += item_sum
            total_items += quantity
            cart_items.append({
                'id': pid,
                'name': product['name'],
                'price': product['price'],
                'quantity': quantity,
                'item_sum': item_sum
            })

    unique_items = len(cart_items)

    return render_template('cart.html',
                           items=cart_items,
                           total_sum=total_sum,
                           total_items=total_items,
                           unique_items=unique_items)

@app.route('/delete/<int:product_id>')
def delete_item(product_id):
    pid = str(product_id)
    if pid in session.get('cart', {}):
        del session['cart'][pid]
    session.modified = True
    return redirect(url_for('view_cart'))

@app.route('/clear')
def clear_cart():
    if 'cart' in session:
        session['cart'].clear()
    session.modified = True
    return redirect(url_for('view_cart'))

if __name__ == '__main__':
    app.run(debug=True)
