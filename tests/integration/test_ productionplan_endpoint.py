from rest_framework import status

# positive tests (happy paths)
##############################


def test_create_productionplan_status_code(client, example_payload1):
    response = client.post('/productionplan', example_payload1, format='json')
    assert response.status_code == status.HTTP_201_CREATED

    payload = {
        "load": 0,
        "fuels": {},
        "powerplants": []
    }
    response = client.post('/productionplan', payload, format='json')
    assert response.status_code == status.HTTP_201_CREATED


# negative tests - invalid input
################################


def test_create_productionplan_empty_payload_status_code(client):
    response = client.post('/productionplan', format='json')
    assert response.status_code == status.HTTP_400_BAD_REQUEST


def test_create_productionplan_imcomplete_data_status_code(client):
    payload = {"load": 0}
    response = client.post('/productionplan', payload, format='json')
    assert response.status_code == status.HTTP_400_BAD_REQUEST
