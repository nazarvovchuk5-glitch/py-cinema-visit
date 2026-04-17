from app.people.customer import Customer
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list, hall_number: int, cleaner: str, movie: str):
    customer_list = [Customer(name=customer["name"], food=customer["food"]) for customer in customers]
    hall = CinemaHall(hall_number)
    cleaner_instance = Cleaner(cleaner)

    for customer in customer_list:
        CinemaBar.sell_product(product=customer.food, customer=customer.name)

    hall.movie_session(movie_name=movie, customers=customers, cleaning_staff=cleaner)