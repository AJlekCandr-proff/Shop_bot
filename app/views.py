"""Представления для пользователя. Текстовые сообщения. """


def msg_product(product: str, product_cost: float) -> str:
    return f"""
Просмотр товара <b>{product}</b>

➖➖➖➖➖➖➖➖➖➖➖
Цена товара: {product_cost}₽
➖➖➖➖➖➖➖➖➖➖    """


def msg_payment(sum: float) -> str:
    return f"""
➖➖➖➖➖➖➖➖➖➖➖
💳 Реквизиты: 

       <code>**** **** **** ****</code>

❗️ВАЖНО: Переводите средства точно и аккуратно!
Сумма к пополнению: {sum}
➖➖➖➖➖➖➖➖➖➖ """


def msg_rules() -> str:
    return """
<b>♦ Правила Магазина:

1. Обязательно перепроверяем корректность данных для пополнения кошелька.
1.1. Если вы произвели пополнение баланса бота: без комментария, неверной суммы, случайно, и т.д. - 
напишите администратору бота.

2. Пользователь согласен, что время обработки заявки занимает до 1 рабочего дня.
2.1 Флуд, мат, оскорбления, невежливое общение, введение в заблуждение, обман - причины ограничения поддержки/доступа 
к боту без дальнейшей помощи в разбирательстве вашей проблемы.
2.2. Фиксируйте покупку на видео. Начинайте запись видео до того как нажали на кнопку "купить", 
не завершая запись продолжайте проверку товара, если есть такая возможность.
2.3. При невалидности товара замена выдаётся при наличии доказательств в течение 20 минут после покупки.


3.Действия администрации не обсуждается.</b> """


def msg_user(user_id: int, balance: float, name: str) -> str:
    return f"""
📌 <a href="tg: user?id={user_id}"><i>{name}</i></a>, твой профиль 📊
🆔 Telegram: <ins>{user_id}</ins>
👤 Имя: {name}
💸 Balance: {balance} ₽ """


def msg_check_payment(user_id: int, sum: float, name: str) -> str:
    return f"""
📄 Новый чек об пополнении баланса 🔔 
📌 <a href="tg: user?id={user_id}"><i>{name}</i></a> 
🆔 Telegram: <ins>{user_id}</ins>
👤 Имя: {name}
💸 Сумма: {sum} ₽ """

