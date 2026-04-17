class CinemaBar:
    @staticmethod
    def sell_product(product: str, customer: str | object) -> None:
        name = customer.name if hasattr(customer, "name") else customer
        print(f"Cinema bar sold {product} to {name}.")
