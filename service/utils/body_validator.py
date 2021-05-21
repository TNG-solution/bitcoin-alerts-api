
def validate_body_required_keys(vals, body):
    if not all (k in body for k in vals): raise Exception("Key(s) were not found in body")