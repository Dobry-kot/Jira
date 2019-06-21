import os, yaml, time
from classes.jira import jira


if __name__ == "__main__":
    
    PWD = os.getenv("HOME")
  
    with open("%s/.python_auth_cfg.yml" % PWD, 'r') as auth:

        auth_conf = yaml.load(auth, Loader=yaml.FullLoader)

    jira_conf            = auth_conf['jira']
    jira_admin_user      = jira_conf['admin_user']
    jira_admin_api_token = jira_conf['admin_api_token']
    jira_basic_url       = jira_conf['jira_basic_url']

    """gropePolicy = ['***', '***'] input your list groupes for user"""
    username    = 'pdl.48.hot'
    email       = 'pdl.48.hot@gmail.com'
    password    = ''
    gropePolicy = ['users'] 

    jira = jira()
    jira.auth(jira_basic_url, auth=(jira_admin_user, jira_admin_api_token))
    jira.user_invite(email)
    # jira.user_delete(username)
    time.sleep(15)
    jira.user_add_group(gropePolicy)