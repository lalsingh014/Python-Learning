import pandas as pd

df = pd.read_csv("titanic_cleaned.csv")
print(df.head())



# Features selection and Target
features = ["sex", "pclass", "age", "fare", "family_size"]
x = df[features]
y = df["survived"]



# Encode categorical data

X = pd.get_dummies(x, columns=["sex"], drop_first=True)
print(X.head())



# Train-test split

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)



# Feature scaling

from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)



# Train the Logistic Regression model

from sklearn.linear_model import LogisticRegression

model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)



# Make Predictions

y_pred = model.predict(X_test)



# Evaluate Model

#Accuracy
from sklearn.metrics import accuracy_score

print("\nModel Accuracy:")
print("Accuracy:", accuracy_score(y_test, y_pred))



# Classification Report

from sklearn.metrics import classification_report

print("\nClassification Report:\n")
print(classification_report(y_test, y_pred))



# Interpret coefficients

coefficients = pd.DataFrame({
    "Feature": X.columns,
    "Coefficient": model.coef_[0]
})

print(coefficients.sort_values(by="Coefficient", ascending=False))