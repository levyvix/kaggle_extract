import polars as pl
from decorators.utils import log_function, time_function


@log_function
@time_function
def unite_pl(data_path: str = "../data"):
    pl.scan_csv(f"{data_path}/brazil_population_2019.csv").sink_parquet(
        f"{data_path}/brazil_population_2019.parquet",
        compression="snappy",
    )


if __name__ == "__main__":
    unite_pl()
