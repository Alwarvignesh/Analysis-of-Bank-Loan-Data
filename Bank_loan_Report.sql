use bank_report;
select * from financial_loans;
select count(id) as Total_Loan_Applications from financial_loans;
select count(id) as MTD_Total_Loan_Applications from financial_loans where month(issue_date)=12 and year(issue_date)=2021;
select count(id) as PMTD_Total_Loan_Applications from financial_loans where month(issue_date)=11;
select sum(loan_amount) as Total_Funded_Amount from financial_loans;
select sum(loan_amount) as MTD_Total_Funded_Amount from financial_loans where month(issue_date)=12 and year(issue_date)=2021;
select sum(loan_amount) as PMTD_Total_Loan_Applications from financial_loans where month(issue_date)=11;
select sum(total_payment) as Total_Amount_Received from financial_loans;
select sum(total_payment) as MTD_Total_Amount_Received from financial_loans where month(issue_date)=12 and year(issue_date)=2021;
select sum(total_payment) as PMTD_Total_Amount_Received from financial_loans where month(issue_date)=11;
select avg(int_rate)*100 as Avg_Int_Rate from financial_loans;
select avg(int_rate)*100 as MTD_Avg_Int_Rate from financial_loans where month(issue_date)=12 and year(issue_date)=2021;
select avg(int_rate)*100 as PMT_Avg_Int_Rate from financial_loans where month(issue_date)=11;
select avg(dti)*100 as Avg_DTI from financial_loans;
select avg(dti)*100 as MTD_Avg_DTI from financial_loans where month(issue_date)=12 and year(issue_date)=2021;
select avg(dti)*100 as PMTD_Avg_DTI from financial_loans where month(issue_date)=11;
select (count(case when loan_status='Fully paid' or loan_status='Current' then id end)*100.0) / count(id) as Good_Loan_Percentage from financial_loans;
select count(id) as Good_Loan_Applications from financial_loans where loan_status='Fully Paid' or loan_status= 'Current';
select sum(loan_amount) as Good_Loan_Funded_Amount from financial_loans where loan_status='Fully Paid'or loan_status='Current';
select sum(total_payment) as Good_Loan_Amount_Received from financial_loans where loan_status='Fully Paid' or loan_status='Current';
select (count(case when loan_status='Charged Off' then id end)*100.0)/count(id) as Bad_Loan_Percentage from financial_loans;
select count(id) as Bad_Loan_Applications from financial_loans where loan_status='Charged Off';
select sum(loan_amount) as Bad_Loan_Funded_Amount from financial_loans where loan_status='Charged Off';
select sum(total_payment) as Bad_Loan_Amount_Received from financial_loans where loan_status='Charged Off';
select loan_status ,count(id) as Loan_count,
sum(total_payment) as Total_Amount_Received,
sum(loan_amount) as Total_Funded_Amount,
avg(int_rate*100) as Interest_Rate,
avg(dti*100) as DTI 
from financial_loans 
group by loan_status;
select loan_status,sum(total_payment) as MTD_Total_Amount_Received,
sum(loan_amount) as MTD_Total_Funded_Amount
from financial_loans 
where month(issue_date)=12 group by loan_status;
select month(issue_date),date_format(issue_date,'%M') as Month_Name,count(id) as Total_Loan_Applications,
sum(loan_amount) as Total_Funded_Amount,
sum(total_payment) as Total_Received_Amount from financial_loans group by month(issue_date),
date_format(issue_date,'%M') order by month(issue_date);
select address_state as State,
count(id) as Total_Loan_Applications,
sum(loan_amount) as Total_Funded_Amount,
sum(total_payment) as Total_Amount_Received
from financial_loans group by address_state order by address_state;
select term as Term,
count(id) as Total_Loan_Applications,
sum(loan_amount) as Total_Funded_Amount,
sum(total_payment) as Total_Amount_Received
from financial_loans group by term order by term;
select home_ownership as Home_Ownership,
count(id) as Total_Loan_Applications,
sum(loan_amount) as Total_Funded_Amount,
sum(total_payment) as Total_Amount_Received
from financial_loans group by home_ownership order by home_ownership;


