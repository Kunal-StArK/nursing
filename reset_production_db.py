import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Hopital.settings")
django.setup()

from django.db import connection

def reset_db():
    with connection.cursor() as cursor:
        print("Disabling foreign key checks...")
        cursor.execute("SET FOREIGN_KEY_CHECKS = 0;")
        
        # Get list of all tables
        cursor.execute("SHOW TABLES;")
        tables = [row[0] for row in cursor.fetchall()]
        
        print(f"Found tables to drop: {tables}")
        for table in tables:
            print(f"Dropping table {table}...")
            cursor.execute(f"DROP TABLE IF EXISTS `{table}` CASCADE;")
            
        cursor.execute("SET FOREIGN_KEY_CHECKS = 1;")
        print("Database reset completed successfully!")

if __name__ == "__main__":
    reset_db()
