from sqlalchemy import Column, Integer, String, ForeignKey

from core.psql import Base


class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    login = Column(String, nullable=False)
    hashed_password = Column(String, nullable=False)


class Profile(Base):
    __tablename__ = 'profiles'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.id'), unique=True)
    name = Column(String, nullable=False)
    last_name = Column(String)
    age = Column(Integer, nullable=False)
    email = Column(String)
    phone = Column(String)
    