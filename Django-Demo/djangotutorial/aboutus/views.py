from django.http import HttpResponse


def my_view(request):
    return HttpResponse("<h2>Hello this is the about us page</h2>")