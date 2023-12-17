
from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from django.http import JsonResponse
from django.http import HttpRequest
import requests



# Create your views here.

###def ticketmaster(request: HttpRequest):
def ticketmaster(request):

    if request.method == 'GET':
        return HttpResponse("The request method was GET")
    
    if request.method == 'POST':
        events = request.POST['events']
        city = request.POST['city']

        #### Some default
        # events = 'Dance'
        # city = 'Chicago'
        # total_events = get_events('Dance','Chicago')
        ## total_events = get_events(events,city)
        apikey = 'OFYGvXGLUFanaijTT1jpItQsJ5Ayf3c8'
        url = "https://app.ticketmaster.com/discovery/v2/events.json"
        params = {
            "classificationName": events,
            "city": city,
            "sort": "date,asc",
            "apikey": apikey
        }
        ### response = requests.get(url, params=params)
        ### response = requests.post(url, params=params)
        ### response = requests.get('https://app.ticketmaster.com/discovery/v2/events.json?apikey=OFYGvXGLUFanaijTT1jpItQsJ5Ayf3c8')
        ### response = requests.get('https://app.ticketmaster.com/discovery/v2/events.json?apikey=OFYGvXGLUFanaijTT1jpItQsJ5Ayf3c8' , params=params)

        # print(request)
        # return JsonResponse({"value": request })


        ### response = requests.get(url, params=params) ############# get or post???
        response = requests.get(url, params=params)
        ### response = requests.get(url, params=params)

        
        total_events = response.json()
        event_list = []

        for event in total_events['_embedded']['events']:
            event_name = event['name']
            ticket_link = event['url']
            event_id = event['id']
            image_url = event['images'[0]['url']]
            venue_name = event['_embedded']['venues'][0]['name']
            venue_address = event['_embedded']['venues'][0]['address']['line1']
            venue_city = event['_embedded']['venues'][0]['city']['name']
            venue_state = event['_embedded']['venues'][0]['state']['name']
            event_datetime = event['dates']['start']['dateTime']
            event_item = {
                'eventName': event_name,
                'ticketLink': ticket_link,
                'eventID': event_id,
                'imageUrl': image_url,
                'venueName': venue_name,
                'venueAddress': venue_address,
                'venueCity': venue_city,
                'venueState': venue_state,
                'eventDate': event_datetime,
                'eventTime': event_datetime,
            }
            event_list.append(event_item)
            
        context = {'events': event_list}
        return render(request, 'ticketmaster.html', context)
