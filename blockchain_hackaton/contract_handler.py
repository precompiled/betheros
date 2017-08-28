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
        self.contract_address = '0x2E4cCDe91cAeb7E8b56E9EeF58e5cDcdd7f740B0'
        self.contract = self.web3.eth.contract(abi=self.abi, address=self.contract_address)

    def handle_contribution(self, username):
        self.web3.personal.unlockAccount(self.web3.eth.accounts[0], 'vidimalidimi', 1000)

        tx_hash = self.contract.transact({'from': self.web3.eth.coinbase,
                                          'to': self.contract_address}).handleContribution(username, 0)
        return tx_hash

    def add_contributor(self, username, address):
        self.web3.personal.unlockAccount(self.web3.eth.accounts[0], 'vidimalidimi', 1000)
        tx_hash = self.contract.transact({'from': self.web3.eth.coinbase,
                                          'to': self.contract_address}).addContributor(username, address)
        return tx_hash

    def handle_issue_create(self, username):


        self.web3.personal.unlockAccount(self.web3.eth.accounts[0], 'vidimalidimi', 1000)
        tx_hash = self.contract.transact({'from': self.web3.eth.coinbase,
                                          'to': self.contract_address}).addContributor(username, 1)
