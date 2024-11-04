from django.http import HttpResponse


def my_view(request):
    return HttpResponse("<h2>Hello this is the contact page</h2>")