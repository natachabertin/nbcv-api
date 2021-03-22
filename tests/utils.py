def get_the_first_id(entity, client):
    response = client.get(f"/{entity}/")
    return response.json()[0]['id']
