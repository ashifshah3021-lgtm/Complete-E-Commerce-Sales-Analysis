# %%
import kagglehub


path = kagglehub.dataset_download("erfan4524/e-commerce-sales-data-analysis-and-eda")

print("Path to dataset files:", path)

# %%
import  pandas as pd
df= pd.read_csv('clean_final_data.csv')
print(df.head())

# %%
# Remove rows with negative sales values
original_rows = len(df)
df = df[df["Sales"] >= 0].copy()

print(f"Removed {original_rows - len(df)} rows with negative Sales values.")
print(f"Remaining rows: {len(df)}")

# %%
# 1. Number of rows and 2. Number of columns
print("=== SHAPE (Rows, Columns) ===")
print(f"Rows: {df.shape[0]}, Columns: {df.shape[1]}")
print("\n" + "="*40 + "\n")

# 3. Column names & 4. Data types
print("=== COLUMN NAMES & DATA TYPES ===")
print(df.dtypes)
print("\n" + "="*40 + "\n")

# 5. Summary statistics for numerical columns
print("=== SUMMARY STATISTICS ===")
print(df.describe())
print("\n" + "="*40 + "\n")

# 6. Unique values in categorical columns
print("=== UNIQUE VALUES IN CATEGORICAL COLUMNS ===")
categorical_cols = df.select_dtypes(include=['object', 'category']).columns

for col in categorical_cols:
    print(f"\nUnique values in '{col}':")
    print(df[col].unique())

print("\n" + "="*40 + "\n")

# 7. First 5 rows
print("=== FIRST 5 ROWS ===")
df.head()

# %%
import matplotlib.pyplot as plt
df['OrderDate'] = pd.to_datetime(df['OrderDate'])
df['Month'] = df['OrderDate'].dt.to_period('M')
monthly_sales = df.groupby('Month')['Sales'].sum().reset_index()

monthly_sales['Month'] = monthly_sales['Month'].astype(str)
highest_month = monthly_sales.loc[monthly_sales['Sales'].idxmax()]
lowest_month = monthly_sales.loc[monthly_sales['Sales'].idxmin()]
print(f"Highest sales month: {highest_month['Month']} with sales of {highest_month['Sales']}")
print(f"Lowest sales month: {lowest_month['Month']} with sales of {lowest_month['Sales']}")

plt.figure(figsize=(8, 6))
plt.plot(monthly_sales['Month'], monthly_sales['Sales'], marker='o' , linestyle='-', color='black')
plt.xlabel('Month', fontsize=12,color='red')
plt.ylabel('Sales', fontsize=12,color='red')
plt.title('Monthly Sales Trend', fontsize=15, fontweight='bold', color='red')
plt.xticks(rotation=60)
plt.tight_layout()
plt.show()

# %%
category_revenue = df.groupby('Category')['Sales'].sum().reset_index()
category_revenue = category_revenue.sort_values(by='Sales', ascending=False)
top_category = category_revenue.iloc[0]
last_category=category_revenue.iloc[-1]
print(f"Top category: {top_category['Category']} with revenue of {top_category['Sales']}")
print(f"last category: {last_category['Category']} with revenue of {last_category['Sales']}")
plt.figure(figsize=(8, 6))
bars = plt.bar(category_revenue['Category'], category_revenue['Sales'], color='skyblue', edgecolor='black')
bars[0].set_color('steelblue'),bars[1].set_color('orange')
for bar in bars:
    height = bar.get_height()
    plt.text(
        bar.get_x() + bar.get_width() / 2.0,  
        height,                                
        f'{height:,.0f}',                     
        ha='center', va='bottom',              
        fontsize=10, fontweight='bold', color='black')
plt.xlabel('Category', fontsize=12, color='red')
plt.ylabel('Sales', fontsize=12, color='red')
plt.title('Category-wise Sales', fontsize=15, fontweight='bold', color='red')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# %%
import pandas as pd
import matplotlib.pyplot as plt

# 1. Deduplicate by Customer_ID so each customer is counted only once


# 2. Count unique customers for New and Repeated types
customer_counts = df['CustomerSegment'].value_counts().reset_index()
customer_counts.columns = ['CustomerSegment', 'Count']

# 3. Calculate Percentage
total_unique_customers = customer_counts['Count'].sum()
customer_counts['Percentage'] = (customer_counts['Count'] / total_unique_customers) * 100

# 4. Separate and print exact results
print("=== NEW vs REPEATED CUSTOMERS BREAKDOWN ===")
for _, row in customer_counts.iterrows():
    print(f"{row['CustomerSegment']} Customers: {row['Count']} ({row['Percentage']:.2f}%)")

print("\nTotal Unique Customers:", total_unique_customers)
print("\n" + "="*40 + "\n")

# 5. Visual Bar Chart showing Count & Percentage
plt.figure(figsize=(7, 5))
pies = plt.pie(customer_counts['Count'],labels=customer_counts['CustomerSegment'], colors=['#4C72B0', '#55A868','red'],autopct='%1.1f%%',)

# Label each bar with exact Count and Percentage


plt.title('New vs Repeated Customers (Unique)', fontsize=14, fontweight='bold')
plt.xlabel('Customer Type', fontsize=12)
plt.ylabel('Number of Unique Customers', fontsize=12)



plt.show()

# %%
status= df['Status'].value_counts().reset_index()
status.columns=['Status','Count']
total=status['Count'].sum()
status['Average']=(status['Count']/total)*100




print(status)
plt.Figure(figsize=(8,8))
plt.pie(status['Count'],autopct='%1.1f%%',labels=status['Status'],colors=['red','green','lightblue'])
plt.title('Status',color='blue',fontsize=23)
plt.tight_layout
plt.show

