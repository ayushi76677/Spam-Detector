import pandas as pd

# Load dataset
data = pd.read_csv("spam.csv", encoding='latin-1')

# Keep only required columns
data = data[['v1', 'v2']]
data.columns = ['label', 'message']

print(data.head())
# Data preprocessing
from sklearn.feature_extraction.text import CountVectorizer

cv = CountVectorizer()
X = cv.fit_transform(data['message'])

y = data['label']
# Train model
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = MultinomialNB()
model.fit(X_train, y_train)
# Test accuracy
accuracy = model.score(X_test, y_test)
print("Accuracy:", accuracy)
# Take user input and predict
msg = input("Enter a message: ")
msg_data = cv.transform([msg])

prediction = model.predict(msg_data)

print("Prediction:", prediction[0])
