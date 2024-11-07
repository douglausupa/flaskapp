def test_homepage():
    response = flaskapp.test_client().get('/')
    assert response.status_code == 200

