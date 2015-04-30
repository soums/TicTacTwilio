from django.shortcuts import render

from django.http import HttpResponse

from twilio.rest import TwilioRestClient

from games.models import Game

from django.views.decorators.csrf import csrf_exempt

# Find these values at https://twilio.com/user/account
account_sid = "AC81adf97947a3e8c71fdc2dd3d2908489"
auth_token = "dff764d671f4a45b5a1f74eb0cda3d76"
client = TwilioRestClient(account_sid, auth_token)

def index(request):
    
	# Create your views here.
	# Download the twilio-python library from http://twilio.com/docs/libraries
	invite("+16507144442", "+3302890947")
	
	return HttpResponse("Welcome to TicTacTwilio!")

@csrf_exempt
def message(request):
	print request.POST

	return HttpResponse("Message doesn't work")


def invite(hometeam,awayteam): 
	
	game=Game(player_1=hometeam, player_2=awayteam)
	game.save()

	message = client.messages.create(to=hometeam, from_="+16502156107",
		body="Your game has started. Make your first move...")
