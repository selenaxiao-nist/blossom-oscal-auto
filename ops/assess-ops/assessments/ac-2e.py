import requests
import json

def get_approved_requests(organization: str, repo: str) -> list:
    url = f"https://api.github.com/repos/{organization}/{repo}/issues?state=closed"
    headers = {"Accept": "application/vnd.github+json"}
    # assumes public repo

    closed_issues = []
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print(f"Failure code when getting approved requests: {response.status_code}")
        exit(1)
    for closed_issue in response.json():
        closed_issues.append(closed_issue['number'])

    return closed_issues

def get_approvers(closed_issues: list) -> list:
    return []