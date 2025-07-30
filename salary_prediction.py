import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv('salary_data.csv')

# Encode 'education_level' (categorical → numeric)
le = LabelEncoder()
df['education_level'] = le.fit_transform(df['education_level'])  # Bachelor=0, Master=1, PhD=2

# Define features and label
X = df[['experience', 'education_level', 'age']]
y = df['salary']

# Split into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the Linear Regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Evaluate the model
score = model.score(X_test, y_test)
print("Model R^2 Score:", score)

# Make predictions on test data
predictions = model.predict(X_test)
print("\nPredictions on Test Data:", predictions)
print("Actual Salaries:", y_test.values)

# Predict salary for a new person
# Example: 4 years experience, Master’s degree, 27 years old
new_data = pd.DataFrame([[4, le.transform(['Master'])[0], 27]], columns=['experience', 'education_level', 'age'])
predicted_salary = model.predict(new_data)
print("\nPredicted Salary for new input:", predicted_salary[0])

# Optional: Visualization
sns.scatterplot(x=y_test, y=predictions)
plt.xlabel("Actual Salary")
plt.ylabel("Predicted Salary")
plt.title("Actual vs Predicted Salary")
plt.grid(True)
plt.show()
