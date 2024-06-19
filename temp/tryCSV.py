import pandas as pd
mycsv = pd.read_csv('./student_data.csv')
for row in mycsv.values:
    for value in row:
        print(value,end=" ")
    print("")