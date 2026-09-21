from contextlib import asynccontextmanager

from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from database import SessionLocal, engine
from models import Base, Recipe
from schemas import (
    RecipeCreate,
    RecipeList,
    RecipeDetail,
    RecipeCreated,
)


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Создаёт таблицы базы данных при запуске приложения."""
    async with engine.begin() as connection:
        await connection.run_sync(Base.metadata.create_all)

    yield

    await engine.dispose()


app = FastAPI(
    title="Cookbook API",
    description=(
        "API сервиса кулинарной книги. "
        "Позволяет создавать рецепты, получать список рецептов "
        "и просматривать подробную информацию о каждом рецепте. "
        "Популярность рецепта определяется количеством просмотров."
    ),
    version="1.0.0",
    lifespan=lifespan,
)


async def get_db():
    """Создаёт асинхронную сессию базы данных."""
    async with SessionLocal() as db:
        yield db


@app.post(
    "/recipes",
    response_model=RecipeCreated,
    status_code=status.HTTP_201_CREATED,
    summary="Создать рецепт",
    description=(
        "Создаёт новый рецепт в кулинарной книге. "
        "Количество просмотров нового рецепта автоматически устанавливается в 0."
    ),
)
async def create_recipe(
    data: RecipeCreate,
    db: AsyncSession = Depends(get_db),
):
    """Создаёт новый рецепт."""

    recipe = Recipe(
        name=data.name,
        cooking_time=data.cooking_time,
        ingredients=data.ingredients,
        description=data.description,
    )

    db.add(recipe)

    await db.commit()
    await db.refresh(recipe)

    return recipe


@app.get(
    "/recipes",
    response_model=list[RecipeList],
    summary="Получить список рецептов",
    description=(
        "Возвращает список всех рецептов. "
        "Рецепты сортируются по количеству просмотров от большего к меньшему. "
        "При одинаковом количестве просмотров рецепты сортируются "
        "по времени приготовления от меньшего к большему."
    ),
)
async def read_recipes(
    db: AsyncSession = Depends(get_db),
) -> list[RecipeList]:
    """Возвращает отсортированный список рецептов."""

    query = select(Recipe).order_by(
        Recipe.views.desc(),
        Recipe.cooking_time,
    )

    result = await db.execute(query)
    recipes = result.scalars().all()

    return recipes


@app.get(
    "/recipes/{recipe_id}",
    response_model=RecipeDetail,
    summary="Получить рецепт",
    description=(
        "Возвращает подробную информацию о рецепте по его идентификатору. "
        "При каждом успешном открытии рецепта количество его просмотров "
        "увеличивается на один."
    ),
    responses={
        404: {
            "description": "Рецепт с указанным идентификатором не найден"
        }
    },
)
async def read_recipe(
    recipe_id: int,
    db: AsyncSession = Depends(get_db),
) -> RecipeDetail:
    """Возвращает подробную информацию о выбранном рецепте."""

    query = select(Recipe).where(
        Recipe.id == recipe_id
    )

    result = await db.execute(query)
    recipe = result.scalar_one_or_none()

    if recipe is None:
        raise HTTPException(
            status_code=404,
            detail="Recipe not found",
        )

    recipe.views += 1

    await db.commit()
    await db.refresh(recipe)

    return recipe

