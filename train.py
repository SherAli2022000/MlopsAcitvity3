import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
import joblib
import json

# Load data and select first 2000 rows
df = pd.read_csv('creditcard.csv', nrows=2000)

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(df.drop('Class', axis=1), df['Class'], test_size=0.2, random_state=42)

# Train a random forest classifier
rf = RandomForestClassifier(n_estimators=100, random_state=42)
rf.fit(X_train, y_train)

# Make predictions on the test set
y_pred = rf.predict(X_test)

# Calculate evaluation metrics
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
# Save metrics to a JSON file
metrics = {'accuracy': accuracy, 'precision': precision}
with open('metrics.json', 'w') as f:
    json.dump(metrics, f)

# Save model to a joblib file
joblib.dump(rf, 'model.joblib')
