# Decode Labs — Project 2

Exploratory Data Analysis on a synthetic e-commerce dataset using pandas, matplotlib, and seaborn.

This was part of my internship at Decode Labs. The notebook loads order data from an Excel file and walks through basic EDA — bar charts for product sales and revenue, a pie chart for payment methods, a histogram for order quantities, and a correlation heatmap.

## Data

The notebook expects `Dataset for Data Analytics (2).xlsx` at the repo root. The file is not checked in — you'll need to provide it yourself if you want to run it.

Columns: OrderID, Date, CustomerID, Product, Quantity, UnitPrice, ShippingAddress, PaymentMethod, OrderStatus, TrackingNumber, ItemsInCart, CouponCode, ReferralSource, TotalPrice.

1200 rows of synthetic data.

## Running

Open in Google Colab and run all cells. No special setup needed — just pandas, matplotlib, and seaborn which are pre-installed in Colab.
