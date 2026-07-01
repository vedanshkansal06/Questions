from notifications.Notification import Notification
from core.Library import Library
from States import LendingStatus

class NotificationService:
    def __init__(self, notification_strategy: Notification):
        self.notification_strategy = notification_strategy

    def notify(self, member, message: str):
        self.notification_strategy.send_notification(member, message)

    def check_over_due_loan(self, current_date):
        library = Library()
        for lending in library.book_lending:
            if lending.status in [LendingStatus.Active, LendingStatus.Renewed] and current_date > lending.due_date:
                member = library.get_member(lending.member_barcode)
                library.notification_service.notify(member, f"The Book '{lending.book_item.book.title}' is Overdue!!")
                return True
        return False