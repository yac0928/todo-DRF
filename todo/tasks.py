from apscheduler.schedulers.background import BackgroundScheduler
from django_apscheduler.jobstores import DjangoJobStore, register_events, register_job
from django.core.mail import send_mail
from datetime import datetime
from django.contrib.auth.models import User
from .models import Todo
import os
import pytz

def count_own_and_participant_todos(author_id):
    today_date = datetime.now().date()
    todos = Todo.objects.filter(date=today_date)
    own_todos = todos.filter(author_id=author_id).count()
    participated_todos = todos.filter(participants__id=author_id).count()
    return today_date, own_todos, participated_todos

def send_emails_to_authors():
    authors = User.objects.all()
    for author in authors:
        today_date, own_todos, participated_todos = count_own_and_participant_todos(author.id)
        email_content = f"Date: {today_date.strftime('%Y/%m/%d')}\nTasks: {own_todos}\nParticipants: {participated_todos}\n"
        send_mail(
            'Daily Task Summary',
            email_content,
            os.getenv('SENDING_EMAIL'),
            [author.email],
            fail_silently=False,
        )
timezone = pytz.timezone('Asia/Taipei')

scheduler = BackgroundScheduler(timezone=timezone)
scheduler.add_jobstore(DjangoJobStore(), "default")

@register_job(scheduler, "cron", hour=23, minute=5, id=datetime.now().strftime("%Y%m%d%H%M%S"))
def scheduled_email_task():
    now = datetime.now()
    print(f"Scheduled email task executed at {now}")
    send_emails_to_authors()

register_events(scheduler)
scheduler.start()