import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import pearsonr

prediction = pd.read_csv('Cibersortx.Prediction.Bi-potent.csv',index_col=0)
cell_annotation = 'Bi-Potent Cells'
prediction = list(prediction[cell_annotation])

preset = pd.read_csv('%s.TestTarget.txt'%cell_annotation,index_col=0,delimiter='\t')
preset = list(preset[cell_annotation])

plt.figure(figsize=(6,6))
plt.scatter(preset,prediction,s=2)
plt.xlabel('Predefined Proportion',fontsize=15)
plt.ylabel('Estimated Fraction',fontsize=15)
plt.title('Bi-potent Cell Prediction',fontsize=15)
plt.text(0.2,0.8,'r = %s'%(round(pearsonr(preset,prediction)[0],3)))
plt.savefig('GSE146409.%s.Validation.pdf'%cell_annotation,format='pdf')


