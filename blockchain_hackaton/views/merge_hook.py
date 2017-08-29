import json

from django.http import HttpResponse
from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt

# @method_decorator(csrf_exempt, name='dispatch')
from web3.main import Web3
from web3.providers.rpc import HTTPProvider

from blockchain_hackaton.contract_handler import ContractHandler
from blockchain_hackaton.getpullrequest.external_call.external_call import get_number_lines


@csrf_exempt
def merge_hook_view(request):
    if request.method == 'POST':
        body = json.loads(request.body)

        contract_handler = ContractHandler()
        if 'pullrequest' in body:
            author_username = body['pullrequest']['author']['username']
            pull_id = body['pullrequest']['id']
            reviewers = body['pullrequest']['reviewers']
            line_num = get_number_lines(pull_id)

            for reviewer in reviewers:
                username = reviewer['username']
                print(username)
                contract_handler.reward_code_reviewer(username)
            contract_handler.handle_contribution(author_username)

        elif 'issue' in body:
            author_username = body['issue']['reporter']['username']
            if body['changes']['status']['new'] == 'resolved':
                contract_handler.handle_issue_create(author_username)

        return JsonResponse({'status': True})
