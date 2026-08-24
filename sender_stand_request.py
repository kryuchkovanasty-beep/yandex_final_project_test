# Крючкова Анастасия, 46-я когорта — Финальный проект. Инженер по тестированию плюс
import requests
import configuration
import data

def post_new_order(order_body):
    #Отправляет POST-запрос. Создаёт новый заказ.
    return requests.post(
        configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,
        json=order_body,
        headers=data.headers
    )


def get_order_by_track(track):
    #Отправляет GET-запрос.Получения заказа по номеру трека
    return requests.get(
        configuration.URL_SERVICE + configuration.GET_ORDER_PATH,
        params={"t": track}
    )
