from sklearn.feature_extraction.text import TfidfVectorizer

docs = [
"The sun is the star at the center of the solar system",
"She wore a beautiful dress to the party last night",
"The book on the table caught my attention immediately"
]

query = ["solar system"]

# TF-IDF vectorization
vectorizer = TfidfVectorizer()
tfidf = vectorizer.fit_transform(docs + query)

print("TF-IDF Matrix:\n")
print(tfidf.toarray())