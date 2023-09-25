from django.db import models
from django.conf import settings
# Create your models here.

USER = settings.AUTH_USER_MODEL


class Room(models.Model):
	name = models.CharField(max_length=30,null=False,blank=False)
	layer = models.CharField(max_length=300)
	admin = models.ForeignKey(USER,on_delete=models.CASCADE)
	created_at = models.DateTimeField(auto_now_add=True)
	modified_at = models.DateTimeField(auto_now=True)
	active = models.BooleanField(default=True)


class ActiveUser(models.Model):
	room = models.ForeignKey(Room,on_delete=models.CASCADE)
	user = models.ManyToManyField(USER)

	def get_count_of_active_user(self):
		return self.user.count()

	def get_queryset_of_active_user(self,exclude_user=None):
		if exclude_user:
			return [{'username':user.username,'id':user.id} for user in self.user.all() if user.id!=exclude_user.id ]
		return [ user for user in self.user.all().values('username','id') ]




class TextMessage(models.Model):
	room = models.ForeignKey(Room,on_delete=models.CASCADE,null=True)
	text = models.CharField(max_length=30,null=True)
	sender = models.ForeignKey(USER,on_delete=models.CASCADE, related_name="sender")
	receiver = models.ForeignKey(USER,on_delete=models.CASCADE, related_name="receiver")
	datetime = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.text

	#class Meta:
		#unique_together = [['text','datetime'],]
		# constraints = [
        # 	models.UniqueConstraint(fields=['text','datetime'], name='unique appversion')
    	# ]





