years = [1996,1997,2000,2005,2002]
ages = []
current = 2018
def getAges(yearList):
  for year in yearList:
    ages.append(current-year)
  print(ages)
getAges(years)


