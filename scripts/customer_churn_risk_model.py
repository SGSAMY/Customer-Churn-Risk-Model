#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd

# Read dataset
df = pd.read_excel(
    r"C:\& Satheesh\Customer-Churn-Risk-Model\data\Financial_Services_KPI_Dashboard_5000Rows.xlsx"
)

# Clean column names
df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

# Check data
df.head()


# In[3]:


def calculate_churn_risk(row):

    score = 0

    # Failed DD
    if row["failed_dd"] == "Yes":
        score += 30

    # Complaints
    if row["complaints"] >= 3:
        score += 25
    elif row["complaints"] >= 1:
        score += 10

    # Online inactivity
    if row["online_login_days"] > 120:
        score += 25
    elif row["online_login_days"] > 60:
        score += 15

    # Low email engagement
    if row["email_open_rate"] < 20:
        score += 20

    # Low website engagement
    if row["web_visits_30d"] < 3:
        score += 15

    # No campaign response
    if row["previous_campaign_response"] == "No":
        score += 15

    # No active DD
    if row["active_dd"] == "No":
        score += 15

    return score


# In[5]:


df["churn_risk_score"] = df.apply(calculate_churn_risk, axis=1)

df.head()


# In[7]:


def churn_category(score):

    if score >= 80:
        return "High Risk"

    elif score >= 50:
        return "Medium Risk"

    else:
        return "Low Risk"


df["churn_risk_category"] = df["churn_risk_score"].apply(churn_category)

df.head()


# In[9]:


import matplotlib.pyplot as plt

df["churn_risk_category"].value_counts().plot(
    kind="bar",
    figsize=(8,5)
)

plt.title("Customer Churn Risk Distribution")
plt.xlabel("Risk Category")
plt.ylabel("Customer Count")

plt.xticks(rotation=0)

plt.show()


# In[11]:


output_path = r"C:\& Satheesh\Customer-Churn-Risk-Model\output\customer_churn_output.xlsx"

df.to_excel(output_path, index=False)

print("Churn model completed successfully.")


# In[ ]:




