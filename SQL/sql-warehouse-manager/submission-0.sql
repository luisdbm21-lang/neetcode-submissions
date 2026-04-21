-- Write your query below
SELECT name AS warehouse_name, SUM(products.width * products.length * products.height * warehouse.units) AS volume
FROM warehouse
JOIN products ON warehouse.product_id = products.product_id
GROUP BY name