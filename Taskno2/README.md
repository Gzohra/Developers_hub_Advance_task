# Loan Default Risk Prediction with Business Cost Optimization 

This project aims to predict the likelihood of a customer defaulting on a loan using machine learning models. Additionally, it optimizes the classification threshold by incorporating business cost values for false positives and false negatives.

---

##  Dataset

I use the publicly available *Home Credit Default Risk* dataset from Kaggle.

🔗 [Download the dataset here](https://www.kaggle.com/competitions/home-credit-default-risk/data)

---

##  Objective

- Predict whether a customer will default on a loan.
- Minimize total business cost by adjusting the classification threshold.
- Compare model performance using different cost values for misclassification.

---

##  Models Used

- Logistic Regression
- CatBoost Classifier

---

##  Business Assumptions

We assign the following costs to model misclassifications:

| Outcome              | Business Cost |
|----------------------|----------------|
| False Positive (FP)  | \500          |
| False Negative (FN)  | \2000         |

These costs are used to evaluate and optimize the decision threshold beyond default 0.5.

---

##  Steps Performed

1. *Data Preprocessing*
   - Handled missing values
   - Label encoding for categorical variables
   - Dropped irrelevant columns

2. *Model Training*
   - Trained Logistic Regression and CatBoost on training set

3. *Threshold Optimization*
   - Predicted probabilities
   - Calculated business cost for each threshold
   - Chose threshold with *minimum total cost*

4. *Evaluation*
   - Confusion Matrix and Classification Report
   - Feature importance analysis (CatBoost)

---

##  Results Summary

###  Logistic Regression

- *Optimal Threshold:* 0.04  
- *Minimum Business Cost:* \$346,000  
- *Classification Report:*  
  Precision, Recall, and F1-score printed for each class  
- *Confusion Matrix:*  
  Displayed and interpreted  

---

###  CatBoost Classifier

- *Optimal Threshold:* 0.15  
- *Minimum Business Cost:* \$307,000  
- *Top 10 Important Features:*  
  

---

##  Dependencies

- Python 3.x  
- pandas  
- numpy  
- matplotlib  
- seaborn  
- scikit-learn  
- catboost
