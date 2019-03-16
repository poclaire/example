import pandas as pd
import os
import numpy as np 




def row_modified(row):
    row['c']=ajjj
    return row

if __name__ == "__main__":
    df=  {'col1': [1,2,3], 'col2': [3,4,5], 'col3': [4,5,6]} 
    df = pd.DataFrame(data = df)
    df['a']=[1,1,1]
    df.apply(lambda x: row_modified(x), axis =1)
    print(df)
    



    