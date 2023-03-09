#  pip install pandas
#  pip install ydata-profiling

import pandas as pd
from ydata_profiling import ProfileReport

df = pd.read_csv('Music artist\Artist.csv')
print(df)

profile = ProfileReport(df)
profile.to_file(output_file="Analysis_Report.html") 