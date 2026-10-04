# Near-Earth Objects Hazard Prediction System

## 📌 Project Description

The **Near-Earth Objects (NEO) Hazard Prediction System** is a Machine Learning classification project that predicts whether a Near-Earth Object is **Hazardous or Non-Hazardous** based on its physical and orbital characteristics.

The project involves data analysis, preprocessing, feature engineering, feature selection, handling class imbalance, training multiple Machine Learning models, hyperparameter tuning, model evaluation, and deployment using Streamlit.

### Why is it useful?

Near-Earth Objects need to be monitored because some objects may potentially pose a risk to Earth. This project helps in the **early identification and classification of potentially hazardous objects**, which can support risk assessment and monitoring of Near-Earth Objects.

---

## 🎯 Project Objective

The main objective of this project is to develop a Machine Learning model that can classify Near-Earth Objects into two categories:

- **Hazardous**
- **Non-Hazardous**

The project also aims to:

- Analyze the NEO dataset
- Perform Exploratory Data Analysis (EDA)
- Preprocess the data
- Perform feature engineering and feature selection
- Handle class imbalance
- Train multiple classification algorithms
- Perform hyperparameter tuning
- Compare model performance
- Select the best-performing model
- Deploy the final model using Streamlit

---

## 🛠️ Technologies Used

- **Python**
- **Pandas**
- **NumPy**
- **Scikit-learn**
- **XGBoost**
- **Machine Learning**
- **Google Colab**
- **Streamlit**
- **GitHub**

---

## 🤖 Machine Learning Models

The following Machine Learning classification algorithms were trained, tuned, and evaluated:

1. K-Nearest Neighbors (KNN)
2. Gaussian Naive Bayes
3. Decision Tree
4. Logistic Regression
5. Support Vector Machine (SVM)
6. Random Forest
7. AdaBoost
8. Gradient Boosting
9. XGBoost

---

## 📊 Dataset

The dataset contains information about **Near-Earth Objects (NEOs)** and their physical and orbital characteristics.

The target variable used for prediction is:

```text
hazardous
```

The target variable contains two classes:

- `True` → Hazardous
- `False` → Non-Hazardous

The dataset was analyzed and preprocessed before being used for Machine Learning.

Columns that were not useful for prediction, such as `id` and `name`, were removed during preprocessing.

---

## 🔍 Exploratory Data Analysis

Exploratory Data Analysis (EDA) was performed to understand the dataset and identify important patterns.

The EDA process included:

- Checking dataset shape
- Checking data types
- Identifying missing values
- Checking duplicate values
- Understanding statistical information
- Analyzing the target variable
- Studying feature distributions
- Identifying relationships between features
- Understanding class imbalance

---

## 🧹 Data Preprocessing

The following preprocessing steps were performed:

- Removal of unnecessary columns
- Handling the target variable
- Checking missing values
- Separating features and target
- Feature transformation
- Feature scaling where required
- Feature engineering
- Feature selection
- Handling class imbalance

The columns `id` and `name` were removed because they were not required for Machine Learning prediction.

---

## 🎯 Feature Engineering and Feature Selection

Feature engineering was performed to prepare the available features for Machine Learning models.

Feature selection was then performed to identify the most relevant features for predicting whether a Near-Earth Object is hazardous.

The selected features were used for model training, hyperparameter tuning, and evaluation.

---

# ⚖️ Handling Class Imbalance

The original dataset was highly imbalanced, with a significantly larger number of **Non-Hazardous** objects compared with **Hazardous** objects.

To understand the effect of class imbalance and identify the best approach, the models were trained and evaluated using different data-handling strategies.

The following approaches were experimented with:

### 1. Original Data

The models were trained using the original imbalanced dataset without downsampling.

This approach was used as a baseline for comparison.

### 2. Balanced Data

Class balancing techniques were applied to handle the imbalance between the Hazardous and Non-Hazardous classes.

The models were then trained and evaluated using the balanced data.

### 3. Downsampled Training Data with Original Test Data

The training data was downsampled to reduce the majority class, while the test data was kept in its original distribution.

This approach was used to check how well the model trained on a reduced majority class performs on the original test distribution.

### 4. Downsampled Data

The majority **Non-Hazardous** class was downsampled while retaining the available **Hazardous** observations.

In the final downsampling approach, the number of Non-Hazardous observations was reduced to approximately **45,000**, while the Hazardous observations were retained.

The resulting dataset was shuffled before the train/test split.

This approach produced the best overall performance for the final Random Forest model.

---

## 🔄 Overall Machine Learning Workflow

The project follows the following workflow:

```text
Data Collection
       ↓
Exploratory Data Analysis (EDA)
       ↓
Data Preprocessing
       ↓
Feature Engineering
       ↓
Feature Selection
       ↓
Handling Class Imbalance
       ↓
Train/Test Split
       ↓
Model Building
       ↓
Hyperparameter Tuning
       ↓
Model Evaluation
       ↓
Comparison of Different Data Approaches
       ↓
Best Model Selection
       ↓
Streamlit Deployment
```

---

# 🧠 Model Training

Multiple classification algorithms were trained using the processed dataset.

Each model was evaluated using different performance metrics, including:

- Accuracy
- Precision
- Recall
- F1-Score
- Confusion Matrix
- Classification Report

Because the dataset was imbalanced, **F1-score** was given particular importance when comparing model performance.

---

# ⚙️ Hyperparameter Tuning

Hyperparameter tuning was performed for the Machine Learning models to improve their performance.

