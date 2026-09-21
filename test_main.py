from fastapi.testclient import TestClient

from main import app


def test_create_recipe():
    with TestClient(app) as client:
        response = client.post(
            "/recipes",
            json={
                "name": "Pasta",
                "cooking_time": 20,
                "ingredients": "Pasta, tomato, cheese",
                "description": "Simple pasta recipe",
            },
        )

        assert response.status_code == 201

        data = response.json()
        assert data["name"] == "Pasta"
        assert data["cooking_time"] == 20
        assert data["views"] == 0


def test_read_recipes():
    with TestClient(app) as client:
        response = client.get("/recipes")

        assert response.status_code == 200
        assert isinstance(response.json(), list)


def test_recipe_not_found():
    with TestClient(app) as client:
        response = client.get("/recipes/999999")

        assert response.status_code == 404
        assert response.json()["detail"] == "Recipe not found"
