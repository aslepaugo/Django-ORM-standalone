import os

import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
django.setup()

from datacenter.models import Passcard  # noqa: E402

if __name__ == '__main__':
    # Программируем здесь
    print('Количество пропусков:', Passcard.objects.count())  # noqa: T001
    passcards = Passcard.objects.all()
    passcard = passcards[0]
    print(f"owner_name: {passcard.owner_name}")
    print(f"passcode: {passcard.passcode}")
    print(f"created_at: {passcard.created_at}")
    print(f"is_active: {passcard.is_active}")

    active_count = len(Passcard.objects.filter(is_active=True))

    print(f"Всего пропусков {len(passcards)}")
    print(f"Активных пропусков {active_count}")
