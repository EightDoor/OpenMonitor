import logging
import os

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)


def init():
    path = os.path.abspath("../")
    print(path)
    logging.basicConfig("")
