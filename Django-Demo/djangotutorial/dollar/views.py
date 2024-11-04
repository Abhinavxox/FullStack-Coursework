from django.http import JsonResponse

def my_view(request):
    data = {
        'message': 'Hello, World!',
        'status': 'success',
    }
    return JsonResponse(data)
