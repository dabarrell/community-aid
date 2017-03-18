from django.contrib import admin
from .models import Item, Comment, Item_Type, Item_Category, Item_Priority, User

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('created_at', 'item_name', 'item_category')
    date_hierarchy = 'created_at'
    search_fields = ('item_name', 'item_category')

@admin.register(Comment)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('created_at', 'comment_text')
    date_hierarchy = 'created_at'
    search_fields = ('comment_text',)

@admin.register(Item_Type)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('created_at', 'type_name')
    date_hierarchy = 'created_at'
    search_fields = ('type_name',)

@admin.register(Item_Category)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('created_at', 'category_name')
    date_hierarchy = 'created_at'
    search_fields = ('category_name',)

@admin.register(Item_Priority)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('created_at', 'priority_name')
    date_hierarchy = 'created_at'
    search_fields = ('priority_name',)

@admin.register(User)
class ItemAdmin(admin.ModelAdmin):
    def user_str(self):
        return self.model.user.get_full_name()

    list_display = ('created_at', 'full_name', 'id', 'phone')
    date_hierarchy = 'created_at'
    search_fields = ('full_name',)


# Register your models here.
