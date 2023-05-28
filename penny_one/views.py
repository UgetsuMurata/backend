from penny_one.models import user, user_info
from django.http import JsonResponse
from penny_one.serializer import UserSerializer, UserInfoSerializer

def users(request):
    data = user.objects.all()
    serializer = UserSerializer(data, many=True)
    return JsonResponse({'users': serializer.data})

def userInfo(request, id):
    try:
        data = user_info.objects.get(UserID=id)
        serializer = UserInfoSerializer(data, many=False)
        return JsonResponse({'user_info': serializer.data})
    except user_info.DoesNotExist:
        return JsonResponse({'error': 'User info not found'}, status=404)
    
