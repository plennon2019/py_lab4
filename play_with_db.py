from models import SessionLocal, User, Address

# Start a session (think: open a connection)
session = SessionLocal()

# --- Create (INSERT) ---
address = Address(street="123 Main St", number=1, county="Galway", country="Ireland", eircode="H91X77E")
session.add(address)
session.commit()
session.refresh(address)

user = User(name="Paul", email="paul@example.com", age=21, address_id=address.id)
session.add(user)
session.commit()
session.refresh(user)
print(f"Added user: {user.name} with address: {address.street}")

# --- Read (SELECT) ---
users = session.query(User).all()
for u in users:
    print(f"User: {u.name}, Email: {u.email}, Address: {u.address.street}")

# --- Delete (DELETE) ---
session.delete(user)
session.commit()
print("Deleted user:", user.name)

session.close()
