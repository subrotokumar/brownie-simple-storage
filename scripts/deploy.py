from brownie import accounts, config, SimpleStorage, network

def get_account():
    if network.show_active() == "development":
        # from ganache-cli
        return accounts[0]
    else:
        # from .env
        # account = accounts.add(os.getenv("PRIVATE_KEY"))
        return accounts.add(config["wallets"]["from_key"])

def deploy_simple_storage():
    account = get_account()
    print(account)

    # From terminal: `brownie accounts add {acount-name}`
    # account = accounts.load("Account1")
    # print(account)

    simple_storage = SimpleStorage.deploy({"from": account})
    print(simple_storage)

    stored_value=simple_storage.retrieve()
    print(stored_value)

    transaction = simple_storage.store(15, {"from": account})
    transaction.wait(1)
    updated_store_value = simple_storage.retrieve()
    print(updated_store_value)

def main():
    deploy_simple_storage()
