from service import app

def test_get_accounts():
    response = app.test_client().get("/accounts")
    assert response.status_code == 200


def test_create_account():
    client = app.test_client()

    response = client.post(
        "/accounts",
        json={
            "name": "Pratiksha",
            "email": "pgd6098@gmail.com"
        }
    )

    assert response.status_code == 201