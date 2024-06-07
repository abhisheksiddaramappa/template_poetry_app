import configparser
import os
import csv
from .bubble_sort import bubble_sort
from .merge_sort import merge_sort
from .logger_setup import logger


def get_input_list_from_csv(file_path):
    """Reads the CSV file and returns the data as a list of integers.

    Args:
        file_path (str): The path to the CSV file.

    Returns:
        list: A list of integers read from the CSV file.
    """
    with open(file_path, newline="") as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            return list(map(int, row))  # Assuming the CSV contains a single row of integers


def get_config():
    """Reads the configuration file and returns the sorting algorithm.

    Returns:
        str: The sorting algorithm specified in the configuration file.
    """
    config = configparser.ConfigParser()
    # Construct the path to the config file
    config_path = os.path.join(os.path.dirname(__file__), "..", "configs", "config.ini")
    logger.debug(f"Reading config from: {config_path}")
    # Read the configuration file
    config.read(config_path)
    # Return the sorting algorithm specified in the config file
    return config["settings"]["sorting_algorithm"]


def get_data():
    """Reads the data from the CSV file and returns it as a list of integers.

    Returns:
        list: A list of integers read from the CSV file.
    """
    # Construct the path to the data file
    data_file_path = os.path.join(os.path.dirname(__file__), "..", "data", "data.csv")
    logger.debug(f"Reading data from: {data_file_path}")
    # Read the data from the CSV file
    return get_input_list_from_csv(data_file_path)


def get_assets():
    """Reads the assets.txt file and returns its contents as a list of strings.

    Returns:
        list: A list of asset strings read from the assets.txt file.
    """
    # Construct the path to the assets file
    assets_file_path = os.path.join(os.path.dirname(__file__), "..", "assets", "assets.txt")
    logger.debug(f"Reading assets from: {assets_file_path}")
    # Read the assets from the file
    with open(assets_file_path, "r") as file:
        assets = file.readlines()
    # Strip any leading/trailing whitespace and return as a list
    return [asset.strip() for asset in assets]


def sort_array(arr, sorting_algorithm):
    """Sorts the array using the specified sorting algorithm.

    Args:
        arr (list): The list of integers to sort.
        sorting_algorithm (str): The sorting algorithm to use.
    """
    # Sort the array using the specified sorting algorithm
    if sorting_algorithm == "bubble_sort":
        bubble_sort(arr)
        logger.info("Sorted array using Bubble Sort: %s", arr)
    elif sorting_algorithm == "merge_sort":
        merge_sort(arr)
        logger.info("Sorted array using Merge Sort: %s", arr)
    else:
        logger.error("Invalid sorting algorithm specified in config.ini.")


def main():
    """Main function to orchestrate reading configuration, data, assets, and sorting."""
    # Get the sorting algorithm from the config file
    sorting_algorithm = get_config()

    logger.info("Loaded configuration:")
    logger.info("Sorting Algorithm: %s", sorting_algorithm)

    # Get the data to sort
    arr = get_data()
    # Sort the data
    sort_array(arr, sorting_algorithm)

    # Get the list of assets
    assets = get_assets()
    logger.info("Assets: %s", assets)
