from penny_one.models.userModels import user, user_info
from django.http import JsonResponse
from penny_one.serializer.userSerializer import UserSerializer, UserInfoSerializer
from django.contrib.auth import get_user_model
from rest_framework.decorators import api_view
from rest_framework.response import Response

User = get_user_model()

@api_view(['POST'])
def register(request):
    username = request.data.get('username')
    password = request.data.get('password')
    email = request.data.get('email')

    # Validate input data
    if not username or not password or not email:
        return Response({'error': 'Please provide all required fields.'}, status=400)

    try:
        # Create a new user
        user = User.objects.create_user(username=username, password=password, email=email)
        return Response({'message': 'Registration successful.'}, status=201)
    except Exception as e:
        return Response({'error': str(e)}, status=400)

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
