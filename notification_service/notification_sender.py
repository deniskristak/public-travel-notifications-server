from firebase_admin import messaging, initialize_app, credentials

from config.fcm_certificate import cert
from helpers.singleton import Singleton


# this is a class that is responsible for sending notifications. just instantiate it and use send_notification method
# (passing token as argument)
class NotificationSender(metaclass=Singleton):

    def __init__(self):
        # this must happen only once - this is why this class is a singleton
        self.__init_fcm_app()

    # setup of Firebase app
    @staticmethod
    def __init_fcm_app():
        initialize_app(credential=credentials.Certificate(cert=cert))

    # main method used to send notifications
    # todo: parametrize title and body
    # todo: add error handling
    def send_notification(self, device_token):
        title = "Notification from python code"
        body = f"Made with love in Python, for device with token: {device_token} "

        notification_instance = messaging.Notification(title=title, body=body)

        message_instance = messaging.Message(notification=notification_instance, token=device_token)

        messaging.send(message_instance)
