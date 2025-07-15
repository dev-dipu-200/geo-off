from typing import Optional
from src.common.helper.paginator import Paginator
from src.app.authentication.schemas.auth_schema import UserSchema
from src.common.response import SuccessResponseModel
from src.models.user_model import User
from src.common.helper.pdf_gen import generate_pdf as pdf_generator
from src.common.helper.csv_gen import generate_csv as csv_generator
async def get_all_users(db, page: int = 1, page_size: int = 10, is_paginate: bool = False):
    """
    Fetch all users from the database, optionally paginated.
    """
    users = db.query(User).all()
    if not users:
        return SuccessResponseModel(data=[], message="No users found")

    results = [UserSchema.from_orm(user) for user in users]

    if is_paginate:
        paginator = Paginator(page=page, page_size=page_size)
        paginated_data = paginator.to_dict(results)
        return SuccessResponseModel(data=paginated_data, message="Users retrieved with pagination")

    return SuccessResponseModel(data=results, message="Users retrieved successfully")


async def generate_pdf(db):
    users = db.query(User).all()
    data = {user.id: user.email for user in users}
    return await pdf_generator(data=data)

async def generate_csv(db=None, header: Optional[list] = None, filename: str = "users_report.csv"):
    """
    Generate a CSV report of all users.
    """
    if header is None:
        header = ["id", "email", 'first_name', 'last_name', 'is_active', 'role', 'created_at', 'updated_at']

    users = await get_all_users(db=db, is_paginate=False)
    data = [user.dict() for user in users.data]

    return await csv_generator(header=header, data=data, filename=filename)