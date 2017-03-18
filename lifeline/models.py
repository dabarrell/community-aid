import uuid

from django.db import models
from django.contrib.auth.models import User as DefaultUser
from django.utils.timesince import timesince


class BaseModel(models.Model):
    # id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    enabled = models.BooleanField(default=True, verbose_name='active')

    class Meta:
        abstract = True
        ordering = ['-created_at']

    @property
    def time_since_create(self):
        return timesince(self.created_at).split(',')[0]

class User(BaseModel):
	user = models.ForeignKey(DefaultUser)
	phone = models.CharField(max_length=20)

	def __str__(self):
		return '%s <%s> - %s' % (self.user.get_full_name(), self.user.email, self.phone)

	@property
	def full_name(self):
		return self.user.get_full_name()

class Item_Priority(BaseModel):
	priority_name = models.CharField(max_length=20)

	def __str__(self):
		return self.priority_name

class Item_Category(BaseModel):
	category_name = models.CharField(max_length=40)

	def __str__(self):
		return self.category_name

class Item_Type(BaseModel):
	type_name = models.CharField(max_length=20)

	def __str__(self):
		return self.type_name


# GET RID OF BLANK, NULLS
class Item(BaseModel):
	user = models.ForeignKey(User,blank=True,null=True)
	item_name = models.CharField(max_length=100,blank=True,null=True)
	item_description = models.CharField(max_length=500,blank=True,null=True)
	item_latitude = models.FloatField(blank=True,null=True)
	item_longitude = models.FloatField(blank=True,null=True)
	item_priority = models.ForeignKey(Item_Priority, on_delete=models.CASCADE,blank=True,null=True)
	item_category = models.ForeignKey(Item_Category, on_delete=models.CASCADE,blank=True,null=True)
	item_type = models.ForeignKey(Item_Type, on_delete=models.CASCADE,blank=True,null=True)

	def __str__(self):
		return self.item_name

class Comment(BaseModel):
	user = models.ForeignKey(User)
	comment_text = models.CharField(max_length=500)
	item = models.ForeignKey(Item, on_delete=models.CASCADE)
