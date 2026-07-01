from abc import ABC, abstractmethod

class Notification(ABC):
    @abstractmethod
    def send_notification(self, member, message: str):
        pass

class SMSNotification(Notification):
    def send_notification(self, member, message: str):
        print(f"Sending SMS to {member.name}: {message}")
