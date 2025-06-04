from services.daobase import BaseDAO
from services.profile.app.models import Profile, User


class UserDAO(BaseDAO):
    model = User


class ProfileDAO(BaseDAO):
    model = Profile