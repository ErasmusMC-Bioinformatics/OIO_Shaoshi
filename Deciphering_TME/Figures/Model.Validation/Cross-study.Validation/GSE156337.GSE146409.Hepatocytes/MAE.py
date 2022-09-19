import pandas as pd
import numpy as np

selected_cell = 'Hepatocytes'
predefine_file = 'Hepatocytes.TestTarget.txt'

prediction = pd.read_csv('Cibersortx.Prediction.csv',index_col=0)
prediction = prediction[selected_cell]

predefine = pd.read_csv(predefine_file,delimiter='\t')
predefine = predefine[selected_cell]

error = np.subtract(np.array(prediction),np.array(predefine))
mean_error = np.mean(error)
mean_absolute_error = np.mean(np.absolute(error))

file = open('%s_MAE.txt'%selected_cell,'w')
print('Mean Error = %s'%round(mean_error,4), file=file)
print('Mean Absolute Error = %s'%round(mean_absolute_error,4), file=file)
file.close()


