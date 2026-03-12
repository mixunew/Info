from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans

docs = [
"Machine learning is the study of computer algorithms that improve through experience",
"Deep learning is a subset of machine learning",
"Natural language processing is a field of artificial intelligence",
"Computer vision enables computers to interpret the visual world",
"Reinforcement learning is a machine learning algorithm",
"Information retrieval is the process of obtaining information from a collection",
"Text mining derives high quality information from text",
"Data clustering divides a set of objects into groups",
"Hierarchical clustering builds a tree of clusters",
"K-means clustering is a method of vector quantization"
]

# convert text → TF-IDF
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(docs)

# apply K-means clustering
kmeans = KMeans(n_clusters=3, random_state=0)
kmeans.fit(X)

# print cluster for each document
for i,label in enumerate(kmeans.labels_):
    print("Document",i+1,"→ Cluster",label)