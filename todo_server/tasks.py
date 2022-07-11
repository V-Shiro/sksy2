from celery import shared_task

@shared_task(bind = True)
def send_msg(self):
    for i in range(9):
        print(i)
    return  "test"