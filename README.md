
# 💼 Salary Prediction using Machine Learning

A Streamlit web application that predicts a person's expected salary based on their experience, education level, and age. Built using Python, scikit-learn, and a simple CSV dataset, this project demonstrates how machine learning can be applied in real-world scenarios like salary estimation.

---

## 🚀 Features

- 🎯 Predict salary using input values:
  - Years of Experience
  - Education Level (Bachelor, Master, PhD)
  - Age
- 📈 Trained using Linear Regression
- 🔤 Encodes categorical data using LabelEncoder
- 🖥️ Interactive and clean UI built with Streamlit
- 📊 Actual vs Predicted salary plot (optional)

---

## 🛠️ Tech Stack

| Component      | Technology           |
|----------------|----------------------|
| Language       | Python               |
| Web Interface  | Streamlit            |
| ML Model       | scikit-learn (Linear Regression) |
| Data Handling  | pandas               |
| Visualization  | matplotlib, seaborn  |

---

## 📁 Project Structure

```
salary-prediction-project/
├── salary_data.csv          # Sample dataset
├── train_model.py           # Trains and saves the model (model.pkl)
├── model.pkl                # Trained ML model (serialized)
├── app.py                   # Streamlit web app
```

---

## 🧪 How to Run Locally

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/salary-prediction-ml.git
cd salary-prediction-ml
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

<sub>If `requirements.txt` is missing, run:</sub>

```bash
pip install pandas scikit-learn streamlit matplotlib seaborn
```

### 3. Train the Model

```bash
python train_model.py
```

### 4. Run the Streamlit App

```bash
streamlit run app.py
```

Then open [http://localhost:8501](http://localhost:8501) in your browser.

---

## 🔍 Sample Prediction

| Feature           | Value       |
|-------------------|-------------|
| Experience        | 4 years     |
| Education Level   | Master      |
| Age               | 27          |

📤 **Predicted Salary**: ₹61,000 (approx)

---

## 📚 Future Enhancements

- Use a real-world dataset (Kaggle, LinkedIn)
- Add more input features (location, skills, industry)
- Train with other algorithms (Random Forest, SVR, XGBoost)
- Model performance dashboard
- Deploy online (Streamlit Cloud / Hugging Face Spaces)
- Add user login & prediction history

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

## 👤 Author
preetisha 
