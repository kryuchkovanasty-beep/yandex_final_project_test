# Крючкова Анастасия, 46-я когорта — Финальный проект. Инженер по тестированию плюс

import data
import sender_stand_request

def test_get_order_by_track():
    #Проверяет что созданный заказ можно получить по его номеру.
    response_create = sender_stand_request.post_new_order(
        data.order_body
    )

    assert response_create.status_code == 201

    track = response_create.json()["track"]

    response_get = sender_stand_request.get_order_by_track(track)

    assert response_get.status_code == 200
    print(f"Код ответа при получении заказа: {response_get.status_code}")
    print("Тест успешно пройден.")