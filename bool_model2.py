docs = {
1: "BSc lectures start at 7",
2: "My lectures are over",
3: "Today is a holiday"
}

# build inverted index
index = {}

for id, text in docs.items():
    for word in text.lower().split():
        if word not in index:
            index[word] = []
        index[word].append(id)

print("Inverted Index:\n", index)

# Boolean NOT query
query = "lectures"

result = []

for doc_id in docs:
    if doc_id not in index.get(query, []):
        result.append(doc_id)

print("\nDocuments for query 'NOT lectures':", result)