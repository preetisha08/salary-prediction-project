# train_model.py

import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import pickle

# Load dataset
df = pd.read_csv('salary_data.csv')

# Encode education
le = LabelEncoder()
df['education_level'] = le.fit_transform(df['education_level'])  # Bachelor=0, Master=1, PhD=2

# Features and label
X = df[['experience', 'education_level', 'age']]
y = df['salary']

# Train model
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = LinearRegression()
model.fit(X_train, y_train)

# Save model
with open('model.pkl', 'wb') as f:
    pickle.dump((model, le), f)

print("✅ Model trained and saved as model.pkl")
