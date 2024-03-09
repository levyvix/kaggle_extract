import os


def extract(dataset_name: str, download_path: str):
    return os.system(
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


if __name__ == "__main__":
    extract(
        "mkechinov/ecommerce-events-history-in-cosmetics-shop",
        "../data/",
    )
