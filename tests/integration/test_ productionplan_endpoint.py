from rest_framework import status


def test_create_productionplan_status_code(client):
    response = client.post('/productionplan')
    assert response.status_code == status.HTTP_201_CREATED
