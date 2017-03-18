from django.db import models

class Item(models.Model):
	item_name = models.CharField(max_length=100)
	pub_date = models.DateTimeField('date published')
	author_name = models.CharField(max_length=100)
	author_phone = models.Charfield(max_length=12)
	item_description = models.Charfield(max_length=500)
	item_location = models.CharField(max_length=100) #change this to the location type
	item_priority = models.ForeignKey(Item_Priority, on_delete=models.CASCADE)
	item_category = models.ForeignKey(Item_Category, on_delete=models.CASCADE)
	item_type = models.ForeignKey(Item_Type, on_delete=models.CASCADE)


class Item_Priority(models.Model):
	priority = models.CharField(max_length=20)

class Item_Category(models.Model):
	priority = models.CharField(max_length=40)

class Item_Type(models.Model):
	priority = models.CharField(max_length=20)


class Comment(models.Model):
	comment_text = models.CharField(max_length=500)
	author_name = models.CharField(max_length=100)
	author_phone = models.Charfield(max_length=12)
	pub_date = models.DateTimeField('date published')
	item = models.ForeignKey(Item, on_delete=models.CASCADE)