import string
from django.contrib.auth.models import User
from django.utils.crypto import get_random_string
from celery import shared_tesk

@shared_tesk
def create_random_user_acount(total):
    for i in range(total):
        username='user_{}'.format(get_random_string(10,string.ascii_letters))
        email='{}@gmail.com'.format(username)
        password=get_random_string(50)
        User.objects.create_user(username=username,email=email,password=password)
    return '{}random user create with success'.format.(total)