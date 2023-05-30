from penny_one.models import user, user_info, ewallet
from django.http import JsonResponse
from penny_one.serializer import UserSerializer, UserInfoSerializer, EwalletSerializer

def users(request):
    data = user.objects.all()
    serializer = UserSerializer(data, many=True)
    return JsonResponse({'users': serializer.data})

def userInfo(request, id):
    try:
        data = user_info.objects.get(userID=id)
        serializer = UserInfoSerializer(data, many=False)
        return JsonResponse({'user_info': serializer.data})
    except user_info.DoesNotExist:
        return JsonResponse({'error': 'User info not found'}, status=404)
    
def EWallet(request, id):
    try:
        data = ewallet.objects.get(walletID=id)
        serializer = EwalletSerializer(data, many=False)
        return JsonResponse({'user_info': serializer.data})
    except user_info.DoesNotExist:
        return JsonResponse({'error': 'ewallet not found'}, status=404)

