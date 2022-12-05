import datetime


class Lesson:
    def __init__(self, title: str, description: list[str], start: datetime.datetime, end: datetime.datetime) -> None:
        self.title: str = title
        self.description: list[str] = description

        self.start: datetime.time = start
        self.end: datetime.time = end

    @classmethod
    def from_skola24_data(cls, data: dict[str, ], year: int,  week: int):
        date = date_from_week(year, week, data["dayOfWeekNumber"] - 1)
        return cls(data["texts"][0],
                   data["texts"][1:],
                   merge_date_and_time(date, parse_time(data["timeStart"])),
                   merge_date_and_time(date, parse_time(data["timeEnd"])),
                   )

    def __repr__(self) -> str:
        return f"Lesson({self.title} at {self.date} {self.start_time}-{self.end_time})"


def merge_date_and_time(date: datetime.date, time: datetime.time) -> datetime.datetime:
    return datetime.datetime(date.year, date.month, date.day, time.hour, time.minute, time.second)


def parse_time(s: str) -> datetime.time:
    times = s.split(":")
    return datetime.time(hour=int(times[0]), minute=int(
        times[1]), second=int(times[2]))


def date_from_week(year: int, week: int, weekday: int) -> datetime.date:
    jan1 = datetime.date(year, 1, 1)
    day_of_year = week * 7 - jan1.weekday() + weekday
    return jan1 + datetime.timedelta(days=day_of_year)