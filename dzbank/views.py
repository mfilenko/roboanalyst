from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_POST

from .forms import GetAccountForm, SelectAccountsForm


def import_depot(request):
    return render(request, 'import.html', {})


def simulation(request):
    return render(request, 'simulation.html', {})


@require_POST
def d_get_accounts(request):
    form = GetAccountForm(request.POST)
    r = {}
    if form.is_valid():
        r = form.call()
    else:
        r.update(success=False)
    return JsonResponse(r)


@require_POST
def d_select_assets(request):
    print request.POST
    form = SelectAccountsForm(request.POST)
    r = {}
    if form.is_valid():
        r = form.call()
        r.update(success=True)
    else:
        r.update(success=False)
    return JsonResponse(r)
