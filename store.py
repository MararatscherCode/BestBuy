import products
from typing import List, Tuple


class Store:
	"""Container for Product instances with operations across multiple products."""

	def __init__(self, products_list: List[products.Product] = None):
		self.products = list(products_list) if products_list else []

	def add_product(self, product: products.Product):
		if product in self.products:
			return
		self.products.append(product)

	def remove_product(self, product: products.Product):
		try:
			self.products.remove(product)
		except ValueError:
			raise Exception("Product not found in store")

	def get_total_quantity(self) -> int:
		return sum(p.get_quantity() for p in self.products)

	def get_all_products(self) -> List[products.Product]:
		return [p for p in self.products if p.is_active()]

	def order(self, shopping_list: List[Tuple[products.Product, int]]) -> float:
		"""Place an order given a list of (Product, quantity) tuples.

		Each product must exist in the store. Raises an Exception when a
		product is not available or a purchase fails. Returns total price.
		"""
		total = 0.0
		for item, qty in shopping_list:
			if item not in self.products:
				raise Exception("Product not in store")
			total += item.buy(qty)
		return total


if __name__ == "__main__":
	product_list = [
		products.Product("MacBook Air M2", price=1450, quantity=100),
		products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
		products.Product("Google Pixel 7", price=500, quantity=250),
	]

	best_buy = Store(product_list)
	prods = best_buy.get_all_products()
	print(best_buy.get_total_quantity())
	print(best_buy.order([(prods[0], 1), (prods[1], 2)]))

