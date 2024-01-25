# Import necessary libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# Load the dataset from a CSV file
file_path = 'data/trainingData.csv'
df = pd.read_csv(file_path)

# Assuming the target variable is 'Creditworthiness' (1 for good, 0 for bad)
# Modify this based on your dataset and business logic
df['Creditworthiness'] = df['Purpose'].apply(lambda x: 1 if x == 'Debt Consolidation' else 0)

# Drop unnecessary columns
df = df.drop(['Loan ID', 'Customer ID', 'Purpose'], axis=1)

# Handle missing values or other preprocessing steps as needed
# Split the data into features (X) and target variable (y)
X = df.drop('Creditworthiness', axis=1)
y = df['Creditworthiness']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Standardize the features
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Build a Random Forest Classifier
clf = RandomForestClassifier(random_state=42)
clf.fit(X_train, y_train)

# Make predictions on the test set
y_pred = clf.predict(X_test)

# Evaluate the model
print(f'Accuracy: {accuracy_score(y_test, y_pred)}')
print('\nClassification Report:\n', classification_report(y_test, y_pred))
print('\nConfusion Matrix:\n', confusion_matrix(y_test, y_pred))
