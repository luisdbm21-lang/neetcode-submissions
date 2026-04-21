-- Write your query below
SELECT c.customer_id, c.customer_name
FROM customers c
WHERE 
    c.customer_id IN (
        SELECT c.customer_id
        FROM customers c
        JOIN orders o ON c.customer_id = o.customer_id
        WHERE o.product_name = 'A'
    )
AND
    c.customer_id IN (
        SELECT c.customer_id
        FROM customers c
        JOIN orders o ON c.customer_id = o.customer_id
        WHERE o.product_name = 'B'
    )
AND
    c.customer_id NOT IN (
        SELECT c.customer_id
        FROM customers c
        JOIN orders o ON c.customer_id = o.customer_id
        WHERE o.product_name = 'C'
)
ORDER BY c.customer_name