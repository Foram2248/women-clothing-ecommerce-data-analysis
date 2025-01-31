import duckdb

# File paths
csv_file = "data/women_clothing_ecommerce_sales.csv"
output_file = "output/analysis_results.txt"

# Define DuckDB queries
queries = [
    # Query 1: Total revenue per product
    """
    SELECT sku, SUM(revenue) AS total_revenue, COUNT(order_id) AS total_orders
    FROM read_csv_auto('data/women_clothing_ecommerce_sales.csv')
    GROUP BY sku
    ORDER BY total_revenue DESC
    """,

    # Query 2: Most popular product sizes
    """
    SELECT size, COUNT(*) AS total_sold
    FROM read_csv_auto('data/women_clothing_ecommerce_sales.csv')
    GROUP BY size
    ORDER BY total_sold DESC
    """,

    # Query 3: Monthly sales trends
    """
    SELECT strftime(order_date, '%Y-%m') AS month, SUM(revenue) AS total_revenue
    FROM read_csv_auto('data/women_clothing_ecommerce_sales.csv')
    GROUP BY month
    ORDER BY month
    """,

    # Query 4: Average revenue per order by product size
    """
    SELECT size, AVG(revenue) AS avg_revenue
    FROM read_csv_auto('data/women_clothing_ecommerce_sales.csv')
    GROUP BY size
    ORDER BY avg_revenue DESC
    """,

    # Query 5: Identify the top 5 products contributing to revenue
    """
    SELECT sku, SUM(revenue) AS total_revenue
    FROM read_csv_auto('data/women_clothing_ecommerce_sales.csv')
    GROUP BY sku
    ORDER BY total_revenue DESC
    LIMIT 5
    """,

    # Query 6: Revenue distribution across colors
    """
    SELECT color, SUM(revenue) AS total_revenue, COUNT(*) AS total_sales
    FROM read_csv_auto('data/women_clothing_ecommerce_sales.csv')
    GROUP BY color
    ORDER BY total_revenue DESC
    """,

    # Query 7: Orders with revenue greater than the average revenue
    """
    WITH avg_revenue AS (
        SELECT AVG(revenue) AS avg_rev
        FROM read_csv_auto('data/women_clothing_ecommerce_sales.csv')
    )
    SELECT order_id, revenue
    FROM read_csv_auto('data/women_clothing_ecommerce_sales.csv'), avg_revenue
    WHERE revenue > avg_revenue.avg_rev
    ORDER BY revenue DESC
    """,

    # Query 8: Revenue trend over time (daily revenue breakdown)
    """
    SELECT strftime(order_date, '%Y-%m-%d') AS day, SUM(revenue) AS total_revenue
    FROM read_csv_auto('data/women_clothing_ecommerce_sales.csv')
    GROUP BY day
    ORDER BY day
    """,

    # Query 9: Median unit price by size
    """
    SELECT size, median(unit_price) AS median_price
    FROM read_csv_auto('data/women_clothing_ecommerce_sales.csv')
    GROUP BY size
    ORDER BY median_price DESC
    """,

    # Query 10: Correlation between quantity and revenue
    """
    SELECT corr(quantity, revenue) AS correlation_quantity_revenue
    FROM read_csv_auto('data/women_clothing_ecommerce_sales.csv')
    """
]

# Run queries and save results
with open(output_file, "w") as f:
    f.write("DuckDB Analysis Results:\n\n")
    
    for i, query in enumerate(queries, 1):
        # Execute the query
        result = duckdb.query(query).df()
        
        # Write results to the output file
        f.write(f"Query {i} Results:\n{result}\n\n")

print(f"Analysis complete. Results saved to {output_file}.")
