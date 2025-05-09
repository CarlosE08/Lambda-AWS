# lambda_function.py

import os
import psycopg2

def lambda_handler(event, context):
    host = os.environ.get('DB_HOST')
    port = int(os.environ.get('DB_PORT', 5432))
    user = os.environ.get('DB_USER')
    password = os.environ.get('DB_PASSWORD')
    database = os.environ.get('DB_NAME')

    try:
        conn = psycopg2.connect(
            host=host,
            port=port,
            user=user,
            password=password,
            dbname=database,
            connect_timeout=5
        )
        conn.close()
        return {
            'statusCode': 200,
            'body': '✅ Conexión a Aurora PostgreSQL exitosa'
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': f'❌ Error al conectar a Aurora PostgreSQL: {str(e)}'
        }
