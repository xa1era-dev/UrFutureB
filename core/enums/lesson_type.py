import enum

class LessonType(str, enum.Enum):
    OK = "Онлайн курс"
    PRACTICE = "Практика"
    LECTURE = "Лекция"
    LABOROTORY = "Лабораторная работа"
    TEST = "Зачет"
    CERTIFICATE = "Аттестация"
    EXAM = "Экзамен"
    CONSULTATION = "Консультанция"