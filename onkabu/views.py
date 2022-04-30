from django.http import JsonResponse, HttpResponse
from django.views.generic.base import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import json

class Onkabu(View):

  def get(self, request):
    res = {
      'text': 'hello'
    }
    return JsonResponse(res)

  def post(self, request):
        json_str = request.body.decode('utf-8')
        json_data = json.loads(json_str)
        buy = json_data["buy"]
        now = json_data["now"]
        stocks = json_data["stocks"]
        onkabu = int(stocks - (now - buy) * 0.79685 / now * stocks)
        if onkabu < stocks:
            result = {
                'onkabu': str(onkabu) + '株売却してください'
            }
        else :
            result = {
                'onkabu': "恩株は作れません"
            }
        
        return JsonResponse(result)

  @csrf_exempt
  def dispatch(self, *args, **kwargs):
      return super(Onkabu, self).dispatch(*args, **kwargs)