from urllib.parse import urljoin

from requests import Session

from app.config import get_config


class JiraSession(Session):
    def __init__(self, jira_cookie):
        super().__init__()
        self.jira_cookie = jira_cookie
        self.url = get_config().JIRA_URL
        self.username = get_config().USERNAME
        self.user_issues = []

    def get_user_issues(self):
        query = f'rest/api/2/search?jql=assignee={self.username}'
        url = urljoin(self.url, query)
        response = self.get(url, cookies=self.jira_cookie)
        if response.status_code == 200:
            self.user_issues = response.json().get('issues', [])

    def extract_info(self):
        # fields
        # - created (YYYY-MM-DDTHH:mm:ss.000+0100)
        # - creator -> displayName
        # - description
        # - duedate (YYYY-MM-DD)
        # - priority -> name
        # - progress -> progress | total
        # - project -> key (MFP) | name (My Fancy Project)
        # - reporter -> displayName
        # - resolution -> name | description
        # - summary
        # - status -> name
        # key

        short = [
            {
                'summary': issue.get('fields', {}).get('summary'),
                'status': issue.get('fields', {}).get('status', {}).get('name')
            }
            for issue in self.user_issues]
        return short
