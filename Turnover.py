# Import necessary libraries
import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sns

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

# Step 3: Define the independent variables (Inventory Turnover Ratio, ROA, ROE)
X = df[['Inventory_Turnover_Ratio', 'ROA', 'ROE']]

# Step 4: Define the dependent variable (Net Profit Margin)
y = df['Net_Profit_Margin']

# Step 5: Add a constant (intercept) to the independent variables
X = sm.add_constant(X)

# Step 6: Fit the multilinear regression model
model = sm.OLS(y, X).fit()

# Step 7: Output the model summary
print(model.summary())

# Step 8: Visualization - Plot relationships between variables using pairplot
sns.pairplot(df)
plt.show()

# Step 9: Additional visualization (optional)
# This plot shows how each independent variable impacts the dependent variable
fig, axes = plt.subplots(1, 3, figsize=(18, 6))

# Inventory Turnover vs Net Profit Margin
sns.regplot(x='Inventory_Turnover_Ratio', y='Net_Profit_Margin', data=df, ax=axes[0])
axes[0].set_title('Inventory Turnover vs Net Profit Margin')

# ROA vs Net Profit Margin
sns.regplot(x='ROA', y='Net_Profit_Margin', data=df, ax=axes[1])
axes[1].set_title('ROA vs Net Profit Margin')

# ROE vs Net Profit Margin
sns.regplot(x='ROE', y='Net_Profit_Margin', data=df, ax=axes[2])
axes[2].set_title('ROE vs Net Profit Margin')

plt.tight_layout()
plt.show()
