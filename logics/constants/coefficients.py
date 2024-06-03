from core import LessonRole, LessonChoiceState

MIN_COEFFICIENT = 0.25

teacher_role_to_coefficient = {
    LessonRole.PRACTICIAN: 1,
    LessonRole.LECTOR: 0.5,
    LessonRole.PROCTOR: 0.75,
    LessonRole.ASSISTANT: 0.75,
    LessonRole.LABORANT: 0.75
}

time_state_to_coefficient = {
    LessonChoiceState.ACCEPT: 1,
    LessonChoiceState.NEUTRAL: 0.75,
    LessonChoiceState.NOT_ACCEPT: 0.5,
    LessonChoiceState.IGNORE: MIN_COEFFICIENT
}
