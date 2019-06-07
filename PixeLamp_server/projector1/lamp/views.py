import json
from django.shortcuts import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import On_Off, Bright, Rotations, Up_down
from dialogflow_lite.dialogflow import Dialogflow
import time
from pygame import mixer
import motor, servo, light

def convert(data):
    if isinstance(data, bytes):
        return data.decode('ascii')
    if isinstance(data, dict):
        return dict(map(convert, data.items()))
    if isinstance(data, tuple):
        return map(convert, data)

    return data


@csrf_exempt
def view_store(request):
    client_access_token = '0bb7a3b7450f4159a441699a80ed6ade'
    dialogflow = Dialogflow(client_access_token=client_access_token)
    input_dict = convert(request.body)
    action = json.loads(input_dict)['queryResult']['action']
    parameters = json.loads(input_dict)['queryResult']['parameters']
    if request.method == "POST":
        
        if (action == 'goodnight'):
            Text = json.loads(input_dict)['queryResult']['fulfillmentMessages'][0]['text']['text'][0]
            Answer = json.loads(input_dict)['queryResult']['fulfillmentMessages']
            ans = parameters['agree']
            if ans == 'yes':
                mixer.init()
                mixer.music.load('/home/pi/Downloads/lalluby.mp3')
                mixer.music.play()
                
        if (action == 'stop_music'):
            Text = json.loads(input_dict)['queryResult']['fulfillmentMessages'][0]['text']['text'][0]
            Answer = json.loads(input_dict)['queryResult']['fulfillmentMessages']
            mixer.music.stop()
        
        if (action == 'rotation'):
            Text = json.loads(input_dict)['queryResult']['fulfillmentMessages'][0]['text']['text'][0]
            Answer = json.loads(input_dict)['queryResult']['fulfillmentMessages']
        
        if (action == 'brightness'):
            Text = json.loads(input_dict)['queryResult']['fulfillmentMessages'][0]['text']['text'][0]
            Answer = json.loads(input_dict)['queryResult']['fulfillmentMessages']
            
            if (parameters['temp'] == 'cold'):
                color = 100
            if (parameters['temp'] == 'warm'):
                color = 100
                
            bright = parameters['bright']
            print('Light')
            light.writeNumber(color, bright)
        
        if (action == 'up_down'):
            Text = json.loads(input_dict)['queryResult']['fulfillmentMessages'][0]['text']['text'][0]
            Answer = json.loads(input_dict)['queryResult']['fulfillmentMessages']
            if parameters['up_down'] == 'up':
                angle = parameters['value']
            if parameters['up_down'] == 'down':
                angle = -1 * parameters['value']
            servo.SetAngle(angle)
            
    data = {'fulfillmentText': Text, 'fulfillmentMessages': Answer}
    return HttpResponse(json.dumps(data))
    
@csrf_exempt
def android(request):
    up_down = dict(request.POST)
    print(up_down)
    result = {'status': 'ok', 'switch_state': up_down}
    temp = up_down['switch_state'][0] 
    if temp == '4':
        motor.motor_move(-100, 0)
        print('left')
    if temp == '3':
        motor.motor_move(100, 0)
        print('right')
    if temp == '2':
        motor.motor_move(0, 100)
        print('forward')
    if temp == '1':
        motor.motor_move(0, -100)
        print('backward')
    if temp == '0':
        motor.motor_move(0, 0)
        print('stop')
    return HttpResponse(json.dumps(result))

