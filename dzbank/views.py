from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_POST, require_GET
from django.views.decorators.csrf import csrf_exempt

from .forms import GetAccountForm, SelectAccountsForm, UserForm


def import_depot(request):
    return render(request, 'import.html', {})


def simulation(request):
    return render(request, 'simulation.html', {})

def d_current_portfolio(request):
    return JsonResponse([{
        'name': 'Installation',
        'data': [43934, 52503, 57177, 69658, 97031, 119931, 137133, 154175]
    }, {
        'name': 'Manufacturing',
        'data': [24916, 24064, 29742, 29851, 32490, 30282, 38121, 40434]
    }, {
        'name': 'Sales & Distribution',
        'data': [11744, 17722, 16005, 19771, 20185, 24377, 32147, 39387]
    }, {
        'name': 'Project Development',
        'data': [None, None, 7988, 12169, 15112, 22452, 34400, 34227]
    }, {
        'name': 'Other',
        'data': [12908, 5948, 8105, 11248, 8989, 11816, 18274, 18111]
    }], safe=False)

def d_conservative_portfolio(request):
    return JsonResponse([{
        'name': 'Installation',
        'data': [43934, 52503, 57177, 69658, 97031, 119931, 137133, 154175]
    }, {
        'name': 'Manufacturing',
        'data': [24916, 24064, 29742, 29851, 32490, 30282, 38121, 40434]
    }, {
        'name': 'Sales & Distribution',
        'data': [11744, 17722, 16005, 19771, 20185, 24377, 32147, 39387]
    }, {
        'name': 'Project Development',
        'data': [None, None, 7988, 12169, 15112, 22452, 34400, 34227]
    }, {
        'name': 'Other',
        'data': [12908, 5948, 8105, 11248, 8989, 11816, 18274, 18111]
    }], safe=False)

def d_balanced_portfolio(request):
    return JsonResponse([{
        'name': 'Installation',
        'data': [43934, 52503, 57177, 69658, 97031, 119931, 137133, 154175]
    }, {
        'name': 'Manufacturing',
        'data': [24916, 24064, 29742, 29851, 32490, 30282, 38121, 40434]
    }, {
        'name': 'Sales & Distribution',
        'data': [11744, 17722, 16005, 19771, 20185, 24377, 32147, 39387]
    }, {
        'name': 'Project Development',
        'data': [None, None, 7988, 12169, 15112, 22452, 34400, 34227]
    }, {
        'name': 'Other',
        'data': [12908, 5948, 8105, 11248, 8989, 11816, 18274, 18111]
    }], safe=False)

def d_bold_portfolio(request):
    return JsonResponse([{
        'name': 'Installation',
        'data': [43934, 52503, 57177, 69658, 97031, 119931, 137133, 154175]
    }, {
        'name': 'Manufacturing',
        'data': [24916, 24064, 29742, 29851, 32490, 30282, 38121, 40434]
    }, {
        'name': 'Sales & Distribution',
        'data': [11744, 17722, 16005, 19771, 20185, 24377, 32147, 39387]
    }, {
        'name': 'Project Development',
        'data': [None, None, 7988, 12169, 15112, 22452, 34400, 34227]
    }, {
        'name': 'Other',
        'data': [12908, 5948, 8105, 11248, 8989, 11816, 18274, 18111]
    }], safe=False)

def d_simulation(request):
    return JsonResponse([{
        'name': 'Installation',
        'data': [43934, 52503, 57177, 69658, 97031, 119931, 137133, 154175]
    }, {
        'name': 'Manufacturing',
        'data': [24916, 24064, 29742, 29851, 32490, 30282, 38121, 40434]
    }, {
        'name': 'Sales & Distribution',
        'data': [11744, 17722, 16005, 19771, 20185, 24377, 32147, 39387]
    }, {
        'name': 'Project Development',
        'data': [None, None, 7988, 12169, 15112, 22452, 34400, 34227]
    }, {
        'name': 'Other',
        'data': [12908, 5948, 8105, 11248, 8989, 11816, 18274, 18111]
    }], safe=False)


@require_POST
@csrf_exempt
def d_figo_connect(request):
    form = GetAccountForm(request.POST)
    r = {}
    if form.is_valid():
        print 'calling'
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
