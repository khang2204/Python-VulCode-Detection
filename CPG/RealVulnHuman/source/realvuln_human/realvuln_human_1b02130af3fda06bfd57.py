if self.user_id != None:
        return
    # User with highest id
    user = User.objects.order_by("-user_id").first()
    if user is not None:
        # Set the new user's id to be one higher
        self.user_id = user.user_id + 1
    else:
        self.user_id = 1

def hash_password(self):
    if self.password is not None:
        hash_obj = hashlib.md5(self.password.encode())
        self.password = hash_obj.hexdigest()

def generate_token(self):
    """
    Generates and sets an auth token for a user.
    :return: None
    """
    self.auth_token = hashlib.md5((self.email + str(random.randint(1,1000000))).encode()).hexdigest()

@staticmethod
def find_by_email(input_email):
