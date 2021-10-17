#!/usr/bin/env python

import json
import sys

from requests.exceptions import HTTPError

from qtrade import Questrade

try:
    print("\n Trying token yaml \n")
    q = Questrade(token_yaml="access_token.yml")
    print("\n Token yaml worked \n")
    print("\n Fetching accounts \n")
    account_ids = q.get_account_id()
    print("\n Accounts fetched \n")
except (HTTPError, FileNotFoundError):
    try:
        print("\n Accounts not fetched \n")
        print("\n Trying refresh \n")
        q = Questrade(token_yaml="access_token.yml")
        q.refresh_access_token(from_yaml=True, yaml_path="access_token.yml")
        print("\n Fetching accounts again \n")
        account_ids = q.get_account_id()
        print("\n Accounts fetched \n")
    except (HTTPError, FileNotFoundError):
        print("\n Accounts not fetched \n")
        print("\n Trying access code \n")
        try:
            with open("access_code.txt") as f:
                access_code = f.read().strip()
                q = Questrade(access_code=access_code)
                account_ids = q.get_account_id()
                print("\n Accounts fetched \n")
        except (HTTPError, FileNotFoundError):
            print("\n Accounts not fetched \n")
            print("\n We're out of options \n")
            print("\n You might need a new access code from Questrade \n")
            print("\n and put it in a file in the root called access_code.txt \n")
            sys.exit(1)

print(f"\n account ids = {account_ids} \n")

accounts = []
for account_id in account_ids:
    info = {"id": account_id}
    bal = q.get_account_balances(account_id)
    positions = q.get_account_positions(account_id)
    info["balances"] = bal
    info["positions"] = positions
    accounts.append(info)

with open('workdir/output.json', 'w') as f:
    json.dump(accounts, f)

print("\n data saved to workdir/output.json \n")
