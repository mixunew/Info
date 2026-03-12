docs = {
1: "The university exam is scheduled next week",
2: "The university of mumbai has declared the result"
}

# build inverted index
index = {}

for id,text in docs.items():
    for word in text.lower().split():
        if word not in index:
            index[word] = []
        if id not in index[word]:
            index[word].append(id)

print("Inverted Index:\n",index)

# Boolean AND query
result = set(index.get("university",[])) & set(index.get("mumbai",[]))

print("\nDocuments for query 'university AND mumbai':",list(result))