# %%
product_count=df['PaymentMethod'].value_counts().reset_index()
top_method= product_count.loc[product_count['count'].idxmax()]
least_method=product_count.loc[product_count['count'].idxmin()]
print(f"Highest method to payment: {top_method['PaymentMethod']}: with the number of {top_method['count']} transactions")
print(f"Highest method to payment: {least_method['PaymentMethod']}: with the number of {least_method['count']} transactions")
print(product_count)
plt.Figure(figsize=(8,10))
bars=plt.bar(product_count['PaymentMethod'],product_count['count'])
bars[0].set_color('Green'),bars[-1].set_color('red')
for bar in bars:
    height = bar.get_height()
    plt.text(
        bar.get_x() + bar.get_width() / 2.0,  
        height,                                
        f'{height:,.0f}',                     
        ha='center', va='bottom',              
        fontsize=10, fontweight='bold', color='black')
plt.title('Payment method')
plt.ylabel('Number of Payment', color='red',fontsize=15)
plt.xlabel('Method',color='red',fontsize=(15))
plt.xticks(rotation=(45))
plt.tight_layout()

plt.show

# %%


# %%
city_sales = (
    df.groupby('City', as_index=False)['Sales']
      .sum()
      .sort_values('Sales', ascending=False)
)

highest_city = city_sales.iloc[0]
lowest_city=city_sales.iloc[-1]
print(f"Highest sales city: {highest_city['City']} "
      f"with sales of {highest_city['Sales']:,.2f}")

print(f"Lowest sales city: {lowest_city['City']} "
      f"with sales of {lowest_city['Sales']:,.2f}")

plt.figure(figsize=(10, 6))
bars = plt.bar(city_sales['City'], city_sales['Sales'], color='steelblue')
bars[0].set_color('green'),bars[-1].set_color('red')
for bar in bars:
    plt.text(
        bar.get_x() + bar.get_width() / 2,
        bar.get_height(),
        f"{bar.get_height():,.0f}",
        ha='center',
        va='bottom',
        fontsize=9
    )

plt.title('Sales by City')
plt.xlabel('City')
plt.ylabel('Total Sales')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# %%
city_customers = (
    df.groupby('City')['CustomerID']
      .nunique()
      .sort_values(ascending=False)
      .reset_index(name='CustomerCount'))

city_customers['Percentage'] = (
    city_customers['CustomerCount'] /
    city_customers['CustomerCount'].sum() * 100)

print(city_customers)

plt.figure(figsize=(9, 7))
plt.pie(
    city_customers['CustomerCount'],
    labels=city_customers['City'],
    autopct='%1.1f%%',
    startangle=90)
plt.title('Percentage of Customers by City')
plt.tight_layout()
plt.show()

# %%
age_bins = [17, 25, 39, float("inf")]
age_labels = ["18–25", "26–39", "40+"]

df["AgeGroup"] = pd.cut(
    df["Age"],
    bins=age_bins,
    labels=age_labels,
    right=True
)

age_sales = (
    df.groupby("AgeGroup", observed=False)["Sales"]
      .sum()
      .reindex(age_labels)
      .reset_index()
)

print(age_sales)

plt.figure(figsize=(8, 5))
bars = plt.bar(age_sales["AgeGroup"], age_sales["Sales"], color="steelblue")

for bar in bars:
    plt.text(
        bar.get_x() + bar.get_width() / 2,
        bar.get_height(),
        f"{bar.get_height():,.0f}",
        ha="center",
        va="bottom"
    )

plt.title("Sales by Customer Age Group")
plt.xlabel("Age Group")
plt.ylabel("Total Sales")
plt.tight_layout()
plt.show()

# %%
product_sales = (
    df.groupby("ProductName", as_index=False)["Sales"]
      .sum()
      .sort_values("Sales", ascending=False)
)

highest_product = product_sales.iloc[0]

print(
    f"Highest-selling product: {highest_product['ProductName']} "
    f"with sales of {highest_product['Sales']:,.2f}"
)

plt.figure(figsize=(10, 6))
bars = plt.bar(product_sales["ProductName"], product_sales["Sales"], color="steelblue")
bars[0].set_color("green")

plt.title("Sales by Product")
plt.xlabel("Product")
plt.ylabel("Total Sales")
plt.xticks(rotation=60, ha="right")
plt.tight_layout()
plt.show()

# %%
original_rows = len(df)
df = df[df["Sales"] >= 0].copy()

print(f"Removed {original_rows - len(df)} rows with negative Sales values.")
print(f"Remaining rows: {len(df)}")

# %%
tehran_product_sales = (
    df[df["City"] == "Tehran"]
      .groupby("ProductName", as_index=False)["Sales"]
      .sum()
      .sort_values("Sales", ascending=False)
)

print("Sales by product in Tehran:")
print(tehran_product_sales)

plt.figure(figsize=(10, 6))
bars = plt.bar(tehran_product_sales["ProductName"], tehran_product_sales["Sales"], color="steelblue")

for bar in bars:
    plt.text(
        bar.get_x() + bar.get_width() / 2,
        bar.get_height(),
        f"{bar.get_height():,.0f}",
        ha="center",
        va="bottom",
        fontsize=9
    )

plt.title("Sales by Product in Tehran")
plt.xlabel("Product")
plt.ylabel("Total Sales")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.show()

# %%
tehran_category_sales = (
    df[df["City"] == "Tehran"]
    .groupby("Category", as_index=False)["Sales"]
    .sum()
    .sort_values("Sales", ascending=False)
)

print("Sales by product category in Tehran:")
print(tehran_category_sales)

