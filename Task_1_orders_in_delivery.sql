# Крючкова Анастасия, 46-я когорта — Финальный проект. Инженер по тестированию плюс
SELECT c.login,
       COUNT(o.id) AS orders_count
FROM "Couriers" AS c
INNER JOIN "Orders" AS o
        ON c.id = o."courierId"
WHERE o."inDelivery" = true
GROUP BY c.login;