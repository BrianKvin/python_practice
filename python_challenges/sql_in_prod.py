# Establish a connection
conn = sqlite3.connect("shopease.db")
cursor = conn.cursor()

# Retrieve product information
def get_product_info (product_id):
  query = f"SELECT name, product, stock FROM products WHERE id = {product_id}"
  cursor.execute(query)
  product_data = cursor.fetchone()
  return product_data

# Process an order
def process_order (order_id, product_id, quantity):
  # check product availability
  product_data = get_product_info(product_id)
  if product_data and product_data[2] >= quantity:
    # update stock
    new_stock = product_data [2] - quantity
    update_query = f"UPDATE products SET stock = {new_stock} WHERE id = {product_id}"
    cursor.execute(update_query)
  