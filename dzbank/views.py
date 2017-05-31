from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_POST

from .forms import GetAccountForm
from .cc_api import CCApi


def import_depot(request):
    return render(request, 'import.html', {})


def simulation(request):
    return render(request, 'simulation.html', {})


@require_POST
def d_get_accounts(request):
    print request.data
    form = GetAccountForm(request.POST)
    if form.is_valid():
        pass
    else:
        print form.errors
    # user = request.POST.get('user')
    # credentials = request.POST.get('credentials')
    CCApi.get_accounts.get_accounts()
    return JsonResponse({})
