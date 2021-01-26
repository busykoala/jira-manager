from app.jira_session import JiraSession
from app.jira_login import JiraLogin


def run_app():
    login = input("Do you wanna login [yes/No]:")
    if login == "yes":
        jira_login = JiraLogin()
        jira_login.login()
        jira_session = JiraSession(jira_login.jira_cookie)
    else:
        jira_session = JiraSession()

    jira_session.get_user_issues()
    __import__('pdb').set_trace()


if __name__ == "__main__":
    run_app()
