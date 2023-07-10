from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from .models import chip_type, chip, case
from random import randint
from user.models import user

def create_new_chip(request):
    if request.method == "GET":
        chip_id = request.GET.get("chip_id")
        chip_name = request.GET.get("chip_name")
        chip_ico = request.GET.get("chip_ico")
        can_drop = request.GET.get("can_drop")
        if chip_id and chip_name and chip_ico and can_drop:
            exist_chip = chip_type.objects.all().filter(chip_id=chip_id).exists()
            if not exist_chip:
                chip_s = chip_type.objects.create(chip_id=chip_id, 
                                    chip_name=chip_name,
                                    chip_ico=chip_ico,
                                    can_drop=can_drop)
                chip_s.save()
                return JsonResponse({"status" : True, "do" : "created"}) 
            else: return JsonResponse({"status" : False, "error" : f"chip_id: {chip_id} already exists"})
        elif not chip_id: return JsonResponse({"status" : False, "error" : "The chip_id parameter was not specified in the request"})
        elif not chip_name: return JsonResponse({"status" : False, "error" : "The chip_name parameter was not specified in the request"})
        elif not chip_ico: return JsonResponse({"status" : False, "error" : "The chip_ico parameter was not specified in the request"})
        elif not can_drop: return JsonResponse({"status" : False, "error" : "The can_drop parameter was not specified in the request"})
        else: return JsonResponse({"status" : False, "error" : "An unexpected error has occurred"})
    else: return JsonResponse({"status" : False, "error" : "This is a GET request"})
    
def register_chip(request):
    if request.method == "GET":
        user_id = request.GET.get("user_id")
        chip_id = request.GET.get("chip_id")
        way = request.GET.get("way")
        if user_id and chip_id:
            if not way:
                way = "Получена потём контрактов"
            new_chip = chip.objects.create(
                user_id = user_id,
                chip_id = chip_id,
                way = way
            )
            new_chip.save()
            return JsonResponse({"status" : True, "do" : "created"}) 
        elif not user_id: return JsonResponse({"status" : False, "error" : "The user_id parameter was not specified in the request"})
        elif not chip_id: return JsonResponse({"status" : False, "error" : "The chip_id parameter was not specified in the request"})
        else: return JsonResponse({"status" : False, "error" : "An unexpected error has occurred"})
    else: return JsonResponse({"status" : False, "error" : "This is a GET request"})

def add_case(request):
    if request.method == "GET":
        case_name = request.GET.get("case_name")
        case_drop = request.GET.get("case_drop")
        if case_name and case_drop:
            exist_case = case.objects.all().filter(case_name=case_name).exists()
            if not exist_case:
                new_case = case.objects.create(
                    case_name = case_name,
                    case_drop = case_drop
                )
                new_case.save()
                return JsonResponse({"status" : True, "do" : "created"}) 
            else: return JsonResponse({"status" : False, "error" : f"case_name: {case_name} already exists"})
        elif not case_name: return JsonResponse({"status" : False, "error" : "The case_name parameter was not specified in the request"})
        elif not case_drop: return JsonResponse({"status" : False, "error" : "The case_drop parameter was not specified in the request"})
        else: return JsonResponse({"status" : False, "error" : "An unexpected error has occurred"})
    else: return JsonResponse({"status" : False, "error" : "This is a GET request"})
    
def open_case(request):
    if request.method == "GET":
        user_id = request.GET.get("user_id")
        case_name = request.GET.get("case_name")
        if user_id and case_name:
            if case.objects.all().filter(case_name=case_name).exists():
                selected_case = case.objects.filter(case_name=case_name)[0]
                can_drop = []
                for item in list(map(str, selected_case.case_drop.split(";"))):
                    can_drop.append(item)
                drop = can_drop[randint(0, len(can_drop))]
                new_chip = chip.objects.create(
                    user_id = user_id,
                    chip_id = drop,
                    way = f"Открытие кейса {case_name}"
                )
                new_chip.save()
                return JsonResponse({"status" : True, "drop" : drop, "img_url" : chip_type.objects.filter(chip_id=drop)[0].chip_ico}) 
            else: return JsonResponse({"status" : False, "error" : f"case_name: {case_name} is not exists"})
        elif not user_id: return JsonResponse({"status" : False, "error" : "The user_id parameter was not specified in the request"})
        elif not case_name: return JsonResponse({"status" : False, "error" : "The case_name parameter was not specified in the request"})
        else: return JsonResponse({"status" : False, "error" : "An unexpected error has occurred"})
    else: return JsonResponse({"status" : False, "error" : "This is a GET request"})
    
def get_inventory(request):
    if request.method == "GET":
        user_id = request.GET.get("user_id")
        if user_id:
            if user.objects.all().filter(user_id=user_id).exists():
                chip_list = chip.objects.all().filter(user_id=user_id)
                inventory = []
                for chipp in chip_list:
                    inventory.append(chip_type.objects.all().filter(chip_id=chipp.chip_id)[0].chip_name)
                return JsonResponse({"status" : True, "inventory" : inventory})
            else: return JsonResponse({"status" : False, "error" : f"user_id: {user_id} is not exists"})
        elif not user_id: return JsonResponse({"status" : False, "error" : "The user_id parameter was not specified in the request"})
        else: return JsonResponse({"status" : False, "error" : "An unexpected error has occurred"})
    else: return JsonResponse({"status" : False, "error" : "This is a GET request"})