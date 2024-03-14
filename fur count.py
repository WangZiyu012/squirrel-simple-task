import csv
import pandas as pd

# Read the csv file

squirrel_data = pd.read_csv("./US-map/squirrel_data.csv")
print(squirrel_data)

color_counts = squirrel_data['Primary Fur Color'].value_counts().to_frame()
color_counts = color_counts.reset_index()
color_counts.columns = ['Primary Fur Color', 'Count']
print(color_counts)