from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

docs = [
"Document about python programming language and data analysis",
"Document discussing machine learning algorithms and programming techniques",
"Overview of natural language processing and its applications"
]

query = ["python programming"]

# TF-IDF vectorization
vectorizer = TfidfVectorizer()

tfidf = vectorizer.fit_transform(docs + query)

# split document and query vectors
doc_vectors = tfidf[:-1]
query_vector = tfidf[-1]

print("TF-IDF Matrix:\n", tfidf.toarray())

# B) Part of the slip - Cosine Similarity between query and documents
# cosine similarity
similarity = cosine_similarity(query_vector, doc_vectors)

print("\nCosine Similarity with Query:\n")

for i,score in enumerate(similarity[0]):
    print("Doc",i+1,"=",round(score,3))