# CodeOrbit_Sales_Data_Analysis
sales analysis projects using Pandas for my CodeOrbit Tech Data Analyst Internship. 
Pandas analysis with Excel outputs 
sales_data.csv — sample sales dataset. 
Sales_Data_Analysis.xlsx — workbook containing summaries, grouped tables, and charts. 
Sales_Analysis_Report.docx — short analysis report.

## Project 2: Sales Data Analysis with Pandas
A sample sales dataset (250 orders, 4 categories, 4 regions, 12 months) is analyzed with pandas to calculate key metrics, identify top products, and summarize trends by category, region, and time period.

**Key findings:** Total sales of $54,966.02 across 250 orders (avg order value $219.86). Furniture drives 67.1% of revenue; the South region leads sales; Q2 was the strongest quarter.

**Files:**
- `make_sales_data.py` — generates the raw sample dataset
- `analyze_sales.py` — main analysis script (metrics, groupings, pivot table)
- `build_sales_excel.py` — builds the formatted Excel deliverable with charts
- `sales_data.csv` — raw sample sales dataset
- `analysis_log.txt` — auto-generated log of all metrics and summaries
- `Sales_Data_Analysis.xlsx` — Excel workbook: summary, raw data, grouped tables, charts
- `Sales_Analysis_Report.docx` — short findings report

**Run it:**
```bash
python make_sales_data.py     # (optional) regenerate raw sample data
python analyze_sales.py       # run the analysis
python build_sales_excel.py   # (optional) rebuild the Excel workbook
```
## Technologies Used
- Python 3.12
- pandas — data manipulation, cleaning, and analysis
- openpyxl — Excel workbook formatting and charts
- NumPy — synthetic data generation

## Setup Instructions

1. **Clone the repository**
   ```bash
   git clone <YOUR_GITHUB_REPO_LINK>
   cd data-cleaning-internship-task
   ```

2. **Install dependencies**
   ```bash
   pip install pandas numpy openpyxl
   ```

3. **Run either project** using the commands listed above.
