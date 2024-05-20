import enum 

class LessonChoiceState(enum.Enum):
    NEUTRAL = 0
    ACCEPT = 1
    NOT_ACCEPT = 2
    IGNORE = 3