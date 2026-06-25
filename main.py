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
if diversification_score >= 85:
    health = "Excellent"
elif diversification_score >= 70:
    health = "Good"
elif diversification_score >= 50:
    health = "Moderate"
else:
    health = "Poor"

print(f"Portfolio Health: {health}")
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
print("\nPERIL-WISE EXPECTED LOSS")
print("=" * 50)

peril_risk = data.groupby(
    "Peril"
)["Expected_Loss"].sum()

print(peril_risk)
# Region-wise Risk Chart

region_risk.plot(
    kind="bar",
    title="Region-wise Expected Loss"
)

plt.ylabel("Expected Loss ($)")
plt.tight_layout()


print("\nPORTFOLIO ALLOCATION")
print("=" * 50)

allocation = (
    data["Investment"] / data["Investment"].sum()
) * 100

data["Allocation_Percentage"] = allocation

print(data[["Bond", "Allocation_Percentage"]])
print("\nBEST BOND RECOMMENDATION")
print("=" * 50)

best_bond = data.sort_values(
    by="Risk_Adjusted_Return",
    ascending=False
)

print(
    best_bond[
        ["Bond", "Region", "Risk_Adjusted_Return"]
    ].head(1)
)
print("\nRISK CATEGORY")
print("=" * 50)

data["Risk_Category"] = data[
    "Probability_of_Loss"
].apply(
    lambda x:
    "Low Risk" if x <= 0.02
    else "Medium Risk" if x <= 0.04
    else "High Risk"
)

print(
    data[
        ["Bond", "Risk_Category"]
    ]
)
plt.figure()

data.plot(
    kind="pie",
    y="Investment",
    labels=data["Bond"],
    autopct="%1.1f%%",
    legend=False
)

plt.title("Portfolio Allocation")
plt.ylabel("")
plt.figure(figsize=(7,7))

peril_risk.plot(
    kind="pie",
    autopct="%1.1f%%",
    title="Peril-wise Expected Loss Distribution"
)

plt.ylabel("")
plt.tight_layout()
print("\nPERIL RISK CONTRIBUTION (%)")
print("=" * 50)

peril_contribution = (
    peril_risk / peril_risk.sum()
) * 100

print(peril_contribution.round(2))
print("\nSTRESS TEST SCENARIO")
print("=" * 50)

stress_factor = 1.20

stressed_probability = (
    data["Probability_of_Loss"] * stress_factor
)

stressed_loss = (
    data["Investment"] *
    stressed_probability
).sum()

increase = stressed_loss - total_expected_loss

print(f"Current Expected Loss: ${total_expected_loss:,.0f}")
print(f"Stressed Expected Loss: ${stressed_loss:,.0f}")
print(f"Increase in Loss: ${increase:,.0f}")
print("\nREGION CONCENTRATION ANALYSIS")
print("=" * 50)

region_allocation = (
    data.groupby("Region")["Investment"].sum()
    / data["Investment"].sum()
) * 100

print(region_allocation.round(2))
plt.show()
print("\nEXPORTING REPORT TO EXCEL...")
print("=" * 50)

data.to_excel(
    "cat_bond_analysis_report.xlsx",
    index=False
)

print("Excel report created successfully!")