import json
from dotenv import dotenv_values
from undetected_chromedriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from database import LinkedInData, get_linkedin_data_list, update_linkedin_data


def scrap_linkedin_profile(profile_url: str, chrome_driver: Chrome) -> dict or None:
    """
    Scrape LinkedIn profile using a Chrome WebDriver to extract full name , company name, job title.

    Args:
        profile_url (str): The URL of the webpage to scrape.
        chrome_driver (Chrome): The Chrome WebDriver instance.

    Returns:
        profile_data (dict): first_name, last_name, company_name, job_title.
    """
    chrome_driver.get(profile_url)

    try:
        # Wait for the webpage to load and find 'nofollow noreferrer' anchor tags
        wait_for_followers_included_div_tag = WebDriverWait(driver=chrome_driver, timeout=10)
        div_tag_element = wait_for_followers_included_div_tag.until(
            ec.presence_of_element_located(
                (By.CSS_SELECTOR, "div.mt2.relative")
            )
        )

        user_data = dict()

        try:
            full_name = div_tag_element.find_element(by=By.CSS_SELECTOR,
                                                     value="a[href^='/in/'][href$='/about-this-profile/']")
            user_data['full_name'] = full_name.text.strip()
        except NoSuchElementException:
            user_data['full_name'] = None
            print("Full name not found")

        try:
            job_title = div_tag_element.find_element(by=By.CSS_SELECTOR, value="div[data-generated-suggestion-target]")
            user_data['job_title'] = job_title.text.strip()
        except NoSuchElementException:
            user_data['job_title'] = None
            print("Job title not found")

        try:
            # Find the ul element inside the parent div
            ul_element = div_tag_element.find_element(by=By.CSS_SELECTOR, value="ul.pv-text-details__right-panel")
        except NoSuchElementException:
            ul_element = None

        if ul_element is not None:
            try:
                # Extract the first li element from the ul
                li_element = ul_element.find_element(by=By.CSS_SELECTOR, value="li")
                user_data['company_name'] = li_element.text.strip()
            except NoSuchElementException:
                user_data['company_name'] = None
                print("Company name not found")

        return user_data

    except TimeoutException:
        # Handle the case where the elements are not found within the specified timeout
        return None
    except AttributeError:
        return None


def extract_first_last_name(full_name):
    # Split the full name into individual words
    name_parts = full_name.split()

    # First name is the first word
    f_name = name_parts[0]

    # Last name consists of the remaining words
    if len(name_parts) > 1:
        l_name = ' '.join(name_parts[1:])
    else:
        l_name = ""

    return f_name, l_name


if __name__ == '__main__':
    # Get the config values from .env file
    config = dotenv_values('.env')

    # QUERY the db based on start id and end id where linkedin first name is None.
    linkedin_profile_url_list = get_linkedin_data_list(
        start_id=int(config.get('SCRAP_START_ID')),
        end_id=int(config.get('SCRAP_END_ID')),
        logic=LinkedInData.first_name == None
    )

    # create the driver instance
    # driver = Chrome(driver_executable_path=config.get('DRIVER_PATH'), use_subprocess=False)
    driver = Chrome(driver_executable_path=config.get('DRIVER_PATH'), use_subprocess=True)
    driver.set_window_size(
        width=int(config.get('SCRAP_WINDOW_WIDTH')),
        height=int(config.get('SCRAP_WINDOW_HEIGHT'))
    )
    driver.get(config.get("LINKEDIN_WEBSITE_URL"))

    # read cookies file and login to facebook website
    with open(file=config.get('COOKIES_FILE_PATH'), mode="r") as read_cookie_file:
        cookie = json.loads(read_cookie_file.read())

        for cookie_data in cookie:
            customized_cookie = dict()
            customized_cookie['domain'] = cookie_data.get("domain")
            customized_cookie['name'] = cookie_data.get("name")
            customized_cookie['value'] = cookie_data.get("value")

            driver.add_cookie(cookie_dict=customized_cookie)

        driver.refresh()
        driver.get(config.get("LINKEDIN_WEBSITE_URL"))


    for linkedin_data in linkedin_profile_url_list:
        print(f"Checking > ID: {linkedin_data.id}, Profile URL: {linkedin_data.profile_url}")

        profile_data = scrap_linkedin_profile(profile_url=linkedin_data.profile_url, chrome_driver=driver)
        first_name, last_name = extract_first_last_name(full_name=profile_data.get('full_name'))
        print(f"First name: {first_name}, Last name: {last_name}")
        print(f"job title > {profile_data.get('job_title')}")
        print(f"company name > {profile_data.get('company_name')}")

        update_linkedin_data(
            profile_url=linkedin_data.profile_url,
            first_name=first_name,
            last_name=last_name,
            company_name=profile_data.get('company_name'),
            job_title=profile_data.get('job_title')
        )

    print("Successfully Completed the tasks")
