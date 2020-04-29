import config
from time import sleep
import random
import database
import string


def main():
	# подключаемся к бд
	db = database.DBCore()
	# входим в бесконечный цикл
	while True:
		# генерируем почту и сообщение для письма
		email = "".join(random.choice(string.ascii_letters) for i in range(10)) + random.choice(config.email_scope)
		content = random.choice(config.content_scope)
		# добавляем рассылку в бд
		db.add_task(email, content)
		print("Задача успешно создана.")
		# имитируем процесс создания в случайное время
		sleep(random.randint(15, 45))


if __name__ == "__main__":
	main()