# knowledge text (source document)
text = """
Computer science is the study of computers and algorithms.
Practical examination will start tomorrow.
Students are appearing for the practical examination.
"""

# Information extraction (create knowledge base)
sentences = text.lower().split(".")

# ask question
question = input("Ask question: ").lower()

# find answer
for s in sentences:
    if "computer science" in question and "computer science" in s:
        print(s)
    elif "exam start" in question or "examination start" in question:
        if "start tomorrow" in s:
            print(s)
    elif "students" in question and "students" in s:
        print(s)