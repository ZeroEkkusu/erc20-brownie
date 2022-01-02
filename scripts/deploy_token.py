from brownie import ModernToken, config, network
from scripts.helpful_scripts import get_account


initial_supply = 1000e18


def deploy():
    account = get_account()
    modern_token = ModernToken.deploy(initial_supply, {"from": account},
                                      publish_source=config["networks"][network.show_active()].get("verify", False))
    print(f"{modern_token.name()} Deployed!")


def main():
    deploy()
