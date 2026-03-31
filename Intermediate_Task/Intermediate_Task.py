import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv(r"E:\Coding\Python\delhiaqi.csv")

print("First 5 Rows:\n")
print(df.head())

print("\nDataset Info:\n")
print(df.info())



df['date'] = pd.to_datetime(df['date'])



df = df.dropna()

print("\nMissing Values:\n")
print(df.isnull().sum())



df['AQI'] = df['pm2_5']

print("\nAQI Column Created\n")


print("\nStatistical Summary\n")

print("Mean AQI =", df['AQI'].mean())

print("Maximum AQI =", df['AQI'].max())

print("Minimum AQI =", df['AQI'].min())

print("Median AQI =", df['AQI'].median())



plt.figure()

plt.plot(df['date'], df['AQI'])

plt.title("AQI Over Time")

plt.xticks(rotation=45)

plt.show()


pollutants = ['pm2_5','pm10','no2','so2','co','nh3','o3']

df[pollutants].plot()

plt.title("Pollutant Comparison")

plt.show()



df['Month'] = df['date'].dt.month

monthly_aqi = df.groupby('Month')['AQI'].mean()

plt.figure()

monthly_aqi.plot(kind='bar')

plt.title("Monthly AQI Variation")

plt.xlabel("Month")

plt.ylabel("Average AQI")

plt.show()


plt.figure()

sns.heatmap(df[['AQI','pm2_5','pm10','no2','so2','co','nh3','o3']].corr(),
            annot=True)

plt.title("Correlation Between Pollutants")

plt.show()



highest = df.sort_values(by='AQI', ascending=False)

print("\nTop 10 Highest AQI Records:\n")

print(highest.head(10))



def season(month):

    if month in [12,1,2]:
        return "Winter"

    elif month in [3,4,5]:
        return "Summer"

    elif month in [6,7,8]:
        return "Monsoon"

    else:
        return "Post-Monsoon"


df['Season'] = df['Month'].apply(season)

seasonal = df.groupby('Season')['AQI'].mean()

plt.figure()

seasonal.plot(kind='bar')

plt.title("Seasonal AQI Variation")

plt.ylabel("Average AQI")

plt.show()



print("\n------ ANALYSIS RESULTS ------\n")

print("Average AQI:", df['AQI'].mean())

print("Worst AQI:", df['AQI'].max())

print("Best AQI:", df['AQI'].min())

print("\nWorst Season Pollution:")

print(seasonal.sort_values(ascending=False))
