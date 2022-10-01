# Predicting Company Performance Using Anonymous Employee Reviews

## 1. Data Collection -

### a. Glassdoor Web Scraper

glassdoor_scraper.py - Use this file to scrape the Glassdoor website for reviews of companies. If needed, the time range can be changed by editing the date variable in the file. <br><br>
values.py - Add your glassdoor login credentials in this file. <br><br>

### b. Earnings data

Get the quarterly earnings for the required time period for the company from Ycharts (SEC) in billions or millions.

## 2. Data Understanding & Visualization

Manually remove Job Title, Job Location, and Advice to Management columns.

meta.ipynb - Change the path of the input file and the Date_Posted according to your requirements. It will calculate and give us the aggregated values of Star_Rating each quarter according to the given time period. Change the value of the list `earnings` to the list of the company earnings, which you have collected from Ycharts. Now the graphs will be plotted against the earnings and ratings column, and the correlations will be shown as well.

## 3. Data preparation

### a. Sentiment Analysis

generating_sentiments.ipynb <br>
This file generates the VADER sentiments for Review_Title and Pros_And_Cons. Change the path of the input csv file to the company you want to generate sentiments of. After the sentiments are generated, the updated csv file with the new columns will be saved in the same directory.

### b. Data Cleaning

data_cleaning.ipynb<br>

<ol>
<li> This file cleans the data and removes the rows with missing values. Missing rows are replaced with averages. </li>
<li> The work_duration column - This column is a string and needs to be converted to a number. </li>
<li> All data before 2012 are removed. If needed, this date can be changed. </li>
<li> Quarterly averages are calculated for all columns. All columns are normalized. </li>
<li> The predictive column is also generated. Change the `earnings` list to the list of the company earnings, which you have collected from Ycharts. </li>
<li> The data is saved in a csv file. </li>
</ol>

### c. Feature Engineering - Text Analysis

feature_engineering.ipynb<br>

<ol>
<li>Change the file name. Use the sentiments file generated in step 3.a.</li>
<li>New features will be generated based on top 20 topics (text analysis) and it will be included in the final dataset. </li>
<li>The final dataset will be stored in the same directory and can be used in RapidMiner</li>
</ol>

# 4. RapidMiner

### a. data
copy the final csv file to the 'data' folder 

### b. process
All the processes with different model are listed in the 'process' folder

### c. Testing the processes
<ol>
<li>Import the csv - Mark the unwanted columns as 'Exclude Column'</li>
<li>Change the 'Type' of the column and mark the 'label' column </li>
<li>Import the process from 'process' folder into the RapidMiner</li> 
<li>Change the input csv files in the processes and run the code</li>
<li>It will give the model design and performance details of that model</li>
</ol>