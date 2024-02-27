import os
from faker import Faker
from mongoengine import connect
from models import Contact
import pika

# Підключення до Mongo
connect('PYHW8_2', host='mongodb+srv://dmytroostrenko:DRZ105T6tvRVV0Sh@cluster0.gjov9oo.mongodb.net/PYHW8_2')

#rabbitmq_uri = os.getenv('RABBITMQ_URI')
credentials = pika.PlainCredentials('guest', 'guest')
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost', port=5672, credentials=credentials))
channel = connection.channel()
channel.queue_declare(queue='contacts')

# Створення фейкових контактів та надсилання повідомлення
fake = Faker()
for _ in range(100):
    name = fake.name()
    email = fake.email()
    contact = Contact(full_name=name, email=email)
    contact.save()
    channel.basic_publish(exchange='', routing_key='contacts', body=str(contact.id))

print("Контакти надіслано до RabbitMQ")
connection.close()
