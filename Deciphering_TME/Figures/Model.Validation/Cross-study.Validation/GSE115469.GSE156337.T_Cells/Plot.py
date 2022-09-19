import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import pearsonr

prediction = pd.read_csv('Cibersortx.Prediction.csv',index_col=0)
cell_annotation = 'T_Cells'
prediction = list(prediction['T_Cells'])

preset = pd.read_csv('%s.TestTarget.txt'%cell_annotation,index_col=0,delimiter='\t')
preset = list(preset['T Cells'])

plt.figure(figsize=(6,6))
plt.scatter(preset,prediction,s=2)
plt.xlabel('Predefined Proportion',fontsize=15)
plt.ylabel('Estimated Fraction',fontsize=15)
plt.title('T Cell (GSE115469 - GSE156337)',fontsize=15)
plt.text(0.2,0.8,'r = %s'%(round(pearsonr(preset,prediction)[0],4)))
ticks = [0,0.2,0.4,0.6,0.8,1]
plt.xticks(ticks)
plt.yticks(ticks)
plt.tight_layout()
plt.savefig('GSE115469.GSE156337.%s.pdf'%cell_annotation,format='pdf')


