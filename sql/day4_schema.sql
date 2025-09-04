-- Schema: star model for orders analytics

-- Dimension: Customer
CREATE TABLE IF NOT EXISTS dim_customer (
  customer_key SERIAL PRIMARY KEY,
  customer_id INTEGER UNIQUE,
  city VARCHAR,
  signup_date DATE
);

-- Dimension: Date (day grain)
CREATE TABLE IF NOT EXISTS dim_date (
  date_key DATE PRIMARY KEY,
  year INTEGER,
  month INTEGER,
  day INTEGER,
  dow INTEGER
);

-- Fact: Orders (order-by-customer-by-day)
CREATE TABLE IF NOT EXISTS fact_orders (
  order_id INTEGER PRIMARY KEY,
  customer_key INTEGER NOT NULL REFERENCES dim_customer(customer_key),
  order_date DATE NOT NULL REFERENCES dim_date(date_key),
  amount DOUBLE PRECISION
);

-- Helpful indexes for joins and filtering
CREATE INDEX IF NOT EXISTS ix_fact_orders_customer_key ON fact_orders(customer_key);
CREATE INDEX IF NOT EXISTS ix_fact_orders_order_date ON fact_orders(order_date);
