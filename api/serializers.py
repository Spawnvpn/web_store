from rest_framework import serializers
from goods.models import Product, Category
from users.models import WebStoreUser


class ProductSerializer(serializers.ModelSerializer):
    categories = serializers.StringRelatedField(many=True)
    creator = serializers.StringRelatedField(many=False)

    class Meta:
        model = Product
        fields = '__all__'


class WebStoreUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = WebStoreUser
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    parent = serializers.StringRelatedField(many=False)

    class Meta:
        model = Category
        fields = '__all__'