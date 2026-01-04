# 🛡️ FraudGuard AI: Enterprise Fraud Detection System

**FraudGuard AI** is a professional machine learning-based security solution designed to identify fraudulent credit card transactions in real-time. By analyzing behavioral and structural transaction patterns using a **Random Forest Classifier**, the system achieves high precision and recall.

---

## 🚀 1. Executive Summary
Financial institutions lose billions annually to credit card fraud. Our system prevents unauthorized transactions before they are settled by providing instant risk scores based on numerical pattern analysis.

---

## ⚙️ 2. System Requirements & Dependencies
To ensure the system runs effectively, the following environment is required:

### **A. Core Software**
* **Python 3.8+**
* **Streamlit**: For the interactive enterprise dashboard.
* **Joblib**: For serializing and loading the trained model.

### **B. Data Science Libraries**
* **Pandas & NumPy**: For large-scale data manipulation.
* **Scikit-Learn**: For preprocessing and model training.
* **Matplotlib & Seaborn**: For generating confusion matrices.

---

## 🔬 3. Methodology

### **3.1 Dataset Analysis**
The system is trained on a dataset of European cardholder transactions containing **284,807 records**.
* **Highly Imbalanced**: Only 492 transactions (**0.17%**) are fraudulent.
* **Feature Transformation**: The dataset uses PCA-transformed features ($V_1$ to $V_{28}$).



### **3.2 Preprocessing Pipeline**
* **Normalization**: Amount and Time features are scaled using `StandardScaler`.
* **Stratified Splitting**: Data is split into 80/20 train-test sets to maintain the rare fraud ratio.

### **3.3 Model Architecture**
The system utilizes a **Random Forest Classifier** with 100 estimators. This ensemble method was chosen because it effectively handles imbalanced classes better than standard linear models.



---

## 📊 4. Performance Evaluation
The model is evaluated based on its ability to identify fraud (**Recall**) while minimizing false alarms (**Precision**).

### **4.1 Key Performance Indicators (KPIs)**
| Metric | Result | Interpretation |
| :--- | :--- | :--- |
| **Accuracy** | 100% | Overall correctly predicted transactions. |
| **Precision** | 94.0% | System reliability when alerting "Fraud". |
| **Recall** | 82.4% | Ability to capture actual fraud attempts. |
| **F1-Score** | 0.87 | Balance between Precision and Recall. |



---

## 💻 5. GUI & Deployment
The project includes a **Streamlit Enterprise Dashboard** for manual transaction audits:
* **Security Audit Panel**: Allows officers to input transaction details manually.
* **Real-time Logic**: The dashboard loads the `model.pkl` file for instant risk assessments.
* **Processing Latency**: Average scan execution time is **4ms**.

---

## 📂 6. Dataset Source
The training data is sourced from the official Kaggle Credit Card Fraud Detection dataset.
* **Dataset Name**: Credit Card Fraud Detection
* **Link**: [Kaggle Credit Card Fraud Dataset](https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud)

---

## 🛡️ 7. Operational Summary
**FraudGuard AI** provides a robust defense against financial crimes. With a high precision rate and fast processing, it is suitable for integration into modern payment gateways.

---

**Developed By**: Mubasher & Fellows  
**Documentation Date**: January 4, 2026  
**Copyright**: © 2026 FraudGuard Global Security | Secure Data Processing Unit  
**Framework**: Scikit-Learn / Streamlit
