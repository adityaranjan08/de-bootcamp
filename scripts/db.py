import duckdb

# connect to duckdb database (or create it if it doesn't exist)
con = duckdb.connect('mydb.duckdb')


# run a query
result = con.execute("SELECT 42 AS answer").fetchall()
print(result)


# example data creation

con.execute("""
CREATE TABLE IF NOT EXISTS orders (
  order_id INTEGER,
  customer_id INTEGER,
  order_date DATE,
  amount DOUBLE
);
""")

con.execute("""
CREATE TABLE IF NOT EXISTS customers (
            customer_id INTEGER,
             city VARCHAR, 
            signup_date DATE
            );
""")



con.execute("""
INSERT INTO orders VALUES 
(1, 10, '2025-07-01',120.0),
(2, 20, '2025-07-02',80.0),
(3, 10, '2025-07-03',200.0),
(4, 30, '2025-07-04',50.0); 
""")

con.execute("""
INSERT INTO customers VALUES 
(10, 'New York', '2024-01-15'),
(20, 'Los Angeles', '2024-02-20'),
(30, 'Chicago', '2024-03-25');
""")

print(con.execute("SELECT * FROM orders").fetchall())
print(con.execute("SELECT * FROM customers").fetchall())


## Basic selection and filtering
print("Orders with amount > 100:")
con.execute("""
SELECT order_id, amount
FROM orders
WHERE amount >= 100
ORDER BY amount DESC
LIMIT 5;
""")

print(con.fetchall())

print("Total amount per customer:")
## join with lookup table
con.execute("""
SELECT o.order_id, c.city, o.amount
FROM orders o 
LEFT JOIN customers c USING (customer_id);
""")
print(con.fetchall())