
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
#%matplotlib inline

data = pd.read_csv('weights_heights.csv', index_col='Index')

# data.plot(y='Height', kind='hist', color='red',  title='Height (inch.) distribution')

ooo = data.head(5)
ooo = sum(data["Weight"])


np.linspace()



pass
