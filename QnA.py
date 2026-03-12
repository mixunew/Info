text = """
Computer science is the study of computers.
Information retrieval helps find relevant documents.
Practical examination will start tomorrow.
"""

sentences = text.lower().split(".")

question = input("Ask question: ").lower()

for s in sentences:
    if "computer science" in question and "computer science" in s:
        print("Answer:", s.strip())
    elif "exam" in question and "start" in s:
        print("Answer:", s.strip())
    elif "information retrieval" in question and "information retrieval" in s:
        print("Answer:", s.strip())