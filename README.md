# ALX Travel App

A Django REST Framework (DRF) project for managing travel listings, with MySQL, Celery, CORS, and Swagger documentation.

## Features

- RESTful APIs for travel listings
- MySQL database
- CORS enabled for frontend at `localhost:3000`
- Swagger & ReDoc API documentation (`drf-yasg`)
- Environment variables for configuration (`.env`)

## Setup

1.  **Clone the repo**

    ```bash
    git clone https://github.com/solomonferede/alx_travel_app_0x00.git
    cd alx_travel_app
    ```

2.  **Create virtual environment**

        python3 -m venv venv
        source venv/bin/activate

3.  **Install dependencies**

        pip install -r requirements.txt

4.  **Set up `.env` file**

    Create a `.env` in project root:

        SECRET_KEY=your_secret_key
        DEBUG=True
        DATABASE_URL=mysql://user:password@localhost:3306/dbname

5.  **Run migrations**

        python manage.py migrate

6.  **Run server**

        python manage.py runserver

## API Documentation

- Swagger UI: [http://127.0.0.1:8000/swagger/](http://127.0.0.1:8000/swagger/)
- ReDoc UI: [http://127.0.0.1:8000/redoc/](http://127.0.0.1:8000/redoc/)

## Notes

- CORS is enabled for frontend at `http://localhost:3000`.
- Use Celery + RabbitMQ for background tasks
