from rest_framework import status

# positive tests (happy paths)
##############################


def test_create_productionplan_payload1_status_code(client, example_payload1):
    response = client.post('/productionplan', example_payload1, format='json')
    assert response.status_code == status.HTTP_201_CREATED


def test_create_productionplan_payload1_schema_validation(client, example_payload1):
    response = client.post('/productionplan', example_payload1, format='json')
    assert response.headers['Content-Type'] == "application/json"

    for item in response.json():
        assert 'name' in item
        assert 'p' in item


def test_create_productionplan_payload1_load_validation1(client, example_payload1):
    response = client.post('/productionplan', example_payload1, format='json')
    total_power = 0
    for item in response.json():
        total_power += item["p"]
    assert total_power == example_payload1["load"]


def test_create_productionplan_payload1_load_validation2(client, example_payload2):
    response = client.post('/productionplan', example_payload2, format='json')
    total_power = 0
    for item in response.json():
        total_power += item["p"]
    assert total_power == example_payload2["load"]


def test_create_productionplan_payload1_load_validation(client, example_payload3):
    response = client.post('/productionplan', example_payload3, format='json')
    total_power = 0
    for item in response.json():
        total_power += item["p"]
    assert total_power == example_payload3["load"]


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


def test_create_productionplan_only_load_status_code(client):
    payload = {"load": 0}
    response = client.post('/productionplan', payload, format='json')
    assert response.status_code == status.HTTP_400_BAD_REQUEST


def test_create_productionplan_no_fuels_status_code(client):
    payload = {
        "load": 10,
        "fuels": {},
        "powerplants": []
    }
    response = client.post('/productionplan', payload, format='json')
    assert response.status_code == status.HTTP_400_BAD_REQUEST


def test_create_productionplan_load_but_no_powerplants_status_code(client):
    payload = {
        "load": 10,
        "fuels": {
            "gas(euro/MWh)": 13.4,
            "kerosine(euro/MWh)": 50.8,
            "co2(euro/ton)": 20,
            "wind(%)": 60
        },
        "powerplants": []
    }
    response = client.post('/productionplan', payload, format='json')
    assert response.status_code == status.HTTP_400_BAD_REQUEST
