# documents
docs = {
1: "the cat chased the dog around the garden",
2: "she was sitting in the garden last night",
3: "i read the book the night before"
}

# build inverted index
index = {}

for id,text in docs.items():
    for word in set(text.split()):
        if word not in index:
            index[word] = []
        index[word].append(id)

print("Inverted Index:", index)

# query: garden OR night
result = set(index.get("garden",[])) | set(index.get("night",[]))

print("\nDocuments for query 'garden OR night':", list(result))