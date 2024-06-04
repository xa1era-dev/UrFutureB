class TimetableBuilder:
    def __init__(self, week_length, lessons_at_day):
        self.week_length = week_length
        self.classes_at_day = lessons_at_day
        self.time_matrix = [0 for i in range(week_length * lessons_at_day)]

    def can_add_lesson(self, day, start, end) -> bool:
        position, upper_bound = self.get_position_and_upperbound(day, start, end)

        for i in range(position, upper_bound):
            if self.time_matrix[i] == 1:
                return False

        return True

    def add_lesson(self, day, start, end):
        position, upper_bound = self.get_position_and_upperbound(day, start, end)

        for i in range(position, upper_bound):
            self.time_matrix[i] = 1

    def get_time_matrix(self):
        return self.time_matrix

    def get_position_and_upperbound(self, day, start, end):
        position = day * self.classes_at_day + start
        upper_bound = position + (end - start + 1)
        return position, upper_bound
