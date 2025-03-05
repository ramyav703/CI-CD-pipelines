import requests

ENDPOINT = "https://todo.pixegami.io"

response = requests.get(ENDPOINT)
print(response)

data = response.json()
print(data)

status_code = response.status_code
print(status_code)

def test_enpoint():
    response = requests.get(ENDPOINT)
    assert response.status_code == 200
    
def test_create_task():
    data = {
        "content": "Casper",
        "user_id": "test_user",
        "is_done": False,
    }
    create_test_response = requests.put(ENDPOINT + "/create-task", json = data)
    assert create_test_response.status_code == 200
    item = create_test_response.json()
    print(item)
    task_id = item["task"]["task_id"]
    get_task_response = requests.get(ENDPOINT + f"/get-task/{task_id}")
    assert get_task_response.status_code == 200
    task_data = get_task_response.json()
    print(task_data)


