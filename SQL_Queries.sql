-- 1) Bar
SELECT
   customer_name as Name,
   COUNT(o.order_id) as Order_Quantity
FROM customers c
  INNER JOIN orders o ON o.customer_id = c.customer_id
GROUP BY customer_name
ORDER BY Order_Quantity ASC;

-- 2) Pie
SELECT
   e.first_name as Name,
   e.level as Level,
   SUM(p.price * d.quantity) as Amount
FROM employees e
  INNER JOIN orders o ON o.employee_id = e.employee_id
  INNER JOIN orderdetails d ON d.order_id = o.order_id
  INNER JOIN products p ON p.product_id = d.product_id
GROUP BY e.first_name, e.level
ORDER BY Amount DESC;

-- 3) Scatter
SELECT
  d.detail_id as ID,
  SUM(d.quantity * p.price) as Amount
FROM orderdetails d
  INNER JOIN products p ON p.product_id = d.product_id
GROUP BY d.detail_id
ORDER BY ID ASC;

-- 4) Line
SELECT
   COUNT(o.order_id) as Order_Quantity,
   SUM(d.quantity * p.price) as Total_Amount
FROM orders o
  INNER JOIN orderdetails d ON d.order_id = o.order_id
  INNER JOIN products p ON p.product_id = d.product_id
GROUP BY p.product_id;