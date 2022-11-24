# with open("weather_data.csv", "r") as data:
#     print(data.read())
#

# import csv
#
# with open("weather_data.csv", "r") as data_file:
#     data = csv.reader(data_file)
#     temperature = []
#
#     for row in data:
#         if row[1] != "temp":
#             temperature.append(int(row[1]))
#     print(temperature)

import pandas

# data = pandas.read_csv("weather_data.csv")
# print(data)
# list_temperature = data["temp"].tolist()
# sum_temp = 0
# for temp in list_temperature:
#     sum_temp += int(temp)
# print(sum_temp / len(list_temperature))
#
# print(data["temp"].mean())
#
# temperature = int(data.temp[data.day == "Monday"])
# print(temperature)
# print(f"C to K: {temperature/9}")

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
results_gray = data[data["Primary Fur Color"] == "Gray"]
results_Cinnamon = data[data["Primary Fur Color"] == "Cinnamon"]
results_Black = data[data["Primary Fur Color"] == "Black"]
count_gray = len(results_gray)
count_Cinnamon = len(results_Cinnamon)
count_Black = len(results_Black)
print(count_gray + count_Cinnamon + count_Black)

data_dict = {
    "Fur_color": ["Gray", "Cinnamon", "Black"],
    "Count": [count_gray, count_Cinnamon, count_Black]
}

data = pandas.DataFrame(data_dict)
data.to_csv("new_data.csv")
