from rest_framework import status

# positive tests (happy paths)
##############################

def test_create_productionplan_status_code(client, example_payload1):
    response = client.post('/productionplan', example_payload1, format='json')
    assert response.status_code == status.HTTP_201_CREATED
