import requests

def test_login_верный_пароль():
    response = requests.post(
        "https://api.demoblaze.com/login",
        json={"username": "kiralay", "password": "a2lsbGVyMjIy"}
    )
    assert response.status_code == 200
    assert "Auth_token" in response.text
    print("PASSED — логин успешен, токен получен")

def test_login_неверный_пароль():
    response = requests.post(
        "https://api.demoblaze.com/login",
        json={"username": "kiralay", "password": "неверныйпароль"}
    )
    assert response.status_code == 401
    assert "errorMessage" in response.text
    print("PASSED — сервер вернул ошибку")

def test_получить_товары():
    response = requests.get("https://api.demoblaze.com/entries")
    assert response.status_code == 200
    assert "Items" in response.text
    print("PASSED — список товаров получен")