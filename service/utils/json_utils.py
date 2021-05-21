import json
from bson import json_util


def convert_to_json(json_obj):
    if json_obj is None:
        return None
    else:
        return json.loads(json_util.dumps(json_obj))