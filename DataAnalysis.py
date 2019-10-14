import warnings
import itertools
import numpy as np
import matplotlib.pyplot as plt
warnings.filterwarnings("ignore")
plt.style.use('fivethirtyeight')
import pandas as pd
import statsmodels.api as sm
import seaborn as sns
import matplotlib
from pandas.plotting import autocorrelation_plot
from statsmodels.tsa.arima_model import ARIMA


matplotlib.rcParams['axes.labelsize'] = 14
matplotlib.rcParams['xtick.labelsize'] = 12
matplotlib.rcParams['ytick.labelsize'] = 12
matplotlib.rcParams['text.color'] = 'k'

df = pd.read_csv("hourly2017.csv", index_col = 0, parse_dates=True)

df_temperature = df[['Temperature']].copy()

model = ARIMA(df_temperature, order=(5,1,0))
model_fit = model.fit(disp=0)
print(model_fit.summary())

df_temperature.plot(figsize=(20,20))

autocorrelation_plot(df_temperature)

#df['Temperature'].plot(linewidth=0.5)


#cols_plot = ['Temperature', 'Apparent Temperature']
#axes = df[cols_plot].plot(marker='.', alpha=0.5, linestyle='None', figsize=(11, 9), subplots=True)
#for ax in axes:
#    ax.set_ylabel('Temperature in Farenheit')

#ay = df.loc['2017-01', 'Temperature'].plot()
#ay.set_ylabel('Temperature');

plt.show()

df.shape
df.head()
df.tail()
#temperature = df.loc[df['Category'] == 'Temperature']
#df.dtypes