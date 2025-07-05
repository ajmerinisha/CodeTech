import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from tabulate import tabulate  

data = {
    'text': [
        "Congratulations! You've won a $1,000 Walmart gift card. Go to http://bit.ly/123456",
        "Hi John, are we still meeting tomorrow?",
        "Urgent! Your account has been compromised. Click here to secure it.",
        "Don't forget to bring the documents to the meeting.",
        "WINNER! Call 123-456-7890 to claim your prize.",
        "Let's catch up soon!",
        "You have received a new voicemail. Click to listen.",
        "Hey, how was your weekend?"
    ],
    'label': ['spam', 'ham', 'spam', 'ham', 'spam', 'ham', 'spam', 'ham']
}
df = pd.DataFrame(data)


X = df['text']
y = df['label']

vectorizer = CountVectorizer()
X_vectorized = vectorizer.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(X_vectorized, y, test_size=0.25, random_state=42)

model = MultinomialNB()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print("✅ Accuracy:", accuracy_score(y_test, y_pred))


conf_matrix = confusion_matrix(y_test, y_pred, labels=["ham", "spam"])
conf_df = pd.DataFrame(conf_matrix, index=["Actual Ham", "Actual Spam"], columns=["Predicted Ham", "Predicted Spam"])
print("\n📊 Confusion Matrix:")
print(tabulate(conf_df, headers='keys', tablefmt='grid'))


report = classification_report(y_test, y_pred, output_dict=True)
report_df = pd.DataFrame(report).transpose()
print("\n📈 Classification Report:")
print(tabulate(report_df, headers='keys', tablefmt='grid', floatfmt=".2f"))


sample = ["Get free coupons now by clicking here!"]
sample_vector = vectorizer.transform(sample)
sample_prediction = model.predict(sample_vector)[0]
print(f"\n💬 Sample Prediction: '{sample[0]}' → {sample_prediction}")
