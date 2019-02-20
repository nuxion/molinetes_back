from werkzeug.security import check_password_hash, generate_password_hash
from molinetes.ext.sql import db
from molinetes.models import User




class Users:

    @staticmethod
    def find(email):
        """
        It gets the firts element that match with email.
        """
        return User.query.filter(User.email == email).first()

    @staticmethod
    def find_all(_dict = False):

        return User.query.all()

    @staticmethod
    def validate_credentials(username, password):
        u = Users.find(username)
        if u:
            if check_password_hash(u.password, password):
                return True

        return False


