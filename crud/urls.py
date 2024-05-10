from django.urls import path
from .views import ProductsView, OrdersView, OrderDetialsView

urlpatterns = [
    path('Products', ProductsView.as_view({'get':'fetch', 'post':'create', 'patch':'update', 'delete':'delete'})),

    path('Orders', OrdersView.as_view({"get":"fetch",
                            "post":"create",
                            "patch":"update",
                            "delete":"delete"})),

    path('Order_detials', OrderDetialsView.as_view({"get":"fetch",
                            "post":"create",
                            "patch":"update",
                            "delete":"delete"})),

]

# path('register', RegisterAPIView.as_view({"post": "create"}), name='register'),

