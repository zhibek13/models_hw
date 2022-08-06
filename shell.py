import json
from my_app.models import Customer, Work, Account

with open ('data.json') as f:
    shell = json.load(f)

shell.save()