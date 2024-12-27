from rest_framework import serializers
from main.models import Book, Order

class BookSerializer(serializers.ModelSerializer):
    # реализуйте сериализацию объектов модели Book
    class Meta:
        model = Book
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['orders_count'] = Order.objects.filter(books=instance).count()
        return representation


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['books', 'days_count', 'user_name', 'date']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['books'] = BookSerializer(instance.books.all(), many=True).data
        return representation

