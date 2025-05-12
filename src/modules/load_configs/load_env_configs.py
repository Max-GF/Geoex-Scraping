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
    load_dotenv( override=True )
    return {
        "APP_NAME" : os.getenv("APP_NAME"),
    }
