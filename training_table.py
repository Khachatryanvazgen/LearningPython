from tabulate import tabulate
# import numpy as np
import pandas as pd

'''
data = [['First_Month', 'Before', 'After'],
              ['Weight', '62.600',  '63.800'],
              ['Biceps', '32', '32.5'],
              ['Back', '96', '97']]

'''

table_data = {
            'First_Month': ['Weight', 'Biceps', 'Back'],
            'Before': ['60.600','31', '95'],
            'After': ['61.800', '31.5', '96']

}


# print(tabulate(data, headers="firstrow", tablefmt="fancy_grid", showindex="always" ))
print(tabulate(table_data, headers="keys", tablefmt="fancy_grid", showindex="always" ))