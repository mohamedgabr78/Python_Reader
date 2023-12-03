#import pandas library
import pandas as pd
pd.set_option('display.max_columns', None)

#variable that stores the name
myName = "Mohamed Gabr"
print("Name: %s" % myName)


dataset = "travel.csv"
travel_dataframe = None

#handle exceptions if the file does not exist or is not available
try:
    #read csv dataframe (record object)
    travel_dataframe = pd.read_csv(dataset)
except:
    #print a error message
    print("Error: %s" % dataset)
    exit(1)
    
    
    # Drop rows with NaN values
travel_dataframe.dropna(inplace=True)


    #show the complete table in csv file
print(travel_dataframe)
print()

for index in travel_dataframe.index:
    print(travel_dataframe['ref_number'][index], ",",
          travel_dataframe['disclosure_group'][index], ",",
          travel_dataframe['title_en'][index], ",",
          travel_dataframe['name'][index], ",",
          travel_dataframe['purpose_en'][index], ",",
          travel_dataframe['start_date'][index], ",",
          travel_dataframe['end_date'][index], ",",
          travel_dataframe['airfare'][index], ",",
          travel_dataframe['other_transport'][index], ",",
          travel_dataframe['lodging'][index], ",",
          travel_dataframe['meals'][index], ",",
          travel_dataframe['other_expenses'][index], ",",
          travel_dataframe['total'][index], ",",
          travel_dataframe['owner_org'][index], ",",
          travel_dataframe['owner_org_title'][index])
    #loop structure
    if index == 20:
        break

print("\nName: %s" % myName)