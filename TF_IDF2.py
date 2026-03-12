from sklearn.feature_extraction.text import TfidfVectorizer

docs = [
"Document about python programming language and data analysis",
"Document discussing machine learning algorithms and programming techniques",
"Overview of natural language processing and its applications"
]

query = ["python programming"]

# TF-IDF vectorization
vectorizer = TfidfVectorizer()
tfidf = vectorizer.fit_transform(docs + query)

print("TF-IDF Matrix:\n")
print(tfidf.toarray())