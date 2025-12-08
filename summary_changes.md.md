# Summary of Data Cleaning – Superstore Dataset

This document summarizes all the cleaning steps performed on the dataset as part of Task 1.

---

## 1. Column Name Cleaning
- Trimmed extra spaces  
- Converted all column names to lowercase  
- Replaced spaces with underscores  
- Removed periods from names  

Example:
`"Order Date"` → `"order_date"`

---

## 2. Data Type Fixing
- Converted date columns (`order_date`, `ship_date`) into datetime format  
- Converted numeric columns (`sales`, `profit`, `quantity`, `discount`, `shipping_cost`) into numeric types

---

## 3. Handling Missing Values
- Filled missing `discount` with median  
- Filled missing `profit` with median  
- Replaced missing `state` and `country` with `"unknown"`

---

## 4. Removing Duplicates
- Dropped all duplicate rows from the dataset

---

## 5. Outlier Treatment (IQR Method)
Applied IQR rule on:
- `sales`
- `profit`

Removed rows outside:


---

## 6. Visualizations Created
- `sales_distribution.png`
- `profit_by_category.png`

---

## 7. Output
Final cleaned dataset saved at:
cleaned_superstore.csv 
