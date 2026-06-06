# with open("Weather Analysis/weather_data.csv") as file:
#     data = file.readlines()
#     print(data)


# import csv
# with open("Weather Analysis/weather_data.csv") as file:
#     data = csv.reader(file)
#     temperature = []
#     for row in data:
#       print(row)
#       if row[1] != "temp":
#         temperature.append(int(row[1]))
#     print(temperature)


import pandas
data = pandas.read_csv("Weather Analysis/weather_data.csv")
# print(data)
data_dict = data.to_dict()
# print(data_dict)
# temp_list = data["temp"].to_list()
# print(temp_list)

# average_temp = data["temp"].mean()
# print(average_temp)

# max_temp = data["temp"].max()
# print(max_temp)

# print(data.condition)

# max = data[data.temp == data.temp.max()]
# print(max)

data_dict = {
      "students": ["Amy", "James", "Angela"],
      "scores": [76, 56, 65]
}
data = pandas.DataFrame(data_dict)
print(data)
data.to_csv("Weather Analysis/new_data.csv", index=False)
