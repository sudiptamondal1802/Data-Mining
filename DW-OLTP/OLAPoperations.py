from sqlalchemy import create_engine
from cubes.tutorial.sql import create_table_from_csv

# Data preparation
engine = create_engine('sqlite:///data.sqlite')
create_table_from_csv(engine,
                      "IBRD_Balance_Sheet__FY2010.csv",
                      table_name="ibrd_balance",
                      fields=[
                          ("category", "string"),
                          ("category_label", "string"),
                          ("subcategory", "string"),
                          ("subcategory_label", "string"),
                          ("line_item", "string"),
                          ("year", "integer"),
                          ("amount", "integer")],
                      create_id=True
                     )

#Create Workspace
from cubes import Workspace

#Create the connection
workspace = Workspace()
workspace.register_default_store("sql", url="sqlite:///data.sqlite")
workspace.import_model("tutorial_model.json")
cube = workspace.cube("ibrd_balance")

# Aggregation and measures
browser = workspace.browser(cube)

#Updated the tutorial.json file for adding the aggregate measure for the minimum and maximum amount

#Use the min and max amount to show the results per year
result = browser.aggregate()
result.summary["amount_max"]
result = browser.aggregate(drilldown=["year"])
for record in result:
    print(record)
