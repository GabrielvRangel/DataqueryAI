import mysql.connector
import openai
from flask import current_app

def init_db(app):
    app.config['DB_CONNECTION'] = mysql.connector.connect(
        host=app.config['DB_HOST'],
        port=app.config['DB_PORT'],
        user=app.config['DB_USER'],
        password=app.config['DB_PASSWORD'],
        database=app.config['DB_NAME']
    )

def get_db():
    if 'DB_CONNECTION' not in current_app.config:
        init_db(current_app)
    return current_app.config['DB_CONNECTION']

def generate_sql(query):
    db_structure = """
    Table customers (customer_id INT, company_name TEXT, contact_name TEXT, contact_title TEXT, address TEXT, city TEXT, region TEXT, postal_code TEXT, country TEXT, phone TEXT, fax TEXT)
    Table employees (employee_id INT, last_name TEXT, first_name TEXT, title TEXT, title_of_courtesy TEXT, birth_date DATE, hire_date DATE, address TEXT, city TEXT, region TEXT, postal_code TEXT, country TEXT, home_phone TEXT, extension TEXT, notes TEXT, reports_to INT)
    Table orders (order_id INT, customer_id INT, employee_id INT, order_date DATE, required_date DATE, shipped_date DATE, ship_via INT, freight REAL, ship_name TEXT, ship_address TEXT, ship_city TEXT, ship_region TEXT, ship_postal_code TEXT, ship_country TEXT)
    Table products (product_id INT, product_name TEXT, supplier_id INT, category_id INT, quantity_per_unit TEXT, unit_price REAL, units_in_stock INT, units_on_order INT, reorder_level INT, discontinued INT)
    """
    
    prompt = f"""
    You are a database expert. Convert the following natural language query to an SQL query based on the given database structure.
    
    Database Structure: {db_structure}
    
    Natural Language Query: {query}
    
    SQL Query:
    """
    
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a database expert."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=150,
        temperature=0.2
    )
    
    sql_query = response.choices[0].message['content'].strip()
    return sql_query

def execute_query(sql_query):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute(sql_query)
    result = cursor.fetchall()
    return result
