import duckdb
import matplotlib.pyplot as plt
import pandas as pd

# File paths
csv_file = "data/women_clothing_ecommerce_sales.csv"
output_file = "output/graph_analysis.txt"


# Define DuckDB queries
queries = {
    "Total Revenue by Product (Top 10)": """
        SELECT sku, SUM(revenue) AS total_revenue
        FROM read_csv_auto('data/women_clothing_ecommerce_sales.csv')
        GROUP BY sku
        ORDER BY total_revenue DESC
        LIMIT 10
    """,
    "Revenue Trend Over Time (Monthly)": """
        SELECT strftime(order_date, '%Y-%m') AS month, SUM(revenue) AS total_revenue
        FROM read_csv_auto('data/women_clothing_ecommerce_sales.csv')
        GROUP BY month
        ORDER BY month
    """,
    "Revenue Distribution Across Colors": """
        SELECT color, SUM(revenue) AS total_revenue
        FROM read_csv_auto('data/women_clothing_ecommerce_sales.csv')
        GROUP BY color
        ORDER BY total_revenue DESC
    """
}

# Create an empty dictionary to store results
results = {}

# Execute queries and save results
for query_name, query in queries.items():
    results[query_name] = duckdb.query(query).df()

# Write results to a text file
with open(output_file, "w") as f:
    f.write("DuckDB Analysis Results:\n\n")
    for query_name, result in results.items():
        f.write(f"{query_name}:\n{result}\n\n")

print(f"Analysis complete. Results saved to {output_file}.")
