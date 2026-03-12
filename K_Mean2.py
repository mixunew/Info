from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans

docs = [
"The sun is the star at the center of the solar system",
"She wore a beautiful dress to the party last night",
"The book on the table caught my attention immediately"
]

# convert text → TF-IDF
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(docs)

# apply K-means clustering
kmeans = KMeans(n_clusters=2, random_state=0)
kmeans.fit(X)

print("Cluster Results:\n")

for i,label in enumerate(kmeans.labels_):
    print("Document", i+1, "→ Cluster", label)