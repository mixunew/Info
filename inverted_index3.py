doc1 = "our class meeting starts soon"
doc2 = "my class starts at 6"

# tokenize
t1 = doc1.lower().split()
t2 = doc2.lower().split()

# unique terms
terms = set(t1 + t2)

# build inverted index
index = {}

for word in terms:
    docs = []
    if word in t1:
        docs.append("Doc1")
    if word in t2:
        docs.append("Doc2")
    index[word] = docs

print("Inverted Index:\n")

for k,v in index.items():
    print(k,"->",v)

query = ["class","meeting"]

# search for documents containing query terms
print("\nDocuments containing 'class meeting':")

for d in ["Doc1","Doc2"]:
    tokens = t1 if d=="Doc1" else t2
    if all(q in tokens for q in query):
        print(d)