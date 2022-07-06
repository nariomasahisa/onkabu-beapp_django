from email.quoprimime import body_check
from logging.config import fileConfig
import math
from tokenize import Number
from urllib import response
from django.http import JsonResponse
from django.views.generic.base import View
from django.views.decorators.csrf import csrf_exempt
import json
from logging import getLogger


logger = getLogger(__name__)
class CalcValue(View):

  def post(self, request):
    json_str = request.body.decode('utf-8')
    data = json.loads(json_str)
    profit = data['profit']
    invest = data['invest']
    depreciation = data['depreciation']
    roic = data['roic'] / 100
    buy_price = data['buyPrice']
    wacc = 0.1
    over_return = roic - wacc

    def calcPV(profit):
      pv = 0
      for i in range(10):
        pv = pv + profit / (1 + wacc) ** i
        i += 1
      pv += (profit / wacc) / (1 + wacc) ** 10
      pv = math.floor(pv)
      return pv
        
    fcf = profit + depreciation - invest
    pv = calcPV(fcf)
    over_pv = calcPV(fcf * (over_return / roic))
    cost = calcPV(fcf * (wacc / roic))


    response = {
      "pv": pv,
      "over_pv": over_pv,
      "cost_pv": cost
    }
    return JsonResponse(response)

  @csrf_exempt
  def dispatch(self, *args, **kwargs):
      return super(CalcValue, self).dispatch(*args, **kwargs)