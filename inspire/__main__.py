import os
import sys
from inspire.utils import NinjaAPI


def main():
    # handle terminal arguments
    category_args = sys.argv[1:]
    assert len(category_args) <= 1, f"Categories exceed max value of 1: `{category_args}`"
    category = category_args[0] if category_args else None

    # make request
    napi = NinjaAPI(api_key=os.environ.get("API_NINJAS_KEY"))
    napi.get_quote(category)
    return None
