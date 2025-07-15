from typing import Optional, Any
from pydantic import BaseModel, root_validator
from fastapi import status


class ResponseModel(BaseModel):
    result: Optional[Any] = {}


class SuccessResponseModel(BaseModel):
    message: str = 'Request processed successfully'
    data: Optional[Any] = {}
    status_code: int = status.HTTP_200_OK
    status: str = 'success'

    @root_validator(pre=True)
    def set_defaults(cls, values):
        values['status_code'] = values.get('status_code', status.HTTP_200_OK)
        values['message'] = values.get('message', 'Request processed successfully')
        values['status'] = values.get('status', 'success')
        return values


class ErrorResponseModel(BaseModel):
    message: str = 'Request failed'
    error: Optional[str] = 'An error occurred'
    status_code: int = status.HTTP_400_BAD_REQUEST
    status: str = 'error'

    @root_validator(pre=True)
    def set_defaults(cls, values):
        values['status_code'] = values.get('status_code', status.HTTP_400_BAD_REQUEST)
        values['message'] = values.get('message', 'Request failed')
        values['error'] = values.get('error', 'An error occurred')
        values['status'] = values.get('status', 'error')
        return values


class ExistingResponseModel(BaseModel):
    message: str = 'Resource already exists'
    data: Optional[Any] = {}
    status_code: int = status.HTTP_409_CONFLICT
    status: str = 'exists'

    @root_validator(pre=True)
    def set_defaults(cls, values):
        values['status_code'] = values.get('status_code', status.HTTP_409_CONFLICT)
        values['message'] = values.get('message', 'Resource already exists')
        values['status'] = values.get('status', 'exists')
        return values
