from fastapi import APIRouter

from services.profile.app.dao import UserDAO
from services.profile.app.schemas import scUser
from services.exceptions import APIException


router = APIRouter(
    prefix='/profile',
    tags=['Профиль']
)


@router.post('/register')
async def create_profile(
    user: scUser
) -> bool:
    user_exists = await UserDAO.get_object(login = scUser.login)
    if user_exists:
        raise APIException.USER_EXISTS
    await UserDAO.add(user)
    

@router.get('/me')
async def get_user(
    
)