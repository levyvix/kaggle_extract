import os
from pathlib import Path

from decorators.utils import log_function, time_function


@time_function
@log_function
def extract(dataset_name: str, download_path: str):

    # check if the dataset is already downloaded (directory empty)
    if not os.listdir(download_path):

        os.system(
            " ".join(
                [
                    "kaggle",
                    "datasets",
                    "download",
                    "-d",
                    dataset_name,
                    "-p",
                    download_path,
                    "--unzip",
                ]
            )
        )


def clean_data(data_path: str):

    csv_path = Path(f"{data_path}/brazil_population_2019.csv")
    csv_text = csv_path.read_text(encoding="utf-8")

    problematic_text = "Manaus, Entorno e Alto Rio Negro"
    fixed_text = f'"{problematic_text}"'

    csv_text = csv_text.replace(problematic_text, fixed_text)

    csv_path.write_text(csv_text, encoding="utf-8")


if __name__ == "__main__":
    extract(
        "unanimad/corona-virus-brazil",
        "../data/",
    )

    clean_data("../data/")
