# Tableau – Superstore Sales Dashboard

An interactive Tableau dashboard exploring Superstore sales performance (2014–2017) across regions, product categories, and customer segments. Built for fast exploration, trend analysis, and executive-level insight.

## Project Overview

The dashboard provides filterable views of sales, profit, and quantity metrics. Key features include:

- Dynamic KPI cards with current vs. previous year comparisons  
- Monthly and weekly performance trends  
- Side-by-side sub-category comparisons for sales and profit  
- Cross-filtering and hover tooltips for deeper insights  
- A collapsible filter panel and year selector for user-driven exploration
- Dashboard styled using University of California’s secondary color palette to enhance consistency and visual clarity.

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
 
## Changelog

### Version 2.0 (April 2025)

> This release improves how the dashboard communicates insights — from more precise number formatting to corrected tooltips and refined color logic. These updates make trends and comparisons easier to interpret, supporting more confident decision-making.

#### Visual Design Improvements
- Unified color logic across all charts (e.g., pink for below-zero values, blue for current-year trends).
- Refined color behavior in **Weekly Sales & Profit Trends** charts: diverging colors now reflect actual financial loss (not just distance from the average), aligning visual cues with meaningful business impact.
- Added clear, intuitive labels to weekly chart legends (e.g., “⬤ Above $0” and “⬤ Below $0”) to reduce ambiguity and reinforce visual thresholds.
- Replaced static KPI cards with dynamic BANs that respond to user filters.
- Synchronized min/max indicators with small trend lines (sparklines) in KPI cards for accurate trend highlighting.
- Floated invisible tiles over interactive areas to prevent accidental clicks, ensuring a smoother user experience.

#### Interactivity Enhancements
- Added **Segment** to the filter panel and ensured all charts respond accordingly.
- Created floating legends for **Category** and **Region** with dynamic text and color-coded markers (e.g., blue for selected Category, pink for highlighted values).
- Created a title container that dynamically displays selected Region and Category filters (e.g., “Superstore Sales | 2017 | Office Supplies | West”).
- Enabled `Use as Filter` on key charts to support intuitive dashboard drill-downs (e.g., clicking on a sub-category filters the rest of the dashboard).

#### Calculated Fields & Logic
- Rebuilt the `Avg CY Sales` field due to duplication-related corruption; verified and replaced with a debug field.
- Fixed naming inconsistencies (e.g., removed trailing space in `PY Quantity`) that caused dependent calculations to break.
- Standardized % difference formatting (e.g., ▲0.0%, ▼-0.0%) to enhance at-a-glance comparisons across KPI titles, legends, and tooltips.
- Left debug fields and a test worksheet in the `.twbx` file for transparency and troubleshooting reference.

#### Usability & Polish
- Updated **weekly trend tooltips** for precision — showing current value, average, and exact difference in a consistent, easy-to-read format (e.g., “Week 23: $0.0K, Avg: $0.4K, Diff: -$0.4K”).
- Resolved tooltip discrepancies caused by aggregation vs. filtered totals.
- Locked down interaction zones using floating tiles to prevent accidental back-end access or highlighting.
- Updated `dashboard_demo.gif` to reflect the latest layout, including dynamic filters and category interactions.

## Portfolio Page

For a business-focused walkthrough and summary, visit my portfolio page:  
[Tableau Superstore Sales Dashboard](https://tonynick.notion.site/Tableau-Superstore-Sales-Dashboard-1ca9c67da0d480a6ad81fbc3b0add2b5)
