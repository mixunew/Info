from sklearn.metrics import precision_score, recall_score, f1_score, average_precision_score

y_true = [0,1,1,0,1]
y_scores = [0.1,0.8,0.6,0.3,0.9]

# convert scores to predicted labels
y_pred = [1 if s>0.5 else 0 for s in y_scores]

precision = precision_score(y_true,y_pred)
recall = recall_score(y_true,y_pred)
f1 = f1_score(y_true,y_pred)
avg_precision = average_precision_score(y_true,y_scores)

print("Precision =",precision)
print("Recall =",recall)
print("F1-score =",f1)
print("Average Precision =",avg_precision)