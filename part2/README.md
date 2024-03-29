Напишіть два скрипти: consumer.py та producer.py. Використовуючи RabbitMQ, організуйте за допомогою черг імітацію розсилки email контактам.

- Використовуючи ODM Mongoengine, створіть модель для контакту. 
- Модель обов'язково повинна включати поля: повне ім'я, email та логічне поле, яке має значення False за замовчуванням. 
- Воно означає, що повідомлення контакту не надіслано і має стати True, коли буде відправлено. Інші поля для інформаційного навантаження можете придумати самі.

  Під час запуску скрипта producer.py він генерує певну кількість (100) фейкових контактів та записує їх у базу даних.
  Потім поміщає у чергу RabbitMQ повідомлення, яке містить ObjectID створеного контакту, і так для всіх згенерованих контактів.

Скрипт consumer.py отримує з черги RabbitMQ повідомлення, обробляє його та імітує функцією-заглушкою надсилання повідомлення по email. 
Після надсилання повідомлення необхідно логічне поле для контакту встановити в True. Скрипт працює постійно в очікуванні повідомлень з RabbitMQ.

### Порядок запуску:

1. Встановлення RabbitMQ за допомогою Docker через команду:   

   docker run -d --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:3.11-management
   ---
2. Запуск *models.py*
3. Запуск *producer.py* для створення контактів через faker
4. Запуск concumer.py

   Для перевірки: http://localhost:15672/   login-guest, pasword - guest.
  


