import requests
import pandas as pd
url ="https://data.gov.sg/api/action/datastore_search?resource_id=f9dbfc75-a2dc-42af-9f50-425e4107ae84&q=2019"
result = requests.get(url).json()
# Try out the following codes
# Try to understand the result and figure out how is the data stored in json.
print(result.keys())  #Level 1
print(result['result'].keys())
print(result['result']['records'])
### Todo
# Print out the part where data is stored.

### Replace the highlighted part with json data containing the data records.
df = pd.DataFrame(result['result']['records'])
print(df)
print(df[df.level_1 == 'Total Residents']) # 19429
### Todo
# Now try to connect the data from the previous page to pandas.
# Then from pandas find out how many total residents were there in  Singapore whose age is 90 Years & Over in year 2019