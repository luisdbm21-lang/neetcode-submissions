SELECT
    e.left_operand,
    e.operator,
    e.right_operand,
    CASE 
        WHEN e.operator = '<' AND left_var.value < right_var.value THEN 'true'
        WHEN e.operator = '>' AND left_var.value > right_var.value THEN 'true'
        WHEN e.operator = '=' AND left_var.value = right_var.value THEN 'true'
        ELSE 'false'
    END AS value
FROM expressions e
JOIN variables left_var ON e.left_operand = left_var.name
JOIN variables right_var ON e.right_operand = right_var.name;