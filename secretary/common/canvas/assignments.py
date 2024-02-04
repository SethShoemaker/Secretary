from secretary.common.canvas import _base_url, _headers
from secretary.common.canvas.courses import get_all_courses
import json
import inquirer
import requests

def list_assignments_from_all_courses() -> any:
    """List all assignments"""

    assignments = []

    for course in get_all_courses():
        assignments.extend(get_assignments_by_course(course["id"]))

    return assignments

def get_assignments_by_course(course_id) -> list[dict]:
    raw_response = requests.get(url=_base_url + f"/courses/{course_id}/assignments", headers=_headers).content
    json_response = json.loads(raw_response)

    return json_response

def prompt_for_selected_assignments(course: dict) -> list[dict]:
    """Prompts the user to select Assignments from a Course, returns the Assignments they have selected"""

    course_assignments_dict: dict = _get_course_assignments_dict(course)

    if len(course_assignments_dict) == 0:
        return []

    choices = [key for key in course_assignments_dict]

    answers = inquirer.checkbox(message=f"Select Assignments from \"{course['name']}\"",choices=choices)

    selected_assignments = [course_assignments_dict[answer] for answer in answers]

    return selected_assignments

def _get_course_assignments_dict(course: dict) -> dict:
    """Returns a dictionary with a unique string as the key and the assignment as the value"""

    course_assignments_dict = {}
    for assignment in get_assignments_by_course(course["id"]):
        course_assignments_dict[assignment["name"] + " (" + str(assignment["id"]) + ")"] = assignment

    return course_assignments_dict