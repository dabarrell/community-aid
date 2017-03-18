from django.db import models


class Item_Priority(models.Model):
	priority_name = models.CharField(max_length=20)

	def __str__(self):
		return self.priority_name

class Item_Category(models.Model):
	category_name = models.CharField(max_length=40)

	def __str__(self):
		return self.category_name

class Item_Type(models.Model):
	type_name = models.CharField(max_length=20)

	def __str__(self):
		return self.type_name

class Item(models.Model):
	item_name = models.CharField(max_length=100)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	author_name = models.CharField(max_length=100)
	author_phone = models.CharField(max_length=12)
	item_description = models.CharField(max_length=500)
	item_location = models.CharField(max_length=100) #change this to the location type
	item_priority = models.ForeignKey(Item_Priority, on_delete=models.CASCADE)
	item_category = models.ForeignKey(Item_Category, on_delete=models.CASCADE)
	item_type = models.ForeignKey(Item_Type, on_delete=models.CASCADE)

	def __str__(self):
		return self.item_name

class Comment(models.Model):
	comment_text = models.CharField(max_length=500)
	author_name = models.CharField(max_length=100)
	author_phone = models.CharField(max_length=12)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	item = models.ForeignKey(Item, on_delete=models.CASCADE)
