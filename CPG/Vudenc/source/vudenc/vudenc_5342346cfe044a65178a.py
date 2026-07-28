def only_years(files, begin=1901, end=2100, split_on='_', elem_year=-1):...
"""docstring"""
import pandas as pd
years = [int(fn.split('.')[0].split(split_on)[elem_year]) for fn in files]
df = pd.DataFrame({'fn': files, 'year': years})
df_slice = df[(df.year >= begin) & (df.year <= end)]
return df_slice.fn.tolist()
