from datetime import datetime
class MovieList:
    def __init__(self):
        self.movies = []
        self.rate = {}
    def add_movie(self, title):
        self.movies.append(title)
        date_added = datetime.now()
        formatted_datetime = date_added.strftime("%d-%m-%Y %I:%M:%S %p")
        return self.movies, formatted_datetime

    def rate_movie(self, title, rates):
        if title not in self.movies:
            return "movie not found", title
        if not (1 <= rates <= 5):
            return "rate must be between 1 and 5", rates
        self.rate.setdefault(title, []).append(rates)
        return title, rates

    def average_rating(self, title):
        if title not in self.rate or not self.rate[title]:
            return 0.0
        total = sum(self.rate[title])
        return total / len(self.rate[title])











