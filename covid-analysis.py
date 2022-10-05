import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer

df = pd.read_csv('C:\covid\covid_19_data.csv')
df.drop(['SNo', 'Last Update'], axis = 1, inplace = True)
df.rename(columns = {'ObservationDate': 'Date', 'Province/State': 'State', 'Country/Region': 'Country'}, inplace = True)
df['Date'] = pd.to_datetime(df['Date'])
imputer = SimpleImputer(strategy = 'constant')
df2 = pd.DataFrame(imputer.fit_transform(df), columns = df.columns)

df3 = df2.groupby(['Country', 'Date'])[['Confirmed', 'Deaths', 'Recovered']].sum().reset_index()

df3.head()

countries = df3['Country'].unique()

for idx in range(0, len(countries)):
    c = df3[df3['Country'] == countries[idx]].reset_index()
    plt.scatter(np.arange(0, len(c)), c['Confirmed'], color = 'blue', label = 'Confirmed')
    plt.scatter(np.arange(0, len(c)), c['Recovered'], color = 'green', label = 'Recovered')
    plt.scatter(np.arange(0, len(c)), c['Deaths'], color = 'red', label = 'Deaths')
    plt.title(countries[idx])
    plt.xlabel('Days since first suspect')
    plt.ylabel('Number of cases')
    plt.legend()
    plt.show()


df4 = df3.groupby(['Date'])[['Confirmed', 'Deaths', 'Recovered']].sum().reset_index()

#for the whole world

d = df4
plt.scatter(np.arange(0, len(d)), d['Confirmed'], color = 'blue', label = 'Confirmed')
plt.scatter(np.arange(0, len(d)), d['Recovered'], color = 'green', label = 'Recovered')
plt.scatter(np.arange(0, len(d)), d['Deaths'], color = 'red', label = 'Deaths')
plt.title('world')
plt.xlabel('Days since first suspect')
plt.ylabel('Number of cases')
plt.legend()
plt.show()
