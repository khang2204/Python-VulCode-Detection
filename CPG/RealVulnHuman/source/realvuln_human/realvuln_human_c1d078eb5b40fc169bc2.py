from flask import render_template, request, redirect, flash
from bcrypt import gensalt, hashpw
from app import app
from models import Session, User, RegistrationCode
from forms.registration_form import RegistrationForm


def validate_token(code: str, session: Session) -> Union[str, None]:
    try:
        result = session.execute(
            text(f"""
                SELECT id, code FROM {RegistrationCode.__tablename__} WHERE code = '{code}'
            """)).first()

        if result is None:
            return None

        return result.id
    except OperationalError:
        return None


@app.route('/signup', methods=['GET'])
