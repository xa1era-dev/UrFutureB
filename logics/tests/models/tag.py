class Tag:
    """
    Этот класс является временным и предназначен только для тестирования.
    Не используйте его в качестве основной модели Тега в бизнес-логике.
    """
    def __init__(self, id):
        self.id = id

    def __eq__(self, other):
        if not isinstance(other, Tag):
            raise TypeError("Нельзя сравнивать объекты других классов с объектами класса Tag")

        return self.id == other.id

    def __ne__(self, other):
        return not self == other

    def __hash__(self):
        return hash(self.id)
