import nltk
from nltk.corpus import stopwords

nltk.download('stopwords', quiet=True)
stop = set(stopwords.words('english'))

docs = {
    "Doc1": "The quick brown fox jumped over the lazy dog",
    "Doc2": "The lazy dog slept in the sun"
}

tokens = {d: t.lower().split() for d, t in docs.items()}

# inverted index
index = {}
for d, w in tokens.items():
    for i in w:
        if i not in stop:
            index.setdefault(i, []).append(d)

print("Inverted Index:\n")
for t in sorted(index):
    print(t, "->", index[t])

# search
query = ["lazy", "sun"]

print("\nDocuments containing 'lazy sun':")
for d, w in tokens.items():
    if all(q in w for q in query):
        print(d)