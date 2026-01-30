from algoliasearch_django import AlgoliaIndex
from algoliasearch_django.decorators import register

# IMPORT the model from your models.py file
from .models import Product 

@register(Product)
class ProductIndex(AlgoliaIndex):
    fields = [
        'title',
        'content',
        'price',
        'get_user_name', # Use the method name defined in your model
    ]
    settings = {
        'searchableAttributes': ['title', 'content'],
        'attributesForFaceting': ['get_user_name']
    }
    index_name = 'Apipractice_Product'

# EVERYTHING BELOW THIS LINE SHOULD BE DELETED