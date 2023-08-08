import uuid
from datetime import datetime


def generate_transation_id():
    unique_id = uuid.uuid4().hex
    timestamp = datetime.now().strftime('%Y%m%d%H%M%S')

    return f'{timestamp}{unique_id}'
