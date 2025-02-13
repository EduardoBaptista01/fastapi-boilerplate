def test_create_todo(client):
    response = client.post("/todos", json={"title": "Write tests"})
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Write tests"
    assert data["completed"] is False

def test_get_todos(client):
    response = client.get("/todos")
    assert response.status_code == 200
    todos = response.json()
    assert len(todos) == 1
    assert todos[0]["title"] == "Write tests"

def test_delete_todo(client):
    # Get first todo ID
    response = client.get("/todos")
    todo_id = response.json()[0]["id"]

    # Delete it
    response = client.delete(f"/todos/{todo_id}")
    assert response.status_code == 200

    # Verify it's gone
    response = client.get("/todos")
    assert response.json() == []
