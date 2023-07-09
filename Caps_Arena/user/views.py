from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
import json
from .models import user
import datetime

def user_create(request):
    if request.method == "GET":
        user_id = request.GET.get("user_id")
        user_name = request.GET.get("user_name")
        photo_url = request.GET.get("photo_url")
        if user_name and user_id and photo_url:
            selected_user = user.objects.all().filter(user_id=user_id).exists()
            if not selected_user:
                us = user.objects.create(user_id=user_id, 
                                    user_name=user_name,
                                    photo_url=photo_url,
                                    date_of_login=datetime.datetime.now())
                us.save()
                return JsonResponse({"status" : True, "do" : "created"})
            else: return JsonResponse({"status" : True, "do" : "exist"})
        elif not user_id: return JsonResponse({"status" : False, "error" : "The user_id parameter was not specified in the request"})
        elif not user_name == None: return JsonResponse({"status" : False, "error" : "The user_name parameter was not specified in the request"})
        elif not photo_url == None: return JsonResponse({"status" : False, "error" : "The photo_url parameter was not specified in the request"})
        else: return JsonResponse({"status" : False, "error" : "An unexpected error has occurred"})
    else: return JsonResponse({"status" : False, "error" : "This is a GET request"})