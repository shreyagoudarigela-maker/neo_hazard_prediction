# Near-Earth Objects Hazard Prediction System

## 📌 Project Description

The **Near-Earth Objects (NEO) Hazard Prediction System** is a Machine Learning classification project that predicts whether a Near-Earth Object is **Hazardous or Non-Hazardous** based on its physical and orbital characteristics.

The project involves data analysis, preprocessing, feature engineering, feature selection, handling class imbalance, training multiple Machine Learning models, hyperparameter tuning, model evaluation, and deployment using Streamlit.

### Why is it useful?

Near-Earth Objects need to be monitored because some objects may potentially pose a risk to Earth. This project helps in the **early identification and classification of potentially hazardous objects**, which can support risk assessment and monitoring of Near-Earth Objects.

---

# 🚀 Live Demo

The Machine Learning model is deployed using Streamlit.

**Live Application:**  
https://neohazardprediction-mlproject.streamlit.app/

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

## 📸 Application Screenshots

### 🛰️ NEO Hazard Prediction Interface – 1

The Streamlit application provides an interactive interface where users can enter the physical and orbital characteristics of a Near-Earth Object.

![NEO Hazard Prediction Interface 1](screenshots/neo_interface_1.png)

### 🛰️ NEO Hazard Prediction Interface – 2

The application provides a user-friendly interface for entering NEO details and generating a hazard prediction.

![NEO Hazard Prediction Interface 2](screenshots/neo_interface_2.png)

### 🔮 Prediction Result

The application displays the predicted result based on the input values provided by the user.

![Prediction Result](screenshots/prediction_result.png)

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

To understand the effect of class imbalance and identify a suitable approach, different data-handling strategies were experimented with.

### 1. Original Data

The models were trained and tested using the original data distribution without downsampling.

This approach was used as a baseline for comparison.

### 2. Downsampled Training Data with Original Test Data

In this approach, only the **training data** was downsampled to reduce the majority Non-Hazardous class.

The **test data was kept in its original distribution**.

This experiment was performed to evaluate how a model trained on a downsampled training set performs when tested on data with the original class distribution.

### 3. Downsampled Data

In the final approach, the majority **Non-Hazardous** class was downsampled while retaining the available **Hazardous** observations.

The number of Non-Hazardous observations was reduced to approximately **45,000**, while the Hazardous observations were retained.

The resulting dataset was shuffled before performing the train/test split.

This approach produced the best performance for the final Random Forest model.

---

# 🔄 Overall Machine Learning Workflow

The project follows the following workflow:

```text
Data Collection
       ↓
Exploratory Data Analysis (EDA)
       ↓
Data Preprocessing
       ↓
Handling Class Imbalance
       ↓
Train/Test Split
       ↓
Feature Engineering
       ↓
Feature Selection
       ↓
Model Building
       ↓
Hyperparameter Tuning
       ↓
Model Evaluation
       ↓
Comparison of Data Approaches
       ↓
Best Model Selection
       ↓
Streamlit Deployment
```

---

# 🧠 Model Training

Multiple classification algorithms were trained using the processed dataset.

The models were evaluated using different performance metrics, including:

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

# 📈 Data Approach Comparison

The project experimented with different approaches to understand the effect of class imbalance on model performance.

The two main comparison approaches were:

- **Original Data**
- **Downsampled Training Data + Original Test Data**

The final **Downsampled Data** approach was then used to develop the final model after observing its performance.

---

## 📊 Original Data Results

The following F1-scores were obtained when the models were trained and evaluated using the **original data without downsampling**:

| Model               | F1-Score |
| ------------------- | -------: |
| KNN                 |     0.52 |
| Naive Bayes         |     0.54 |
| Decision Tree       |     0.46 |
| Logistic Regression |     0.36 |
| Random Forest       |     0.45 |
| AdaBoost            |     0.27 |
| Gradient Boosting   |     0.27 |
| XGBoost             |     0.27 |

---

## 📊 Downsampled Training Data + Original Test Data Results

In this experiment, the **training data was downsampled**, while the **test data retained the original class distribution**.

The following F1-scores were obtained:

| Model               | F1-Score |
| ------------------- | -------: |
| KNN                 |     0.43 |
| Naive Bayes         |     0.29 |
| Decision Tree       |     0.42 |
| Logistic Regression |     0.25 |
| Random Forest       |     0.48 |
| AdaBoost            |     0.29 |
| Gradient Boosting   |     0.34 |
| XGBoost             |     0.35 |

This experiment showed that changing the training class distribution affected the model's performance when evaluated on the original test distribution.

---

# 🏆 Final Best Model

After experimenting with different data approaches, training multiple Machine Learning models, performing hyperparameter tuning, and comparing the evaluation results, **Random Forest** was selected as the final model.

### Final Model

**Random Forest Classifier**

### Best Data Approach

**Downsampled Data**

### Best F1-Score

**Approximately 0.56**

The Random Forest model trained using the **downsampled data** produced the best F1-score among the approaches tested.

Therefore, the Random Forest model was selected for the final prediction system and deployment.

---

# 📊 Final Model Comparison

The following results represent the approximate F1-scores obtained from the final downsampled data approach:

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

# 💻 How to Run the Project Locally

## 1. Clone the Repository

```bash
git clone https://github.com/shreyagoudarigela-maker/neo_hazard_prediction.git
```

## 2. Open the Project Folder

```bash
cd neo_hazard_prediction
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
neo_hazard_prediction/
│
├── app.py
│
├── model_pipe (1).pkl
│
├── requirements.txt
│
├── runtime.txt
│
├── README.md
│
└── other project files
```

### File Description

| File                  | Description |
| --------------------- | ----------- |
| `app.py`              | Streamlit application used for NEO hazard prediction |
| `model_pipe (1).pkl`  | Saved final Machine Learning model/pipeline |
| `requirements.txt`    | Required Python libraries |
| `runtime.txt`         | Python runtime version used for deployment |
| `README.md`           | Project documentation |

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

# 📜 Conclusion

The **Near-Earth Objects Hazard Prediction System** demonstrates the application of Machine Learning for classifying Near-Earth Objects as hazardous or non-hazardous.

The project involved **EDA, data preprocessing, feature engineering, feature selection, class imbalance handling, model training, hyperparameter tuning, and model evaluation**.

Different data approaches were investigated, including training and testing on the **original data**, training on **downsampled training data with the original test data**, and training and testing using the **downsampled data**.

Multiple Machine Learning classification algorithms were trained and tuned. The results from these experiments were compared using evaluation metrics, with particular importance given to the **F1-score** due to the class imbalance in the dataset.

Among the approaches tested, the **Random Forest model trained using the downsampled data** produced the best performance, achieving an F1-score of approximately **0.56**.

The final Random Forest model was integrated into a **Streamlit web application**, allowing users to enter Near-Earth Object information and receive a prediction of whether the object is hazardous or non-hazardous.

# 👩‍💻 Author

**Shreya**

B.Tech in Computer Science and Engineering  
Specialization: Artificial Intelligence and Machine Learning

Linkedin:https://www.linkedin.com/in/shreya-arigela
Github:https://github.com/shreyagoudarigela-maker

---
