from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import declarative_base


Base = declarative_base()


class Recipe(Base):
    """Модель рецепта в базе данных."""

    __tablename__ = "recipe"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    cooking_time = Column(Integer, nullable=False)
    ingredients = Column(Text, nullable=False)
    description = Column(Text, nullable=False)
    views = Column(Integer, default=0, nullable=False)