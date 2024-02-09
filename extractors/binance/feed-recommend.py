import argparse
import json
from datetime import datetime


import requests

from extractors.binance.default_config import (
    DATA_LANDING_FOLDER,
    DEFAULT_HEADER,
    DEFAULT_URL,
)


def generate_date_string():
    return datetime.now().strftime("%Y_%m_%d_%H_%M_%S")


def generate_file_name(prefix_name: str, suffix_name: str = ".json"):
    prefix_name = prefix_name.strip()
    prefix_name = prefix_name.removeprefix("")
    prefix_name = prefix_name.removesuffix("")
    prefix_name = prefix_name.replace(" ", "_")
    prefix_name = prefix_name.replace("-", "_")
    return f"{prefix_name}_{generate_date_string()}{suffix_name}"


if __name__ == "__main__":
    arg_parse = argparse.ArgumentParser()
    arg_parse.add_argument("--landing-path", type=str, default=DATA_LANDING_FOLDER)
    args = arg_parse.parse_args()

    data = {"pageIndex": 1, "pageSize": 20, "scene": "web-homepage"}

    response = requests.post(DEFAULT_URL, headers=DEFAULT_HEADER, json=data)
    with open(f'{args.landing_path}/{generate_file_name("feed-recommend")}', "w") as f:
        response_dict = response.json()
        response_dict["extraction"] = data
        json.dump(response_dict, f)
