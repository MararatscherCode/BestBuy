import products
import store
from typing import List, Tuple


def start(store_obj: store.Store):
	"""Start a simple CLI for interacting with the store.

	Menu:
	1. List all products in store
	2. Show total amount in store
	3. Make an order
	4. Quit
	"""
	while True:
		print("\nWelcome to the store - choose an option:")
		print("1. List all products in store")
		print("2. Show total amount in store")
		print("3. Make an order")
		print("4. Quit")

		choice = input("Enter option (1-4): ").strip()
		if choice == "1":
			products_list = store_obj.get_all_products()
			if not products_list:
				print("No active products in store.")
			else:
				for idx, p in enumerate(products_list, start=1):
					print(f"{idx}.", end=" ")
					p.show()

		elif choice == "2":
			print(f"Total items in store: {store_obj.get_total_quantity()}")

		elif choice == "3":
			# Build shopping list interactively
			products_list = store_obj.get_all_products()
			if not products_list:
				print("No active products to order.")
				continue

			print("Select products to order by number (empty line to finish):")
			for idx, p in enumerate(products_list, start=1):
				print(f"{idx}. {p.name} (Price: {int(p.price) if p.price.is_integer() else p.price}, Qty: {p.get_quantity()})")

			shopping_list: List[Tuple[products.Product, int]] = []
			while True:
				selection = input("Product number (or press Enter to finish): ").strip()
				if not selection:
					break
				if not selection.isdigit() or int(selection) < 1 or int(selection) > len(products_list):
					print("Invalid product number")
					continue
				prod_idx = int(selection) - 1
				qty_str = input("Quantity: ").strip()
				if not qty_str.isdigit() or int(qty_str) <= 0:
					print("Invalid quantity")
					continue
				qty = int(qty_str)
				shopping_list.append((products_list[prod_idx], qty))

			if not shopping_list:
				print("No items selected for order.")
				continue

			try:
				total = store_obj.order(shopping_list)
				print(f"Order placed. Total cost: {total} dollars")
			except Exception as e:
				print(f"Failed to place order: {e}")

		elif choice == "4":
			print("Goodbye!")
			break
		else:
			print("Invalid option, please choose 1-4.")


if __name__ == "__main__":
	# setup initial stock of inventory
	product_list = [
		products.Product("MacBook Air M2", price=1450, quantity=100),
		products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
		products.Product("Google Pixel 7", price=500, quantity=250),
	]

	best_buy = store.Store(product_list)
	start(best_buy)

