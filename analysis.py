import csv

list_data = []
with open("states_all.csv", "r") as infile:
    # load in data as DictReader
    reader = csv.DictReader(infile)
    # go through each year and get highest and lowest gdp
    for row in reader:
        list_data.append(row)

print(len(list_data))
#list comprehension
state_analysis=[row for row in list_data if row["STATE"]=="NEW_YORK"]
score_data=[row["AVG_READING_4_SCORE"] for row in state_analysis]
print(len(score_data))

#list comprhension

#create function to return only one state and one column to analyze
def filter(state,column):
  state_analysis=[row for row in list_data if row["STATE"]==state]
  score_data=[row[column] for row in state_analysis]
  return score_data
result=filter("NEW_YORK","AVG_READING_4_SCORE")
print(len(result))
