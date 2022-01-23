"""
@author: Maxime.

Github: https://github.com/maximedrn
Demonstration website: https://maximedrn.github.io/hcaptcha-test/
Version: 1.0
"""

# Colorama module: pip install colorama
from colorama import init, Fore, Style

# Selenium module imports: pip install selenium
from selenium import webdriver
from selenium.common.exceptions import TimeoutException as TE
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as WDW
from selenium.webdriver.common.by import By

# Python default import.
import sys
import os


"""Colorama module constants."""
init(convert=True)  # Init colorama module.
red = Fore.RED  # Red color.
green = Fore.GREEN  # Green color.
yellow = Fore.YELLOW  # Yellow color.
reset = Style.RESET_ALL  # Reset color attribute.


class hCaptcha:
    """Main class of the hCaptcha solver."""

    def __init__(self) -> None:
        """Set path of used file and start webdriver."""
        self.webdriver_path = 'assets/chromedriver.exe'
        self.extension_path = 'assets/Tampermonkey.crx'
        self.driver = self.webdriver()  # Start new webdriver.

    def webdriver(self):
        """Start webdriver and return state of it."""
        options = webdriver.ChromeOptions()  # Configure options for Chrome.
        options.add_extension(self.extension_path)  # Add extension.
        options.add_experimental_option('prefs', {'intl.accept_languages': 'en,en_US'})  # Set webdriver language to English.
        # options.add_argument("headless")  # Headless ChromeDriver.
        options.add_argument('log-level=3')  # No logs is printed.
        options.add_argument('--mute-audio')  # Audio is muted.
        options.add_argument("--enable-webgl-draft-extensions")
        options.add_argument("--ignore-gpu-blocklist")
        driver = webdriver.Chrome(self.webdriver_path, options=options)
        driver.maximize_window()  # Maximize window to reach all elements.
        return driver

    def element_clickable(self, element: str) -> None:
        """Click on element if it's clickable using Selenium."""
        WDW(self.driver, 5).until(EC.element_to_be_clickable(
            (By.XPATH, element))).click()

    def element_visible(self, element: str):
        """Check if element is visible using Selenium."""
        return WDW(self.driver, 20).until(EC.visibility_of_element_located(
            (By.XPATH, element)))

    def window_handles(self, window_number: int) -> None:
        """Check for window handles and wait until a specific tab is opened."""
        WDW(self.driver, 30).until(lambda _: len(
            self.driver.window_handles) == window_number + 1)
        # Switch to asked tab.
        self.driver.switch_to.window(self.driver.window_handles[window_number])

    def download_userscript(self) -> None:
        """Download the hCaptcha solver userscript."""
        try:
            print('Installing the hCaptcha solver userscript.', end=' ')
            self.window_handles(1)  # Wait that Tampermonkey tab loads.
            self.driver.get('https://greasyfork.org/en/scripts/425854-hcaptcha'
                            '-solver-automatically-solves-hcaptcha-in-browser')
            # Click on "Install" Greasy Fork button.
            self.element_clickable('//*[@id="install-area"]/a[1]')
            # Click on "Install" Tampermonkey button.
            self.window_handles(2)  # Switch on Tampermonkey install tab.
            self.element_clickable('//*[@value="Install"]')
            self.window_handles(1)  # Switch to Greasy Fork tab.
            self.driver.close()  # Close this tab.
            self.window_handles(0)  # Switch to main tab.
            print(f'{green}Installed.{reset}')
        except TE:
            sys.exit(f'{red}Failed.{reset}')

    def demonstration(self) -> None:
        """Demonstration of the hCaptcha solver."""
        try:
            print('Solving hCaptcha.', end=' ')
            # hCaptcha solver URL test.
            self.driver.get(
                'https://maximedrn.github.io/hcaptcha-solver-python-selenium/')
            # Check if lenght of "data-hcaptcha-response" attribute is not
            # null. If it's not null, hCaptcha is solved.
            WDW(self.driver, 600).until(lambda _: len(self.element_visible(
                '//div[@class="h-captcha"]/iframe').get_attribute(
                    'data-hcaptcha-response')) > 0)
            print(f'{green}Solved.{reset}')
        except TE:
            print(f'{red}Failed.{reset}')


def cls() -> None:
    """Clear console function."""
    # Clear console for Windows using 'cls' and Linux & Mac using 'clear'.
    os.system('cls' if os.name == 'nt' else 'clear')


if __name__ == '__main__':

    cls()  # Clear console.

    print(f'{green}Made by Maxime. '
          f'\n@Github: https://github.com/maximedrn{reset}')

    hcaptcha = hCaptcha()  # Init hCaptcha class.
    hcaptcha.download_userscript()  # Download the hCaptcha solver userscript.
    hcaptcha.demonstration()  # Demonstrate the hCaptcha solver.
