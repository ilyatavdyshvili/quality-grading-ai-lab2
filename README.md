## Лабораторная работа №2. Вариант №14

# Предсказатель зарплаты

## Описание

Проект предсказывает зарплату сотрудника на основе его опыта, города, должности и навыков. Модель обучалась на CSV-файле data/hr_data.csv.

## Запуск

```bash
# Установка зависимостей
poetry install

# Активировать виртуальное окружение
poetry shell

# Запустить MinIO
docker compose up -d

#Проверка работоспособности MinIO (в браузере)
http://localhost:9001

# Запуск API
poetry run uvicorn src.presentation.api:app --reload

# API доступен по адресу: http://127.0.0.1:8000
# Документация Swagger: http://127.0.0.1:8000/docs

```
## Пример запроса.

# Endpoint: POST /predict

# Request body (application json): 
```json
{
  "experience": 1,
  "city": "Moscow",
  "position": "Junior Data Scientist",
  "skills": "Python"
}
```
```json
{
  "experience": 4,
  "city": "Moscow",
  "position": "ML Engineer",
  "skills": "Python"
}
```
```json
{
  "experience": 5,
  "city": "SPb",
  "position": "Senior Data Scientist",
  "skills": "Python"
}
```
Пример ответа (JSON):
```json
{
  "predicted_salary": 183333.33
}
```



