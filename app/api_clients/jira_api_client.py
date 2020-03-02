# -*- coding: utf-8 -*-

#
# Unless explicitly stated otherwise all files in this repository are licensed
# under the Apache 2 License.
#
# This product includes software developed at Datadog
# (https://www.datadoghq.com/).
#
# Copyright 2018 Datadog, Inc.
#

"""jira_api_client.py

Concrete class representing Jira API Client.
"""

from os import environ

from jira import JIRA
from . import APIClient


class JiraAPIClient(APIClient):
    """
    This class provides an API client to interact with the JIRA API
    """

    def __init__(self):
        server = environ.get('JIRA_SERVER_ADDRESS')
        username = environ.get('JIRA_USERNAME')
        key = environ.get('JIRA_API_KEY')
        if not (bool(server) and bool(username) and bool(key)):
            self._client = None
        else:
            self._client = JIRA(
                options={
                    'server': environ.get('JIRA_SERVER_ADDRESS')
                },
                basic_auth=(environ.get('JIRA_USERNAME'),
                            environ.get('JIRA_API_KEY'))
            )

    def client(self):
        return self._client

# TODO?: make either JIRA or Trello mandatory, but not necessarily both