from django.contrib import admin
from penny_one.models.userModels import user, user_info, userCreatesEwallet, userHasInfo, userReceivesPoints
from penny_one.models.orderModels import order, order_items, products, food, drink
from penny_one.models.ewalletModels import ewallet, ewallet_transaction, recovery_codes
from penny_one.models.pointsModel import points, points_transaction, reward
from penny_one.models.authorizedModels import workerPortal, deliveryPersonnel, workerHasDP, workerHasBranch, branch

myModels = [user, user_info, userCreatesEwallet, userHasInfo, userReceivesPoints, order, order_items, products, food, drink,
            ewallet, ewallet_transaction, recovery_codes, points, points_transaction, reward, workerPortal, deliveryPersonnel,
            branch, workerHasDP, workerHasBranch]
admin.site.register(myModels)