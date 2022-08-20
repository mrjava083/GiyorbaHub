from django.db import models
from account.models import User 
from froala_editor.fields import FroalaField
# Create your models here.

class Roman(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="کاربر")
	title = models.CharField(max_length=200, verbose_name="عنوان رمان")	
	slug = models.SlugField(max_length=200,unique=True ,verbose_name="نشانی")
	body = models.TextField(verbose_name="متن رمان")
	vote = models.BigIntegerField(default=0,verbose_name="ویو")

	class Meta:
		verbose_name = "زمان"
		verbose_name_plural = "رمان ها"

	def __str__(self):
		return "کاربر  : {} | عنوان رمان : {}".format(self.user, self.title)
