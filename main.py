import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data.csv")
x = df["Calories"].mean()
df.fillna({"Calories": x}, inplace=True)

print(
    f"After replace missing values in the Calories column with the mean value: \n {df.to_string()}\n"
)


print(
    f"For ennsure all values in Duration, Pulse, and Maxpulse are integers, and Calories is a float: \n {df.dtypes}\n"
)

for x in df.index:
    if df.loc[x, "Duration"] > 120:
        df.drop(x, inplace=True)

print(
    f"After remove any rows where Duration is greater than 120 minutes: \n {df.to_string()}\n"
)

print(f"Check duplicate rows if any exist: \n {df.duplicated().to_string()}\n")

print(f"Find correlations between the columns: \n {df.corr()}")

df.plot(kind="scatter", x="Duration", y="Calories")
plt.show()

plt.hist("Pulse")
plt.show()
