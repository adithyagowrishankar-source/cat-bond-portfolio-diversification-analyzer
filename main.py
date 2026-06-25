import pandas as pd
import matplotlib.pyplot as plt

# Load data
data = pd.read_csv("portfolio_data.csv")

print("CAT BOND PORTFOLIO DIVERSIFICATION ANALYZER")
print("=" * 50)

print("\nPortfolio Data:")
print(data)

# Expected Loss Calculation
data["Expected_Loss"] = (
    data["Investment"] * data["Probability_of_Loss"]
)

# Risk Adjusted Return
data["Risk_Adjusted_Return"] = (
    data["Expected_Return"] - data["Probability_of_Loss"]
)

print("\nPortfolio Analysis:")
print(data[[
    "Bond",
    "Region",
    "Peril",
    "Expected_Loss",
    "Risk_Adjusted_Return"
]])

# Portfolio Summary
total_investment = data["Investment"].sum()
total_expected_loss = data["Expected_Loss"].sum()

# Diversification Metrics
unique_regions = data["Region"].nunique()
unique_perils = data["Peril"].nunique()

# Diversification Score
diversification_score = ((unique_regions + unique_perils) / 10) * 100

if diversification_score > 100:
    diversification_score = 100

print("\nPORTFOLIO SUMMARY")
print("=" * 50)
print(f"Total Investment: ${total_investment:,.0f}")
print(f"Total Expected Loss: ${total_expected_loss:,.0f}")
print(f"Number of Regions: {unique_regions}")
print(f"Number of Perils: {unique_perils}")
print(f"Diversification Score: {diversification_score:.0f}/100")
# Region-wise Risk Analysis
print("\nREGION-WISE EXPECTED LOSS")
print("=" * 50)

region_risk = data.groupby("Region")["Expected_Loss"].sum()

print(region_risk)
# Risk Ranking
print("\nRISK RANKING")
print("=" * 50)

risk_ranking = data.sort_values(
    by="Expected_Loss",
    ascending=False
)

print(
    risk_ranking[
        ["Bond", "Region", "Expected_Loss"]
    ]
)
# Region-wise Risk Chart

region_risk.plot(
    kind="bar",
    title="Region-wise Expected Loss"
)

plt.ylabel("Expected Loss ($)")
plt.tight_layout()

plt.show()