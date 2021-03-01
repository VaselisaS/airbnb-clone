from django.views.generic import ListView, DetailView
from . import models


class HomeView(ListView):

    """HomeView Definition"""

    model = models.Room
    paginate_by = 10
    ordering = "created"


class RoomView(DetailView):

    """RoomView Definition"""

    model = models.Room
