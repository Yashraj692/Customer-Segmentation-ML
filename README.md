# 🧠 Customer Segmentation using RFM & K-Means Clustering

This machine learning project segments e-commerce customers based on their purchase behavior using **RFM analysis** and **K-Means clustering**.

---

## 📦 Dataset

- Source: Online Retail dataset (Kaggle)
- Columns used: `CustomerID`, `InvoiceDate`, `Quantity`, `UnitPrice`

📁 **Note:** The dataset has been compressed to stay within GitHub's file size limit.  
Please **download and extract `data.zip`** before running the notebook.

---

## 🔧 Process Overview

### ✅ Step 1: Data Cleaning
- Removed returns (negative quantity)
- Handled missing values in `CustomerID`

### ✅ Step 2: Feature Engineering
- Created `Revenue = Quantity × UnitPrice`
- Calculated Recency, Frequency, and Monetary values for each customer

### ✅ Step 3: Clustering
- Normalized RFM data using `StandardScaler`
- Applied **K-Means (n=4)** to segment customers

### ✅ Step 4: Visualization
- Plotted clusters using `Seaborn` scatter plots
- Exported results to Excel for optional Power BI use

---

## 📁 Files Included

- `data.zip` – Compressed dataset (extract to use)
  

---

## 📊 Tools & Libraries

- Python: `Pandas`, `Scikit-learn`, `Matplotlib`, `Seaborn`
- Machine Learning: `KMeans`, `StandardScaler`
- Business Concepts: RFM Analysis, Customer Segmentation

---

## 💼 Business Use Case

This segmentation helps marketing and product teams:
- Identify high-value customers for loyalty campaigns
- Re-engage churned or at-risk customers
- Allocate budgets effectively for each segment

---
