from sqlalchemy import create_engine
from cubes.tutorial.sql import create_table_from_csv

#Load csv file using cubes
engine = create_engine('sqlite:///data.sqlite')
create_table_from_csv(engine,
                      "country-income.csv",
                      table_name="country_income",
                      fields=[
                          ("region", "string"),
                          ("age", "integer"),
                          ("income", "integer"),
                          ("online_shopper", "string")],
                      create_id=True
                     )
                     
#JSON file for the data created manually which serves as the model metadata dictionary
#Create data cube for the data
from cubes import Workspace
workspace = Workspace()
workspace.register_default_store("sql", url="sqlite:///data.sqlite")
workspace.import_model("country_income.json")
cube = workspace.cube("country_income")

#aggregate results for the whole data cube
browser = workspace.browser(cube)
result = browser.aggregate()
result.summary

#results per region
result = browser.aggregate(drilldown=["region"])
for record in result:
    print(record)
    
#results per online shopping activity
result = browser.aggregate(drilldown=["online_shopper"])
for record in result:
    print(record)

#results for all people aged between 40 and 50
import cubes as cubes
cuts = [cubes.RangeCut("age", ["40"],["50"])]
cell = cubes.Cell(cube, cuts)
result = browser.aggregate(cell, drilldown=["age"])
for record in result:
    print(record)
