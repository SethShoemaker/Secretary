from secretary.common.canvas import _base_url, _headers
import inquirer
import json
import requests

def get_all_courses() -> any:
    """List all courses"""

    raw_response = requests.get(url=_base_url + "/courses?per_page=50", headers=_headers).content
    json_response = json.loads(raw_response)

    return json_response

def _get_all_courses_dict() -> dict:
    """Returns a dictionary with a unique string as the key and the course as the values"""

    all_courses_dict = {}
    for course in get_all_courses():
        all_courses_dict[course["name"] + " (" + str(course["id"]) + ")"] = course

    return all_courses_dict

def prompt_for_selected_courses() -> list[dict]:
    """Prompts the user to select from their courses, returns the courses they have selected."""

    all_courses_dict: dict = _get_all_courses_dict()

    if len(all_courses_dict) == 0:
        return []

    choices = [key for key in all_courses_dict]

    answers = inquirer.checkbox("Select Courses to export from", choices=choices)

    selected_courses = [all_courses_dict[answer] for answer in answers]

    return selected_courses