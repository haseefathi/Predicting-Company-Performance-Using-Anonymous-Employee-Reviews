# Predicting Company Performance Using Anonymous Employee Reviews

## Abstract
Forecasting an organization's growth is critical for investors to make timely choices in order to optimize profits. To that purpose, investors utilize alternative data from other parties to forecast a company's success before it releases its quarterly financial reports. Employee evaluations may be indicative of a firm's performance in the sense that employee happiness may be directly tied to corporate productivity. In this paper, we analyzed the reviews of three companies: Home Depot, General Electric, and Meta. We created various models for each company since each company has unique intrinsic complexity.  We used different machine learning algorithms for each organization and examined which model was best suited to that company. We discovered that our models were predictive of corporate performance for some but not all companies. When we used the Decision Tree method, we got the best results for Meta, with an accuracy of 80%. As a result, we concluded that Glassdoor reviews can forecast company success and serve as an alternate data source.

## Process
![image](https://user-images.githubusercontent.com/58848482/193426257-1eb36d0e-5606-4b29-8b7e-26d665f22576.png)
<ol>
<li>
Data Collection and Understanding
  <ol>
   <li>Feature Selection and Data Visualization</li>
  </ol>
</li>
  
<li>
Data preprocessing and preparation
<ol>
   <li>Data Preprocessing</li>
   <li>Sentiment analysis using VADER</li>
   <li>Feature engineering through text analysis</li>
   <li>Developing a predictive column</li>
  </ol>
</li>
<li>Modeling and finding best model for each company</li>
</ol>


## Results
In this work, we made different models for Home Depot, General Electric and Meta as different companies have different inherent intricacies specific to that company. We utilized multiple machine learning algorithms for each of the companies and analyzed which model is suitable to that specific company. We found that our models were predictive of the company performance for some companies, but not for all. The best result we obtained was for Meta, with an accuracy of 80% when the algorithm was Decision Tree. Therefore, we can conclude that Glassdoor reviews can be predictive of company performance and can be used as an alternative data source. 

# Instructions to run code
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

