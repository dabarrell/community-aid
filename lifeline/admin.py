from django.contrib import admin


from .models import Item, Comment, Item_Type, Item_Category, Item_Priority

admin.site.register(Comment)
admin.site.register(Item_Type)
admin.site.register(Item_Category)
admin.site.register(Item_Priority)

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('created_at', 'item_name', 'author_name', 'item_category')
    date_hierarchy = 'created_at'
    search_fields = ('item_name', 'author_name', 'item_category')

# Register your models here.
