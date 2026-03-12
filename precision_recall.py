TP = 60
FP = 30
FN = 20

precision = TP / (TP + FP)
recall = TP / (TP + FN)
f_score = 2 * (precision * recall) / (precision + recall)

print("Precision =", precision)
print("Recall =", recall)
print("F-score =", f_score)