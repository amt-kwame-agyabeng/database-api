 -- Query to execute Top Customers by Spending
 SELECT c.name, SUM(oi.quantity * oi.unit_price) AS total_spent
            FROM customers c
            JOIN orders o ON c.customer_id = o.customer_id
            JOIN order_items oi ON o.order_id = oi.order_id
            GROUP BY c.customer_id
            ORDER BY total_spent DESC;

            
-- Query to execute Average Order Value by Country
SELECT country, AVG(order_total) AS avg_order_value
            FROM (
                SELECT c.country, o.order_id, SUM(oi.quantity * oi.unit_price) AS order_total
                FROM orders o
                JOIN customers c ON o.customer_id = c.customer_id
                JOIN order_items oi ON o.order_id = oi.order_id
                GROUP BY o.order_id, c.country
            ) AS order_summary
            GROUP BY country;


-- Query to execute Monthly Sales Report (Only Shipped/Delivered)
 SELECT DATE_FORMAT(o.order_date, '%Y-%m') AS month,
                   SUM(oi.quantity * oi.unit_price) AS total_sales
            FROM orders o
            JOIN order_items oi ON o.order_id = oi.order_id
            WHERE o.status IN ('Shipped', 'Delivered')
            GROUP BY month
            ORDER BY month;


-- Query to execute Products Never Ordered
SELECT p.name
            FROM products p
            LEFT JOIN order_items oi ON p.product_id = oi.product_id
            WHERE oi.product_id IS NULL;


-- Query to execute Frequent Buyers (More Than One Order)
SELECT c.name, COUNT(o.order_id) AS order_count
            FROM customers c
            JOIN orders o ON c.customer_id = o.customer_id
            GROUP BY c.customer_id
            HAVING order_count > 1;