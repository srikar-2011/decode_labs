# AGENTS.md — srikarprojrcts

## What this is

Data analytics exercises for "Decode Labs." Two Jupyter notebooks (Google Colab) performing EDA on a synthetic e-commerce order dataset.

## Notebooks

- `Project_2_Decode_Labs (1).ipynb` — pandas EDA: bar plots, pie charts, histograms, correlation heatmap, seaborn.
- `project_3_DECODE_LABS.ipynb` — SQL-based EDA using `pandasql` (`sqldf`) with GROUP BY queries, filtering, aggregations.

## Data

- Both notebooks expect an `.xlsx` file at repo root (`Dataset for Data Analytics (2).xlsx` and `Dataset for Data Analytics (1).xlsx`).
- The `.xlsx` files are **not committed** to the repository. Notebooks will fail without them.
- The data is a synthetic 1200-row e-commerce order table with columns: `OrderID, Date, CustomerID, Product, Quantity, UnitPrice, ShippingAddress, PaymentMethod, OrderStatus, TrackingNumber, ItemsInCart, CouponCode, ReferralSource, TotalPrice`.

## Environment

- Designed for **Google Colab** (Python 3 kernel).
- `project_3` requires `pandasql` — installed via `!pip install pandasql` inside the notebook.
- No local toolchain, no tests, no linters, no package manager.
- No existing AGENTS.md, README, or config files.
