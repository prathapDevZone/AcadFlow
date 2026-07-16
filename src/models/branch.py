from datetime import datetime

class Branch:
    def __init__(
        self,
        branch_id : str,
        branch_code : str,
        academy_id : str,
        branch_name : str,
        email : str,
        mobile : str,
        address : str,
        city : str,
        state : str,
        country : str,
        status : str = "Active",
    ):

        self.branch_id = branch_id
        self.branch_code = branch_code
        self.academy_id = academy_id

        self.branch_name = branch_name

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
            f"\nBranch Code : {self.branch_code}"
            f"\nBranch Name : {self.branch_name}"
            f"\nCity        : {self.city}"
            f"\nState       : {self.state}"
            f"\nCountry     : {self.country}"
            f"\nStatus      : {self.status}"
        )