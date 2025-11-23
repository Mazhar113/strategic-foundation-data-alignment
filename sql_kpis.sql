-- KPI SQL scripts (Postgres-compatible)
-- 1) Monthly revenue by segment
CREATE OR REPLACE VIEW vw_revenue_month_segment AS
SELECT DATE_TRUNC('month', order_date)::date AS month, c.segment, SUM(order_value) AS revenue
FROM orders o JOIN customers c USING (customer_id)
GROUP BY 1,2;

-- 2) Monthly churn rate
WITH prev AS (
  SELECT DATE_TRUNC('month', order_date)::date AS month, customer_id FROM orders GROUP BY 1,2
)
SELECT p.month AS month,
  (COUNT(DISTINCT p.customer_id) - COUNT(DISTINCT c.customer_id))::float / NULLIF(COUNT(DISTINCT p.customer_id),0) AS churn_rate
FROM prev p
LEFT JOIN prev c ON p.month = c.month - INTERVAL '1 month' AND p.customer_id = c.customer_id
GROUP BY 1 ORDER BY 1;

-- 3) Inventory value by month and location
CREATE OR REPLACE VIEW vw_inventory_value AS
SELECT DATE_TRUNC('month', date)::date AS month, location, SUM(on_hand_qty * unit_cost) AS inventory_value
FROM inventory
GROUP BY 1,2;