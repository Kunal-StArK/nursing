import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Hopital.settings")
django.setup()

from django.db import connection
from contactUs.models import contact

def add_column():
    table_name = contact._meta.db_table
    with connection.cursor() as cursor:
        print(f"Checking columns for table {table_name}...")
        cursor.execute(f"SHOW COLUMNS FROM `{table_name}` LIKE 'date';")
        result = cursor.fetchone()
        if not result:
            print(f"Adding date column to {table_name}...")
            cursor.execute(f"ALTER TABLE `{table_name}` ADD COLUMN date DATE NULL;")
            cursor.execute(f"UPDATE `{table_name}` SET date = CURDATE() WHERE date IS NULL;")
            cursor.execute(f"ALTER TABLE `{table_name}` MODIFY COLUMN date DATE NOT NULL;")
            print("Successfully added date column!")
        else:
            print("date column already exists!")

if __name__ == "__main__":
    add_column()
