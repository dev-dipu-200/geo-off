<!-- Project Structure -->

##Project Structure 
### You're 90% Microservices-Ready!

```
├── main.py # Main entry point
├── readme.md
├── requirements.txt
├── src # Source code
│ ├── app # All application modules
│ │ ├── authentication # Authentication module
│ │ │ ├── init.py
│ │ │ ├── repository
│ │ │ │ └── auth_repo.py
│ │ │ ├── router.py
│ │ │ ├── schemas
│ │ │ │ └── auth_schema.py
│ │ │ ├── service.py
│ │ │ └── tasks.py
│ │ ├── _lib # Common module for shared functionality
│ │ │ ├── base.py
│ │ │ ├── init.py
│ │ │ ├── repository
│ │ │ │ ├── base.py
│ │ │ │ ├── common.py
│ │ │ │ └── init.py
│ │ │ └── schemas
│ │ ├── users # User module (all user-related APIs)
│ │ │ ├── init.py
│ │ │ ├── repository
│ │ │ │ └── user_repo.py
│ │ │ ├── router.py
│ │ │ ├── schemas
│ │ │ │ └── user_schema.py
│ │ │ ├── service.py
│ │ │ └── tasks.py
│ │ └── voucher # Voucher module (all voucher-related APIs)
│ │ ├── init.py
│ │ ├── repository
│ │ │ └── voucher_repo.py
│ │ ├── router.py
│ │ ├── schemas
│ │ │ └── voucher_schema.py
│ │ ├── service.py
│ │ └── tasks.py
│ ├── common # Shared functionality across modules
│ │ ├── constants
│ │ │ └── constant.py # Example: "User not found" messages
│ │ ├── enums # Project enums
│ │ │ ├── card_type_enum.py
│ │ │ ├── role_enum.py
│ │ │ └── rupee_enum.py
│ │ ├── helper # Excel, PDF generators, and utilities
│ │ │ ├── csv_gen.py
│ │ │ ├── paginator.py
│ │ │ └── pdf_gen.py
│ │ ├── keygen.py # UUID generator for models
│ │ ├── response.py # Standardized API response structure
│ │ └── utils # Validation and utility functions
│ │ ├── date_formate.py
│ │ └── validation.py
│ ├── configuration # Configuration for DB and third-party services
│ │ ├── env_settings.py
│ │ ├── mongo_db.py
│ │ └── sql_config.py
│ ├── models # SQLAlchemy models (DB tables)
│ │ ├── etc_model.py
│ │ ├── init.py
│ │ ├── user_model.py
│ │ └── voucher_model.py
│ ├── seeder # Seeder for bulk data from Excel, PDF, or APIs
│ │ └── seeder.py
│ ├── tests # Unit and integration tests
│ │ ├── test_authentication.py
│ │ ├── test_user.py
│ │ └── test_voucher.py
│ └── worker # Celery config for background tasks
│ ├── celery_config.py
│ └── web_socket.py
├── static # Stores uploaded files (images, docs, etc.)
├── templates # HTML templates (invoices, PDFs, emails)
```

## Celery Worker Run
celery -A src.worker.celery_config.celery_app worker --loglevel=info


## Celery Beat Run
celery -A src.worker.celery_config.celery_app beat --loglevel=info
