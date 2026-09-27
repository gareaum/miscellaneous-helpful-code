import logging
from pathlib import Path


def setup_logger(name: str) -> logging.Logger:
    """
    Description: Create and configures a logging tool for the system.
    
    inputs:
              name - The file where the log information came from 

    returns:
            logger - connects the tool to the file so information from the file can be writen to it
    """

    log_dir = Path("logs")
    log_dir.mkdir(exist_ok=True)

    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    if not logger.handlers:

        formatter = logging.Formatter(
            "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
        )

        # Console output
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)

        # Log file output
        file_handler = logging.FileHandler(log_dir / "system.log")
        file_handler.setFormatter(formatter)

        logger.addHandler(console_handler)
        logger.addHandler(file_handler)

    return logger