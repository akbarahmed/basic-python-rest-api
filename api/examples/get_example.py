from api import app
from schematics.models import Model


@app.route('/examples/<int: example_id>')
def get_example(example_id):
    """Get one example's details"""
    # Get inputs

    # Validate inputs
    # If validation exception:
    #     Log exception
    #     Return error

    # Perform logic, file or DB operations

    # If error in logic/file/DB operations:
    #     Log exception
    #     Return error

    # Return response
    return "GET one example"
