from celery import shared_task
from django.utils import timezone
from datetime import timedelta
from .models import CarApplication
from django.core.mail import send_mail

@shared_task
def delete_old_car_applications():
    threshold_date = timezone.now() - timedelta(days=30)
    old_applications = CarApplication.objects.filter(created_at__lt=threshold_date)
    deleted_count = 0

    for app in old_applications:
        user_email = app.user.email
        car_info = f"{app.car_brand} {app.car_model} ({app.car_year})"
        app.delete()
        deleted_count += 1

        send_mail(
            subject="Ваша заявка была удалена",
            message=f"Ваша заявка на {car_info} была удалена, так как прошло 30 дней.",
            from_email=None,
            recipient_list=[user_email],
        )

    return f"Deleted {deleted_count} old CarApplication(s)"
