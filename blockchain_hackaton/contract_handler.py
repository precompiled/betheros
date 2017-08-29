import json
from os import path

from web3 import Web3
from web3.providers.rpc import HTTPProvider

from blockchain_hackaton.settings.settings import BASE_DIR


class ContractHandler:
    def __init__(self):
        self.web3 = Web3(HTTPProvider('http://localhost:8545'))
        with open(str(path.join(BASE_DIR, 'abis/contract_abi.json')), 'r') as abi_definition:
            self.abi = json.load(abi_definition)
        self.contract_address = '0x9c5589c9AD34648e2a67d9F058dA564e38291cDC'
        self.contract = self.web3.eth.contract(abi=self.abi, address=self.contract_address)

    def handle_contribution(self, username, num_lines=0):
        self.web3.personal.unlockAccount(self.web3.eth.accounts[0], 'vidimalidimi', 1000)

        tx_hash = self.contract.transact({'from': self.web3.eth.coinbase,
                                          'to': self.contract_address}).handleContribution(username, 0, num_lines)
        return tx_hash

    def add_contributor(self, username, address):
        self.web3.personal.unlockAccount(self.web3.eth.accounts[0], 'vidimalidimi', 1000)
        tx_hash = self.contract.transact({'from': self.web3.eth.coinbase,
                                          'to': self.contract_address}).addContributor(username, address)
        return tx_hash

    def reward_code_reviewer(self, username, num_lines = 0):
        self.web3.personal.unlockAccount(self.web3.eth.accounts[0], 'vidimalidimi', 1000)
        tx_hash = self.contract.transact({'from': self.web3.eth.coinbase,
                                          'to': self.contract_address}).handleContribution(username, 1, num_lines)
        return tx_hash

    def handle_issue_create(self, username, num_lines=0):
        self.web3.personal.unlockAccount(self.web3.eth.accounts[0], 'vidimalidimi', 1000)
        tx_hash = self.contract.transact({'from': self.web3.eth.coinbase,
                                          'to': self.contract_address}).handleContribution(username, 2, num_lines)
        return tx_hash
