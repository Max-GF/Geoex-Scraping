"""
    Load environment variables from .env file.
"""
import os
from dotenv import load_dotenv

def load_env_configs() -> dict[str, str]:
    """
    Load environment variables from .env file.

    Returns:
        Dict: A dictionary containing the credentials
        loaded from the environment variables.
    """
    load_dotenv()
    return {
        "cookies": os.getenv("COOKIES"),
        "gxsessao": os.getenv("GXSESSION"),
        "gxbot": os.getenv("GXBOT"),
        "APP_NAME" : os.getenv("APP_NAME"),
    }
