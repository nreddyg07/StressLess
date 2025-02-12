import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib
data = {
    'Q1': [2, 1, 1, 2, 2, 1, 2, 0, 2, 1],
    'Q2': [1, 0, 1, 1, 1, 1, 2, 0, 1, 1],
    'Q3': [2, 0, 1, 2, 1, 1, 2, 1, 2, 1],
    'Q4': [2, 2, 1, 2, 2, 2, 1, 0, 2, 1],
    'Q5': [1, 1, 1, 1, 2, 1, 2, 0, 2, 1],
    'Q6': [1, 1, 1, 1, 1, 2, 1, 0, 1, 1],
    'Q7': [1, 0, 1, 2, 1, 1, 1, 1, 2, 1],
    'Q8': [1, 1, 0, 2, 2, 1, 2, 1, 1, 1],
    'Q9': [2, 1, 1, 2, 1, 2, 2, 1, 2, 2],
    'Q10': [1, 0, 2, 1, 1, 1, 2, 1, 1, 1],
    'Stress_Level': ['High', 'Low', 'Moderate', 'High', 'Moderate', 'Low', 'High', 'Low', 'Moderate', 'Low']
}
df = pd.DataFrame(data)
X = df.iloc[:, :-1]
y = df['Stress_Level']
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
y = le.fit_transform(y)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f'Model Accuracy: {accuracy * 100:.2f}%')
joblib.dump(model, 'stress_model.pkl')
joblib.dump(le, 'label_encoder.pkl')
