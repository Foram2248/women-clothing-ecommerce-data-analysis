# Women Clothing E-commerce Sales Analysis

## Introduction
This project analyzes sales data from a women's clothing e-commerce store using DuckDB. The analysis includes revenue trends, product popularity, and customer purchasing patterns.

## Features
- **Total Revenue Analysis**: Identify top-selling products by revenue.
- **Size Popularity**: Determine which clothing sizes sell the most.
- **Monthly Sales Trends**: Analyze revenue trends over time.
- **Revenue per Order**: Compute average revenue per order for different sizes.
- **Top 5 Revenue-Contributing Products**: Identify best-selling products.
- **Revenue by Color**: Understand sales distribution by color.
- **High Revenue Orders**: List orders generating above-average revenue.
- **Daily Revenue Trends**: Track revenue fluctuations over time.
- **Median Unit Price by Size**: Identify pricing trends.
- **Revenue and Quantity Correlation**: Measure correlation between quantity sold and revenue.

## Technology Stack
- **Python**
- **DuckDB**
- **CSV Data Processing**

## Installation
Ensure you have Python installed along with DuckDB.

```bash
pip install duckdb pandas
```

## Usage
1. Place the dataset in the `data/` folder.
2. Run the analysis script to generate insights:

```bash
python analysis_script.py
```

3. Results will be saved in the `output/` folder.

## Importing DuckDB
This project uses DuckDB to run SQL queries on CSV data efficiently.

```python
import duckdb
```
