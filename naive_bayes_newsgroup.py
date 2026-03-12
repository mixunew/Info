from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

# categories we want
categories = ['alt.atheism','soc.religion.christian','comp.graphics','sci.med']

# load dataset
data = fetch_20newsgroups(
    subset='train',
    categories=categories,
    remove=('headers','footers','quotes')
)

# convert text to TF-IDF features
vectorizer = TfidfVectorizer(max_features=2000)
X = vectorizer.fit_transform(data.data)

# train model
model = MultinomialNB()
model.fit(X, data.target)

print("Naive Bayes Model Trained!\n")

# user input
text = input("Enter a document: ")

# transform input
text_vec = vectorizer.transform([text])

# predict category
pred = model.predict(text_vec)

print("Predicted Category:", data.target_names[pred[0]])