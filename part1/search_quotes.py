from mongoengine import connect
from models import Quote, Author

# Підключення до MongoDB Atlas
connect('PYHW8', host='mongodb+srv://dmytroostrenko:DRZ105T6tvRVV0Sh@cluster0.gjov9oo.mongodb.net/PYHW8')



def search_quotes(command):
    if command.startswith('name:'):
        author_name = command.split(':')[1].strip()
        author = Author.objects(fullname=author_name).first()
        if author:
            quotes = Quote.objects(author=author)
            for quote in quotes:
                print(f"{quote.author.fullname}: {quote.quote}")
        else:
            print(f"No quotes found for author '{author_name}'.")
    elif command.startswith('tag:'):
        tag = command.split(':')[1].strip()
        quotes = Quote.objects(tags=tag)
        for quote in quotes:
            print(f"{quote.author.fullname}: {quote.quote}")
    elif command.startswith('tags:'):
        tags = command.split(':')[1].strip().split(',')
        quotes = Quote.objects(tags__in=tags)
        for quote in quotes:
            print(f"{quote.author.fullname}: {quote.quote}")
    else:
        print("Invalid command format.")


if __name__ == "__main__":
    while True:
        command = input("Enter command (name: author_name, tag: tag_name, tags: tag1,tag2, exit to quit): ").strip()
        if command.lower() == 'exit':
            break
        search_quotes(command)