from rest_framework import status

# positive tests (happy paths)
##############################


def test_create_productionplan_payload1_status_code(client, example_payload1):
    response = client.post('/productionplan', example_payload1, format='json')
    assert response.status_code == status.HTTP_201_CREATED


def test_create_productionplan_payload2_status_code(client, example_payload2):
    response = client.post('/productionplan', example_payload2, format='json')
    assert response.status_code == status.HTTP_201_CREATED


def test_create_productionplan_payload3_status_code(client, example_payload3):
    response = client.post('/productionplan', example_payload3, format='json')
    assert response.status_code == status.HTTP_201_CREATED


# negative tests - invalid input
################################


def test_create_productionplan_empty_payload_status_code(client):
    response = client.post('/productionplan', format='json')
    assert response.status_code == status.HTTP_400_BAD_REQUEST


def test_create_productionplan_incomplete_data_status_code(client):
    payload = {"load": 0}
    response = client.post('/productionplan', payload, format='json')
    assert response.status_code == status.HTTP_400_BAD_REQUEST

    payload = {
        "load": 0,
        "fuels": {},
        "powerplants": []
    }
    response = client.post('/productionplan', payload, format='json')
    assert response.status_code == status.HTTP_400_BAD_REQUEST
