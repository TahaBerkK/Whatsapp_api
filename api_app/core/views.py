from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponse
import json
import requests


@csrf_exempt
def webhook(request):
    if request.method == 'GET':
        verify_token = 'YOUR_VERIFY_TOKEN'
        hub_mode = request.GET.get('hub.mode')
        hub_challenge = request.GET.get('hub.challenge')
        hub_verify_token = request.GET.get('hub.verify_token')

        if hub_mode == 'subscribe' and hub_verify_token == verify_token:
            return HttpResponse(hub_challenge)
        return HttpResponse('Verification token mismatch', status=403)

    if request.method == 'POST':
        data = json.loads(request.body)
        # Process the incoming data
        print(data)  # For debugging purposes
        # Add your logic here to handle different types of events
        return JsonResponse({"status": "received"}, status=200)

    return JsonResponse({"status": "bad request"}, status=400)

def send_text(request, to, text):
    api = "EAAV3yOYZCYRsBOy9zWIZBZAEefLud2ZAMT1DRL3xEvNgfurldoYiNnPy64vwjam2iOrSJtoNNZBZCv4JYbENVzlip6OTt23XlrhCgZCUoPtUd9qHxudLwIGdjwDoYF8G6GnLcQWZCNE5BAmE1VNvuC4VyKy0znbuPhNZBnpVIUBpddSWKTKUZCDtZBPIFc5dkDOLLvYq9eiyhAiXOcTecg1Bo0ZD"
    phone_id = "367538839783725"
    url = f"https://graph.facebook.com/v20.0/{phone_id}/messages"

    head ={
        "Authorization": f"Bearer {api}",
        "Content-Type": "application/json",
    }
    data = {
        "messaging_product": "whatsapp",
        "to": to,
        "type": "text",
        "text": {
            "body": text
        }
    }
    response = requests.post(url, headers=head, data=json.dumps(data))
    return response.json()

# Create your views here.
