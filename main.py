#! /usr/bin/python3.7
import os, yaml, time
from classes.jira import jira

if __name__ == "__main__":

    username    = 'test'
    email       = 'test@example.com'
    email       = 'test@example'
    password    = 't4too7a'
    groupPolicy = 'exampleGroupName' # view in config file (jira_group_access.yml)

# class for working with users 
    # jira = jira().auth()
    # jira.user_invite(email)
    # jira.user_delete(username)
    # jira.user_blocked(username) # sorry, but this module maybe failed. Usualy failed error code 401. (bug Jira library)
    # jira.user_add_group(groupPolicy)