import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def run_pipeline():
    print("Loading SaaS subscription dataset...")
    df = pd.read_csv("data/saas_subscriptions.csv")
    os.makedirs("outputs", exist_ok=True)
    
    print("Calculating core RevOps metrics...")
    summary = df.groupby('subscription_plan').agg(
        total_customers=('customer_id', 'count'),
        total_mrr=('monthly_recurring_revenue', 'sum'),
        churned_customers=('is_churned', 'sum')
    ).reset_index()
    summary['churn_rate_pct'] = round((summary['churned_customers'] / summary['total_customers']) * 100, 2)
    summary.to_csv("outputs/saas_mrr_summary.csv", index=False)

    df['support_tier'] = np.where(df['support_tickets_raised'] >= 3, 'High Tickets (3+)', 'Low Tickets (<3)')
    risk_summary = df.groupby(['contract_type', 'support_tier']).agg(
        customers=('customer_id', 'count'),
        avg_nps=('nps_score', 'mean'),
        churn_rate_pct=('is_churned', 'mean')
    ).reset_index()
    risk_summary['churn_rate_pct'] = (risk_summary['churn_rate_pct'] * 100).round(2)
    risk_summary.to_csv("outputs/churn_by_risk_tier.csv", index=False)

    print("Pipeline executed successfully! Outputs saved to outputs/")

if __name__ == "__main__":
    run_pipeline()
