from __future__ import annotations
from jira import JIRA
from jira.client import ResultList
from jira.resources import Issue
from datetime import *
from dateutil.relativedelta import relativedelta
from dateutil.parser import isoparse
import yaml

credentials = yaml.safe_load(open('credentials.yml'))

jira = JIRA('https://uinsure.atlassian.net',
    basic_auth=(credentials['user'], credentials['token']),
)

query = 'updated >= -14d AND project = "Uinsure Core" AND "Story Points Estimate[Number]" > 0'
issues: ResultList[Issue] = jira.search_issues(query, expand="changelog")

print("Issues burnt up in the last two weeks:")
print()

cutoff = datetime.now(tz=timezone.utc) + relativedelta(days=-14)

for issue in issues:
    recently_burnt_up = False
    estimate = int(issue.get_field('customfield_10023'))
    completed = int(issue.get_field('customfield_10041'))

    if estimate < completed:
        for history in issue.changelog.histories:
            when = isoparse(history.created)
            recent = when > cutoff

            for item in history.items:
                if item.field == "Story Points Completed" and recent == True:
                    recently_burnt_up = True

        if recently_burnt_up == True:
            print(issue.key, "burnt up by", completed-estimate)

print()
