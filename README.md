# E-Commerce Sales Analysis Report

## Overview
This project analyzes an e-commerce sales dataset covering 49,203 orders from 2024-01-01 to 2026-06-30. The dataset includes 9,820 unique customers and evaluates sales trends, customer behavior, geographic performance, product performance, and churn risk.

## Business Objective
The analysis aims to:
- Understand total sales performance over time
- Identify the best-performing products and categories
- Measure city-level and customer-segment performance
- Analyze customer behavior and churn risk
- Provide actionable business recommendations

## Dataset Summary
- Total records: 49,203
- Total columns: 19
- Unique customers: 9,820
- Date range: 2024-01-01 to 2026-06-30

## Key Findings

### Sales Performance
- Highest sales month: 2025-05 with 130,625.00 in sales
- Lowest sales month: 2026-02 with 75,132.00 in sales
- Highest sales city: Tehran with 964,119.00
- Lowest sales city: Qom with 163,177.00
- Best-performing category: Electronics with 1,751,491.00
- Lowest-performing category: Stationery with 67,237.00

### Product Insights
- Highest-selling product: Headphones with 333,531.00
- Sales by age group:
    - 18–25: 574,897.00
    - 26–39: 1,007,885.00
    - 40+: 1,862,988.00

### Customer Segments
- Customer segment distribution:
    - Regular: 27,285
    - New: 17,050
    - VIP: 4,868
- Segment with highest average discount: VIP (7.58)
- Segment with highest average order value: Regular (70.19)

### Payment and Order Status
- Most-used payment method: Gateway (23,882 transactions)
- Least-used payment method: Cash (4,922 transactions)
- Order status distribution:
    - Completed: 45,258
    - Cancelled: 2,437
    - Returned: 1,508

### Churn Analysis
Customers were classified as churned when recency exceeded 90 days.
- Customers analyzed: 9,820
- Churned customers: 6,844
- Non-churned customers: 2,976

Risk summary:
- Low Risk: 2,976
- Medium Risk: 0
- High Risk: 6,844

### Model Performance
The churn prediction workflow used a balanced Random Forest model and a Logistic Regression benchmark.
- Logistic Regression Accuracy: 0.9827
- Logistic Regression Precision: 1.0000
- Logistic Regression Recall: 0.9749
- Logistic Regression F1-score: 0.9873

## Business Recommendations
1. Focus marketing campaigns on Tehran and the top-performing categories, especially Electronics.
2. Prioritize retention strategies for customers with high recency and high churn probability.
3. Increase attention to the categories with the most cancelled orders, especially Accessories.
4. Use customer segmentation to personalize discounts and promotions for VIP and Regular customers.
5. Monitor payment method preferences to optimize checkout efficiency and conversion rates.
6. Consider age-based targeting, since the 40+ segment contributes the highest sales volume.

## Conclusion
This analysis shows strong e-commerce performance driven by category demand, geographic concentration in Tehran, and customer retention opportunities. By leveraging churn prediction and segment-based insights, the business can improve customer retention, maximize revenue, and refine sales strategy.

## Files Included
- Notebook with exploratory analysis and model building
- DOCX report generated from the analysis
- Chart images for visual reporting
