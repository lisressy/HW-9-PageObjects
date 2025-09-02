from selene import browser

from pages.PageRegistration import RegistrationPage
import os
import pytest

def test_registration():
    page = RegistrationPage()

    page.open() \
        .fill_fn("John") \
        .fill_ln("Doe") \
        .fill_email("lisressy@test.com") \
        .fill_phone_number("1122334455") \
        .fill_address("Ghandi str., 11") \
        .fill_subject("Math") \
        .choose_gender("Male") \
        .choose_hobbies("Reading") \
        .avatar(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'resources', 'avatar.png'))) \
        .choose_birthday(day=15, month='May', year='1990') \
        .choose_state("NCR") \
        .choose_city("Delhi") \
        .submit_click() \

    page.should_have_registered(
        full_name='John Doe',
        email='lisressy@test.com',
        phone='1122334455',
        address='Ghandi str., 11',
        subjects='Math',
        hobbies='Reading',
        state_city='NCR Delhi',
        gender='Male',
        avatar_name='avatar.png'
    )

