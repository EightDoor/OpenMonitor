import logging
import os

logger = logging.getLogger(__name__)
logger.setLevel(logger=logging.DEBUG)


def init():
    path = os.path.abspath("../")
    print(path)
    logging.basicConfig("")
