class InvalidStateTransitionError(Exception):
    """Returns Error for all Invalid State Transition."""
    def __init__(self,current_state, target_state,  message = "Invalid State Transition"):
        self.current_state = current_state
        self.target_state = target_state
        self.message = f"{message} from {current_state} to {target_state}"

def safe_transition(current_state, target_state, allowed_sources):
    if current_state not in allowed_sources:
        raise InvalidStateTransitionError(current_state, target_state)

class CheckOutLimitError(Exception):
    """Returns Error when Check Out Limit is reached."""
    pass

class MemberNotActiveError(Exception):
    """Returns Error when Member Not Active."""
    pass

class BookNotAvailableError(Exception):
    """Returns Error when Book Not Available."""
    pass
