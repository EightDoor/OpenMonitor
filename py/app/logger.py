import logging
import os

logger = logging.getLogger(__name__)
def init():
    path = os.path.abspath('../')
    print(path)
    logging.basicConfig('')