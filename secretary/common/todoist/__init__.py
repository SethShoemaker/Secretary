from todoist_api_python.api import TodoistAPI
import os

_api = TodoistAPI(os.environ.get("TODOIST_API_KEY"))

add_task = _api.add_task