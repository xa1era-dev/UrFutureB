class Timetable:
    def __init__(self, week_length, classes_at_day):
        self.week_length = week_length
        self.classes_at_day = classes_at_day
        self.time_matrix = [0 for i in range(week_length * classes_at_day)]

    def can_add(self, day, start, end) -> bool:
        position, upper_bound = self.get_position_and_upperbound(day, start, end)

        for i in range(position, upper_bound):
            if self.time_matrix[i] == 1:
                return False

        return True

    def add_without_validation(self, day, start, end):
        position, upper_bound = self.get_position_and_upperbound(day, start, end)

        for i in range(position, upper_bound):
            self.time_matrix[i] = 1

    def get_position_and_upperbound(self, day, start, end):
        self.validate_input(day, start, end)

        position = day * self.classes_at_day + start
        upper_bound = position + (end - start + 1)

        return position, upper_bound

    def validate_input(self, day, start, end):
        if start > end:
            raise Exception("Start should be less or equal to end.")

        if day < 0 or day > self.week_length:
            raise Exception(f"Day must be positive and less or equal to week length. Got {day}")

        if start < 0 or start > self.classes_at_day:
            raise Exception(f"Start must be positive and less or equal to classes at day. Got {start}.")

        if end < 0 or end > self.classes_at_day:
            raise Exception(f"End must be positive and less or equal to classes at day. Got {end}.")
