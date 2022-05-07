import datetime
import sqlalchemy
from .db_session import SqlAlchemyBase


class User(SqlAlchemyBase):
    __tablename__ = 'brawlers'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    name_rus = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    href_img = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    href_json = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    rarity = sqlalchemy.Column(sqlalchemy.String, nullable=True)
