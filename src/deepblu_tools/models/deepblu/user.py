from datetime import datetime
from deepblu_tools.models import uddf as um 


# Deepblu User
class DeepbluUser:
    def __init__(self):
        self.logged_in = False
        self.auth_code = None

    # Populate DeepbluUser properties with JSON data returned from API
    def update(self, user_data):
        self.user_id = user_data.get("ownerId")
        self.first_name = user_data.get("firstName")
        self.last_name = user_data.get("lastName")
        self.email = user_data.get("email")
        self.gender = user_data.get("gender")
        birthday = user_data.get("Birthday", {})
        if birthday:
            self.birthday = datetime(
                int(birthday.get("Year")),
                int(birthday.get("Month")),
                int(birthday.get("Day")),
            )

        return self

    def to_person_type(self):
        if not self.logged_in:
            return None

        return um.PersonType(
            id=f"deepblu_user_{ self.user_id }",
            personal=um.PersonalType(
                firstname=self.first_name,
                lastname=self.last_name,
                sex=getattr(um.SexType, self.gender.upper()),
                birthdate=um.EncapsulatedDateTimeType(self.birthday.isoformat())
            ),
            contact=um.ContactType(email=self.email)
        )
