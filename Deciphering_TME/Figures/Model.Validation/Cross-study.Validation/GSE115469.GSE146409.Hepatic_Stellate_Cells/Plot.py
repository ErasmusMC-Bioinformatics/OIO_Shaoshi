import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import pearsonr

prediction = pd.read_csv('Cibersortx.Prediction.csv',index_col=0)
cell_annotation = 'Hepatic_Stellate_Cells'
prediction = list(prediction['Hepatic_Stellate_Cells'])

preset = pd.read_csv('Stellate_cells.TestTarget.txt',index_col=0,delimiter='\t')
preset = list(preset['Stellate cells'])

plt.figure(figsize=(6,6))
plt.scatter(preset,prediction,s=2)
plt.xlabel('Predefined Proportion',fontsize=15)
plt.ylabel('Estimated Fraction',fontsize=15)
plt.title('Hepatic Stellate Cells (GSE115469 - GSE146409)',fontsize=15)
plt.text(0.2,0.8,'r = %s'%(round(pearsonr(preset,prediction)[0],4)))
ticks = [0,0.2,0.4,0.6,0.8,1]
plt.xticks(ticks)
plt.yticks(ticks)
plt.tight_layout()
plt.savefig('GSE115469.GSE146409.%s.Validation.pdf'%cell_annotation,format='pdf')


