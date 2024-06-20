from enum import Enum

class ChangeStatus(Enum):
    CREATED = "created"
    IN_MODIFICATION = "in_modification"
    IN_REVIEW = "in_review"
    ACCEPTED = "accepted"
    REJECTED = "rejected"
