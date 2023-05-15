# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()
# print(data)

# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

import pandas

# data = pandas.read_csv("weather_data.csv")
# data_series = data["temp"]
#
# data_dict = data.to_dict()
# print(data_dict)
# temp_list = data["temp"].to_list()
# print(temp_list)
# max_temp = data_series.max()
#
# print(data[data.temp == data["temp"].max()])
#
# monday = data[data.day == "Monday"]
# monday_temp = int(monday.temp[0])
# monday_temp_f = monday_temp * 1.8 + 32
# print(monday_temp_f)
# print(monday.temp * 1.8 + 32)

data = pandas.read_csv("Central_Park_Squirrel.csv")
total = len(data["Primary Fur Color"])
gray = len(data[data["Primary Fur Color"] == "Gray"])
black = len(data[data["Primary Fur Color"] == "Black"])
cinnamon = len(data[data["Primary Fur Color"] == "Cinnamon"])
print(total)
print(gray)
print(black)
print(cinnamon)
data_dict = {
    "Fur Color": ["grey", "black", "red"],
    "Count": [gray, black, cinnamon]
}
new_data = pandas.DataFrame(data_dict)
new_data.to_csv("squirrel_count.csv")
