# Mall Customer Segmentation using KMeans Clustering

##  Project Overview

Customer segmentation is a key marketing strategy that allows businesses to better understand their customers and target them with personalized offers.  
This project applies *KMeans clustering* to group mall customers based on their:

- Age  
- Annual Income (k$)  
- Spending Score (1–100)  

By identifying these segments, companies can optimize marketing efforts and increase customer engagement and sales.

---

##  Dataset Information

- *Dataset Name:* Mall Customers Dataset  
- *Source:* [Kaggle - Mall Customers Dataset](https://www.kaggle.com/datasets/vjchoudhary7/customer-segmentation)  
- *Format:* CSV  
- *Features:*
  - CustomerID
  - Gender
  - Age
  - Annual Income (k$)
  - Spending Score (1-100)

---

##  Technologies Used

| Tool        | Description                           |
|-------------|---------------------------------------|
| Python      | Main programming language             |
| Pandas      | Data manipulation                     |
| NumPy       | Numerical operations                  |
| Seaborn     | Data visualization                    |
| Matplotlib  | Plotting graphs                       |
| Scikit-learn| KMeans, StandardScaler, PCA           |


---

##  Workflow Steps

1. *Data Preprocessing*
   - Handled missing values (none found)
   - Encoded categorical variables (Gender)
   - Scaled features using StandardScaler

2. *Exploratory Data Analysis (EDA)*
   - Visualized relationships between income, age, and spending
   - Heatmap to check feature correlation

3. *Optimal Clusters with Elbow Method*
   - Calculated inertia for K = 1 to 10
   - Chose *K = 5* based on elbow curve

4. *Model Building*
   - Applied KMeans clustering on scaled data
   - Added cluster labels to the dataset

5. *Visualization*
   - Reduced dimensions using PCA
   - Created 2D cluster scatterplot to visualize customer segments

6. *Segment-wise Analysis*
   - Used .describe() to understand customer stats per cluster

7. *Strategy Recommendation*
   - Proposed targeted marketing strategies for each segment

---

##  Cluster-Based Insights & Marketing Strategies

| Cluster | Customer Profile                    | Suggested Strategy                                  |
|---------|-------------------------------------|----------------------------------------------------|
| 0       | High income, high spenders          | Luxury promotions, premium products                |
| 1       | Moderate income, moderate spenders  | Loyalty programs, festive discounts                |
| 2       | Young customers with low spending   | Entry-level product promotions                     |
| 3       | Mid-income and mid-age group        | Occasional discounts, social media marketing       |
| 4       | Older or low-income segment         | Personalized communication, basic needs marketing  |

---

##  Visual Results

-  *Elbow Method Plot* – to determine optimal number of clusters  
-  *PCA Scatter Plot* – clear visualization of customer segments  
-  *Heatmap* – correlation between features  
-  *Pairplot* – helps understand distribution and outliers  

---

##  How to Run This Project

###  In Jupyter Notebook

1. Clone or download the repository  
2. Ensure Mall_Customers.csv is in the same directory  
3. Install required libraries:
   ```bash
   pip install pandas numpy matplotlib seaborn scikit-learn
