"""
    Finds a user by email.
    :param input_email: The email of the user being searched for
    :return: the user with an email matching input_email
    """
    return User.objects.filter(email=input_email).first()

def full_name(self):
    return self.first_name + ' ' + self.last_name

def safe_name(self):
    return mark_safe(self.first_name)

@staticmethod
def validate_signup_form(form):
    err_list = []
    if len(form["password"]) < 6:
        err_list.append("Password minimum 6 characters")
    if len(form["password"]) > 40:
        err_list.append("Password maximum 40 characters")
    if form["password"] != form["confirm"]:
        err_list.append("Password and Confirm Password does not match")
