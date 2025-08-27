from selene import browser, have
from selenium.webdriver import Keys



class RegistrationPage:
    def __init__(self):
        self.url = 'https://demoqa.com/automation-practice-form'

    def open(self):
        browser.open(self.url)
        return self

    def fill_fn(self, fn):
        browser.element('#firstName').type(fn)
        return self

    def fill_ln(self, ln):
        browser.element('#lastName').type(ln)
        return self

    def fill_email(self, email):
        browser.element('#userEmail').type(email)
        return self

    def fill_phone_number(self, phone_number):
        browser.element('#userNumber').type(phone_number)
        return self

    def fill_address(self, address):
        browser.element('#currentAddress').type(address)
        return self

    def fill_subject(self, subject):
        browser.element('#subjectsInput').type(subject).press_enter()
        return self


    def choose_gender(self, gender):
        if gender == 'Male':
            browser.element('label[for="gender-radio-1"]').click()
        elif gender == 'Female':
            browser.element('label[for="gender-radio-2"]').click()
        elif gender == 'Other':
            browser.element('label[for="gender-radio-3"]').click()
        return self

    def choose_hobbies(self, hobby):
        if hobby == 'Sports':
            browser.element('label[for="hobbies-checkbox-1"]').click()
        elif hobby == 'Reading':
            browser.element('label[for="hobbies-checkbox-2"]').click()
        elif hobby == 'Music':
            browser.element('label[for="hobbies-checkbox-3"]').click()
        return self


    def avatar(self, file_path):
        browser.element('#uploadPicture').set_value(file_path)
        return self


    def choose_birthday(self, day, month, year):
        date = browser.element('#dateOfBirthInput')
        date.click()
        date.send_keys(Keys.CONTROL + 'a')
        date.send_keys(str(day) + " " + str(month) + " " + str(year))
        date.press_enter()
        return self

    def choose_state(self, state):
        browser.element('#state').click()
        #browser.element(f'//div[text()="{state}"]').wait().be_clickable().click()
        browser.element(f'//div[text()="{state}"]').click()
        return self

    def choose_city(self, city):
        browser.element('#city').click()
        browser.element(f'//div[text()="{city}"]').click()
        return self

    def submit_click(self):
        browser.element('#submit').click()
        return self

    def should_have_registered(self, full_name=None, email=None, phone=None, address=None, subjects=None, hobbies=None,
                               state_city=None, gender=None, avatar_name=None):
        modal = browser.element('.modal-content')
        if full_name:
            modal.should(have.text(full_name))
        if email:
            modal.should(have.text(email))
        if phone:
            modal.should(have.text(phone))
        if address:
            modal.should(have.text(address))
        if subjects:
            for subject in subjects:
                modal.should(have.text(subject))
        if hobbies:
            for hobby in hobbies:
                modal.should(have.text(hobby))
        if state_city:
            modal.should(have.text(state_city))
        if gender:
            modal.should(have.text(gender))
        if avatar_name:
            modal.should(have.text(avatar_name))
        return self
