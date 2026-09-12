# 📩 Spam Message Classifier

A Machine Learning project that classifies messages as **Spam** or **Ham (Not Spam)** using **TF-IDF** for text feature extraction and **Support Vector Classifier (SVC)** for classification.

The model is deployed using **Streamlit**, allowing users to enter a message and get a prediction through a simple web interface.

## 📌 Project Overview

Spam messages are unwanted messages that may contain advertisements, scams, fake offers, or other unwanted content.

This project uses Machine Learning to automatically determine whether a given message is:

* 🚨 **Spam**
* ✅ **Ham**

## 🛠️ Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Scikit-learn
* TF-IDF Vectorizer
* Support Vector Classifier (SVC)
* Streamlit
* Pickle

## 📊 Dataset

The dataset contains messages labeled as:

* `1` → Spam
* `0` → Ham

The dataset was cleaned before training by removing duplicate records and performing basic text preprocessing.

## 🔄 Machine Learning Workflow

```text
Dataset
   ↓
Data Cleaning
   ↓
Exploratory Data Analysis
   ↓
Train-Test Split
   ↓
TF-IDF Vectorization
   ↓
Model Training
   ↓
Hyperparameter Tuning
   ↓
Model Evaluation
   ↓
Save Trained Model
   ↓
Streamlit Deployment
```

## 🤖 Model

Several classification models were tested during the project, including:

* Logistic Regression
* K-Nearest Neighbors
* Decision Tree
* Random Forest
* SVC

The **SVC model** achieved the best overall performance on the test dataset.

### SVC Performance

* **Accuracy:** 99.65%
* **Precision:** 99.27%
* **Recall:** 99.27%
* **F1 Score:** 99.27%

## 🧠 TF-IDF

TF-IDF (Term Frequency-Inverse Document Frequency) converts text messages into numerical features that can be understood by Machine Learning algorithms.

The project uses a Pipeline containing:

```text
Text Message
     ↓
TF-IDF Vectorizer
     ↓
SVC
     ↓
Spam / Ham
```
```

### File Description

**`app.py`**
Streamlit application used to create the web interface and make predictions.

**`spam_model.pkl`**
Saved trained Machine Learning pipeline containing TF-IDF and SVC.

**`spam_classifier.ipynb`**
Jupyter Notebook containing data cleaning, EDA, model training, tuning, and evaluation.

## 💻 Run Locally

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### 2. Go into the project directory

```bash
cd spam-classifier
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Streamlit application

```bash
streamlit run app.py
```

The application will open in your browser.

## 🧪 Example

### Input

```text
Congratulations! You have won a cash prize. Claim your reward now!
```

### Output

```text
🚨 This is SPAM
```

Another example:

### Input

```text
Hey, are we still meeting at the library at 5 PM?
```

### Output

```text
✅ This is HAM
```

## 🌐 Deployment

The application can be deployed using **Streamlit Community Cloud**.

Basic deployment process:

```text
GitHub Repository
       ↓
Streamlit Community Cloud
       ↓
Deploy app.py
       ↓
Public Web Application
```

## 📚 What I Learned

Through this project, I learned:

* Data cleaning using Pandas
* Exploratory Data Analysis
* Handling duplicate data
* Text preprocessing
* TF-IDF feature extraction
* Train-test splitting
* Classification algorithms
* Hyperparameter tuning
* Cross-validation
* Model evaluation
* Confusion matrix
* Precision, Recall and F1 Score
* Saving Machine Learning models using Pickle
* Deploying a Machine Learning model with Streamlit

## 👨‍💻 Author

**Adesh Rajpoot**

GitHub: Add your GitHub profile link here.

---

⭐ If you found this project useful, consider giving the repository a star!
