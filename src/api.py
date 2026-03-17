import requests, csv, io
from config import API_BASE_URL

def fetch_data(dataset_id, endpoint, token, parameters=None):
    url = API_BASE_URL + endpoint.replace("{id}", dataset_id)

    payload = "parameters=" + requests.utils.quote(str(parameters or []).replace("'", '"'))

    response = requests.post(
        url,
        data=payload,
        headers={
            "X-Session-Token": token,
            "Content-Type": "application/x-www-form-urlencoded"
        }
    )

    if not response.ok:
        raise RuntimeError(f"{response.status_code}: {response.text[:200]}")

    reader = csv.reader(io.StringIO(response.text))
    return list(reader)
