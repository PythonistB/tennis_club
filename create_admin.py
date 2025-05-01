from django.contrib.auth import get_user_model

User = get_user_model()

if not User.objects.filter(username="admin").exists():
    User.objects.create_superuser("Nazar1", "nazar@mail.ru", "1234")
    print("Superuser 'admin' created.")
else:
    print("Superuser 'admin' already exists.")
