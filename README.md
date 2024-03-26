# scheduler_simple

# Инструкция по запуску планировщика задач:

# Установка:

    1. Установите Python 3.7+
    2. Установите Django 3.2+
    3. Установите SQLite 3+
    4. Создайте виртуальное окружение Python:

python -m venv venv

    Активируйте виртуальное окружение:

source venv/bin/activate

    Установите зависимости проекта:

pip install -r requirements.txt

# Настройка:

    Создайте файл .env в корне проекта.
    Добавьте в него следующие переменные:

SECRET_KEY=<your_secret_key>
DEBUG=<True|False>
ALLOWED_HOSTS=<comma_separated_list_of_allowed_hosts>
DATABASE_URL=sqlite:///db.sqlite3

# Запуск:

    Запустите сервер Django:

python manage.py runserver

# Использование:

    Откройте браузер и перейдите по адресу http://localhost:8000/.

    Вы можете использовать API для добавления, получения списка, редактирования и удаления задач.

    Доступные методы API:
        POST /api/tasks/create/ - Добавить задачу
        GET /api/tasks/ - Получить список задач
        PUT /api/tasks/<id>/ - Редактировать задачу
        DELETE /api/tasks/<id>/ - Удалить задачу

# Примеры использования:

    Добавить задачу:

curl -X POST \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Новая задача",
    "description": "Описание задачи",
    "status": "added"
  }' \
  http://localhost:8000/api/tasks/create/

    Получить список задач:

curl -X GET \
  http://localhost:8000/api/tasks/

    Редактировать задачу:

curl -X PUT \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Измененное имя",
    "description": "Измененное описание",
    "status": "in_progress"
  }' \
  http://localhost:8000/api/tasks/1/

    Удалить задачу:

curl -X DELETE \
  http://localhost:8000/api/tasks/1/
