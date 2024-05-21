import enum 

class LessonChoiceState(enum.Enum):
    NEUTRAL = "NEUTRAL"
    ACCEPT = "ACCEPT"
    NOT_ACCEPT = "NOT_ACCEPT"
    IGNORE = "IGNORE"