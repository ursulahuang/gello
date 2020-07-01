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

"""fetch_jira_projects.py

Fetches JIRA projects.
"""

from celery.task import Task
from ..services.project_service import ProjectService


class FetchJIRAProjects(Task):
    """A task to fetches JIRA projects."""

    def __init__(self):
        """Initializes a `FetchJIRAProjects` object for the class."""
        pass

    def run(self):
        """Fetches JIRA projects.

        Args:
            None

        Returns:
            None
        """
        ProjectService().fetch()