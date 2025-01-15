import dotenv
import os

def get_env(name: str):
    path = os.path.abspath("../")
    return dotenv.get_key(dotenv_path=path, key_to_get=name)