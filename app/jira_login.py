from selenium import webdriver

from app.config import get_config


class JiraLogin:
    def __init__(self):
        self.jira_cookie = {}
        self.driver = None

    def login(self):
        options = webdriver.ChromeOptions()
        options.add_argument('--ignore-certificate-errors')
        options.add_argument("--test-type")
        options.binary_location = get_config().CHROME_BINARY
        self.driver = webdriver.Chrome(chrome_options=options)
        self.driver.get(get_config().JIRA_URL)

    def get_cookies(self):
        mrh_cookies = self.driver.get_cookie('MRHSession')
        mrh_last_cookies = self.driver.get_cookie('LastMRH_Session')
        jsid_cookies = self.driver.get_cookie('JSESSIONID')
        route_cookie = self.driver.get_cookie('route')
        xsrf_cookie = self.driver.get_cookie('atlassian.xsrf.token')
        self.jira_cookie = {
            'MRHSession': mrh_cookies.get('value'),
            'LastMRH_Session': mrh_last_cookies.get('value'),
            'JSESSIONID': jsid_cookies.get('value'),
            'route': route_cookie.get('value'),
            'atlassian.xsrf.token': xsrf_cookie.get('value'),
        }
