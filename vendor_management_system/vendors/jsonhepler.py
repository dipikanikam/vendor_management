from django.http import JsonResponse


def SuccessJson(message, status_code, data=[]):
    return JsonResponse({
            'status': True,
            'message': message,
            'data': data
        },status=status_code)

def ErrorJson(message, status_code, data=[]):
    return JsonResponse({
            'status': False,
            'message': message,
            'data': data
        },status=status_code)