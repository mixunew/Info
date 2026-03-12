text = """Natural language processing (NLP) is a field of computer science,
artificial intelligence and computational linguistics concerned with
interactions between computers and human languages.
Many challenges in NLP involve natural language understanding and
machine learning.
Text summarization is the process of extracting important information
from text to produce a shorter version.
Automatic summarization helps manage the large amount of text data
available online."""

# split sentences
sentences = text.split(".")

# word frequency
freq = {}

for word in text.lower().split():
    freq[word] = freq.get(word,0)+1

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