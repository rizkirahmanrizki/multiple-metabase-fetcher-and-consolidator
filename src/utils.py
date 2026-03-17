def clean_datetime(value):
    if isinstance(value, str) and "T" in value:
        return value.replace("T", " ")
    return value

def format_rows(rows):
    return [[clean_datetime(v) for v in row] for row in rows]
