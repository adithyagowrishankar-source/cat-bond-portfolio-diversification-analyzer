PROJECT OVERVIEW


The Cat Bond Portfolio Diversification Analyzer is a Python-based financial risk analytics tool designed to evaluate catastrophe bond portfolios. The project helps investors and risk managers assess portfolio diversification, estimate expected losses, identify concentration risks, perform stress testing, and generate analytical reports.
The analyzer processes catastrophe bond data from a CSV file, calculates key risk metrics, visualizes portfolio exposures, and exports results to Excel for further analysis.


FEATURES


>>Import catastrophe bond portfolio data from CSV

>>Calculate Expected Loss for each bond

>>Calculate Risk-Adjusted Return

>>Portfolio Diversification Analysis

>>Portfolio Health Rating

>>Region-wise Risk Analysis

>>Peril-wise Risk Analysis

>>Risk Ranking of Bonds

>>Portfolio Allocation Analysis

>>Best Bond Recommendation

>>Risk Category Classification

>>Stress Testing Scenario Analysis

>>Region Concentration Analysis

>>Bar Chart Visualization

>>Portfolio Allocation Pie Chart

>>Peril Distribution Pie Chart

>>Excel Report Export


SOFTWARES USED


>>Python 3

>>Pandas

>>Matplotlib

>>OpenPyXL

>>Git

>>GitHub


PROJECT STRUCTURE

CatBond-Portfolio-Diversification-Analyzer/ 

├── main.py 

├── portfolio_data.csv 

├── cat_bond_analysis_report.xlsx 

├── requirements.txt 

└── README.md


SAMPLE OUTPUT

PORTFOLIO SUMMARY
=============================================

Total Investment: $3,600,000

Total Expected Loss: $120,000

Number of Regions: 4

Number of Perils: 5

Diversification Score: 90/100

Portfolio Health: Excellent

STRESS TEST SCENARIO
=============================================
Current Expected Loss: $120,000

Stressed Expected Loss: $144,000

Increase in Loss: $24,000

REGION CONCENTRATION ANALYSIS
=============================================
Australia  -  19.44%

Europe     -  16.67%

Japan      -  22.22%

USA        -  41.67%


VISUALIZATIONS

The project generates:

Region-wise Expected Loss Bar Chart

Portfolio Allocation Pie Chart

Peril-wise Expected Loss Distribution Pie Chart


HOW TO RUN:

1. Clone the Repository
git clone <repository-url>

2. Navigate to the Project Folder
cd CatBond-Portfolio-Diversification-Analyzer

3. Install Dependencies
pip install -r requirements.txt

4. Run the Program
python3 main.py

5. View Results
The program will:
Display portfolio analytics in the terminal

Generate charts

Export an Excel report named:

cat_bond_analysis_report.xlsx


