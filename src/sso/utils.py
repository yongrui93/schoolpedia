from django.core.mail import send_mail as django_send_email


def send_email(email_to, subject, body):
    django_send_email(
        subject=subject,
        message=body,
        from_email='schoolpediacz2006@gmail.com',
        recipient_list=[email_to],
        html_message=body,
        fail_silently=False,
    )
    return True
