import configparser
import logging
import os


def setup_logger():
    """Sets up the logger based on configuration."""
    config = configparser.ConfigParser()
    config_path = os.path.join(os.path.dirname(__file__), "..", "configs", "config.ini")
    config.read(config_path)

    logger_name = config["logger"]["name"]
    logfile = config["logger"]["logfile"]
    logfile_path = config["logger"]["logfile_path"]
    log_level = config["logger"]["log_level"].upper()
    enable_console = config["logger"].getboolean("enable_console")

    log_full_path = os.path.join(logfile_path, logfile)

    # Ensure the log directory exists
    os.makedirs(logfile_path, exist_ok=True)

    logger = logging.getLogger(logger_name)
    logger.setLevel(getattr(logging, log_level))

    # Create file handler
    file_handler = logging.FileHandler(log_full_path)
    file_handler.setLevel(getattr(logging, log_level))

    # Create formatter and add it to the handlers
    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    # Add console handler only if enabled
    if enable_console:
        console_handler = logging.StreamHandler()
        console_handler.setLevel(getattr(logging, log_level))
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)

    return logger


# Set up the logger when the module is imported
logger = setup_logger()
