import pandas as pd
import pandas_profiling as pf
df = pd.read_csv("C:/Users/Pavel/Downloads/db.csv", sep=';')
report = pf.ProfileReport(df)
report.to_file(output_file='C:/Users/Pavel/Downloads/report.html')
print('******* Process finished *******')
