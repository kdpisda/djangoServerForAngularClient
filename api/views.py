from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from app_profile.models import Profile
from section.models import Achievement, Project, Activity, Team, Announcement
from decorators import controller_api

# Create your views here.
def switch_profile_type(arguement):
	switcher = {
		"STUDENTS" : "STU",
		"FACULTIES" : "FAC",
		"STAFF" : "STF",
		"ALUMNIES" : "ALU"
	}
	return switcher.get(arguement, False)

@controller_api
def profile(request, profile_type):
	req_profile_type = switch_profile_type(profile_type.upper())
	response = {}
	if type(req_profile_type) == str:
		if Profile.objects.filter(profile_type=req_profile_type).exists():
			temp_profiles = Profile.objects.filter(profile_type=req_profile_type)
			req_profiles = []
			req_profile = {}
			for temp_profile in temp_profiles:
				req_profile['name'] = str(temp_profile.user.first_name + " " + temp_profile.user.last_name)
				req_profile['email'] = temp_profile.user.email
				req_profile['bio'] = temp_profile.bio
				req_profile['avatar'] = str(temp_profile.avatar)
				req_profiles.append(req_profile)
				req_profile = {}
			response['success'] = True
			response['data'] = req_profiles
		else:
			response['success'] = False
			response['message'] = "Sorry the request query does not exists in our database"
	else:
		response['success'] = False
		response['message'] = "Sorry the requested query does not exists"
	return JsonResponse(response)

@controller_api
def achievements(request):
	response = {}
	if Achievement.objects.filter(status=True).exists():
		response['success'] = True
		req_achievements = []
		req_achievement = {}
		temp_achievements = Achievement.objects.filter(status=True)
		for temp_achievement in temp_achievements:
			req_achievement['user'] = {}
			req_achievement['user']['name'] = str(temp_achievement.profile.user.first_name + " " + temp_achievement.profile.user.last_name)
			req_achievement['user']['email'] = temp_achievement.profile.user.email
			req_achievement['user']['avatar'] = str(temp_achievement.profile.avatar)
			req_achievement['user']['bio'] = temp_achievement.profile.bio
			req_achievement['user']['user_type'] = temp_achievement.profile.profile_type
			req_achievement['description'] = temp_achievement.description
			req_achievement['meta'] = str(temp_achievement.meta)
			req_achievement['date'] = temp_achievement.date
			req_achievements.append(req_achievement)
			req_achievement = {}
		response['data'] = req_achievements
	else:
		response['success'] = False
		response['message'] = "Sorry the requested query does not exists on the database"
	return JsonResponse(response)

@controller_api
def projects(request):
	response = {}
	if Project.objects.filter(status=True).exists():
		response['success'] = True
		req_projects = []
		req_project = {}
		temp_projects = Project.objects.filter(status=True)
		for temp_project in temp_projects:
			req_project['user'] = {}
			req_project['user']['name'] = str(temp_project.profile.user.first_name + " " + temp_project.profile.user.last_name)
			req_project['user']['email'] = temp_project.profile.user.email
			req_project['user']['avatar'] = str(temp_project.profile.avatar)
			req_project['user']['bio'] = temp_project.profile.bio
			req_project['user']['user_type'] = temp_project.profile.profile_type
			req_project['description'] = temp_project.description
			req_project['meta'] = str(temp_project.meta)
			req_project['document'] = str(temp_project.document)
			req_project['start_date'] = temp_project.start_date
			req_project['end_date'] = temp_project.end_date
			req_project['ongoing'] = temp_project.ongoing
			req_projects.append(req_project)
			req_project = {}
		response['data'] = req_projects
	else:
		response['success'] = False
		response['message'] = "Sorry the requested query does not exists on the database"
	return JsonResponse(response)

@controller_api
def activities(request):
	response = {}
	if Activity.objects.filter(status=True).exists():
		response['success'] = True
		temp_activities = Activity.objects.filter(status=True)
		req_activities = []
		req_activity = {}
		for temp_activity in temp_activities:
			req_activity['title'] = temp_activity.title
			req_activity['date'] = temp_activity.date
			req_activity['description'] = temp_activity.description
			req_activity['link'] = temp_activity.link
			req_activities.append(req_activity)
			req_activity = {}
		response['data'] = req_activities
	else:
		response['success'] = False
		response['message'] = "Sorry the requested query does not exists on the database"
	return JsonResponse(response)

@controller_api
def team(request):
	response = {}
	if Team.objects.filter(status=True).exists():
		response['success'] = True
		temp_team_members = Team.objects.filter(status=True)
		req_team_members = []
		req_team_member = {}
		for temp_team_member in temp_team_members:
			req_team_member['user'] = {}
			req_team_member['user']['name'] = str(temp_team_member.profile.user.first_name + " " + temp_team_member.profile.user.last_name)
			req_team_member['user']['email'] = temp_team_member.profile.user.email
			req_team_member['user']['avatar'] = str(temp_team_member.profile.avatar)
			req_team_member['user']['bio'] = temp_team_member.profile.bio
			req_team_member['user']['user_type'] = temp_team_member.profile.profile_type
			req_team_member['position'] = temp_team_member.position
			req_team_members.append(req_team_member)
			req_team_member = {}
		response['data'] = req_team_members
	else:
		response['success'] = True
		response['message'] = "Sorry the requested query does not exists on the database"
	return JsonResponse(response)

@controller_api
def announcements(request):
	response = {}
	if Announcement.objects.filter(status=True).exists():
		response['success'] = True
		temp_announcements = Announcement.objects.filter(status=True)
		req_announcements = []
		req_announcement = {}
		for temp_announcement in temp_announcements:
			req_announcement['title'] = temp_announcement.title
			req_announcement['date'] = temp_announcement.date
			req_announcement['description'] = temp_announcement.description
			req_announcement['link'] = temp_announcement.link
			req_announcements.append(req_announcement)
			req_announcement = {}
		response['data'] = req_announcements
	else:
		response['success'] = False
		response['message'] = "Sorry the requested query does not exists on the database"
	return JsonResponse(response)