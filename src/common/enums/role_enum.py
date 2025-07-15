from enum import Enum
class UserRole(str, Enum):
    USER = "user"
    ADMIN = "admin"
    SUPER_ADMIN = "super_admin"

    @classmethod
    def choices(cls):
        return [role.value for role in cls]
