import pandas as pd

def re_partition(ds_nodash):
    print("+"* 100)
    print("enter repartion")
    df = pd.read_parquet(f'~/tmp/sparkdata/{ds_nodash}')
    df.to_parquet(f'~/tmp/sparkpartition/{ds_nodash}', partition_cols=['load_dt','multiMovieYn','repNationCd'])
