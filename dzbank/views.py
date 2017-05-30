from django.shortcuts import render


def import_depot(request):
    return render(request, 'import.html', {})
