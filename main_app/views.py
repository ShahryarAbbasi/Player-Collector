from django.shortcuts import render
from django.views import View # <- View class to handle requests
from django.http import HttpResponse # <- a class to handle sending a type of response
from django.views.generic.base import TemplateView
# import models
from .models import Player
# Create your views here.
class Home(TemplateView):
    template_name = "home.html"

#...
#...
class About(TemplateView):
    template_name = "about.html"

class Player:
    def __init__(self, name, image, bio):
        self.name = name
        self.image = image
        self.bio = bio

players = [
  Player("Kyrie Irving", "https://s22928.pcdn.co/wp-content/uploads/2022/07/Kyrie-Irving-1.jpg",
          "Kyrie Irving is one of the most skilled players of all time and has a championship on his resume"),
  Player("Lebron James",
          "https://gray-kvvu-prod.cdn.arcpublishing.com/resizer/qIq9w62uoS_708GI4yQ5uWYechs=/1200x675/smart/filters:quality(85)/cloudfront-us-east-1.images.arcpublishing.com/gray/VPMKBLA6VFB53DDAWLN4DZGBPM.jpg", "One of the best basketball players of all time, virtually nothing is missing from his resume"),
  Player("Derrick Rose", "https://cdn.nba.com/manage/2018/10/derrick-rose-mvp-2011.jpg",
          "The youngest MVP of all time, one of the biggest what-ifs in the NBA due to getting injured very early in his career."),
  Player("Kevin Durant",
          "https://a.espncdn.com/photo/2022/0504/r1008244_1296x729_16-9.jpg", "One of the greatest scorers and talent this world will ever see, a very under appriciated superstar."),
  Player("Kobe Bryant",
          "https://media.vanityfair.com/photos/5e2e3af23f3d910008fc55c0/master/pass/remembering-kobe-bryant.jpg", "RIP Mamba, one of the best of all time, the closest to Michael Jordan we will ever see."),
  Player("Steph Curry",
          "https://www.si.com/.image/ar_16:9%2Cc_fill%2Ccs_srgb%2Cfl_progressive%2Cg_faces:center%2Cq_auto:good%2Cw_768/MTkyNzUzOTg3MDY0MTc3Njkz/14022232290.jpg", "Changed the game with his 3 point shooting ability, is one of the best players of all time and still adding to his already impressive resume."),
]

class PlayerList(TemplateView):
    template_name = "player_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["players"] = Player.objects.all() # this is where we add the key into our context object for the view to use
        return context
