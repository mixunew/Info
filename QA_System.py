# knowledge corpus
text = """
India has the second-largest population in the world.
Tiger is the national animal of India.
Peacock is the national bird of India.
Mango is the national fruit of India.
"""

# split into sentences
sentences = text.lower().split(".")

# take question from user
question = input("Ask your question: ").lower()

# search answer
for s in sentences:
    if "national bird" in question and "national bird" in s:
        print("Answer:", s.strip())