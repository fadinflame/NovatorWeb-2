import psycopg2
import config


class DBCore:
	""" Класс для работы с БД PostgreSQL """
	def __init__(self):
		# При инициализации класса происходит подключение к бд
		self.__connection = psycopg2.connect(dbname=config.DB_NAME, user=config.DB_USER, 
 										password=config.DB_PASSWORD, host=config.SERVER_NAME)
		self.__cursor = self.__connection.cursor()


	def __execute_query(self, query):
		""" Приватный метод для исполнения SQL-команд """
		self.__cursor.execute(query)
		self.__connection.commit()


	def add_task(self, email, message):
		"""
		Паблик метод для добавления рассылки
		
		Параметры
		_________

		email : str
			Почта для рассылки
		
		message : str
			Сообщение для рассылки
		"""
		self.__execute_query(f"INSERT INTO storage (email, msg)\
							VALUES ('{email}', '{message}')")


	def get_tasks(self):
		""" Паблик метод для получения рассылок """
		self.__cursor.execute("SELECT * FROM storage")
		return self.__cursor.fetchall()

	
	def delete_task(self, email):
		"""
		Паблик метод для удаления рассылки 
		
		Параметры
		_________

		email : str
			Почта для рассылки
		"""
		self.__execute_query(f"DELETE FROM storage WHERE email = '{email}'")


