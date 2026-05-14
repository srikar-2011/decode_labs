# Decode Labs — EDA Exercises

Two notebooks I made during my internship at Decode Labs. Both do exploratory data analysis on the same synthetic e-commerce dataset but take different approaches.

## Notebooks

**Project 2** — `Project_2_Decode_Labs (1).ipynb`
Uses pandas and matplotlib/seaborn. Has bar charts for product sales and revenue, a pie chart for payment methods, a histogram for quantity distribution, and a correlation heatmap at the end.

**Project 3** — `project_3_DECODE_LABS.ipynb`
Same data but queried through SQL via the `pandasql` library. Uses GROUP BY, filtering, and ORDER BY to answer the same kind of questions — product counts, revenue by product, payment method breakdown, order status totals, and filtering by a specific product.

## Data

Both notebooks load an `.xlsx` file from the repo root. The files are not checked in — you'll need to place them yourself if you want to run the notebooks.

- Project 2 expects: `Dataset for Data Analytics (2).xlsx`
- Project 3 expects: `Dataset for Data Analytics (1).xlsx`

The dataset is about 1200 rows of synthetic order data with columns like OrderID, Date, Product, Quantity, UnitPrice, PaymentMethod, OrderStatus, TotalPrice, etc.

## Running

Open either notebook in Google Colab and run the cells. Project 3 installs `pandasql` via pip inside the first cell. That's it — no other setup needed.

## What I noticed

- Products are fairly evenly distributed in count, but revenue varies more
- Digital payment methods are the most common
- Most orders are small (1-2 items per order)
- Quantity and total price are correlated (expected, but the heatmap confirms it)
- Order statuses are spread pretty evenly across delivered, shipped, pending, returned, cancelled — the dataset looks like it was generated to be balanced rather than realistic
