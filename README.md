# hCAPTCHA solver for Python Selenium (any operating system, ChromeDriver and GeckoDriver).

_A Selenium Python tool to automatically solve the hCAPTCHAs using a Tampermonkey userscript._  
➜ **Version 1.2.1** (July 19, 2022).

This script is solely intended for the use of **educational purposes only** and **not to abuse any website**.  
The solving speed depends on your PC's compute power and Internet connection.

# Table of contents

* [Instructions](#instructions), how to install Python and this repository.
  * [Installation of Python](#installation-of-python), step by step learn how to install Python.
  * [Installation and configuration of this tool](#installation-and-configuration-of-this-tool), step by step learn how to download and use this tool.
* [Website preview](#simple-website-to-try-to-solve-an-hcaptcha) to try this solver.


# Instructions

* [Download](https://github.com/maximedrn/hcaptcha-solver-python-selenium/archive/refs/heads/master.zip) this repository or clone it by typing this command:
  
  ```
  git clone https://github.com/maximedrn/hcaptcha-solver-python-selenium.git
  ```
* Download and install [Google Chrome](https://www.google.com/intl/en_en/chrome/) or [Mozilla Firefox](https://www.mozilla.org/firefox/new/).

## Installation of Python

* Download and install [Python](https://www.python.org/) _(version 3.9.11 recommended)_ according to your operating system.
  * Make sure you add Python in your path by checking the checkbox when you run the installation.
* Check that your version of Python is correct by typing one of these commands in a command prompt:

  * ```
    python --version
    ```
  * ```
    python3 --version
    ```
  * ```
    py --version
    ```
* If pip is not installed by default with Python, install [pip](https://pip.pypa.io/en/stable/installation/) to be able to have needed Python modules.
* Verify that pip is correctly installed by typing one of thess commands in a command prompt:

  * ```
    pip --version
    ```
  * ```
    pip3 --version
    ```  

## Installation and configuration of this tool

* [Download this repository](https://github.com/maximedrn/hcaptcha-solver-python-selenium/archive/refs/heads/master.zip) or clone it by typing this command in your command prompt (it requires [Git](https://git-scm.com/downloads)):
    
    ```
    git clone https://github.com/maximedrn/hcaptcha-solver-python-selenium.git
    ```
* Extract the repository folder from the ZIP file, you should have a folder named  `hcaptcha-solver-python-selenium-master/`.
* Open a command prompt in the repository folder and type one of these commands (may require ``sudo`` on MacOS and Linux and administrator privileges for Windows):
    
  * ```
    pip install -r requirements.txt
    ```
  * ```
    pip3 install -r requirements.txt
    ```
  * ```
    python -m pip install -r requirements.txt
    ```
  * ```
    python3 -m pip install -r requirements.txt
    ```
  * ```
    py -m pip install -r requirements.txt
    ```
* Download and install [Google Chrome](https://www.google.com/intl/en_en/chrome/) and/or [Mozilla Firefox](https://www.mozilla.org/en-US/firefox/new/).


# Simple website to try to solve an hCAPTCHA

* Open a new tab and go to the website [hCAPTCHA test](https://maximedrn.github.io/hcaptcha-solver-python-selenium/).
* Website preview:

  ![Website preview](https://github.com/maximedrn/hcaptcha-test/blob/master/images/preview.png)
