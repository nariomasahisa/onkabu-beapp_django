import base64
from urllib import response
from django.http import JsonResponse
from django.views.generic.base import View
from django.views.decorators.csrf import csrf_exempt
import os
import json
import boto3
import environ

class CalcValue(View):

  def post(self, request):
      # 環境の設定など
      env = environ.Env()
      env.read_env('../.env')
      access_key= env('AWS_ACCESS_KEY_ID')
      secret_key=env('AWS_SECRET_ACCESS_KEY')
      lambda_client = boto3.client(
        'lambda',
        aws_access_key_id=access_key,
        aws_secret_access_key=secret_key
      )
      # データについて
      json_str = request.body.decode('utf-8')
      b = json.dumps(json_str).encode("utf-8")
      ClientContext = base64.b64encode(b).decode('utf-8')

      response = lambda_client.invoke(
        FunctionName=env('LAMBDA_FUNCTION'),
        InvocationType='Event',
        LogType='None',
        ClientContext=ClientContext,
        Payload=json_str
      )
      print('---------------------------')
      print(response['Payload'].read().decode('utf-8'))
      print('---------------------------')
      return response['Payload'].read()


  @csrf_exempt
  def dispatch(self, *args, **kwargs):
      return super(CalcValue, self).dispatch(*args, **kwargs)