from brownie import accounts, config

def get_account(index=None, id=None):
    return accounts.add(config["wallets"]["from_key"])

