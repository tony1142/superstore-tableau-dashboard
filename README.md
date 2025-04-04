# Tableau – Superstore Sales Dashboard

An interactive Tableau dashboard exploring Superstore sales performance (2014–2017) across regions, product categories, and customer segments. Built for fast exploration, trend analysis, and executive-level insight.

## Project Overview

The dashboard provides filterable views of sales, profit, and quantity metrics. Key features include:

- Dynamic KPI cards with current vs. previous year comparisons  
- Monthly and weekly performance trends  
- Side-by-side sub-category comparisons for sales and profit  
- Cross-filtering and hover tooltips for deeper insights  
- A collapsible filter panel and year selector for user-driven exploration

## Explore the Dashboard
1. Download the Tableau workbook: [tableau_superstore_dashboard_v10.twbx](tableau/tableau_superstore_dashboard_v10.twbx) 
2. Open it in Tableau Desktop (version 2021.4 or later recommended)  
3. Click any chart element to cross-filter and reveal detailed insights  
4. Click the **funnel icon** to open the filter panel and explore by segment, region, category, and more

## Dataset

The dataset is the **Sample - Superstore.xls** sales data (2014–2017). It was cleaned and separated into four logical tables:

- **Orders** – Sales transactions  
- **Customers** – Customer ID and name  
- **Products** – Product and category details  
- **Location** – Region, state, city, and postal code  

For detailed structure and transformation notes, see [tableau_dataset_details.md](data/tableau_dataset_details.md)

## Repository Structure

- **tableau/** – Tableau workbook and dashboard visuals  
  - [tableau_superstore_dashboard_v10.twbx](tableau/tableau_superstore_dashboard_v10.twbx) – Final interactive dashboard  
  - [Screenshots/](tableau/Screenshots/) – Portfolio visuals and demo images  
  - [dashboard_demo.gif](tableau/dashboard_demo.gif) – Animated preview of the dashboard  
- **data/** – Cleaned CSVs and supporting Python script  
  - [customers.csv](data/customers.csv), [orders.csv](data/orders.csv), [products.csv](data/products.csv), [location.csv](data/location.csv)  
  - [extract_superstore_csvs.py](data/extract_superstore_csvs.py) – Python script used to generate the cleaned datasets  
  - [tableau_dataset_details.md](data/tableau_dataset_details.md) – Dataset structure and transformation notes  
- **docs/** – Supporting documentation  
  - [calculated_fields.md](docs/calculated_fields.md) – Key calculated fields used in the dashboard

## Portfolio Page

For a business-focused walkthrough and summary, visit my portfolio page:  
[Tableau Superstore Sales Dashboard](https://tonynick.notion.site/Tableau-Superstore-Sales-Dashboard-1ca9c67da0d480a6ad81fbc3b0add2b5)
