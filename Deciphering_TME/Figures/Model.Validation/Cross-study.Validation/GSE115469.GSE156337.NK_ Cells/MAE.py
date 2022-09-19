import pandas as pd
import numpy as np

selected_cell = 'Nk_Cells'
predefine_file = 'Nk_Cells.TestTarget.txt'

prediction = pd.read_csv('Cibersortx.Prediction.csv',index_col=0)
prediction = prediction['NK-like_Cells']

predefine = pd.read_csv(predefine_file,delimiter='\t')
predefine = predefine['Nk Cells']

error = np.subtract(np.array(prediction),np.array(predefine))
mean_error = np.mean(error)
mean_absolute_error = np.mean(np.absolute(error))

file = open('%s_MAE.txt'%selected_cell,'w')
print('Mean Error = %s'%round(mean_error,4), file=file)
print('Mean Absolute Error = %s'%round(mean_absolute_error,4), file=file)
file.close()


