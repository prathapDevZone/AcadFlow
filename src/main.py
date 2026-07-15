from models.academy import Academy
from utils.id_generator import generate_uuid

academy = Academy(
    academy_id=generate_uuid(),
    academy_code="JB001",
    academy_name="JB's Academy",
    owner_name="John",
    email="jbacademy@gmail.com",
    mobile="9876543210",
    address="Anna Nagar",
    city="Chennai",
    state="Tamil Nadu",
    country="India"
)

print(academy)