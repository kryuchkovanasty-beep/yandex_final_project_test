# Крючкова Анастасия, 46-я когорта — Финальный проект. Инженер по тестированию плюс

import pytest

import data
import sender_stand_request


@pytest.fixture
def track():
    response_create = sender_stand_request.post_new_order(data.order_body)
    return response_create.json()["track"]


def test_get_order_by_track(track):
    #Проверяет, что по треку заказа можно получить данные о заказе.
    response_get = sender_stand_request.get_order_by_track(track)

    assert response_get.status_code == 200
