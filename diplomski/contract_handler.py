import json
from os import path

from web3 import Web3
from web3 import HTTPProvider

from diplomski.settings.settings import BASE_DIR



class ContractHandler:
    def __init__(self):
        self.web3 = Web3(HTTPProvider('http://localhost:8545'))
        with open(str(path.join(BASE_DIR, 'abis/contract_abi_malisa.json')), 'r') as abi_definition:
            self.abi = json.load(abi_definition)
        #  self.contract_address = '0x9c5589c9AD34648e2a67d9F058dA564e38291cDC'
        #  self.contract_address = '0x2E4cCDe91cAeb7E8b56E9EeF58e5cDcdd7f740B0'
        self.contract_address = '0xD2E8C7b3e7d56FdD3478Faae84e27F878A572a8c'
        self.contract = self.web3.eth.contract(abi=self.abi, address=self.contract_address)
        #  print json.dumps(self.web3.eth.accounts)
        #  print self.web3.eth.accounts
        #  print ' malisa'
        #  print self.web3.personal.listAccounts
        self.admin = self.web3.eth.accounts[0]
        self.password = ''  # password here

    def handle_contribution(self, username, num_lines=0):
        self.web3.personal.unlockAccount(self.admin, self.password, 1000)

        tx_hash = self.contract.transact({'from': self.web3.eth.coinbase,
                                          'to': self.contract_address}).handleContribution(username, 0, num_lines)
        return tx_hash

    def add_contributor(self, username, address):
        self.web3.personal.unlockAccount(self.admin, self.password, 1000)
        tx_hash = self.contract.transact({'from': self.web3.eth.coinbase,
                                          'to': self.contract_address}).addContributor(username, address)
        return tx_hash

    def reward_code_reviewer(self, username, num_lines = 0):
        self.web3.personal.unlockAccount(self.admin, self.password, 1000)
        tx_hash = self.contract.transact({'from': self.web3.eth.coinbase,
                                          'to': self.contract_address}).handleContribution(username, 1, num_lines)
        return tx_hash

    def handle_issue_create(self, username, num_lines=0):
        self.web3.personal.unlockAccount(self.admin, self.password, 1000)
        tx_hash = self.contract.transact({'from': self.web3.eth.coinbase,
                                          'to': self.contract_address}).handleContribution(username, 2, num_lines)
        return tx_hash
