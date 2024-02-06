#!/usr/bin/env python
# coding: utf-8

# In[136]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import seaborn as sns


# In[137]:


bank_loan=pd.read_csv('D:/AVN/Internship/Project - 2-Analysis of Bank Loan Data/Data Set/financial_loans.csv')


# In[149]:


bank_loan.head(10)


# In[140]:


bank_loan.tail(10)


# In[141]:


bank_loan.info()


# In[142]:


bank_loan.describe()


# In[143]:


bank_loan.duplicated().sum()


# In[144]:


bank_loan.isnull().sum()


# In[145]:


bank_loan['emp_title'].fillna("553742017",inplace=True)


# In[150]:


bank_loan.isnull().sum()


# In[151]:


bank_loan.head(25)


# # Distribution of Loan Purposes
# 
# 

# In[152]:


#Create a bar chart using matplotlib to visualize the distribution of loan purposes
purpose_count=bank_loan['purpose'].value_counts()
colors = ['red', 'lightgreen', 'coral', 'lightblue', 'pink', 'orange', 'yellow', 'violet', 'brown', 'grey', 'green', 'skyblue', 'blue', 'purple']
bars=plt.bar(purpose_count.index,purpose_count,color=colors)
plt.title("Distribution of Loan Purpose")
plt.xlabel("Loan Purpose")
plt.ylabel("Number of Loans")
plt.xticks(rotation=45,ha='right')
for bar in bars:
    y_value= bar.get_height()
    plt.text(bar.get_x() + bar.get_width() / 2, y_value + 0.05, round(y_value, 1), ha='center', va='bottom')

plt.show()


# # #Presence of Grades in States
# 

# In[153]:


#Compare the grades with geographical location.
grade_state=pd.crosstab(bank_loan['address_state'],bank_loan['grade'])
plt.figure(figsize=(18,12))
different_color=sns.color_palette("tab10")
sns.heatmap(grade_state,annot=True,cmap=different_color,fmt='d',cbar_kws={'label':'Number of States'})
plt.title("Presence of Grades in States")
plt.xlabel("Grade")
plt.ylabel("State")
plt.show()


# # Distribution of Loan status 
# 

# In[154]:


#Create a pie chart using matplotlib to show the distribution of loan statuses
loan_view=bank_loan['loan_status'].value_counts()
plt.figure(figsize=(12,6))
plt.pie(loan_view,labels=loan_view.index,autopct='%1.1f%%',startangle=90,colors=['orange','red','green'])
plt.title("Distribution of Loan status")
plt.show()


# # Loan Performance by Home Ownership
# 

# In[155]:


#Does home ownership status impact loan performance?
plt.figure(figsize=(12,6))
ax=sns.countplot(x='home_ownership',hue='loan_status',data=bank_loan,palette='Set1')
plt.title('Loan Performance by Home Ownership')
plt.xlabel("Home Ownership Status")
plt.ylabel("Loan Status")
for i in ax.containers:
    ax.bar_label(i,)
plt.show()


# # Loan Status by Employee Length

# In[156]:


#•	Is there a correlation between employment length and loan status
plt.figure(figsize=(12,6))
ax=sns.countplot(x='emp_length',hue='loan_status',data=bank_loan,palette='viridis')
plt.title("Loan Status by Employment Length")
plt.xlabel("Employee Length")
plt.ylabel("Loan Status")
for i in ax.containers:
    ax.bar_label(i,)
plt.show()


# # Loan Performance by Income Verification Status

# In[157]:


#•	How does income verification status impact loan performance?-
plt.figure(figsize=(10, 6))
ax=sns.countplot(x='home_ownership', hue='term', data=bank_loan, palette='Set2')
plt.title('Loan Performance by Income Verification Status')
plt.xlabel('Income Verification Status')
plt.ylabel('Count of Loans')
for i in ax.containers:
    ax.bar_label(i,)
plt.show()


# # Number of Loans Issued Over Time

# In[158]:


#
bank_loan['issue_date']=pd.to_datetime(bank_loan['issue_date'],format="%d-%m-%Y")
loans_by=bank_loan.groupby('issue_date').size().reset_index(name='Number of Loans')
plt.figure(figsize=(12,6))
ax=plt.plot(loans_by['issue_date'],loans_by['Number of Loans'],marker='o',linestyle='-')
plt.title('Number of Loans Issued Over Time')
plt.xlabel('Issue Date')
plt.ylabel('Number of loans')
plt.grid(True)
plt.show()


# # Distribution of Loan Amounts,Interest Rates and Annual Incomes

# In[159]:


#Can you visualize the distribution of loan amounts, interest rates, and annual incomes?-
plt.figure(figsize=(15, 6))
plt.subplot(1, 3, 1)
plt.hist(bank_loan['loan_amount'], bins=20, color='skyblue', edgecolor='black')
plt.title('Distribution of Loan Amount')
plt.xlabel('Loan Amount')
plt.ylabel('Frequency')
plt.subplot(1, 3, 2)
plt.hist(bank_loan['int_rate'], bins=20, color='orange', edgecolor='black')
plt.title('Distribution of Interest Rate')
plt.xlabel('Interest Rate')
plt.ylabel('Frequency')
plt.subplot(1, 3, 3)
plt.hist(bank_loan['annual_income'], bins=20, color='green', edgecolor='black')
plt.title('Distribution of Annual Income')
plt.xlabel('Annual Income')
plt.ylabel('Frequency')
plt.tight_layout()
plt.show()


# In[ ]:





# In[ ]:





# In[ ]:




