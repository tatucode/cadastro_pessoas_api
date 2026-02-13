import requests

BASE_URL = "http://127.0.0.1:8001"

def test_health():
    r = requests.get(f"{BASE_URL}/health")
    print("health:", r.status_code, r.text)
    assert r.status_code == 200

def test_criar_pessoa():
    data = {"nome": "João", "idade": 30, "email":" teste.joao@gmail.com"}
    r = requests.post(f"{BASE_URL}/pessoas", json=data)
    print("criar pessoa:", r.status_code, r.text)
    assert r.status_code in (201, 409)

    r = requests.get(f"{BASE_URL}/pessoas")
    print("listar pessoas:", r.status_code, r.text)
    assert r.status_code == 200
    assert isinstance(r.json(), list)

if __name__ == "__main__":
    test_health()
    test_criar_pessoa()
    print("Todos os testes passaram!")
