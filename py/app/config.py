import dotenv

def get_env(name: str):
    return dotenv.get_key(name)