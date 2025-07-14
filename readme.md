<!-- Project Structure  -->

├── main.py
├── readme.md
├── requirements.txt
├── src
│   ├── app
│   │   ├── authentication
│   │   │   ├── __init__.py
│   │   │   ├── repository
│   │   │   │   └── auth_repo.py
│   │   │   ├── router.py
│   │   │   ├── schemas
│   │   │   │   └── auth_schema.py
│   │   │   ├── service.py
│   │   │   └── tasks.py
│   │   ├── _lib
│   │   │   ├── base.py
│   │   │   ├── __init__.py
│   │   │   ├── repository
│   │   │   │   ├── base.py
│   │   │   │   ├── common.py
│   │   │   │   └── __init__.py
│   │   │   └── schemas
│   │   ├── users
│   │   │   ├── __init__.py
│   │   │   ├── repository
│   │   │   │   └── user_repo.py
│   │   │   ├── router.py
│   │   │   ├── schemas
│   │   │   │   └── user_schema.py
│   │   │   ├── service.py
│   │   │   └── tasks.py
│   │   └── voucher
│   │       ├── __init__.py
│   │       ├── repository
│   │       │   └── voucher_repo.py
│   │       ├── router.py
│   │       ├── schemas
│   │       │   └── voucher_schema.py
│   │       ├── service.py
│   │       └── tasks.py
│   ├── common
│   │   ├── constants
│   │   │   └── constant.py
│   │   ├── enums
│   │   │   ├── card_type_enum.py
│   │   │   ├── role_enum.py
│   │   │   └── rupee_enum.py
│   │   ├── helper
│   │   │   ├── csv_gen.py
│   │   │   ├── paginator.py
│   │   │   └── pdf_gen.py
│   │   ├── keygen.py
│   │   ├── response.py
│   │   └── utils
│   │       ├── date_formate.py
│   │       └── validation.py
│   ├── configuration
│   │   ├── env_settings.py
│   │   ├── mongo_db.py
│   │   └── sql_config.py
│   ├── models
│   │   ├── etc_model.py
│   │   ├── __init__.py
│   │   ├── user_model.py
│   │   └── voucher_model.py
│   ├── seeder
│   │   └── seeder.py
│   ├── tests
│   │   ├── test_authentication.py
│   │   ├── test_user.py
│   │   └── test_voucher.py
│   └── worker
│       ├── celery_config.py
│       └── web_socket.py
├── static
├── templates