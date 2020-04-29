import config
from time import sleep
import database

    
def main():
    # подключаемся к бд
    db = database.DBCore()
    # входим в бесконечный цикл
    while True:
        # получаем рассылки
        tasks = db.get_tasks()
        for task in tasks:
            # делаем имитацию отправления писем
            print(f"Новое сообщение было отправлено по адресу: {task[0]}\nСодержание: {task[1]}\n\n")
            # удаляем рассылку из бд
            db.delete_task(task[0])
        # уходим в сон на 15 сек и ждём след. рассылки
        sleep(15)


if __name__ == "__main__":
	main()