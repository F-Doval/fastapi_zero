from http import HTTPStatus

from fastapi.testclient import TestClient

from fastapi_zero.app import app


def test_root_deve_retornar_ola_mundo():
    client = TestClient(app)
    """
    Esse teste tem 3 etapas (AAA)
    - A: Arrange - Arranjo
    - A: Act - Executa a coisa(o SUT - System Under Test)
    - A: Assert - garante que A é A
    """

    response = client.get("/")

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {"Message": "Hello world !"}