plt.figure(figsize=(9, 6))
bars = plt.bar(
    tehran_category_sales["Category"],
    tehran_category_sales["Sales"],
    color="steelblue"
)

for bar in bars:
    plt.text(
        bar.get_x() + bar.get_width() / 2,
        bar.get_height(),
        f"{bar.get_height():,.0f}",
        ha="center",
        va="bottom"
    )

plt.title("Sales by Product Category in Tehran")
plt.xlabel("Category")
plt.ylabel("Total Sales")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# %%
other_city_category_sales = (
    df[df["City"] != "Tehran"]
    .groupby(["City", "Category"], as_index=False)["Sales"]
    .sum()
)

print("Sales by product category in cities other than Tehran:")
print(other_city_category_sales)

sales_pivot = (
    other_city_category_sales
    .pivot(index="City", columns="Category", values="Sales")
    .fillna(0)
)

ax = sales_pivot.plot(
    kind="bar",
    figsize=(12, 6),
    colormap="tab10"
)

ax.set_title("Sales by Product Category in Other Cities")
ax.set_xlabel("City")
ax.set_ylabel("Total Sales")
plt.xticks(rotation=45, ha="right")
plt.legend(title="Category")
plt.tight_layout()
plt.show()

# %%
yearly_sales = (
    df.assign(Year=df["OrderDate"].dt.year)
      .groupby("Year", as_index=False)["Sales"]
      .sum()
      .sort_values("Year")
)

print("Yearly Sales:")
print(yearly_sales)


plt.figure(figsize=(10, 6))
bars = plt.bar(yearly_sales["Year"], yearly_sales["Sales"], color="steelblue")

for bar in bars:
    plt.text(
        bar.get_x() + bar.get_width() / 2,
        bar.get_height(),
        f"{bar.get_height():,.0f}",
        ha="center",
        va="bottom",
        fontsize=9
    )

plt.title("Sales by Year")
plt.xlabel("Year")
plt.ylabel("Total Sales")
plt.tight_layout()
plt.show()

# %%
cancelled_by_category = (
    df[df["Status"].eq("Cancelled")]
      .groupby("Category", as_index=False)
      .agg(
          CancelledOrders=("OrderID", "count"),
          CancelledSales=("Sales", "sum")
      )
      .sort_values("CancelledOrders", ascending=False)
      .reset_index(drop=True)
)

print("Cancelled orders by product category:")
print(cancelled_by_category)

# Optional chart
plt.figure(figsize=(9, 5))
bars = plt.bar(cancelled_by_category["Category"], cancelled_by_category["CancelledOrders"], color="tomato")

for bar in bars:
    h = bar.get_height()
    plt.text(
        bar.get_x() + bar.get_width() / 2,
        h,
        f"{int(h)}",
        ha="center",
        va="bottom",
        fontsize=9
    )

plt.title("Cancelled Orders by Product Category")
plt.xlabel("Category")
plt.ylabel("Cancelled Orders")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.show()

# %%
age_category_sales = (
    df.groupby(["Category", "AgeGroup"], observed=False)["Sales"]
      .sum()
      .reset_index()
)

highest_age_by_category = (
    age_category_sales.loc[
        age_category_sales.groupby("Category")["Sales"].idxmax()
    ]
    .sort_values("Sales", ascending=False)
    .reset_index(drop=True)
)

print("Highest-selling age group by product category:")
print(highest_age_by_category)

sales_pivot = age_category_sales.pivot(
    index="Category",
    columns="AgeGroup",
    values="Sales"
)

sales_pivot.plot(
    kind="bar",
    figsize=(10, 6),
    color=["steelblue", "orange", "green"]
)

plt.title("Sales by Age Group and Product Category")
plt.xlabel("Product Category")
plt.ylabel("Total Sales")
plt.xticks(rotation=45, ha="right")
plt.legend(title="Age Group")
plt.tight_layout()
plt.show()

# %%
discount_by_segment = (
    df.groupby("CustomerSegment", as_index=False)
      .agg(
          AvgDiscount=("Discount", "mean"),
          TotalDiscount=("Discount", "sum"),
          TotalOrders=("OrderID", "count")
      )
      .sort_values("AvgDiscount", ascending=False)
)

print("Average discount by customer segment:")
print(discount_by_segment)

highest_discount_segment = discount_by_segment.iloc[0]
print(
    f"\nCustomer type with the highest discount: "
    f"{highest_discount_segment['CustomerSegment']} "
    f"(Average Discount: {highest_discount_segment['AvgDiscount']:.2f})"
)

plt.figure(figsize=(8, 5))
bars = plt.bar(
    discount_by_segment["CustomerSegment"],
    discount_by_segment["AvgDiscount"],
    color=["gold", "steelblue", "lightcoral"]
)

for bar in bars:
    plt.text(
        bar.get_x() + bar.get_width() / 2,
        bar.get_height(),
        f"{bar.get_height():.2f}",
        ha="center",
        va="bottom"
    )

plt.title("Average Discount by Customer Segment")
plt.xlabel("Customer Segment")
plt.ylabel("Average Discount")
plt.tight_layout()
plt.show()

# %%
segment_aov = (
    df.groupby("CustomerSegment", as_index=False)
      .agg(
          AverageOrderValue=("OrderValue", "mean"),
          TotalOrders=("OrderID", "count")
      )
      .sort_values("AverageOrderValue", ascending=False)
)

print("Average Order Value by Customer Segment:")
print(segment_aov)

highest_aov_segment = segment_aov.iloc[0]
print(
    f"\nHighest AOV: {highest_aov_segment['CustomerSegment']} "
    f"({highest_aov_segment['AverageOrderValue']:,.2f})"
)

