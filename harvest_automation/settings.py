from decouple import config


class Harvest:
    TOKEN = config('TOKEN', cast=str)
    ACCOUNT_ID = config('ACCOUNT_ID', cast=str)
    PAYROLL_PROJECT_ID = config('PAYROLL_PROJECT_ID', cast=int)
    SOFTWARE_DEVELOPMENT_TASK_ID = config('SOFTWARE_DEVELOPMENT_TASK_ID', cast=int)
    AMOUNT_HOURS = config('AMOUNT_HOURS', cast=int)

