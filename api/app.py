from flask import Flask, jsonify
from flask_restx import Api, Resource
import mysql.connector

app = Flask(__name__)

# API setup with Swagger documentation
api = Api(app, version='1.0', title='E-commerce API',
          description='A simple API for e-commerce analytics', doc='/swagger')

# Replace with your RDS connection details
db_config = {
    'host': 'mydb-instance.cn8kcow48xsh.eu-west-1.rds.amazonaws.com',
    'user': 'admin',
    'password': 'Kwame!1168',
    'database': 'assignment_db'
}

def execute_query(query):
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor(dictionary=True)
    cursor.execute(query)
    results = cursor.fetchall()
    cursor.close()
    conn.close()
    return results

# TopCustomers resource
@api.route('/top-customers')
class TopCustomers(Resource):
    def get(self):
        """Top spending customers"""
        query = """
            SELECT c.name, SUM(oi.quantity * oi.unit_price) AS total_spent
            FROM customers c
            JOIN orders o ON c.customer_id = o.customer_id
            JOIN order_items oi ON o.order_id = oi.order_id
            GROUP BY c.customer_id
            ORDER BY total_spent DESC;
        """
        return jsonify(execute_query(query))

# MonthlySales resource
@api.route('/monthly-sales')
class MonthlySales(Resource):
    def get(self):
        """Monthly sales grouped by month"""
        query = """
            SELECT DATE_FORMAT(o.order_date, '%Y-%m') AS month,
                   SUM(oi.quantity * oi.unit_price) AS total_sales
            FROM orders o
            JOIN order_items oi ON o.order_id = oi.order_id
            WHERE o.status IN ('Shipped', 'Delivered')
            GROUP BY month
            ORDER BY month;
        """
        return jsonify(execute_query(query))

# ProductsNeverOrdered resource
@api.route('/products-never-ordered')
class ProductsNeverOrdered(Resource):
    def get(self):
        """Products that were never ordered"""
        query = """
            SELECT p.name
            FROM products p
            LEFT JOIN order_items oi ON p.product_id = oi.product_id
            WHERE oi.product_id IS NULL;
        """
        return jsonify(execute_query(query))

# AvgOrderValue resource
@api.route('/avg-order-value')
class AvgOrderValue(Resource):
    def get(self):
        """Average order value grouped by country"""
        query = """
            SELECT country, AVG(order_total) AS avg_order_value
            FROM (
                SELECT c.country, o.order_id, SUM(oi.quantity * oi.unit_price) AS order_total
                FROM orders o
                JOIN customers c ON o.customer_id = c.customer_id
                JOIN order_items oi ON o.order_id = oi.order_id
                GROUP BY o.order_id, c.country
            ) AS order_summary
            GROUP BY country;
        """
        return jsonify(execute_query(query))

# FrequentBuyers resource
@api.route('/frequent-buyers')
class FrequentBuyers(Resource):
    def get(self):
        """Customers with more than 1 order"""
        query = """
            SELECT c.name, COUNT(o.order_id) AS order_count
            FROM customers c
            JOIN orders o ON c.customer_id = o.customer_id
            GROUP BY c.customer_id
            HAVING order_count > 1;
        """
        return jsonify(execute_query(query))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
