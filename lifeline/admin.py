from django.contrib import admin


from .models import Item, Comment, Item_Type, Item_Category, Item_Priority

admin.site.register(Item)
admin.site.register(Comment)
admin.site.register(Item_Type)
admin.site.register(Item_Category)
admin.site.register(Item_Priority)

# Register your models here.
