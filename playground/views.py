# from django.core.mail import BadHeaderError
from django.core.cache import cache
from django.shortcuts import render
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from rest_framework.views import APIView
import requests
# from templated_mail.mail import BaseEmailMessage
# for CELERY
# from .tasks import notify_customers

# cache decorator
# @cache_page(5*60)
# def say_hello(request):
    # try:
    #     message = BaseEmailMessage(
    #         template_name='emails/hello.html',
    #         context= {'name': 'Vibhu'}
    #     )
    #     message.send(['vibhu.ug20@nsut.ac.in'])
    # except BadHeaderError:
    #     pass
    # notify_customers.delay('Hello')
    # below server will first make a delay of 2 secs after that the data loads
    
    # response = requests.get('https://httpbin.org/delay/2')
    # data = response.json()
    # return render(request, 'hello.html', {'name': data})


# trying caching on the class based views
class HelloView(APIView):
    @method_decorator(cache_page(5*60))
    def get(self, request):
        response = requests.get('https://httpbin.org/delay/2')
        data = response.json()
        return render(request, 'hello.html', {'name': data})
        
