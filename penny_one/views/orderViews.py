from penny_one.models.orderModels import order, order_items, products, food, drink
from django.http import JsonResponse
from penny_one.serializer.orderSerializer import OrderSerializer, OrderItemsSerializer, ProductsSerializer, FoodSerializer, DrinkSerializer

def ordersView(request):
    data = order.objects.all()
    serializer = OrderSerializer(data, many=True)
    return JsonResponse({'orders': serializer.data})


def orderItemsView(request):
    data = order_items.objects.all()
    serializer = OrderItemsSerializer(data, many=True)
    return JsonResponse({'orders_items': serializer.data})

def drinkCategoryView(request):
    data = products.objects.filter(productName='Coffee').union(products.objects.filter(productName='Non Coffee'))
    serializer = DrinkSerializer(data, many=True)
    drink.objects.select_related("prodfk")
    return JsonResponse({'products': serializer.data})

