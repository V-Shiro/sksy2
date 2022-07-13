from celery import shared_task
from multiprocessing import context
from firstapp.models import Cluster, Reservation, UserProfile, Users_reservations_dict
from firstapp import models
from firstapp.forms import *
from datetime import datetime, timedelta
from django.core.mail import send_mail


@shared_task(bind = True)
def send_msg(self):
    for i in range(9):
        print(i)
    return  "test"



@shared_task(bind = True)
def notify(self): 
    set_of_users_with_reservations = Users_reservations_dict.objects.all()

    for dt in set_of_users_with_reservations:
        if ((datetime.strptime(dt.reservation.date, '%Y-%m-%d').date()) == (datetime.today().date() + timedelta(days = 1))):
            first_name = dt.user
            last_name = ' '
            email = dt.user.email
            need =  "Friendly reminder. Tomorrow's Reservation :)" 
            message = 'Test profiler. Your reservation of ' + str(dt.reservation.clusterr.title) + ' for ' + str(dt.reservation.date) + " is soon. Don't forget your ID "  

            data = {
                'name': f'{first_name} {last_name}',
                'email': email,
                'need': need,
                'message': message,
            }

            message = '''
            Neue Nachricht: {}
            von: {}
            Thema: {}

            {}

            '''.format(data['name'], data['email'], data['need'], data['message'])

            send_mail(need, message, '', ['simpleslot101@gmail.com'],fail_silently=False)
        #     return 'success'
        # else: 
        #     return 'not matching'



@shared_task(bind = True)
def update_slots(self): 
    set_of_users_with_reservations = Users_reservations_dict.objects.all()

    for dt in set_of_users_with_reservations:
        if ((datetime.strptime(dt.reservation.date, '%Y-%m-%d').date()) < (datetime.today().date())):
            dt.delete()
        elif ((datetime.strptime(dt.reservation.date, '%Y-%m-%d').date()) == (datetime.today().date())):
            if len(dt.not_av_slots) == 0:
                dt.delete()
            else: 
                for sl in dt.not_av_slots:
                    sl_value = datetime.strptime(sl[-5:], '%H:%M').time()
                    if sl_value < datetime.now().time():
                        dt.not_av_slots.remove(sl)




