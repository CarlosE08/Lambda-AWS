# lambda_function.py

import urllib.request

def lambda_handler(event, context):
    url = 'https://www.google.com'
    
    try:
        response = urllib.request.urlopen(url, timeout=5)
        status_code = response.getcode()
        return {
            'statusCode': 200,
            'body': f'✅ Conexión a internet exitosa. Código HTTP: {status_code}'
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': f'❌ No se pudo conectar a Internet: {str(e)}'
        }
