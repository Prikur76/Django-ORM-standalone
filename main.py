import os

import django
from django.utils.timezone import localtime
from datetime import datetime, timedelta


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
django.setup()

from datacenter.models import Passcard, Visit  # noqa: E402

if __name__ == '__main__':
    # Программируем здесь
    # print('Количество пропусков:', Passcard.objects.count())  # noqa: T001
    # passcards = Passcard.objects.all()
    passcode = 'ceb148a6-fb27-4106-890c-89dc8cedfe83'
    passcard = Passcard.objects.get(passcode=passcode)
    print(passcard.id)

    # print(f"owner_name: {passcards[10].owner_name}")
    # print(f"passcode: {passcards[10].passcode}")
    # print(f"created_at: {passcards[10].created_at}")
    # print(f"is_active: {passcards[10].is_active}")

    # active_passcards = []
    # for passcard in passcards:
    #     if passcard.is_active:
    #         active_passcards.append(passcard)

    # active_passcards = Passcard.objects.filter(is_active=True)
    # print('Активных пропусков: ', len(active_passcards))
    # visits = Visit.objects.filter(passcard__id=10)
    # print(visits)
    # for visit in visits:
    #     visit_entered = localtime(visit.entered_at)
    #     duration = localtime() - visit_entered
    #     # if visit.leaved_at:
    #     #     duration = str(localtime(visit.leaved_at) - visit_entered)
    #     days, seconds = duration.days, duration.seconds
    #     hours = days * 24 + seconds // 3600
    #     minutes = (seconds % 3600) // 60
    #     seconds = (seconds % 60)
    #     owner_name = Visit.objects.get(id=visit.id).passcard.owner_name
    #
    #
    #     print(f"Посетитель: {owner_name}"
    #           "\nЗашёл в хранилище, время по Москве:\n"
    #           f"{visit_entered}\n"
    #           f"Покинул: {visit.leaved_at}\n"
    #           "Находится в хранилище:\n"
    #           f"{hours} час. {minutes} мин.")
