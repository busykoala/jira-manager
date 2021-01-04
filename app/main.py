from app.jira_session import JiraSession
from app.jira_login import JiraLogin


def run_app():
    jira_login = JiraLogin()
    jira_login.login()

    jira_session = JiraSession(jira_login.jira_cookie)
    jira_session.get_user_issues()


if __name__ == "__main__":
    run_app()
