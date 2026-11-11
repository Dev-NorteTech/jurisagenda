from django.db import migrations, models


class Migration(migrations.Migration):
    """
    Merge das branches paralelas:
      - 0003_add_oitiva_event_type  (adiciona OITIVA)
      - 0004_add_pericia_event_type (adiciona PERICIA, depende de 0003_setup_email_periodic_tasks)

    Este merge garante que ambas as branches sejam aplicadas e unifica os choices
    com todos os tipos: AUDIENCIA, REUNIAO, PRAZO, CONTRATO, OITIVA, PERICIA.
    """

    dependencies = [
        ('events', '0003_add_oitiva_event_type'),
        ('events', '0004_add_pericia_event_type'),
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
                    ('OITIVA', 'Oitiva'),
                    ('PERICIA', 'Perícia'),
                ],
                db_index=True,
                max_length=30,
                verbose_name='Tipo',
            ),
        ),
    ]
