# from apscheduler.schedulers.background import BackgroundScheduler
# from django_apscheduler.jobstores import DjangoJobStore, register_events, register_job
# from django.core.mail import send_mail
# from datetime import datetime
# from django.contrib.auth.models import User
# from .models import Todo
# import os

# def count_own_and_participant_todos(author_id):
#     today_date = datetime.now().date()
#     todos = Todo.objects.filter(date=today_date)
#     own_todos = todos.filter(author_id=author_id).count()
#     participated_todos = todos.filter(participants__id=author_id).count()
#     return today_date, own_todos, participated_todos

# def send_emails_to_authors():
#     authors = User.objects.all()
#     for author in authors:
#         today_date, own_todos, participated_todos = count_own_and_participant_todos(author.id)
#         email_content = f"Date: {today_date.strftime('%Y/%m/%d')}\nTasks: {own_todos}\nParticipants: {participated_todos}\n"
#         send_mail(
#             'Daily Task Summary',
#             email_content,
#             os.getenv('SENDING_EMAIL'),
#             [author.email],
#             fail_silently=False,
#         )

# scheduler = BackgroundScheduler()
# scheduler.add_jobstore(DjangoJobStore(), "default")

# @register_job(scheduler, "cron", hour=0)
# def scheduled_email_task():
#     send_emails_to_authors()

# # 測試用
# # @register_job(scheduler, "interval", minutes=1, id=datetime.now().strftime("%Y%m%d%H%M%S"))
# # def scheduled_email_task():
# #     send_emails_to_authors()

# register_events(scheduler)
# scheduler.start()