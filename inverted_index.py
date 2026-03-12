import nltk
from nltk.corpus import stopwords

nltk.download('stopwords', quiet=True)
stop = set(stopwords.words('english'))

docs = {
    "Doc1": "The computer science students are appearing for practical examination",
    "Doc2": "computer science practical examination will start tomorrow"
}

tokens = {d: text.lower().split() for d, text in docs.items()}

# build inverted index
index = {}
for d, words in tokens.items():
    for w in words:
        if w not in stop:
            index.setdefault(w, []).append(d)

# print inverted index
for term, doc in index.items():
    print(term, "->", doc)

# search query
query = ["computer", "science"]

print("\nDocuments containing 'computer science':")
for d, words in tokens.items():
    if all(q in words for q in query):
        print(d)