# with open("weather_data.csv") as weather_file:
#     data = weather_file.readlines()
#     print(data)

# import csv
#
# with open("weather_data.csv") as weather_file:
#     data = csv.reader(weather_file)
#     temperatures = []
#     for row in data:
#         temperatures.append(row[1])
#     for temp in temperatures[1:]:
#         print(temp, end=" ")

# import pandas
#
# data = pandas.read_csv("weather_data.csv")
# print(type(data))
# print(data)

#data_dict = data.to_dict()
# print(data_dict)
#
# print(data["temp"].mean())
# print(data["temp"].max())
#
# # get data in columns
# print(data["condition"])
# print(data.condition)

# get data in row
# print(data[data["temp"] == data["temp"].max()])

# monday = data[data.day == "Monday"]
# monday_temp_fahrenheit = (monday.temp * 9/5) + 32
# print(monday_temp_fahrenheit[0])

# create data frame from scratch
# data_dict = {
#     "students": ["Martin", "Simon", "Andrej"],
#     "scores": ["88", "77", "80"]
# }
#
# data_2 = pandas.DataFrame(data_dict)
# data_2.to_csv("score_data.csv")

import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
count_colors = data["Primary Fur Color"].value_counts()

colors_file = pandas.DataFrame(count_colors)
colors_file.to_csv("squirrel_color_count.csv")


