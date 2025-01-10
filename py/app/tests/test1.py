import logging
import os

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

logging.basicConfig(level=logging.DEBUG)

if __name__ == "__main__":
    current_path = os.path.basename()
    logger.debug(f"当前路径：{current_path}")
