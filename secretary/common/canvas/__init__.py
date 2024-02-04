import os

_base_url: str = os.environ.get("CANVAS_API_URL")

_api_key: str = os.environ.get("CANVAS_API_KEY")

_headers = {
    "Authorization" : f"Bearer {_api_key}"
}

from secretary.common.canvas.courses import *
from secretary.common.canvas.assignments import *