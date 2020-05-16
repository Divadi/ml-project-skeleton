import requests

# returns True if scheduled for termination
def check_termination():
    return requests.get('http://169.254.169.254/latest/meta-data/spot/termination-time').status_code != 404