# knowledge corpus
text = """
India has the second-largest population in the world.
Tiger is the national animal of India.
Peacock is the national bird of India.
Mango is the national fruit of India.
"""

# split into sentences
sentences = text.lower().split(".")

# user input
question = input("Ask your question: ").lower()

# search answer
for s in sentences:
    if "national bird" in question and "national bird" in s:
        print("Answer:", s.strip())
    elif "national animal" in question and "national animal" in s:
        print("Answer:", s.strip())
    elif "national fruit" in question and "national fruit" in s:
        print("Answer:", s.strip())