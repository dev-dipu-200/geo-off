from fastapi import APIRouter, Depends, Query
from src.app.users import service as user_service
from src.common.response import ResponseModel
from src.configuration.sql_config import get_db
from fastapi.responses import StreamingResponse
from sqlalchemy.orm import Session
from io import BytesIO

router = APIRouter(
    prefix="/users",
    tags=["Users"],
)


@router.get("/user-list")
async def read_users(
    page: int = Query(1, ge=1),
    page_size: int = Query(10, ge=1),
    is_paginate: bool = Query(False),
    db: Session = Depends(get_db),
):
    """
    Fetch all users from the database.
    This endpoint retrieves all user records and returns them in a structured format.
    """
    response = await user_service.get_all_users(
        db=db, page=page, page_size=page_size, is_paginate=is_paginate
    )
    return ResponseModel(result=response)


@router.get("/generate-pdf")
async def generate_pdf(db: Session = Depends(get_db), filename: str = "users_report.pdf"):
    """
    Generate a PDF report of all users.
    This endpoint creates a PDF document containing user information.
    """
    pdf_bytes = await user_service.generate_pdf(db)

    return StreamingResponse(
        BytesIO(pdf_bytes),
        media_type="application/pdf",
        headers={"Content-Disposition": f"attachment; filename={filename}"}
    )


@router.get("/generate-csv")
async def generate_csv(
    db: Session = Depends(get_db), filename: str = "users_report.csv"
):
    """
    Generate a CSV report of all users.
    This endpoint creates a CSV document containing user information.
    """

    csv_bytes = await user_service.generate_csv(db=db,filename=filename)

    return StreamingResponse(
        csv_bytes,
        media_type="text/csv",
        headers={"Content-Disposition": f"attachment; filename={filename}"}
    )