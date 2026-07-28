def sort_files(files, split_on='_', elem_month=-2, elem_year=-1):...
"""docstring"""
import pandas as pd
months = [int(fn.split('.')[0].split(split_on)[elem_month]) for fn in files]
years = [int(fn.split('.')[0].split(split_on)[elem_year]) for fn in files]
df = pd.DataFrame({'fn': files, 'month': months, 'year': years})
df_sorted = df.sort_values(['year', 'month'])
return df_sorted.fn.tolist()
