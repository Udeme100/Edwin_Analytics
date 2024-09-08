# Import necessary libraries
import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

# Step 1: Create the dataset
data = {
    'Company': ['A', 'B', 'C', 'D', 'E'],
    'Inventory_Turnover_Ratio': [4, 2, 2, 4, 4],
    'Net_Profit_Margin': [15, 18, 13, 26, 18],
    'ROA': [6, 26, 20, 25, 1],
    'ROE': [18, 36, 25, 50, 13]
}

# Step 2: Convert the data to a pandas DataFrame
df = pd.DataFrame(data)

# Step 3: Correlation Analysis
# Exclude the 'Company' column, which contains non-numeric data
correlation_matrix = df[['Inventory_Turnover_Ratio', 'Net_Profit_Margin', 'ROA', 'ROE']].corr()
print("Correlation Matrix:")
print(correlation_matrix)

# Step 4: Define the independent variable (Inventory Turnover Ratio) and dependent variables (Net Profit Margin, ROA, ROE)
X = df[['Inventory_Turnover_Ratio']]
X = sm.add_constant(X)  # Add constant for intercept
y_npm = df['Net_Profit_Margin']
y_roa = df['ROA']
y_roe = df['ROE']

# Step 5: Fit the multilinear regression models
model_npm = sm.OLS(y_npm, X).fit()
model_roa = sm.OLS(y_roa, X).fit()
model_roe = sm.OLS(y_roe, X).fit()

# Step 6: Output the model summaries
print("\nNet Profit Margin Regression Summary:")
print(model_npm.summary())
print("\nROA Regression Summary:")
print(model_roa.summary())
print("\nROE Regression Summary:")
print(model_roe.summary())

# Step 7: Visualization - Pairplot to show relationships between variables
sns.pairplot(df)
plt.savefig('pairplot.png')
plt.show()

# Step 8: Scatter plots with regression line for each variable
fig, axes = plt.subplots(1, 3, figsize=(18, 6))

# Inventory Turnover vs Net Profit Margin
sns.regplot(x='Inventory_Turnover_Ratio', y='Net_Profit_Margin', data=df, ax=axes[0])
axes[0].set_title('Inventory Turnover vs Net Profit Margin')

# Inventory Turnover vs ROA
sns.regplot(x='Inventory_Turnover_Ratio', y='ROA', data=df, ax=axes[1])
axes[1].set_title('Inventory Turnover vs ROA')

# Inventory Turnover vs ROE
sns.regplot(x='Inventory_Turnover_Ratio', y='ROE', data=df, ax=axes[2])
axes[2].set_title('Inventory Turnover vs ROE')

plt.tight_layout()
plt.savefig('regression_plots.png')
plt.show()

# Step 9: t-tests for the relationship between variables
print("t-test results for Net Profit Margin and Inventory Turnover Ratio:")
t_stat_npm, p_val_npm = stats.ttest_ind(df['Net_Profit_Margin'], df['Inventory_Turnover_Ratio'])
print(f"t-statistic: {t_stat_npm}, p-value: {p_val_npm}")

print("t-test results for ROA and Inventory Turnover Ratio:")
t_stat_roa, p_val_roa = stats.ttest_ind(df['ROA'], df['Inventory_Turnover_Ratio'])
print(f"t-statistic: {t_stat_roa}, p-value: {p_val_roa}")

print("t-test results for ROE and Inventory Turnover Ratio:")
t_stat_roe, p_val_roe = stats.ttest_ind(df['ROE'], df['Inventory_Turnover_Ratio'])
print(f"t-statistic: {t_stat_roe}, p-value: {p_val_roe}")
