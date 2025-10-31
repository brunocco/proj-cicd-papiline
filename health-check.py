import urllib3
import boto3

client = boto3.client('sns')

urls = { 'App Upload File': 'https://app.labaws.lat/health' }

def lambda_handler(event, context):
   http = urllib3.PoolManager()
  
   for platform_name, url in urls.items():
       try:
           response = http.request('GET', url)
           status_code = response.status


           if status_code == 200:
               print(f"HEALTH >> OK ({platform_name})")
           else:
               print(f"HEALTH >> FAIL ({platform_name}) - Status Code: {status_code}")
               send_notify(platform_name, status_code)
              
       except Exception as e:
           print(f"HEALTH >> FAIL ({platform_name}) - Error: {str(e)}")
           send_notify(platform_name, error_message=str(e))
      
def send_notify(platform_name, status_code=None, error_message=None):
   message = f"HEALTH >> FAIL ({platform_name})"
   if status_code:
       message += f" - Status Code: {status_code}"
   if error_message:
       message += f" - Error: {error_message}"
      
   client.publish(
       TopicArn="arn:aws:sns:us-east-1:AWS_ACCOUNT_ID:HealthCheck",
       Message=message,
       Subject="[ALERT CHECK HEALTH]"
   )
