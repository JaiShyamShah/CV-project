import matplotlib.pyplot as plt
import numpy as np
test_tolerances = np.linspace(0.5,0.9,9)
with open('D:\CV_project\stanford_ocsr\chemtype2\precision_recall_by_tolerance.txt', 'r') as f:
  lines = f.readlines()
  precisions = [float(line.split()[0]) for line in lines]
  recalls = [float(line.split()[1]) for line in lines]

plt.scatter(test_tolerances,precisions,color='blue',label='Precision')
plt.scatter(test_tolerances,recalls,color='red',label='Recall')
plt.title("Precision/Recall Curve, OCR")
plt.xlabel("Tolerance")
plt.legend()
plt.show()