#!/usr/bin/env python

import logging
import settings
import utils.date

from harvest.credentials import PersonalAccessAuthCredential
from harvest.endpoints import TimeEntryEndpoint
from requests.exceptions import HTTPError

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
)

class Harvest:
    def __init__(self):
        config = settings.Harvest()
        self.token = config.TOKEN
        self.account_id = config.ACCOUNT_ID
        self.project_id = config.PAYROLL_PROJECT_ID
        self.task_id = config.SOFTWARE_DEVELOPMENT_TASK_ID
        self.today = utils.date.currentday()
        self.amount_hours = config.AMOUNT_HOURS
        self.credential = None

    def harvest_auth(self):
        self.credential = PersonalAccessAuthCredential(
            token=self.token,
            account_id=self.account_id
        )

    def run(self):
        if utils.date.isweekday(self.today):
            logging.info("Is weekday, let's try to set time entry in harvest")
            self.harvest_auth()
            try:
                resp = TimeEntryEndpoint(self.credential).post(params={
                    'project_id': self.project_id,
                    'task_id': self.task_id,
                    'spent_date': self.today,
                    'hours': self.amount_hours
                })
            except HTTPError as http_err:
                logging.exception(f'HTTP error occurred: {http_err}')
            except Exception as err:
                logging.exception(f'Other error occurred: {err}')
            else:
                logging.info("Time added succesfully")
        else:
            logging.info("Nothing to log today, just relax!")

if __name__ == '__main__':
    Harvest().run()
