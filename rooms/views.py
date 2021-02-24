from django.shortcuts import render, redirect
from django.core.paginator import Paginator, EmptyPage
from . import models


def all_rooms(request):
    rooms = models.Room.objects.all()
    paginator = Paginator(object_list=rooms, per_page=10)
    page_number = int(request.GET.get("page", 1))
    try:
        page_obj = paginator.page(page_number)
        return render(
            request, "rooms/all_rooms.html", context={"page": page_obj}
        )
    except EmptyPage:
        return redirect("/")