plt.figure(figsize=(8, 5))
bars = plt.bar(
    segment_aov["CustomerSegment"],
    segment_aov["AverageOrderValue"],
    color=["gold", "steelblue", "lightcoral"]
)

for bar in bars:
    plt.text(
        bar.get_x() + bar.get_width() / 2,
        bar.get_height(),
        f"{bar.get_height():,.2f}",
        ha="center",
        va="bottom"
    )

plt.title("Average Order Value by Customer Segment")
plt.xlabel("Customer Segment")
plt.ylabel("Average Order Value")
plt.tight_layout()
plt.show()

# %%
#pip install sklearn.ensemble

# %%
import sklearn
from sklearn.ensemble import RandomForestClassifier

# %%
from sklearn.ensemble import RandomForestClassifier

# Customer-level features
max_date = df["OrderDate"].max()

customer_features = (
    df.groupby("CustomerID")
      .agg(
          Recency=("OrderDate", lambda x: (max_date - x.max()).days),
          Frequency=("OrderID", "nunique"),
          Monetary=("Sales", "sum")
      )
      .reset_index()
)

# Define churn: no purchase within the last 90 days
customer_features["Churn"] = (
    customer_features["Recency"] > 90
).astype(int)

X = customer_features[["Recency", "Frequency", "Monetary"]]
y = customer_features["Churn"]

# Shopping timeline information used by the prediction cell
timeline = (
    df.sort_values(["CustomerID", "OrderDate"])
      .groupby("CustomerID")
      .agg(
          LastPurchaseDate=("OrderDate", "max"),
          TotalOrders=("OrderID", "nunique"),
          AverageOrderValue=("OrderValue", "mean")
      )
      .reset_index()
)

order_dates = (
    df.sort_values(["CustomerID", "OrderDate"])
      .groupby("CustomerID")["OrderDate"]
      .diff()
      .dt.days
      .groupby(df.sort_values(["CustomerID", "OrderDate"])["CustomerID"])
      .mean()
      .reset_index(name="AverageDaysBetweenOrders")
)

timeline = timeline.merge(order_dates, on="CustomerID", how="left")

print("Features and target created successfully.")
print("X shape:", X.shape)
print("Churn distribution:")
print(y.value_counts())

# %%
churn_model = RandomForestClassifier(
    n_estimators=300,
    class_weight="balanced",
    random_state=42,
    n_jobs=-1
)

churn_model.fit(X, y)

# Get the probability of churn (class 1)
churn_class_index = list(churn_model.classes_).index(1)
churn_probability = churn_model.predict_proba(X)[:, churn_class_index]

# Build customer risk results
customer_churn_predictions = customer_features[
    ["CustomerID", "Recency", "Frequency", "Monetary"]
].copy()

customer_churn_predictions["ChurnProbability"] = churn_probability
customer_churn_predictions["RiskLevel"] = pd.cut(
    customer_churn_predictions["ChurnProbability"],
    bins=[-float("inf"), 0.30, 0.60, float("inf")],
    labels=["Low Risk", "Medium Risk", "High Risk"]
)

# Add shopping timeline information
customer_churn_predictions = customer_churn_predictions.merge(
    timeline[
        [
            "CustomerID",
            "LastPurchaseDate",
            "AverageDaysBetweenOrders",
            "TotalOrders",
            "AverageOrderValue"
        ]
    ],
    on="CustomerID",
    how="left"
)

# Predict the next expected shopping date
customer_churn_predictions["AverageDaysBetweenOrders"] = (
    customer_churn_predictions["AverageDaysBetweenOrders"]
    .fillna(customer_churn_predictions["AverageDaysBetweenOrders"].median())
)

customer_churn_predictions["ExpectedNextPurchase"] = (
    pd.to_datetime(customer_churn_predictions["LastPurchaseDate"])
    + pd.to_timedelta(
        customer_churn_predictions["AverageDaysBetweenOrders"],
        unit="D"
    )
)

customer_churn_predictions["DaysUntilExpectedPurchase"] = (
    customer_churn_predictions["ExpectedNextPurchase"] - max_date
).dt.days

# Sort customers by highest churn risk
customer_churn_predictions = customer_churn_predictions.sort_values(
    "ChurnProbability",
    ascending=False
).reset_index(drop=True)

print("Highest-risk customers:")
display(customer_churn_predictions.head(20))

print("\nRisk summary:")
print(customer_churn_predictions["RiskLevel"].value_counts())

# Plot churn-risk distribution
plt.figure(figsize=(8, 5))
customer_churn_predictions["RiskLevel"].value_counts().reindex(
    ["Low Risk", "Medium Risk", "High Risk"]
).plot(
    kind="bar",
    color=["green", "orange", "red"],
    edgecolor="black"
)

plt.title("Customer Churn Risk Distribution")
plt.xlabel("Risk Level")
plt.ylabel("Number of Customers")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

# Customers expected to shop soon
upcoming_customers = customer_churn_predictions[
    (customer_churn_predictions["DaysUntilExpectedPurchase"] >= 0) &
    (customer_churn_predictions["DaysUntilExpectedPurchase"] <= 30)
].sort_values("ExpectedNextPurchase")

print("Customers expected to shop within the next 30 days:")
display(upcoming_customers.head(20))

# %%
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)


# %%
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    classification_report,
    confusion_matrix
)

# Create and train the Logistic Regression model
logistic_model = Pipeline([
    ("scaler", StandardScaler()),
    ("classifier", LogisticRegression(
        class_weight="balanced",
        max_iter=1000,
        random_state=42
    ))
])

