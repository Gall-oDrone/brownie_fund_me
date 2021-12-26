from brownie import network, config, accounts, MockV3Aggregator
from web3 import Web3

FORKED_LOCA_ENVIRONMENTS = ["mainnet-fork"]
LOCAL_BLOCKCHAIN_EVN = ["development", "ganache-local"]
DECIMALS = 8
STARTING_PRICE = 200000000000


def get_account():
    if (
        network.show_active() in LOCAL_BLOCKCHAIN_EVN
        or network.show_active() in FORKED_LOCA_ENVIRONMENTS
    ):
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])


def deploy_mocks():
    print(f"The active network is {network.show_astive()}")
    print("Deploying Mocks...")
    if len(MockV3Aggregator) <= 0:
        mock_aggregator = MockV3Aggregator.deploy(
            DECIMALS, STARTING_PRICE, {"from": get_account()}
        )
    price_feed_address = MockV3Aggregator[-1].address
    print("Mock deployed")
