from src.app.authentication.router import router as auth_router
from src.app.users.router import router as users_router
from src.app.voucher.router import router as vouchers_router

routers = [
    auth_router,
    users_router,
    vouchers_router,
]