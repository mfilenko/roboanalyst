from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_POST, require_GET

from .forms import GetAccountForm, SelectAccountsForm, UserForm


def import_depot(request):
    return render(request, 'import.html', {})


def simulation(request):
    return render(request, 'simulation.html', {})


@require_POST
def d_figo_connect(request):
    form = GetAccountForm(request.POST)
    r = {}
    if form.is_valid():
        r = form.call()
    else:
        r.update(success=False)
    return JsonResponse(r)


@require_POST
def d_select_assets(request):
    form = SelectAccountsForm(request.POST)
    r = {}
    if form.is_valid():
        r = form.call()
        r.update(success=True)
    else:
        r.update(success=False)
    return JsonResponse(r)


@require_GET
def d_get_selected_assets(request):
    form = UserForm(request.GET)
    if form.is_valid():
        return JsonResponse({
            'success': True,
            'data': form.get_selected_assets()
        })
    return JsonResponse({'success': False})


@require_GET
def d_get_all_assets(request):
    form = UserForm(request.GET)
    if form.is_valid():
        return JsonResponse({
            'success': True,
            'data': form.get_all_assets()
        })
    return JsonResponse({'success': False})
