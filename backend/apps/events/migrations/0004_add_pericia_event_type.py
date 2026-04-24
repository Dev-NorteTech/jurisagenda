from django.db import migrations


class Migration(migrations.Migration):
    """
    Adiciona PERICIA como tipo de evento.
    Não requer alteração de schema — EventType é TextChoices (CharField).
    """

    dependencies = [
        ('events', '0003_setup_email_periodic_tasks'),
    ]

    operations = []