**GridSearchCV** was used to find suitable hyperparameter combinations for the models.

The tuned models were then evaluated on the respective test data.

This process helped identify the best-performing model and its suitable hyperparameter configuration.

---

# 📈 Model and Data Approach Comparison

The models were trained and evaluated using different data approaches, including:

- Original data
- Balanced data
- Downsampled training data with original test data
- Downsampled data

The performance of the models was compared using evaluation metrics, with particular importance given to the **F1-score** because of the class imbalance.

Among the approaches tested, the **downsampled data approach with Random Forest** produced the best result for this project.

---

## 🏆 Best Performing Model

After training, tuning, and comparing multiple Machine Learning models and different data-handling approaches, **Random Forest** was selected as the final model.

### Final Model

**Random Forest Classifier**

### Best F1-Score

**Approximately 0.56**

The Random Forest model trained using the **downsampled data** produced the best F1-score among the approaches tested.

The model was therefore selected for the final prediction system and deployment.

---

## 📊 Model Comparison

The following table shows the approximate F1-scores obtained from the model comparison using the selected downsampled data approach:

| Model               | Approximate F1-Score |
| ------------------- | -------------------: |
| KNN                 |                 0.52 |
| Naive Bayes         |                 0.54 |
| Decision Tree       |                 0.46 |
| Logistic Regression |                 0.36 |
| SVM                 |                 0.40 |
| **Random Forest**   |             **0.56** |
| AdaBoost            |                 0.38 |
| Gradient Boosting   |                 0.41 |
| XGBoost             |                 0.40 |

**Random Forest achieved the highest F1-score of approximately 0.56 and was selected as the final model.**

---

# 🌐 Streamlit Deployment

The final trained Random Forest model was integrated into a **Streamlit web application**.

The application provides an interactive interface where users can enter the required Near-Earth Object information.

The entered information is passed to the trained Machine Learning model, which predicts whether the object is hazardous or non-hazardous.

### Prediction Output

The application provides one of the following predictions:

```text
Hazardous
```

or

```text
Non-Hazardous
```

---

# 🚀 Live Demo

The Machine Learning model is deployed using Streamlit.

**Live Application:**
(https://neohazardprediction-mlproject.streamlit.app/)
---

# 💻 How to Run the Project Locally

## 1. Clone the Repository

```bash
git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY-NAME.git
```

## 2. Open the Project Folder

```bash
cd YOUR-REPOSITORY-NAME
```

## 3. Create a Virtual Environment

```bash
python -m venv venv
```

## 4. Activate the Virtual Environment

For Windows:

```bash
venv\Scripts\activate
```

## 5. Install Required Libraries

```bash
pip install -r requirements.txt
```

## 6. Run the Streamlit Application

```bash
streamlit run app.py
```

The application will open in your browser.

---

# 📁 Project Structure

```text
Near-Earth-Objects-Hazard-Prediction/
│
├── app.py
│
├── model_pipe.pkl
│
├── requirements.txt
│
├── README.md
│
└── other project files
```

### File Description

| File               | Description                                          |
| ------------------ | ---------------------------------------------------- |
| `app.py`           | Streamlit application used for NEO hazard prediction |
| `model_pipe.pkl`   | Saved final Machine Learning model/pipeline          |
| `requirements.txt` | Required Python libraries                            |
| `README.md`        | Project documentation                                |

---

# 🔮 Prediction Workflow

The deployed Streamlit application follows this process:

```text
User Enters NEO Information
          ↓
Input Data Preprocessing
          ↓
Feature Transformation
          ↓
Trained Random Forest Model
          ↓
Hazard Prediction
          ↓
Hazardous / Non-Hazardous
```

---

# 📌 Key Features

- Near-Earth Object hazard classification
- Exploratory Data Analysis
- Data preprocessing
- Feature engineering
- Feature selection
- Class imbalance handling
- Original data model training
- Balanced data model training
- Downsampled training data with original test data
- Downsampled data model training
- Multiple Machine Learning algorithms
- Hyperparameter tuning
- Model performance comparison
- Random Forest final model selection
- Interactive Streamlit interface
- Web-based prediction system

---

# 🎓 Project Information

### Project Type

**Machine Learning Classification Project**

### Problem Type

**Binary Classification**

### Target Variable

```text
hazardous
```

### Target Classes

```text
True  → Hazardous
False → Non-Hazardous
```

### Final Model

```text
Random Forest Classifier
```

### Best Data Approach

```text
Downsampled Data
```

### Best F1-Score

```text
Approximately 0.56
```

### Deployment

```text
Streamlit
```

---

# 👩‍💻 Author

**Shreya**

B.Tech in Computer Science and Engineering
Specialization: Artificial Intelligence and Machine Learning

---

# 📜 Conclusion

The **Near-Earth Objects Hazard Prediction System** demonstrates the application of Machine Learning for classifying Near-Earth Objects as hazardous or non-hazardous.

The project involved **EDA, data preprocessing, feature engineering, feature selection, class imbalance handling, model training, hyperparameter tuning, and model evaluation**.

Different data-handling approaches were also investigated, including **original data, balanced data, downsampled training data with original test data, and fully downsampled data**.

Multiple Machine Learning classification algorithms were trained and compared. After evaluating the different approaches, the **Random Forest model trained using the downsampled data** produced the best performance, achieving an F1-score of approximately **0.56**.

The final Random Forest model was integrated into a **Streamlit web application**, allowing users to enter Near-Earth Object information and receive a prediction of whether the object is hazardous or non-hazardous.
