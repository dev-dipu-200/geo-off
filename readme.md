<!-- Project Structure -->

## Project Structure 
### You're 90% Microservices-Ready!

```
.
├── main.py                # Main Entry Point
├── readme.md
├── requirements.txt      
├── src                    # Source file
│   ├── app                             # Module existing Folder
│   │   ├── authentication                     #  Authentication Module 
│   │   │   ├── __init__.py
│   │   │   ├── repository
│   │   │   │   └── auth_repo.py
│   │   │   ├── router.py
│   │   │   ├── schemas
│   │   │   │   └── auth_schema.py
│   │   │   ├── service.py
│   │   │   └── tasks.py
│   │   ├── _lib                              # Common Module for common funtioinality apply to all module
│   │   │   ├── base.py
│   │   │   ├── __init__.py
│   │   │   ├── repository
│   │   │   │   ├── base.py
│   │   │   │   ├── common.py
│   │   │   │   └── __init__.py
│   │   │   └── schemas
│   │   ├── users                            # User Module, all users api exist in the module 
│   │   │   ├── __init__.py
│   │   │   ├── repository
│   │   │   │   └── user_repo.py
│   │   │   ├── router.py
│   │   │   ├── schemas
│   │   │   │   └── user_schema.py
│   │   │   ├── service.py
│   │   │   └── tasks.py
│   │   └── voucher                          # Voucher Module, all voucher related api exist in the module
│   │       ├── __init__.py
│   │       ├── repository
│   │       │   └── voucher_repo.py
│   │       ├── router.py
│   │       ├── schemas
│   │       │   └── voucher_schema.py
│   │       ├── service.py
│   │       └── tasks.py
│   ├── common                               # Common Directory work on if any common fuction and class use in the project.
│   │   ├── constants
│   │   │   └── constant.py                  # Constant variable write in the file like "User not found"
│   │   ├── enums                            # Keep enum files in the enums directory
│   │   │   ├── card_type_enum.py
│   │   │   ├── role_enum.py
│   │   │   └── rupee_enum.py
│   │   ├── helper                           # Helper director will help in hole project to generate excel, pdf
│   │   │   ├── csv_gen.py
│   │   │   ├── paginator.py
│   │   │   └── pdf_gen.py
│   │   ├── keygen.py                        # keygen.py will help to make unique id with uuid4 for every models
│   │   ├── response.py                      # Response.py keep a structure base response for every success or faild api response
│   │   └── utils                            # Utils folder keep validations files
│   │       ├── date_formate.py
│   │       └── validation.py
│   ├── configuration                        # Configuration folder exist for to config db, third party api,
│   │   ├── env_settings.py
│   │   ├── mongo_db.py
│   │   └── sql_config.py
│   ├── models                               # Models folder use for create Database table
│   │   ├── etc_model.py
│   │   ├── __init__.py
│   │   ├── user_model.py
│   │   └── voucher_model.py
│   ├── seeder                                # Seeder will help to upload bulk data from excel, pdf, or api call.
│   │   └── seeder.py
│   ├── tests                                 # Test folder help us about testing  
│   │   ├── test_authentication.py
│   │   ├── test_user.py
│   │   └── test_voucher.py
│   └── worker                                # Worker folder exists for celery configuration which help to run background task
│       ├── celery_config.py
│       └── web_socket.py
├── static                                    # static folder keep to store uploaded files
├── templates                                 # tempates to help generate invoice, pdf, in the folder we keep html files.

```
