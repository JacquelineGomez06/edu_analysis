import csv

list_data = []
with open("states_all.csv", "r") as infile:
    # load in data as DictReader
    reader = csv.DictReader(infile)
    # go through each year and get highest and lowest gdp
    for row in reader:
        list_data.append(row)

'''
#FILTERING DATA USING LIST COMPREHENSION
print(len(list_data))
#data for NY and AVG_READING_4_SCORE
state_analysis=[row for row in list_data if row["STATE"]=="NEW_YORK"]
score_data=[row["AVG_READING_4_SCORE"] for row in state_analysis]
print(len(score_data))
'''

#expanding on code above to create function to pass different states and score data
def filter(state,column):
  """filter data for 1 state and 1 score data

    Parameters
    ----------
    state: str
      U.S state
    column: int
      score data in different school subjects
    
    Returns
    -------
    int
      score data for ONLY 1 specified state
"""
  state_analysis=[row for row in list_data if row["STATE"]==state]
  score_data=[row[column] for row in state_analysis]
  return score_data

result=filter("NEW_YORK","AVG_READING_4_SCORE")

#get years for 1 state and 1 score data
yrs=[row for row in list_data if row["STATE"]=="NEW_YORK" and row["AVG_READING_4_SCORE"]]


def percent_change(list_data, year1, year2,column):
  """calculate percent change between 2 years in a specified score column

    Parameters
    ----------
    year1: int
        first year to calculate change
    year2: int
        second year to calculate change
    column: str
        score to include in analysis

    Returns
    -------
    float
        percent change 
    """
  old_val=0
  new_val=0
  for row in list_data:
    if row["YEAR"]==year1:
      old_val=float(row[column])
    if row["YEAR"]==year2:
      new_val=float(row[column])
  perchange=((old_val-new_val)/old_val)*100
  return perchange

print(percent_change(list_data, "2009", "2013","AVG_READING_4_SCORE"))


