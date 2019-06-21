from jira import JIRA
from jira.exceptions import JIRAError
import requests

class jira():

    def __init__(self):
        pass

    def auth(self, url, **auth_data):

        self.url            = url 
        self.jira_options   = {
                                  'server'        : url,
                                  'max_retries'   : 1
                              } 
        try:
            self._session = JIRA(self.jira_options, basic_auth=(auth_data['auth'][0], auth_data['auth'][1]))

        except JIRAError and TypeError and KeyError as error:
            print(error)

    def user_invite(self, email):

        self.USERNAME = email.split('@')[0]
       
        try:
            self._session.add_user(self.USERNAME, email, active=True)
        
        except JIRAError as error:
            print('jira.init.user_invite <%s>' % error.text)
   
    def user_delete(self, username):

        try:
            DELETE_USER = self._session.delete_user(username)

        except JIRAError and TypeError and KeyError as error:
            print('jira.init.user_delete <%s>' % error)

    def user_blocked(self, username):
        DEACTIVATE_USER = self._session.deactivate_user(username)

        try:
            DELETE_USER = self._session.deactivate_user(username)

        except JIRAError and TypeError and KeyError as error:
            print('jira_api_user.init.user_blocked <%s>' % error)

    def user_add_group(self, group_list):

        for group in group_list:
            
            try:
                self._session.add_user_to_group(self.USERNAME , group)

            except JIRAError and TypeError and KeyError as error:
                print('jira_api_user.init.user_add_group <%s>' % error)
          