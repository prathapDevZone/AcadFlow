from datetime import datetime

class Academy:

    def __init__(self,
        academy_id:str,
        academy_code: str,
        academy_name: str,
        owner_name: str,
        email: str,
        mobile: str,
        address: str,
        city: str,
        state: str,
        country: str,
        status: str="Active",
        ):

        self.academy_id =academy_id
        self.academy_code = academy_code
        self.academy_name = academy_name
        self.owner_name = owner_name
        self.email = email
        self.mobile = mobile
        self.address = address
        self.city = city
        self.state = state
        self.country = country
        self.status = status

        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        return (
            f"\nAcademy Code : {self.academy_code}"
            f"\nAcademy Name : {self.academy_name}"
            f"\nOwner Name   : {self.owner_name}"
            f"\nEmail        : {self.email}"
            f"\nMobile       : {self.mobile}"
            f"\nAddress      : {self.address}"
            f"\nCity         : {self.city}"
            f"\nState        : {self.state}"
            f"\nCountry      : {self.country}"
            f"\nStatus       : {self.status}"
        )