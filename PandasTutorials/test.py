import pandas as pd
import matplotlib.pyplot as plt

# CSV to Python
df = pd.read_csv("data/titanic.csv")
#print(df.tail(5))

# Python to Excel
df.to_excel("data/titanic.xlsx", sheet_name="passengers", index=False)

# Excel to Python
titanic = pd.read_excel("data/titanic.xlsx", sheet_name="passengers")
#print(titanic.tail(5))

# Print only the age column
ages = titanic["Age"]
#print(ages)

# Print the age and sex columns
age_sex = titanic[["Age", "Sex"]]
# print(age_sex)

# Select rows where age > 35
above_35 = titanic[titanic["Age"] > 35]
above_35s = above_35["Age"]
# print(above_35s)

# Select rows where the person is in either cabin 2 or 3 (pclass)
class_23 = titanic[titanic["Pclass"].isin([2, 3])]
# This is functionally the same: class_23 = titanic[(titanic["Pclass"] == 2) | (titanic["Pclass"] == 3)]
# print(class_23)

# Select rows where there is data in the "Age" column
age_no_na = titanic[titanic["Age"].notna()]
# print(age_no_na)

# Display names of passengers older than 35 years old
adult_names = titanic.loc[titanic["Age"] > 35, "Name"]
# print(adult_names)

# Display rows 1 to 5 and columns 3 to 5 (the id is zero indexed, left bound's id is printed, but right bound's id is
# not included. The count
sliced = titanic.iloc[0:5, 2:5]
# print(sliced) # Count of 5 rows, ids 0-4 are printed. Count of 4 columns, id, column #3, 4, 5.
                # So the columns are also zero-index, the "0" is the dataframe unique id

# Assign the name "anonymous" to the first 3 elements of the third column
titanic.iloc[0:3, 3] = "anonymous"
# print(titanic["Name"]) # Works for pandas id 0-2

# loc works with label names, iloc treats the columns as as a list and only accepts integers

# Making graphs
air_quality = pd.read_csv("data/air_quality_no2.csv", index_col=0, parse_dates=True)
# print(air_quality.head())
# print(air_quality.plot())
# plt.show()

# Create a new column called "london_mg_per_cubic", which is the value of station_london * 1.882
air_quality["london_mg_per_cubic"] = air_quality["station_london"] * 1.882
# print(air_quality.head())

# Create a new column called "ratio_paris_antwerp", which is the ratio between station_paris and station_antwerp.
air_quality["ratio_paris_antwerp"] = (
    air_quality["station_paris"] / air_quality["station_antwerp"]
    # Can use apply() for more advanced logic, but basic math and logic operators work
)
# print(air_quality.head())

# Rename the columns from station_X to other stuff, using Python dictionary
# You can do extra stuff like columns=str.lower() too
air_quality_renamed = air_quality.rename(
    columns={
        "station_antwerp": "BETR801",
        "station_paris": "FR04014",
        "station_london": "London Westminster",
    }
)
# print(air_quality_renamed)

titanic = pd.read_excel("data/titanic.xlsx", sheet_name="passengers")

# Calculate mean of age of passengers
pass_mean = titanic["Age"].mean()
# print(pass_mean)

# Group statistics by category. Find average age for male versus female passengers.
pass_gender_age_avg = titanic[["Sex", "Age"]].groupby("Sex").mean()
# print(pass_gender_age_avg) # First row is "female", second row is "male". And there's a second column that displays
                            # each group's mean

titanic = pd.read_csv("data/titanic.csv")
air_quality = pd.read_csv(
    "data/air_quality_long.csv", index_col="date.utc", parse_dates=True
)

# Sort the Titanic data according to age of passengers
sorted_age = titanic.sort_values(by="Age").head()
# print(sorted_age["Age"]) # This returns a lost sorted from lowest age to highest age (ascending order)

# Do the same in descending order, sorting first by Pclass, and then second　by Age
sorted_age2 = titanic.sort_values(by=['Pclass', 'Age'], ascending=False)
# print(sorted_age2[["Pclass", "Age"]]) # This returns a list sorted from highest age to lowest age (descending order)

air_quality_no2 = pd.read_csv("data/air_quality_no2_long.csv",
                              parse_dates=True)
air_quality_no2 = air_quality_no2[["date.utc", "location",
                                   "parameter", "value"]]

air_quality_pm25 = pd.read_csv("data/air_quality_pm25_long.csv",
                               parse_dates=True)
air_quality_pm25 = air_quality_pm25[["date.utc", "location",
                                     "parameter", "value"]]

# Combine the two similarly shaped tables no2_long and pm25_long
air_quality_combined = pd.concat([air_quality_pm25, air_quality_no2], axis=0)
# print(air_quality_combined)




