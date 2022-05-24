#!/usr/bin/python
# main.py


"""
@author: Maxime Dréan.

Github: https://github.com/maximedrn
Telegram: https://t.me/maximedrn

Copyright © 2022 Maxime Dréan. All rights reserved.
Any distribution, modification or commercial use is strictly prohibited.
"""


# Selenium module imports: pip install selenium
from selenium.webdriver.support.ui import WebDriverWait as WDW
from selenium.common.exceptions import TimeoutException as TE

# Python internal imports.
from app.hcaptcha import hCaptcha
from app.utils.colors import GREEN, RED, RESET
from app.utils.const import DEMONSTRATION_URL


def demonstration(hcaptcha: object) -> None:
    """Demonstration of the hCAPTCHA solver."""
    try:
        print('Solving the hCAPTCHA.', end=' ')
        hcaptcha.driver.get(DEMONSTRATION_URL)  # hCAPTCHA solver test URL.
        # Check if the lenght of "data-hcaptcha-response" attribute is
        # not null. If it's not null, the hCAPTCHA is solved.
        WDW(hcaptcha.driver, 600).until(lambda _: len(hcaptcha.visible(
            '//div[@class="h-captcha"]/iframe').get_attribute(
                'data-hcaptcha-response')) > 0)
        print(f'{GREEN}Solved.{RESET}')
    except TE:  # Something went wrong.
        print(f'{RED}Failed.{RESET}')


if __name__ == '__main__':
    hcaptcha = hCaptcha(  # Initialize the hCAPTCHA class.
        browser=1, headless=False, comments=True, download=False)
    hcaptcha.download_userscript()  # Download the userscript.
    demonstration(hcaptcha)  # Demonstrate the hCAPTCHA solver.