logistic_model.fit(X_train, y_train)

# Predictions and churn probabilities
logistic_pred = logistic_model.predict(X_test)
logistic_probability = logistic_model.predict_proba(X_test)[:, 1]

# Evaluation metrics
logistic_metrics = {
    "Accuracy": accuracy_score(y_test, logistic_pred),
    "Precision": precision_score(y_test, logistic_pred, zero_division=0),
    "Recall": recall_score(y_test, logistic_pred, zero_division=0),
    "F1-Score": f1_score(y_test, logistic_pred, zero_division=0)
}

print("Logistic Regression Performance:")
for metric, value in logistic_metrics.items():
    print(f"{metric}: {value:.4f}")

print("\nClassification Report:")
print(classification_report(
    y_test,
    logistic_pred,
    target_names=["Not Churned", "Churned"],
    zero_division=0
))

print("Confusion Matrix:")
print(confusion_matrix(y_test, logistic_pred))

# Create customer churn-risk results
logistic_risk_results = customer_features.loc[X_test.index, ["CustomerID"]].copy()
logistic_risk_results["ChurnProbability"] = logistic_probability
logistic_risk_results["RiskLevel"] = pd.cut(
    logistic_risk_results["ChurnProbability"],
    bins=[-float("inf"), 0.30, 0.60, float("inf")],
    labels=["Low Risk", "Medium Risk", "High Risk"]
)

print("\nHighest-risk customers:")
display(
    logistic_risk_results.sort_values(
        "ChurnProbability",
        ascending=False
    ).head(20)
)

# %%
import docx

# %%
# Create a comprehensive DOCX report from the analyses performed in this notebook

new_report = Document()

# Basic document formatting
new_report.core_properties.title = "E-Commerce Sales Analysis Report"
new_report.core_properties.subject = "Sales, customer, product, and churn analysis"

title = new_report.add_heading("E-Commerce Sales Analysis Report", level=0)
title.alignment = WD_ALIGN_PARAGRAPH.CENTER

new_report.add_paragraph(
    "This report summarizes the exploratory analysis, sales performance, "
    "customer behavior, payment methods, churn prediction, and business insights."
)

def add_dataframe_table(document, data, title=None, max_rows=30):
    if title:
        document.add_heading(title, level=2)

    table_data = data.head(max_rows).copy()

    table = document.add_table(
        rows=1,
        cols=len(table_data.columns)
    )
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    table.style = "Table Grid"

    for i, column in enumerate(table_data.columns):
        table.rows[0].cells[i].text = str(column)

    for _, record in table_data.iterrows():
        cells = table.add_row().cells
        for i, value in enumerate(record):
            if pd.isna(value):
                value = ""
            elif isinstance(value, float):
                value = f"{value:,.2f}"
            cells[i].text = str(value)

    if len(data) > max_rows:
        document.add_paragraph(
            f"Showing the first {max_rows} of {len(data)} rows."
        )

# 1. Dataset overview
new_report.add_heading("1. Dataset Overview", level=1)
new_report.add_paragraph(f"Total rows: {len(df):,}")
new_report.add_paragraph(f"Total columns: {len(df.columns):,}")
new_report.add_paragraph(
    f"Date range: {df['OrderDate'].min().date()} to {df['OrderDate'].max().date()}"
)

add_dataframe_table(
    new_report,
    df.head(),
    "Sample Records",
    max_rows=5
)

add_dataframe_table(
    new_report,
    df.describe(include="all").transpose().reset_index(),
    "Summary Statistics",
    max_rows=30
)

# 2. Monthly sales
new_report.add_heading("2. Monthly Sales Analysis", level=1)
new_report.add_paragraph(
    f"Highest sales month: {highest_month['Month']} "
    f"({highest_month['Sales']:,.2f})"
)
new_report.add_paragraph(
    f"Lowest sales month: {lowest_month['Month']} "
    f"({lowest_month['Sales']:,.2f})"
)
add_dataframe_table(new_report, monthly_sales, "Monthly Sales", max_rows=40)

# 3. Category analysis
new_report.add_heading("3. Category Sales Analysis", level=1)
new_report.add_paragraph(
    f"Top category: {top_category['Category']} "
    f"({top_category['Sales']:,.2f})"
)
new_report.add_paragraph(
    f"Lowest-selling category: {last_category['Category']} "
    f"({last_category['Sales']:,.2f})"
)
add_dataframe_table(new_report, category_revenue, "Revenue by Category")

# 4. Customer segments
new_report.add_heading("4. Customer Segment Analysis", level=1)
add_dataframe_table(
    new_report,
    customer_counts,
    "Customer Segment Distribution"
)
add_dataframe_table(
    new_report,
    discount_by_segment,
    "Discounts by Customer Segment"
)
add_dataframe_table(
    new_report,
    segment_aov,
    "Average Order Value by Customer Segment"
)

new_report.add_paragraph(
    f"Segment receiving the highest average discount: "
    f"{highest_discount_segment['CustomerSegment']} "
    f"({highest_discount_segment['AvgDiscount']:.2f})"
)
new_report.add_paragraph(
    f"Segment with the highest average order value: "
    f"{highest_aov_segment['CustomerSegment']} "
    f"({highest_aov_segment['AverageOrderValue']:,.2f})"
)

# 5. Payment and order status
new_report.add_heading("5. Payment Methods and Order Status", level=1)
add_dataframe_table(new_report, product_count, "Payment Method Usage")
add_dataframe_table(new_report, status, "Order Status Distribution")
new_report.add_paragraph(
    f"Most-used payment method: {top_method['PaymentMethod']} "
    f"({top_method['count']:,} transactions)"
)
new_report.add_paragraph(
    f"Least-used payment method: {least_method['PaymentMethod']} "
    f"({least_method['count']:,} transactions)"
)

