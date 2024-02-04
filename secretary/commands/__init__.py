from secretary import app
import secretary.common.canvas as canvas
import secretary.common.todoist as todoist

@app.command("export-canvas-assignments-to-todoist")
def export_canvas_assignments_to_todoist() -> None:
    """Exports Canvas assignments to Todoist."""
    
    selected_courses: list[dict] = canvas.prompt_for_selected_courses()

    for course in selected_courses:
        selected_assignments = canvas.prompt_for_selected_assignments(course)

        for assignment in selected_assignments:
            _export_canvas_assignment_to_todoist(course, assignment)

def _export_canvas_assignment_to_todoist(course: dict, assignment: dict):
    todoist.add_task(
        content=f'{assignment["name"]} - {course["name"]}',
        description=f'{assignment["html_url"]}',
        due_datetime=assignment["due_at"],
        project_id=2328058402
    )