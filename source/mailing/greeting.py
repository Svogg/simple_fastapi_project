from email.message import EmailMessage

import aiosmtplib


async def greet(appname: str, password: str, user_email: str, username: str):
    """
    Рассылка приветственного письма, после регистрации пользователя
    :param appname: str your google mail
    :param password: str your google app password
    :param user_email: str registered user email
    :param username: str username
    :return: str Приветсвенное письмо
    """
    message = EmailMessage()
    message["From"] = appname
    message["To"] = user_email
    message["Subject"] = "Sent via https://github.com/Svogg fastapi pet application "
    message.set_content("Dear {}!\nThanks for registration in my pet application ;)".format(username))
    await aiosmtplib.send(
        message,
        hostname="smtp.gmail.com",
        port=465,
        use_tls=True,
        username=appname,
        password=password
    )