# 6. Geographic analysis
new_report.add_heading("6. Geographic Analysis", level=1)
add_dataframe_table(new_report, city_sales, "Sales by City")
add_dataframe_table(new_report, city_customers, "Customers by City")
new_report.add_paragraph(
    f"Highest-sales city: {highest_city['City']} "
    f"({highest_city['Sales']:,.2f})"
)
new_report.add_paragraph(
    f"Lowest-sales city: {lowest_city['City']} "
    f"({lowest_city['Sales']:,.2f})"
)

# 7. Age analysis
new_report.add_heading("7. Age Group Analysis", level=1)
add_dataframe_table(new_report, age_sales, "Sales by Age Group")
add_dataframe_table(
    new_report,
    highest_age_by_category,
    "Highest-Selling Age Group by Category"
)

# 8. Product analysis
new_report.add_heading("8. Product Analysis", level=1)
add_dataframe_table(new_report, product_sales, "Sales by Product", max_rows=25)
new_report.add_paragraph(
    f"Highest-selling product: {highest_product['ProductName']} "
    f"({highest_product['Sales']:,.2f})"
)

# 9. Tehran analysis
new_report.add_heading("9. Tehran-Specific Analysis", level=1)
add_dataframe_table(
    new_report,
    tehran_category_sales,
    "Tehran Sales by Category"
)
add_dataframe_table(
    new_report,
    tehran_product_sales,
    "Tehran Sales by Product",
    max_rows=25
)

# 10. Yearly analysis
new_report.add_heading("10. Yearly Sales Analysis", level=1)
add_dataframe_table(new_report, yearly_sales, "Sales by Year")

# 11. Cancelled orders
new_report.add_heading("11. Cancelled Orders Analysis", level=1)
add_dataframe_table(
    new_report,
    cancelled_by_category,
    "Cancelled Orders by Category"
)

# 12. Churn analysis
new_report.add_heading("12. Customer Churn Analysis", level=1)
new_report.add_paragraph(
    "Customers were classified as churned when their recency exceeded 90 days."
)
new_report.add_paragraph(
    f"Total customers analyzed: {len(customer_features):,}"
)
new_report.add_paragraph(
    f"Churned customers: {(customer_features['Churn'] == 1).sum():,}"
)
new_report.add_paragraph(
    f"Non-churned customers: {(customer_features['Churn'] == 0).sum():,}"
)

add_dataframe_table(
    new_report,
    customer_churn_predictions.head(20),
    "Highest-Risk Customers",
    max_rows=20
)

risk_summary = (
    customer_churn_predictions["RiskLevel"]
    .value_counts()
    .rename_axis("RiskLevel")
    .reset_index(name="CustomerCount")
)
add_dataframe_table(new_report, risk_summary, "Churn Risk Summary")

# 13. Machine learning evaluation
new_report.add_heading("13. Churn Model Evaluation", level=1)

new_report.add_heading("Random Forest Model", level=2)
new_report.add_paragraph(
    "A balanced Random Forest classifier was trained using Recency, "
    "Frequency, and Monetary customer-level features."
)

new_report.add_heading("Logistic Regression Model", level=2)
for metric_name, metric_value in logistic_metrics.items():
    new_report.add_paragraph(
        f"{metric_name}: {metric_value:.4f}"
    )

new_report.add_paragraph(
    "The logistic regression model was evaluated using a held-out test set. "
    "It achieved strong accuracy, precision, recall, and F1-score."
)

add_dataframe_table(
    new_report,
    logistic_risk_results.sort_values(
        "ChurnProbability",
        ascending=False
    ).head(20),
    "Highest-Risk Customers from Logistic Regression",
    max_rows=20
)

# 14. Business conclusions
new_report.add_heading("14. Key Business Conclusions", level=1)

conclusions = [
    f"Electronics is the leading product category with revenue of "
    f"{top_category['Sales']:,.2f}.",
    f"Tehran generates the highest city-level sales with "
    f"{highest_city['Sales']:,.2f}.",
    f"{highest_product['ProductName']} is the highest-selling product.",
    f"{highest_discount_segment['CustomerSegment']} customers receive "
    f"the highest average discount.",
    f"{highest_aov_segment['CustomerSegment']} customers have the highest "
    f"average order value.",
    "Customers with high recency values should be prioritized for retention campaigns.",
    "Churn-risk predictions can be used to target customers with personalized offers.",
    "Cancelled orders are most concentrated in the categories shown in the cancellation analysis."
]

for conclusion in conclusions:
    new_report.add_paragraph(conclusion, style="List Bullet")

# Save the report
report_path = "ecommerce_sales_analysis_report.docx"
new_report.save(report_path)

print(f"Report created successfully: {report_path}")

# %%


# %%
from pathlib import Path
from docx import Document
from docx.shared import Inches, Pt
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
import numpy as np

import matplotlib.pyplot as plt

# Create output folder for chart images
charts_dir = Path("ecommerce_analysis_charts")
charts_dir.mkdir(exist_ok=True)

report = Document()
report.core_properties.title = "Complete E-Commerce Sales Analysis Report"

# Basic formatting
styles = report.styles
styles["Normal"].font.name = "Arial"
styles["Normal"].font.size = Pt(10)

