TP = 60
FP = 30
FN = 20

precision = TP / (TP + FP)
recall = TP / (TP + FN)
fscore = 2 * (precision * recall) / (precision + recall)

print("Precision =", round(precision,2))
print("Recall =", round(recall,2))
print("F-score =", round(fscore,2))