from .models import *
from django.core.mail import send_mail
from django.conf import settings
import random
from django.utils.html import format_html
from django.template import Context, Template

def send_email_to_user(user,email):
    subject = "Account Verification For Restoran User"
    random_num = random.randint(100000, 999999)
    str_num = str(random_num)
    t = Template("<a href='/verify/{{ message }}'>click here</a>")
    c = Context({'message': str_num})
    html = t.render(c)
    message = format_html("Please " + html + " to verify your account.")
    from_email = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject, message, from_email, recipient_list)
    link = verify_link.objects.create(rnd_no=random_num, user=user)
    