def add_table(document, data, title, max_rows=100):
    document.add_heading(title, level=2)
    table_data = data.head(max_rows).copy()

    table = document.add_table(
        rows=1,
        cols=len(table_data.columns)
    )
    table.style = "Table Grid"
    table.alignment = WD_TABLE_ALIGNMENT.CENTER

    for i, column in enumerate(table_data.columns):
        table.rows[0].cells[i].text = str(column)

    for _, record in table_data.iterrows():
        cells = table.add_row().cells
        for i, value in enumerate(record):
            if pd.isna(value):
                value = ""
            elif isinstance(value, (float, np.floating)):
                value = f"{value:,.2f}"
            cells[i].text = str(value)

def add_chart(title, filename, plot_function):
    fig, ax = plt.subplots(figsize=(10, 6))
    plot_function(ax)
    ax.set_title(title, fontsize=14, fontweight="bold")
    fig.tight_layout()

    image_path = charts_dir / filename
    fig.savefig(image_path, dpi=150, bbox_inches="tight")
    plt.close(fig)

    report.add_heading(title, level=2)
    report.add_picture(str(image_path), width=Inches(6.5))

# Title
title = report.add_heading("Complete E-Commerce Sales Analysis", level=0)
title.alignment = WD_ALIGN_PARAGRAPH.CENTER

report.add_paragraph(
    "This report contains the complete exploratory data analysis, sales analysis, "
    "customer analysis, geographic analysis, product analysis, cancellation analysis, "
    "and churn prediction performed in the notebook."
)

# Dataset overview
report.add_heading("1. Dataset Overview", level=1)
report.add_paragraph(f"Total records: {len(df):,}")
report.add_paragraph(f"Total columns: {len(df.columns):,}")
report.add_paragraph(
    f"Order date range: {df['OrderDate'].min().date()} "
    f"to {df['OrderDate'].max().date()}"
)
add_table(report, df.head(), "Sample Records", 5)
add_table(report, df.describe(include="all").transpose().reset_index(),
          "Dataset Summary Statistics", 30)

# Monthly sales
report.add_heading("2. Monthly Sales Analysis", level=1)
report.add_paragraph(
    f"Highest sales month: {highest_month['Month']} "
    f"({highest_month['Sales']:,.2f})"
)
report.add_paragraph(
    f"Lowest sales month: {lowest_month['Month']} "
    f"({lowest_month['Sales']:,.2f})"
)
add_table(report, monthly_sales, "Monthly Sales Data", 100)

add_chart(
    "Monthly Sales Trend",
    "monthly_sales.png",
    lambda ax: ax.plot(
        monthly_sales["Month"],
        monthly_sales["Sales"],
        marker="o",
        color="steelblue"
    )
)

# Category analysis
report.add_heading("3. Category Analysis", level=1)
add_table(report, category_revenue, "Revenue by Category")

add_chart(
    "Sales by Product Category",
    "category_sales.png",
    lambda ax: ax.bar(
        category_revenue["Category"],
        category_revenue["Sales"],
        color="steelblue"
    )
)

# Customer segments
report.add_heading("4. Customer Segment Analysis", level=1)
add_table(report, customer_counts, "Customer Segment Distribution")
add_table(report, discount_by_segment, "Discount by Customer Segment")
add_table(report, segment_aov, "Average Order Value by Segment")

add_chart(
    "Customer Segment Distribution",
    "customer_segments.png",
    lambda ax: ax.bar(
        customer_counts["CustomerSegment"],
        customer_counts["Count"],
        color=["steelblue", "orange", "green"]
    )
)

add_chart(
    "Average Discount by Customer Segment",
    "discount_by_segment.png",
    lambda ax: ax.bar(
        discount_by_segment["CustomerSegment"],
        discount_by_segment["AvgDiscount"],
        color="gold"
    )
)

add_chart(
    "Average Order Value by Customer Segment",
    "segment_aov.png",
    lambda ax: ax.bar(
        segment_aov["CustomerSegment"],
        segment_aov["AverageOrderValue"],
        color="mediumpurple"
    )
)

# Status and payments
report.add_heading("5. Order Status and Payment Methods", level=1)
add_table(report, status, "Order Status Distribution")
add_table(report, product_count, "Payment Method Usage")

add_chart(
    "Order Status Distribution",
    "order_status.png",
    lambda ax: ax.bar(
        status["Status"],
        status["Count"],
        color=["green", "red", "orange"]
    )
)

add_chart(
    "Payment Method Usage",
    "payment_methods.png",
    lambda ax: ax.bar(
        product_count["PaymentMethod"],
        product_count["count"],
        color="teal"
    )
)

# Geographic analysis
report.add_heading("6. Geographic Analysis", level=1)
add_table(report, city_sales, "Sales by City")
add_table(report, city_customers, "Customers by City")

add_chart(
    "Sales by City",
    "city_sales.png",
    lambda ax: ax.bar(
        city_sales["City"],
        city_sales["Sales"],
        color="steelblue"
    )
)

add_chart(
    "Customers by City",
    "city_customers.png",
    lambda ax: ax.bar(
        city_customers["City"],
        city_customers["CustomerCount"],
        color="darkorange"
    )
)

# Age analysis
report.add_heading("7. Age Group Analysis", level=1)
add_table(report, age_sales, "Sales by Age Group")
add_table(report, highest_age_by_category,
          "Highest-Selling Age Group by Category")

add_chart(
    "Sales by Customer Age Group",
    "age_sales.png",
    lambda ax: ax.bar(
        age_sales["AgeGroup"].astype(str),
        age_sales["Sales"],
        color="cornflowerblue"
    )
)

def age_category_plot(ax):
    pivot = age_category_sales.pivot(
        index="Category",
        columns="AgeGroup",
        values="Sales"
    )
    pivot.plot(kind="bar", ax=ax, color=["steelblue", "orange", "green"])

add_chart(
    "Sales by Age Group and Category",
    "age_category_sales.png",
    age_category_plot
)

