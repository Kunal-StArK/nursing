from django.apps import AppConfig
from django.db.models.signals import post_migrate

def add_missing_date_column(sender, **kwargs):
    try:
        from django.db import connection
        from .models import contact
        table_name = contact._meta.db_table
        with connection.cursor() as cursor:
            cursor.execute(f"SHOW COLUMNS FROM `{table_name}` LIKE 'date';")
            result = cursor.fetchone()
            if not result:
                cursor.execute(f"ALTER TABLE `{table_name}` ADD COLUMN date DATE NULL;")
                cursor.execute(f"UPDATE `{table_name}` SET date = CURDATE() WHERE date IS NULL;")
                cursor.execute(f"ALTER TABLE `{table_name}` MODIFY COLUMN date DATE NOT NULL;")
    except Exception:
        pass

class contactUsConfig(AppConfig):
    name = 'contactUs'

    def ready(self):
        post_migrate.connect(add_missing_date_column, sender=self)
