from django.shortcuts import render
from django.http import JsonResponse
import re
from .models import SubscribedUsers
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.decorators import login_required


@login_required
def newsletter(request):
    """ Function to create newsletter for user  """

    if request.method == 'POST':
        try:
            subscribedUsers = SubscribedUsers.objects.get(user=request.user)
        except SubscribedUsers.DoesNotExist:
            subscribedUsers = SubscribedUsers()
        finally:
            post_data = request.POST.copy()
            email = post_data.get("email", None)
            name = post_data.get("name", None)
            subscribedUsers.email = email
            subscribedUsers.name = name
            subscribedUsers.user = request.user
            subscribedUsers.save()
            # send a confirmation mail
            subject = 'NewsLetter Subscription'
            message = 'Hello ' + name + \
                ', Thanks for subscribing us. You will get notification of latest articles posted on our website. Please do not reply on this email.'
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [email, ]
            send_mail(subject, message, email_from, recipient_list)
            res = JsonResponse({'msg': 'Thanks. Subscribed Successfully!'})
            return res

    return render(request, 'index.html')


def validate_email(request):
    """ Funcion to validate email """
    email = request.POST.get("email", None)
    try:
        if email is None:
            res = JsonResponse({'msg': 'Email is required.'})
        elif not re.match(r"^\w+([-+.']\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*$", email):
            res = JsonResponse({'msg': 'Invalid Email Address'})

        elif SubscribedUsers.objects.get(email=email):
            res = JsonResponse({'msg': 'Email Address already exists'})

        else:
            res = JsonResponse({'msg': ''})
    except SubscribedUsers.DoesNotExist:
        pass
    return res
