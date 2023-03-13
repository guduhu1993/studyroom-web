from app.models.user import User


async def create_user(user: dict):
    await User.objects.create(**user)
