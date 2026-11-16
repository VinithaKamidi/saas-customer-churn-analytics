# Power BI Setup & DAX Guide for SaaS Churn Analytics

## Core DAX Measures
1. **Total MRR:**
   ```dax
   Total MRR = SUM(saas_subscriptions[monthly_recurring_revenue])
   ```
2. **Active MRR (Retained):**
   ```dax
   Active MRR = CALCULATE(SUM(saas_subscriptions[monthly_recurring_revenue]), saas_subscriptions[is_churned] = 0)
   ```
3. **Churn Rate %:**
   ```dax
   Churn Rate % = DIVIDE(CALCULATE(COUNT(saas_subscriptions[customer_id]), saas_subscriptions[is_churned] = 1), COUNT(saas_subscriptions[customer_id]), 0)
   ```
4. **Average NPS:**
   ```dax
   Average NPS = AVERAGE(saas_subscriptions[nps_score])
   ```
