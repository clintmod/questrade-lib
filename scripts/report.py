#!/usr/bin/env python

import json
import pandas as pd

with open("workdir/output.json", 'r') as f:
    accounts = json.load(f);

ar = []
positions = []

for account in accounts:
    info = {"id": account['id']}
    for bal in account["balances"]["combinedBalances"]:
        if bal["currency"] == "USD":
            info["balance"] = bal['marketValue']
            info["cash"] = bal['cash']
    ar.append(info)
    act_position = account['positions'][0]
    positions.append({
        "symbol": act_position["symbol"],
        "qty": act_position["openQuantity"],
        "cur": act_position["currentMarketValue"],
        "price": act_position["currentPrice"],
        "avg": act_position["averageEntryPrice"],
        "in": act_position["totalCost"],
    })

df = pd.DataFrame(ar)
df.loc["Totals"] = df.sum(numeric_only=True)
df["balance"] = df["balance"].apply(lambda x: "${:.2f}".format(x))
df["cash"] = df["cash"].apply(lambda x: "${:.2f}".format(x))

print("\nAccount Summary\n")
print(df)
print()
df2 = pd.DataFrame(positions)
df2["profit"] = df2["cur"] - df2["in"]
df2.loc["Totals"] = df2.sum(numeric_only=True)
df2["cur"] = df2["cur"].apply(lambda x: "${:.2f}".format(x))
df2["price"] = df2["price"].apply(lambda x: "${:.2f}".format(x))
df2["avg"] = df2["avg"].apply(lambda x: "${:.2f}".format(x))
df2["in"] = df2["in"].apply(lambda x: "${:.2f}".format(x))
df2["profit"] = df2["profit"].apply(lambda x: "${:.2f}".format(x))

print("\nPositions\n")
print(df2)
print()
