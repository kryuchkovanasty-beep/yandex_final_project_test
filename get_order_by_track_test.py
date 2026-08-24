# Крючкова Анастасия, 46-я когорта — Финальный проект. Инженер по тестированию плюс

import pytest

import data
import sender_stand_request


@pytest.fixture
def track():
    # Подготовка данных
    response_create = sender_stand_request.post_new_order(data.order_body)
    return response_create.json()["track"]


def test_get_order_by_track(track):
    # Проверяет успешное получение заказа по его треку.
    response_get = sender_stand_request.get_order_by_track(track)

# Проверка
    assert response_get.status_code == 200
