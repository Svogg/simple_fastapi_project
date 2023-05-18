from conftest import client


def test_add_tour():
    response = client.post(
        '/tour/add_tour',
        json={
            "tour_id": 0,
            "tour_name": "test",
            "city_from": "test",
            "city_to": "test",
            "airline_name": "test",
            "flight_start": "2023-05-14T18:41:06.602Z",
            "flight_end": "2023-05-14T18:41:06.602Z",
            "flight_price": 1
        }
    )
    assert response.status_code == 200
