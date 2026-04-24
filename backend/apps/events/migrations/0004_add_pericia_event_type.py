from django.db import migrations, models


class Migration(migrations.Migration):
    """
    Adiciona PERICIA como tipo de evento.
    TextChoices não altera schema — apenas atualiza o campo choices para documentação.
    """

    dependencies = [
        ('events', '0003_setup_email_periodic_tasks'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='event_type',
            field=models.CharField(
                choices=[
                    ('AUDIENCIA', 'Audiência'),
                    ('REUNIAO', 'Reunião'),
                    ('PRAZO', 'Prazo'),
                    ('CONTRATO', 'Contrato'),
                    ('PERICIA', 'Perícia'),
                ],
                db_index=True,
                max_length=30,
                verbose_name='Tipo',
            ),
        ),
    ]
