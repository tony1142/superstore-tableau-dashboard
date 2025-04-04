
# Calculated Fields – Tableau Superstore Dashboard

This document summarizes the key calculated fields used to power KPIs, dynamic behavior, trend analysis, and tooltips in the Tableau dashboard.

---

## 🔹 Year-Based Comparisons

### **Current Year**
```tableau
YEAR([Order Date]) = [Select Year]
```

### **Previous Year**
```tableau
YEAR([Order Date]) = [Select Year] - 1
```

### **CY Sales / PY Sales**
```tableau
IF YEAR([Order Date]) = [Select Year] THEN [Sales] END
IF YEAR([Order Date]) = [Select Year] - 1 THEN [Sales] END
```

### **% Difference in Sales**
```tableau
(SUM([CY Sales]) - SUM([PY Sales])) / ABS(SUM([PY Sales]))
```

---

## 🔹 Weekly Trends Logic

### **Avg CY Sales**
```tableau
WINDOW_AVG(SUM([CY Sales]))
```

### **Above/Below Benchmark (Sales)**
```tableau
IF SUM([CY Sales]) > WINDOW_AVG(SUM([CY Sales]))
THEN 'above'
ELSE 'below'
END
```

### **Min/Max Weekly Values (Profit, Sales)**
```tableau
IF SUM([CY Profit]) = WINDOW_MAX(SUM([CY Profit]))
THEN 'Max'
ELSEIF SUM([CY Profit]) = WINDOW_MIN(SUM([CY Profit]))
THEN 'Min'
END
```

---

## 🔹 KPI Cards & BANs

### **Total CY Profit**
```tableau
SUM([CY Profit])
```

### **Filtered % Diff Profit**
```tableau
(SUM([CY Profit]) - SUM([PY Profit])) / ABS(SUM([PY Profit]))
```

### **Filtered $ Diff in Profit**
```tableau
SUM([CY Profit]) - SUM([PY Profit])
```

> These values update based on user filters and are used in dynamic titles and tooltips.

---

## 🔹 Tooltip-Specific Fields

### **Debug Field (for validation)**
```tableau
SUM([CY Sales]) - WINDOW_AVG(SUM([CY Sales]))
```

Used to troubleshoot tooltip logic and visual alignment in trend charts.

---

## Notes

- All fields were tested for compatibility with filters and parameter selections.
- Curly bracket `{}` expressions were avoided in favor of flexible filtering logic.
- Detail or Tooltips shelf was used for tooltip values to avoid chart clutter.

---

## Visual Formatting Details

### Custom Formatting – % Differences
Used in the KPI cards and tooltips to visually emphasize performance direction.

**Format used:**
▲ 0.0%; ▼ -0.0%;

This displays:
- Upward arrows (`▲`) for positive differences  
- Downward arrows (`▼`) for negative differences  
- Values rounded to one decimal place

---

### Custom Formatting – Category Legends & Labels
Used for consistent legend styling and sub-headings.

**Format used:**
⬤ Above   ⬤ Below

The bullet circles (`⬤`) are Unicode characters used to give the impression of labeled indicators. These were placed in legends and titles to reflect conditional color formatting (distinguishing Weekly Profit above or below $0, or flagging sub-category sales that declined compared to the previous year).

*Created by Tony Nick*
