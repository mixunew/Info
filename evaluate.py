from sklearn.metrics import average_precision_score

# true relevance of documents
y_true = [1,0,1,1,0]

# predicted ranking scores
y_scores = [0.9,0.3,0.8,0.7,0.2]

ap = average_precision_score(y_true, y_scores)

print("Average Precision =", round(ap,2))