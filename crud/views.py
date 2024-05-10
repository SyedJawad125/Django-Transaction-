from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .controller import ProductsController, OrdersController, OrderdetialsController
# Create your views here.

products_controller= ProductsController()
orders_controller= OrdersController()
orderdetials_controller= OrderdetialsController()

class ProductsView(ModelViewSet):

    def create(self, request):
        return products_controller.create_product(request)

    def fetch(self, request):
        return products_controller.fetch_product(request)

    def update(self, request):
        return products_controller.update_product(request)

    def delete(self, request):
        return products_controller.delete_product(request)
    


class OrdersView(ModelViewSet):

    def create(self, request):
        return orders_controller.create_orders(request)

    def fetch(self, request):
        return orders_controller.fetch_orders(request)

    def update(self, request):
        return orders_controller.update_orders(request)

    def delete(self, request):
        return orders_controller.delete_orders(request)
    



class OrderDetialsView(ModelViewSet):

    def create(self, request):
        return orderdetials_controller.create_order_detials(request)

    def fetch(self, request):
        return orderdetials_controller.fetch_order_detials(request)

    def update(self, request):
        return orderdetials_controller.update_order_detials(request)

    def delete(self, request):
        return orderdetials_controller.delete_order_detials(request)