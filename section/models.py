from django.db import models
from app_profile.models import Profile
import datetime

# Create your models here.
class Achievement(models.Model):
	profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
	description = models.TextField(max_length=256)
	meta = models.ImageField(upload_to='static/uploads/achievements', null=True, blank=True)
	date = models.DateField()
	status = models.BooleanField(default=False)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	def __str__(self):
		return str(self.profile.user.first_name + " " + self.profile.user.last_name + " => " + str(self.date))

class Project(models.Model):
	profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
	description = models.TextField(max_length=512)
	meta = models.ImageField(upload_to='static/uploads/projects/images', null=True, blank=True)
	document = models.FileField(upload_to='static/uploads/projects/documents', null=True, blank=True)
	status = models.BooleanField(default=False)
	start_date = models.DateField(null=False, blank=False)
	end_date = models.DateField(null=True, blank=True)
	ongoing = models.BooleanField(default=False)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	def save(self, *args, **kwargs):
		if self.ongoing:
			self.end_date = None
		elif self.end_date == None:
			self.end_date = self.start_date
		super(Project, self).save(*args, **kwargs)

	def __str__(self):
		return str(self.profile.user.first_name + " " + self.profile.user.last_name + " => " + str(self.start_date))

class Activity(models.Model):
	date = models.DateField()
	title = models.TextField(max_length=32)
	description = models.TextField(max_length=256)
	link = models.TextField(max_length=32)
	status = models.BooleanField(default=False)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	class Meta:
		verbose_name_plural = "Activities"

	def __str__(self):
		return self.title

class Team(models.Model):
	CONVENER = 'CON'
	COCONVENER = 'COC'
	TREASERER = 'TRE'
	WEB = 'WEB'
	TECH = 'TEC'
	DOC = 'DOC'
	DESIGN = 'DSG'
	RND = 'RND'
	EXECUTIVE = "EXE"
	TEAM_POSITIONS = (
		(CONVENER, 'Convener'),
		(COCONVENER, 'Co-Convener'),
		(TREASERER, 'Treaserer'),
		(WEB, 'Web Team'),
		(TECH, 'Tech Team'),
		(DOC, 'Documentation Team'),
		(DESIGN, 'Design Team'),
		(RND, 'Research and Development Team'),
		(EXECUTIVE, 'Executive')
	)
	position = models.CharField(
		max_length=3,
		choices=TEAM_POSITIONS,
		default=EXECUTIVE,
	)
	profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
	status = models.BooleanField(default=False)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	def __str__(self):
		return str(self.position + " => " + self.profile.user.first_name + " " + self.profile.user.last_name)

class Announcement(models.Model):
	date = models.DateField()
	title = models.TextField(max_length=32)
	description = models.TextField(max_length=256)
	meta = models.ImageField(upload_to='static/uploads/announcements', null=True, blank=True)
	link = models.TextField(max_length=32)
	status = models.BooleanField(default=False)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.title