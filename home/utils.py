from .models import *
from django.core.mail import send_mail
from django.conf import settings
import random


def send_email_to_user(user,email):
    subject = "Account Verification For Restoran User"
    random_num = random.randint(100000, 999999)
    str_num = str(random_num)
    message = "Your Otp for Restoran account verfication is " + str_num
    from_email = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject, message, from_email, recipient_list)
    link = otp.objects.create(otp_no=random_num, user=user)
    link.save()
    
