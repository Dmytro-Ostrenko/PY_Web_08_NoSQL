import pika
import json
from mongoengine import connect
from models import Contact

# Підключення до бази даних Mongo
connect('PYHW8_2', host='mongodb+srv://dmytroostrenko:DRZ105T6tvRVV0Sh@cluster0.gjov9oo.mongodb.net/PYHW8_2')

# Встановлення з'єднання з RabbitMQ
credentials = pika.PlainCredentials('guest', 'guest')
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost', port=5672, credentials=credentials))
channel = connection.channel()
channel.queue_declare(queue='email')


def send_email(contact):
    print(f"Sending email to {contact.email}")
    
def callback(ch, method, properties, body):
    data = json.loads(body)
    contact_id = data['contact_id']
    contact = Contact.objects(id=contact_id).first()
    if contact:
        send_email(contact)
        contact.email_sent = True
        contact.save()
        print(f"Email sent to {contact.email}")
    else:
        print(f"Contact with id {contact_id} not found")


channel.basic_consume(queue='email', on_message_callback=callback, auto_ack=True)
print('Очікування повідомлення')
channel.start_consuming()

