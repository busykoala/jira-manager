from flask import Flask
from flask import render_template
from flask import redirect
from flask import request
from flask import url_for
from pathlib import Path

from app.jira_session import JiraSession
from app.jira_login import JiraLogin
from app.config import get_config

ISSUE_BASE_URL = '{}/browse/'.format(get_config().JIRA_URL.rstrip('/'))
TODOS = Path('./todos')
app = Flask(__name__)
jira_login = JiraLogin()


def load_jira_info():
    jira_session = JiraSession()
    jira_session.get_user_issues()
    return jira_session.user_issues


@app.route('/')
def overview():
    todos = ''
    if TODOS.exists():
        with TODOS.open(mode='rb') as f_:
            todos = f_.read().decode('utf-8')
    user_issues = load_jira_info()
    issues = [
        {
            'summary': issue.get('fields', {}).get('summary'),
            'status': issue.get('fields', {}).get('status', {}).get('name'),
            'key': issue.get('key'),
            'url': ISSUE_BASE_URL + issue.get('key'),
            'description': issue.get('fields', {}).get('description'),
            'duedate': issue.get('fields', {}).get('duedate'),
        }
        for issue in user_issues
        if issue.get('fields', {}).get('status', {}).get('name') != 'Done']
    return render_template('overview.html', issues=issues, todos=todos)


@app.route('/save-todos', methods=["POST"])
def save_todos():
    req = request.form
    todos = req.get('todos', '')
    with TODOS.open(mode='wb+') as f_:
        f_.write(todos.encode('utf-8'))
    return redirect(url_for('overview'))


@app.route('/await-login')
def await_login():
    return render_template('await_login.html')


@app.route('/login')
def login():
    global jira_login
    jira_login.login()
    return redirect(url_for('await_login'))


@app.route('/after-await-login')
def after_await_login():
    global jira_login
    jira_login.get_cookies()
    JiraSession(jira_login.jira_cookie)
    return redirect(url_for('overview'))


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000)
