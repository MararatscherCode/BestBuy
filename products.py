class Product:
	"""Represents a product in the store with name, price, quantity and active flag."""

	def __init__(self, name: str, price: float, quantity: int):
		if not isinstance(name, str) or not name.strip():
			raise Exception("Invalid product name")
		if not isinstance(price, (int, float)) or price < 0:
			raise Exception("Invalid product price")
		if not isinstance(quantity, int) or quantity < 0:
			raise Exception("Invalid product quantity")

		self.name = name
		self.price = float(price)
		self.quantity = quantity
		self.active = True

	def get_quantity(self) -> int:
		return self.quantity

	def set_quantity(self, quantity: int):
		if not isinstance(quantity, int) or quantity < 0:
			raise Exception("Invalid quantity value")
		self.quantity = quantity
		if self.quantity == 0:
			self.deactivate()

	def is_active(self) -> bool:
		return bool(self.active)

	def activate(self):
		self.active = True

	def deactivate(self):
		self.active = False

	def show(self):
		# Format price without unnecessary decimals when possible
		price_display = int(self.price) if self.price.is_integer() else self.price
		print(f"{self.name}, Price: {price_display}, Quantity: {self.quantity}")

	def buy(self, quantity: int) -> float:
		if not isinstance(quantity, int) or quantity <= 0:
			raise Exception("Purchase quantity must be a positive integer")
		if not self.is_active():
			raise Exception("Product is not active")
		if quantity > self.quantity:
			raise Exception("Not enough quantity available")

		total = float(self.price * quantity)
		self.quantity -= quantity
		if self.quantity == 0:
			self.deactivate()
		return total


if __name__ == "__main__":
	bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
	mac = Product("MacBook Air M2", price=1450, quantity=100)

	print(bose.buy(50))
	print(mac.buy(100))
	print(mac.is_active())

	bose.show()
	mac.show()

	bose.set_quantity(1000)
	bose.show()

