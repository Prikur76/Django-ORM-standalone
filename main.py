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
    passcards = Passcard.objects.all()
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
    visits = Visit.objects.all()
    # print(len(visits))
    for visit in visits[:10]:
        visit_entered = localtime(visit.entered_at)
        visit_leaved = localtime()
        if visit.leaved_at:
            visit_leaved = localtime(visit.leaved_at)

        duration = str(visit_leaved - visit_entered).split('.')[0]
        owner_name = Visit.objects.get(passcard=Passcard.owner_name)

        print(f"Посетитель: {owner_name}"
              "\nЗашёл в хранилище, время по Москве:\n"
              f"{visit_entered}\n"
              "Находится в хранилище:\n"
              f"{duration}")

