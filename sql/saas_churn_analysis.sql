-- SaaS Churn & MRR Analytics SQL Queries

-- 1. Overall MRR and Churn Rate Summary by Plan
SELECT 
    subscription_plan,
    COUNT(customer_id) AS total_customers,
    SUM(monthly_recurring_revenue) AS total_mrr,
    SUM(CASE WHEN is_churned = 1 THEN 1 ELSE 0 END) AS churned_customers,
    ROUND(CAST(SUM(CASE WHEN is_churned = 1 THEN 1 ELSE 0 END) AS FLOAT) / COUNT(customer_id) * 100, 2) AS churn_rate_pct
FROM saas_subscriptions
GROUP BY subscription_plan
ORDER BY total_mrr DESC;

-- 2. Churn Risk by Contract Type and Support Tickets
SELECT 
    contract_type,
    CASE 
        WHEN support_tickets_raised >= 3 THEN 'High Tickets (3+)'
        ELSE 'Low Tickets (<3)'
    END AS support_tier,
    COUNT(customer_id) AS customers,
    ROUND(AVG(nps_score), 2) AS avg_nps,
    ROUND(AVG(CAST(is_churned AS FLOAT)) * 100, 2) AS churn_rate_pct
FROM saas_subscriptions
GROUP BY 1, 2
ORDER BY churn_rate_pct DESC;
