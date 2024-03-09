import duckdb
from decorators.utils import log_function, time_function
import polars as pl


@time_function
def unite_pl(data_path: str = "../data"):
    pl.scan_csv(f"{data_path}/*.csv").sink_parquet(
        f"{data_path}/events.parquet",
        compression="snappy",
    )


if __name__ == "__main__":
    unite_pl()
