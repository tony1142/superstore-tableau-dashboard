# Dataset Details – Tableau Superstore Dashboard

## Overview

This project uses the **Sample - Superstore.xls** dataset (2014–2017), a fictional retail dataset commonly used in Tableau training. It contains transaction-level sales data for customer orders, including location, product, and customer details.

The original Excel file included three sheets:  
- `Orders`: 9,994 rows  
- `Returns`: 296 rows  
- `People`: 4 rows

Only the `Orders` sheet was used for this Tableau project.

## Data Source

Original dataset from the Tableau Community:  
[Sample - Superstore Sales (Excel).xls](https://community.tableau.com/s/question/0D54T00000CWeX8SAL/sample-superstore-sales-excelxls)

## Data Preparation

The Excel file was cleaned and split into four CSVs using a custom Python script (../data/extract_superstore_csvs.py). Each file represents a clean logical table used in Tableau.

**Script Location:**  
`data/extract_superstore_csvs.py`

## Extracted Tables

### 1. Orders ([orders.csv](../data/orders.csv))
- Core transaction-level data
- Fields retained:  
  `Row ID`, `Order ID`, `Order Date`, `Ship Date`, `Ship Mode`, `Customer ID`, `Segment`, `Postal Code`, `Product ID`, `Sales`, `Quantity`, `Discount`, `Profit`

### 2. Customers (`customers.csv`)
- Fields:  
  `Customer ID`, `Customer Name`  
- Duplicates removed

### 3. Products (`products.csv`)
- Fields:  
  `Product ID`, `Product Name`, `Category`, `Sub-Category`  
- Duplicates removed

### 4. Location (`location.csv`)
- Fields:  
  `Postal Code`, `City`, `State`, `Region`  
- Duplicates removed  

## Notes

- All CSVs were imported into Tableau and modeled using standard relationships
- Data types were verified and adjusted manually in Tableau
- No joins or blending were done in Python — the structure was designed for visual modeling in Tableau
- The dataset was kept intentionally simple to focus on key KPIs and performance insights

---

## Summary

This dataset was restructured to support clean, filterable Tableau visualizations focused on sales, profit, and customer performance. All transformations were done using Python for reproducibility and clarity.

---

Special thanks to Baraa Khatib Salkini for his inspiration and excellent tableau instructional materials (LinkedIn: [baraa-khatib-salkini](https://www.linkedin.com/in/baraa-khatib-salkini)).

---

## Portfolio Page

For a walkthrough and project summary, visit:  
[Tableau Superstore Sales Dashboard](https://tonynick.notion.site/Tableau-Superstore-Sales-Dashboard-1ca9c67da0d480a6ad81fbc3b0add2b5)
