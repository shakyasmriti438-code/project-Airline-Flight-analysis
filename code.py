import pandas as pd
import numpy as np

TIME_COL = "Departure_Time"

# Task 1: Load and inspect
df = pd.read_csv("14_flight_delays.csv")
df["Delay_Cause"] = df["Delay_Cause"].fillna("None")  
print(df.shape)
print(df.dtypes)
print(df.head())

# Task 2: Missing values and duplicates
print(df.isnull().sum())
print("Duplicates:", df["Flight_ID"].duplicated().sum())
df = df.drop_duplicates(subset="Flight_ID")

# Task 3: Fill missing arrival delay with median (not affected by extreme delays)
df["Arrival_Delay_Mins"] = df["Arrival_Delay_Mins"].fillna(df["Arrival_Delay_Mins"].median())

# Task 4: Date, month, day of week
df["Flight_Date"] = pd.to_datetime(df["Flight_Date"])
df["Month"] = df["Flight_Date"].dt.month_name()
df["DayOfWeek"] = df["Flight_Date"].dt.day_name()

# Task 5: Total flights, average delay, on-time %
total = len(df)
on_time = len(df[df["Departure_Delay_Mins"] <= 15]) / total * 100
print("Total flights:", total)
print("Average departure delay:", df["Departure_Delay_Mins"].mean())
print("On-time %:", on_time)

# Task 6: Airport ranking
print("--- Airport ranking ---")
print(df.groupby("Origin")["Departure_Delay_Mins"].mean().sort_values(ascending=False))

# Task 7: Top 10 worst routes
df["Route"] = df["Origin"] + " to " + df["Destination"]
print("--- Top 10 worst routes ---")
print(df.groupby("Route")["Arrival_Delay_Mins"].mean().sort_values(ascending=False).head(10))

# Task 8: Time of day
print("--- Time of day: average delay, then delay % ---")
print(df.groupby(TIME_COL)["Departure_Delay_Mins"].mean())
late = df[df["Departure_Delay_Mins"] > 15]
print(late.groupby(TIME_COL).size() / df.groupby(TIME_COL).size() * 100)

# Task 9: Delay causes
print("--- Delay causes: count, then % ---")
print(df["Delay_Cause"].value_counts())
print(df["Delay_Cause"].value_counts() / total * 100)

# Task 10: Cancellation and diversion % by airline
print("--- Cancellation %, then diversion % ---")
print((df["Canceled"] == "Yes").groupby(df["Airline"]).mean() * 100)
print((df["Diverted"] == "Yes").groupby(df["Airline"]).mean() * 100)

# Task 11: Correlation
print("Correlation:", df["Departure_Delay_Mins"].corr(df["Arrival_Delay_Mins"]))

# Task 12: NumPy stats (median, standard deviation, 90th percentile)
delays = df["Departure_Delay_Mins"].values
print(np.median(delays), np.std(delays), np.percentile(delays, 90))

# Task 13: Outliers using IQR
q1 = np.percentile(delays, 25)
q3 = np.percentile(delays, 75)
upper = q3 + 1.5 * (q3 - q1)
print("Upper limit:", upper)
print("Outliers:", len(df[df["Departure_Delay_Mins"] > upper]))

# Task 14: Delay severity (<=15 On-Time, <=30 Minor, <=60 Moderate, else Severe)
def severity(d):
    if d <= 15:
        return "On-Time"
    elif d <= 30:
        return "Minor"
    elif d <= 60:
        return "Moderate"
    return "Severe"

df["Delay_Severity"] = df["Departure_Delay_Mins"].apply(severity)
print(df["Delay_Severity"].value_counts())

# Task 15: Recommendations (add your real airport/time/cause names after running)
print("1. Add ground staff at the airport with the highest delay.")
print("2. Add extra gap between flights in the worst time of day.")
print("3. Make a plan for the biggest delay cause.")
print("4. Review the schedule of the 10 worst routes.")
print("5. Inform passengers early when a departure delay happens.")