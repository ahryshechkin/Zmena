from sqlglot import parse_one

ast = parse_one("""
SELECT customer_id, SUM(amount)
FROM sales
GROUP BY customer_id
""")

print(ast)
