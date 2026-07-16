from models.academy import Academy
from models.branch import Branch
from utils.id_generator import generate_uuid

academy = Academy(
    academy_id=generate_uuid(),
    academy_code="JB",
    academy_name="JB's Academy",
    owner_name="John",
    email="jbacademy@gmail.com",
    mobile="9876543210",
    address="Anna Nagar",
    city="Chennai",
    state="Tamil Nadu",
    country="India"
)

branch = Branch(
    branch_id=generate_uuid(),
    branch_code="JB-AN01",
    academy_id=academy.academy_id,   # Relationship
    branch_name="Anna Nagar Branch",
    email="annanagar@jbacademy.com",
    mobile="9876543211",
    address="Anna Nagar",
    city="Chennai",
    state="Tamil Nadu",
    country="India"
)

print(academy)
print(branch)