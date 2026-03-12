from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import LinearSVC

categories = ['alt.atheism','soc.religion.christian','comp.graphics','sci.med']

# load dataset
data = fetch_20newsgroups(
    subset='train',
    categories=categories,
    remove=('headers','footers','quotes')
)

# TF-IDF vectorization
vectorizer = TfidfVectorizer(max_features=2000)
X = vectorizer.fit_transform(data.data)

# train SVM model
model = LinearSVC()
model.fit(X, data.target)

print("SVM Model Trained!\n")

# user input
text = input("Enter a document: ")

# convert text
text_vec = vectorizer.transform([text])

# prediction
pred = model.predict(text_vec)

print("Predicted Category:", data.target_names[pred[0]])