import uuid

def generate_uuid() -> str:
    """ Generating a unique indentifier to the AcadFlow entities.
    """
    return str(uuid.uuid4())