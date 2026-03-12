import pandas as pd
from insolacion import H

file = '25.038_-111.660_25.0384_-111.66_psm3-tmy_60_tmy.csv'

df = pd.read_csv(file, header=None, names=["Year", "Month", "Day", "Hour", "Minute", "DNI", "DHI", "GHI", "Dew Point", "Temperature", "Pressure", "Wind Direction", "Wind Speed", "Surface Albedo"], sep=",", skiprows=3)

df["fecha"]=pd.to_datetime(df[['Year', 'Month', 'Day', 'Hour', 'Minute']])

df.fecha = pd.to_datetime(df.fecha, format='%Y %m %d %H %M')
df.set_index('fecha', inplace=True)

dni = df.DNI
dt = 60*60

Hi = H(dni, dt)

Hi.index = Hi.index.map(lambda t: t.replace(year=2026))
nsrdb = Hi.resample('ME').mean() # [MJ/m2/dia]
nsrdb.to_csv('DNI.csv')
