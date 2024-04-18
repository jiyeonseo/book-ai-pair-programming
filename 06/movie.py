import uuid
from uuid import UUID
from datetime import datetime

class Movie:
    id : UUID
    title: str

    def __init__(self, title: str):
        self.id = uuid.uuid4()
        self.title = title

class Ticket:
    id: UUID
    movie_id: str
    time: datetime 
    
    def __init__(self, movie: Movie, time: datetime):
        self.id = uuid.uuid4()
        self.movie_id = movie.id
