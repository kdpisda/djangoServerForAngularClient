from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Profile model
class Profile(models.Model):
	STUDENT = 'STU'
	FACULTY = 'FAC'
	STAFF = 'STF'
	ALUMNI = 'ALU'
	PROFILE_TYPE = (
		(STUDENT, 'Student'),
		(FACULTY, 'Faculty'),
		(STAFF, 'Staff'),
		(ALUMNI, 'Alumni'),
	)
	profile_type = models.CharField(
		max_length=2,
		choices=PROFILE_TYPE,
		default=STUDENT,
	)
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	bio = models.TextField(max_length=500, blank=True)
	location = models.CharField(max_length=30, blank=True)
	birth_date = models.DateField(null=True, blank=True)
	def __str__(self):
		return str(self.user.first_name + " " + self.user.last_name)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
	if created:
		Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
	instance.profile.save()