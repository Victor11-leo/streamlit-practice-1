import pandas as pd
import numpy as np

# Reading data
data = pd.read_excel('data.xlsx',engine='openpyxl',sheet_name='New Data')

#Units sold each month
def unitsSoldMonth ():
    required_values = ['Units Sold','Date']
    df = data[required_values]

    return df


