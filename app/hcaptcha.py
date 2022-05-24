#!/usr/bin/python
# app/hcaptcha.py


"""
@author: Maxime Dréan.

Github: https://github.com/maximedrn
Telegram: https://t.me/maximedrn

Copyright © 2022 Maxime Dréan. All rights reserved.
Any distribution, modification or commercial use is strictly prohibited.
"""


# Selenium module imports: pip install selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as SC
from selenium.webdriver.firefox.service import Service as SG
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as WDW
from selenium.common.exceptions import TimeoutException as TE
from selenium.webdriver.common.by import By

# Webdriver Manager module: pip install webdriver-manager
from webdriver_manager.chrome import ChromeDriverManager as CDM
from webdriver_manager.firefox import GeckoDriverManager as GDM

# Python internal imports.
from .utils.const import CHROMEDRIVER_EXTENSION_PATH, \
    GECKODRIVER_EXTENSION_PATH, SCRIPT_URL
from .utils.func import exit


class hCaptcha:
    """Main class of the hCaptcha solver."""

    def __init__(self, browser: int = 0, headless: bool = False,
                 comments: bool = True, download: bool = False) -> None:
        """
        Initialize the hCAPTCHA class according to choices.

        There is a choice of browser: 0 for the ChromeDriver (Google
        Chrome) and 1 for the GeckoDriver (Mozilla Firefox).
        You can choose if you want to enable or disable comments in
        the command prompt for userscript download.
        You can choose to enable or disable automatic userscript download.
        """
        self.browser = browser  # Browser number.
        self.headless = headless  # Heamless mode.
        self.comments = comments  # Comments in the command prompt.
        # Set the Tampermonkey extension path.
        # Then start a new webdriver.
        if self.browser == 0:  # Chromedriver (Google Chrome).
            self.extension_path = CHROMEDRIVER_EXTENSION_PATH
            self.driver = self.chromedriver()
        else:  # GeckoDriver (Mozilla Firefox).
            self.extension_path = GECKODRIVER_EXTENSION_PATH
            self.driver = self.geckodriver()
        if download:  # Download the usercript.
            self.download_userscript()

    def chromedriver(self) -> webdriver:
        """Start a Chrome webdriver and return its state."""
        options = webdriver.ChromeOptions()  # Options for the ChromeDriver.
        options.add_extension(self.extension_path)  # Install the extension.
        options.add_argument('--lang=en-US')  # Set the webdriver language
        options.add_experimental_option('prefs', {  # to English (US).
            'intl.accept_languages': 'en,en_US'})
        if self.headless:  # Set the headless mode.
            options.add_argument('--headless')
        options.add_argument('--log-level=3')  # Not logs will be displayed.
        options.add_argument('--mute-audio')  # Audio is muted.
        options.add_argument(  # Enable the WebGL Draft extension.
            '--enable-webgl-draft-extensions')
        options.add_argument('--disable-infobars')  # Disable popup
        options.add_argument('--disable-popup-blocking')  # and info bars.
        driver = webdriver.Chrome(service=SC(CDM(  # Start the webdriver.
            log_level=0).install()), options=options)
        driver.maximize_window()  # Maximize window to reach all elements.
        return driver

    def geckodriver(self) -> webdriver:
        """Start a Firefox webdriver and return its state."""
        options = webdriver.FirefoxOptions()  # Options for the GeckoDriver.
        # Set the webdriver language to English (US).
        options.set_preference('intl.accept_languages', 'en,en-US')
        if self.headless:  # Set the headless mode.
            options.add_argument('--headless')
        options.add_argument('--log-level=3')  # Not logs will be displayed.
        options.add_argument('--mute-audio')  # Audio is muted.
        options.add_argument(  # Enable the WebGL Draft extension.
            '--enable-webgl-draft-extensions')
        options.add_argument('--disable-infobars')  # Disable popup
        options.add_argument('--disable-popup-blocking')  # and info bars.
        driver = webdriver.Firefox(service=SG(GDM(  # Start the webdriver.
            log_level=0).install()), options=options)
        driver.install_addon(self.extension_path)  # Add extension.
        driver.maximize_window()  # Maximize window to reach all elements.
        return driver

    def quit(self) -> None:
        """Stop the webdriver."""
        try:  # Try to close the webdriver.
            self.driver.quit()
        except Exception:  # The webdriver is closed
            pass  # or no webdriver is started.

    def clickable(self, element: str) -> None:
        """Click on an element if it's clickable using Selenium."""
        try:
            WDW(self.driver, 5).until(EC.element_to_be_clickable(
                (By.XPATH, element))).click()
        except Exception:  # Some buttons need to be visible to be clickable,
            self.driver.execute_script(  # so JavaScript can bypass this.
                'arguments[0].click();', self.visible(element))

    def visible(self, element: str):
        """Check if an element is visible using Selenium."""
        return WDW(self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, element)))

    def window_handles(self, window_number: int) -> None:
        """Check for window handles and wait until a specific tab is opened."""
        WDW(self.driver, 10).until(lambda _: len(
            self.driver.window_handles) > window_number)
        self.driver.switch_to.window(  # Switch to the asked tab.
            self.driver.window_handles[window_number])

    def download_userscript(self) -> None:
        """Download the hCaptcha solver userscript."""
        if self.comments:  # Import the Coloroma colors.
            from .utils.colors import GREEN, RED, RESET
        try:  # Download and install the userscript.
            if self.comments:  # Display this comment only if wanted.
                print('Adding the hCAPTCHA solver userscript.', end=' ')
            self.window_handles(1)  # Wait that Tampermonkey tab loads.
            self.driver.get(SCRIPT_URL)  # Go to the userscript URL page.
            # Click on the "Install" GreasyFork button.
            self.clickable('//*[@id="install-area"]/a[1]')
            # Click on "Install" Tampermonkey button.
            self.window_handles(2)  # Switch to the Tampermonkey tab.
            self.clickable('//*[@value="Install"]')
            self.window_handles(1)  # Switch to the GreasyFork tab.
            self.driver.close()  # Close the GreasyFork tab.
            self.window_handles(0)  # Switch to main tab.
            if self.comments:  # Display this comment only if wanted.
                print(f'{GREEN}Installed.{RESET}')
        except TE:  # Something went wrong.
            if self.comments:  # Display this comment only if wanted.
                print(f'{RED}Failed.{RESET}')
            self.quit()  # Close the webdriver.
            exit()  # Exit the program.
