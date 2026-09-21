from pydantic import BaseModel, Field


class RecipeCreate(BaseModel):
    """Данные, необходимые для создания нового рецепта."""

    name: str = Field(
        description="Название блюда",
        examples=["Pasta Carbonara"],
    )
    cooking_time: int = Field(
        gt=0,
        description="Время приготовления блюда в минутах",
        examples=[25],
    )
    ingredients: str = Field(
        description="Список ингредиентов рецепта",
        examples=["pasta, eggs, cheese, bacon"],
    )
    description: str = Field(
        description="Подробное описание приготовления блюда",
        examples=["Boil the pasta and prepare the sauce."],
    )


class RecipeList(BaseModel):
    """Краткая информация о рецепте для списка рецептов."""

    name: str = Field(
        description="Название блюда",
    )
    views: int = Field(
        description="Количество просмотров рецепта",
    )
    cooking_time: int = Field(
        description="Время приготовления в минутах",
    )


class RecipeDetail(BaseModel):
    """Подробная информация о выбранном рецепте."""

    name: str = Field(
        description="Название блюда",
    )
    cooking_time: int = Field(
        description="Время приготовления в минутах",
    )
    ingredients: str = Field(
        description="Список ингредиентов рецепта",
    )
    description: str = Field(
        description="Подробное описание приготовления блюда",
    )


class RecipeCreated(BaseModel):
    """Информация о созданном рецепте."""

    id: int = Field(
        description="Уникальный идентификатор рецепта",
    )
    name: str = Field(
        description="Название блюда",
    )
    cooking_time: int = Field(
        description="Время приготовления в минутах",
    )
    ingredients: str = Field(
        description="Список ингредиентов рецепта",
    )
    description: str = Field(
        description="Подробное описание приготовления блюда",
    )
    views: int = Field(
        description="Количество просмотров рецепта",
    )
