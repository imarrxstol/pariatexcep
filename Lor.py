def enter_password(driver, account):
    """Enters the password for an account.

    Args:
        driver: The WebDriver instance to use.
        account: The account to enter the password for.
    """

    password_input = driver.find_element_by_name("password")
    password_input.send_keys(account.password)
    password_input.submit()

