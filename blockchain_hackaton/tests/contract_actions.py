from django.test.testcases import TestCase

from blockchain_hackaton.contract_handler import ContractHandler
from blockchain_hackaton.getpullrequest.external_call.external_call import get_number_lines
class TestContractActions(TestCase):
    def test_add_contributor(self):


        contract_handler = ContractHandler()

        print(contract_handler.add_contributor('Heisenberg', '0x415ADfBA2FbeD9e67Ad5400156cB4e8Bc3bAE6fC'))

    def test_skrpy(self):
        pr_url = '4'

        a = get_number_lines(pr_url)

        print('test')
        print(a)