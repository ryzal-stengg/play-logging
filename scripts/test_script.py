import os
import sys
from pathlib import Path
import logging
import logging.config
import random
import time

sys.path.append(str(Path(__file__).resolve().parent.parent))

import main_package as mp

logger = logging.getLogger(__name__)

def main():

    logger.info("Setting up logging configuration for scraping.")
    mp.utils.setup_logging(
        logging_config_path=os.path.join(
            os.getcwd(), "conf/logging.yaml"
        )
    )

    test_list = ["this", "is", "a", "list"]

    try:
        print(test_list[5])
    except Exception as e:
        logger.error(e)

    mp.another_mod.simple_arith(random.randint(0, 9))

    while True:
        slept_value = random.randint(3, 10)
        time.sleep(slept_value)
        logger.info(f"Slept for {slept_value}")

if __name__ == "__main__":
    main()
