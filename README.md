# Retail Sales Analysis 📊

A Python-based data analysis project that explores retail sales data to identify revenue trends, top-performing suppliers, monthly sales performance, and product category insights.

This project uses **Python, Pandas, and NumPy** to clean, process, aggregate, and analyse retail sales data, transforming raw records into meaningful business insights.

## 📌 Project Overview

The objective of this project is to analyse retail sales transactions and understand sales performance across different suppliers, months, and item categories.

The analysis focuses on identifying:
- Top-performing suppliers based on retail sales.
- Monthly revenue distribution and performance.
- Best-performing item types.
- Overall sales statistics and distribution.
- Months with above-average revenue.
- High-value sales records within the top 1%.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Data analysis and processing |
| Pandas | Data cleaning and manipulation |
| NumPy | Numerical operations and statistical analysis |

## 📂 Project Structure

```text
retail-sales-analysis/
│
├── data/
│   └── Dataset.csv
│
├── src/
│   └── analysis.py
│
├── requirements.txt
│
└── README.md
```

## 📊 Dataset Information

The project uses a retail sales dataset containing **30,000 records and 9 columns**.

| Column | Description |
|---|---|
| YEAR | Year of the transaction |
| MONTH | Month of the transaction |
| SUPPLIER | Supplier name |
| ITEM CODE | Unique item identifier |
| ITEM DESCRIPTION | Product description |
| ITEM TYPE | Product category |
| RETAIL SALES | Retail sales quantity |
| RETAIL TRANSFERS | Number of retail transfers |
| WAREHOUSE SALES | Warehouse sales quantity |

**Data period:** 2020

## ⚙️ Key Analysis Performed

### 1. Data Cleaning and Preprocessing
- Loaded the dataset using Pandas.
- Removed records with missing supplier, month, item type, or retail sales values.
- Converted month values into integers.
- Converted retail sales into numeric format.
- Replaced invalid retail sales values with zero.

### 2. Supplier Performance Analysis
- Calculated total retail sales for each supplier.
- Identified the top 10 suppliers based on sales.
- Determined the highest-performing supplier.

### 3. Monthly Sales Analysis
- Calculated total sales for each month.
- Identified the best-performing month.
- Compared monthly sales against average monthly revenue.

### 4. Item Category Analysis
- Aggregated sales across different item types.
- Identified the best-performing item category.

### 5. Statistical Analysis
Calculated the following statistical measures:

- Mean
- Median
- Standard deviation
- Minimum value
- Maximum value

These statistics were calculated for both the complete sales array and non-zero sales values.

### 6. High-Value Sales Identification
- Calculated the 99th percentile of non-zero sales.
- Identified sales records exceeding this threshold.
- Displayed the corresponding supplier, month, item type, and sales value.

## 🚀 Getting Started

Follow these steps to run the project locally.

### 1. Clone the Repository

```bash
git clone https://github.com/neelsoni3/retail-sales-analysis.git
```

### 2. Navigate to the Project Directory

```bash
cd retail-sales-analysis
```

### 3. Create a Virtual Environment (Optional)

```bash
python -m venv venv
```

Activate it:

**Windows:**
```bash
venv\Scripts\activate
```

**Linux / macOS:**
```bash
source venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the Analysis

First, ensure the dataset path in `src/analysis.py` is:

```python
df = pd.read_csv("data/Dataset.csv")
```

Then execute the script from the project root:

```bash
python src/analysis.py
```

## 📦 Dependencies

The project requires:

```text
pandas
numpy
```

## 📈 Expected Results

After executing the analysis script, the program displays:

- Total number of records.
- Available years in the dataset.
- Number of unique suppliers and item types.
- Sales array dimensions.
- Total retail sales.
- Top 10 suppliers by revenue.
- Monthly sales totals.
- Sales totals by item category.
- Best-performing supplier, item type, and month.
- Overall statistical summaries.
- Above-average sales months.
- Top 1% high-value sales records.

## 🎯 Project Objectives

This project demonstrates practical skills in:

- Data cleaning and preprocessing.
- Exploratory data analysis (EDA).
- Data aggregation and grouping.
- Numerical computing with NumPy.
- Statistical analysis.
- Business-oriented data interpretation.
- Working with structured CSV datasets.

## 👨‍💻 Author

**Neel Soni**

---

⭐ If you find this project useful, consider giving the repository a star!
