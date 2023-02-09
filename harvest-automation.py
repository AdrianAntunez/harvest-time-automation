#!/bin/env python

import logging
from datetime import date
from harvest.credentials import PersonalAccessAuthCredential
from harvest.endpoints import TimeEntryEndpoint
from requests.exceptions import HTTPError

# DEFS
TOKEN=<your_harvest_token>
ACCOUNT_ID=<your_harvesst_account_id>
PAYROLL_PROJECT_ID=<harvest_project_id>
SOFTWARE_DEVELOPMENT_TASK_ID=<harvest_task_id>
AMOUNT_HOURS=<harvest_hours_to_log>
# END DEFS

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s.%(msecs)03d %(levelname)s %(module)s - %(funcName)s: %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
)

def currentday():
    return date.today()

def isweekday(set_day):
    if set_day.weekday() < 5:
        return True
    else:
        return False

def harvest_auth():
    credential = PersonalAccessAuthCredential(
        token=TOKEN,
        account_id=ACCOUNT_ID,
    )
    return credential
    

today = currentday()
if isweekday(today):
    logging.info("Is weekday, let's try to set time entry in harvest")
    credential = harvest_auth()
    try:
        resp = TimeEntryEndpoint(credential).post(params={
            'project_id': PAYROLL_PROJECT_ID,
            'task_id': SOFTWARE_DEVELOPMENT_TASK_ID,
            'spent_date': today,
            'hours': AMOUNT_HOURS
        })
    except HTTPError as http_err:
        logging.error(f'HTTP error occurred: {http_err}')
    except Exception as err:
        logging.error(f'Other error occurred: {err}')
    else:
        logging.info("Time added succesfully")
else:
    logging.info("Nothing to log today, just relax!")