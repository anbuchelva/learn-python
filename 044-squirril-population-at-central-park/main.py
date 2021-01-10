import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
# Option 1
# color_wise_count = data.groupby(["Primary Fur Color"]).size()
# export_csv = pandas.DataFrame(color_wise_count)
# export_csv.to_csv("Squirrel-count.csv")

# Option 2
gray_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
cinnamon_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])

squirrels_count_summary = {
    "squirrel_color": ["Gray", "Cinnamon", "Black"],
    "squirrel_count": [gray_squirrels_count, cinnamon_squirrels_count, black_squirrels_count],
}

x = pandas.DataFrame(squirrels_count_summary)
x.to_csv("Squirrel-count.csv")

# Option 3