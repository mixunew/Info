text = """Information Retrieval is the process of searching for information.
Search engines use indexing and ranking algorithms.
PageRank is used by Google to rank web pages.
Information retrieval helps users find relevant documents."""

# split sentences
sentences = text.split(".")

# word frequency
freq = {}

for word in text.lower().split():
    freq[word] = freq.get(word,0) + 1

# score sentences
scores = {}

for s in sentences:
    score = 0
    for w in s.lower().split():
        score += freq.get(w,0)
    scores[s] = score

# best sentence
summary = max(scores, key=scores.get)

print("Summary:\n")
print(summary.strip())