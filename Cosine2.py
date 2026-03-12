import math

query = "gold silver truck"
doc = "shipment of gold damaged in a gold fire"

q_words = query.split()
d_words = doc.split()

vocab = set(q_words + d_words)

q_vec = []
d_vec = []

for w in vocab:
    q_vec.append(q_words.count(w))
    d_vec.append(d_words.count(w))

# cosine similarity
dot = sum(q_vec[i]*d_vec[i] for i in range(len(vocab)))

q_mag = math.sqrt(sum(x*x for x in q_vec))
d_mag = math.sqrt(sum(x*x for x in d_vec))

similarity = dot/(q_mag*d_mag)

print("Cosine Similarity =", round(similarity,3))