# Product analysis
report.add_heading("8. Product Analysis", level=1)
add_table(report, product_sales, "Sales by Product", 50)

add_chart(
    "Sales by Product",
    "product_sales.png",
    lambda ax: ax.bar(
        product_sales["ProductName"],
        product_sales["Sales"],
        color="steelblue"
    )
)
plt.xticks(rotation=60, ha="right")

# Tehran analysis
report.add_heading("9. Tehran Analysis", level=1)
add_table(report, tehran_category_sales, "Tehran Sales by Category")
add_table(report, tehran_product_sales, "Tehran Sales by Product", 50)

add_chart(
    "Tehran Sales by Category",
    "tehran_category_sales.png",
    lambda ax: ax.bar(
        tehran_category_sales["Category"],
        tehran_category_sales["Sales"],
        color="darkcyan"
    )
)

add_chart(
    "Tehran Sales by Product",
    "tehran_product_sales.png",
    lambda ax: ax.bar(
        tehran_product_sales["ProductName"],
        tehran_product_sales["Sales"],
        color="steelblue"
    )
)

# Other cities and categories
report.add_heading("10. Category Sales in Other Cities", level=1)
add_table(report, other_city_category_sales,
          "Other City Category Sales", 100)

def other_city_plot(ax):
    pivot = other_city_category_sales.pivot(
        index="City",
        columns="Category",
        values="Sales"
    ).fillna(0)
    pivot.plot(kind="bar", ax=ax, colormap="tab10")

add_chart(
    "Sales by Category in Other Cities",
    "other_city_category_sales.png",
    other_city_plot
)

# Yearly analysis
report.add_heading("11. Yearly Sales Analysis", level=1)
add_table(report, yearly_sales, "Sales by Year")

add_chart(
    "Sales by Year",
    "yearly_sales.png",
    lambda ax: ax.bar(
        yearly_sales["Year"].astype(str),
        yearly_sales["Sales"],
        color="slateblue"
    )
)

# Cancelled orders
report.add_heading("12. Cancelled Orders Analysis", level=1)
add_table(report, cancelled_by_category,
          "Cancelled Orders by Category")

add_chart(
    "Cancelled Orders by Category",
    "cancelled_orders.png",
    lambda ax: ax.bar(
        cancelled_by_category["Category"],
        cancelled_by_category["CancelledOrders"],
        color="tomato"
    )
)

# Churn analysis
report.add_heading("13. Customer Churn Analysis", level=1)
report.add_paragraph(
    "Customers with a recency value greater than 90 days were classified as churned."
)
report.add_paragraph(f"Customers analyzed: {len(customer_features):,}")
report.add_paragraph(
    f"Churned customers: {(customer_features['Churn'] == 1).sum():,}"
)
report.add_paragraph(
    f"Non-churned customers: {(customer_features['Churn'] == 0).sum():,}"
)

add_table(report, risk_summary, "Churn Risk Summary")
add_table(
    report,
    customer_churn_predictions.head(20),
    "Highest-Risk Customers",
    20
)

add_chart(
    "Customer Churn Risk Distribution",
    "churn_risk.png",
    lambda ax: ax.bar(
        risk_summary["RiskLevel"],
        risk_summary["CustomerCount"],
        color=["red", "orange", "green"][:len(risk_summary)]
    )
)

# Churn model evaluation
report.add_heading("14. Churn Model Evaluation", level=1)
report.add_paragraph("Logistic Regression performance:")

for metric_name, metric_value in logistic_metrics.items():
    report.add_paragraph(
        f"{metric_name}: {metric_value:.4f}",
        style="List Bullet"
    )

add_table(
    report,
    logistic_risk_results.sort_values(
        "ChurnProbability",
        ascending=False
    ).head(20),
    "Highest-Risk Customers from Logistic Regression",
    20
)

# Confusion matrix chart
cm = confusion_matrix(y_test, logistic_pred)

add_chart(
    "Logistic Regression Confusion Matrix",
    "confusion_matrix.png",
    lambda ax: (
        ax.imshow(cm, cmap="Blues"),
        ax.set_xlabel("Predicted Label"),
        ax.set_ylabel("Actual Label"),
        ax.set_xticks([0, 1]),
        ax.set_yticks([0, 1]),
        ax.set_xticklabels(["Not Churned", "Churned"]),
        ax.set_yticklabels(["Not Churned", "Churned"]),
        [
            ax.text(j, i, cm[i, j], ha="center", va="center")
            for i in range(2)
            for j in range(2)
        ]
    )
)

# Business conclusions
report.add_heading("15. Business Conclusions", level=1)

conclusions_text = [
    f"{top_category['Category']} is the leading category with sales of "
    f"{top_category['Sales']:,.2f}.",
    f"{highest_city['City']} has the highest city-level sales with "
    f"{highest_city['Sales']:,.2f}.",
    f"{highest_product['ProductName']} is the highest-selling product.",
    f"{highest_discount_segment['CustomerSegment']} customers receive the "
    f"highest average discount.",
    f"{highest_aov_segment['CustomerSegment']} customers have the highest "
    f"average order value.",
    "Customers with high recency should be targeted with retention campaigns.",
    "High-risk customers can receive personalized discounts and reminders.",
    "Cancelled orders should be monitored by category, especially in the "
    "categories with the highest cancellation counts."
]

for conclusion_text in conclusions_text:
    report.add_paragraph(conclusion_text, style="List Bullet")

# Save final report
report_path = "complete_ecommerce_sales_analysis_report.docx"
report.save(report_path)

print(f"Complete DOCX report created successfully: {report_path}")


