<p align="center"><img src="https://img.shields.io/badge/Version-1.0.0-brightgreen"></p>
<p align="center">
  <a href="https://github.com/majesticminhaz">
    <img src="https://img.shields.io/github/followers/majesticminhaz?label=Follow&style=social">
  </a>
</p>
<p align="center">
</p>

---

# **LinkedIn Profile Scraper Tool Setup Guide**

## Installation
This guide will walk you through the setup process for running the LinkedIn Profile Scraper Tool on macOS. Please ensure you follow each step carefully to ensure smooth installation and setup.

### Installing Python for macOS

#### Step 1: Check and Install Python (if not already installed)

- Open the Terminal application on your macOS.
- Type the following command and press Enter:
```commandline
python3 --version
```
- If Python is installed, you will see a version number displayed. You can skip to Step 4.
- If Python is not installed, continue with the following steps:

#### Step 2: Download Python

- Open a web browser and navigate to the [official Python website](https://www.python.org/downloads/).
- Download the latest version of Python for macOS by clicking on the "Download Python" button.

#### Step 3: Install Python

- Once the download is complete, locate the downloaded file (typically in your Downloads folder) and double-click to open it.
- Follow the on-screen instructions in the Python installer.
- During the installation process, make sure to check the box that says "Add Python x.x to PATH".

#### Step 4: Verify Installation

- Once the installation is complete, open the Terminal application on your macOS.
- Type the following command and press Enter:
```commandline
python3 --version
```
- If Python is installed correctly, you will see a version number displayed.
- 
### Updating Chrome Browser and Obtaining ChromeDriver Executable on macOS

#### Step 1: Check Existing Chrome Browser Version and Update

- Open Google Chrome on your macOS.
- Click on the three vertical dots in the top-right corner of the browser window to open the Chrome menu.
- From the menu, navigate to "Help" > "About Google Chrome".
- Note down the version number displayed on the About page.
- Chrome will automatically check for updates and prompt you to install if a new version is available.
- Follow the on-screen instructions to update Google Chrome to the latest version.

#### Step 2: Download ChromeDriver Executable

- Open a web browser and navigate to the [ChromeDriver downloads](https://sites.google.com/a/chromium.org/chromedriver/downloads) page.
- Download the latest version of ChromeDriver that matches your Chrome browser version. Ensure that you download the version compatible with macOS.

#### Step 3: Verify ChromeDriver and Chrome Browser Installation

- Once Chrome is updated, revisit the "About Google Chrome" page to ensure that it's updated to the latest version.
- Locate the downloaded ChromeDriver ZIP file (typically in your Downloads folder) and extract its contents.
- Open a terminal window and navigate to the directory where you saved the ChromeDriver executable.
- Type the following command to verify ChromeDriver installation:

```bash
./chromedriver --version
```
- You should see the ChromeDriver version displayed. Ensure that the version number matches the current version of Google Chrome you have installed (current version when the scraper was developed [121.0.6167.something]).

### Automated Project Download and Setup Guide

This guide outlines the steps to download a project from GitHub as a zip file, extract its contents, place an executable file into the extracted folder, and create new files within it.

#### Step 1: Downloading the Project

1. Go to the [GitHub repository](https://github.com/MajesticMinhaz/LinkedIn-Profile-Scraper) containing the project you want to download.
2. Click on the "Code" button.
3. Select "Download ZIP" to download the project as a zip file.
4. Save the zip file to a safe folder on your computer.

#### Step 2: Extracting the Project

1. Navigate to the safe folder where the zip file is saved.
2. Right-click on the zip file.
3. Choose "Extract Here" or "Extract to [your chosen folder name]" to extract the contents of the zip file into a new folder.

#### Step 3: Placing the Executable Chrome Driver

1. Inside the newly extracted folder, locate the executable chrome driver file.
2. If the chrome driver is not present, you may need to download it separately and place it in the folder.
3. Ensure the chrome driver is compatible with your system and the project requirements.

#### Step 4: Creating the Cookies and .env Files

1. Open the newly created folder.
2. Right-click within the folder.
3. Choose "New" and then "Text Document" or any text editor you prefer.
4. Rename the first file to "cookies.json".
5. Open the "cookies.json" file and add the necessary JSON structure or content as per the project requirements.
6. Repeat steps 2-3 to create another new text document.
7. Rename the second file to ".env".
8. Open the ".env" file and add the necessary configurations for your project, following the example provided in the project's "[.env.example](https://github.com/MajesticMinhaz/LinkedIn-Profile-Scraper/blob/master/.env.example)" file.

#### Conclusion

You have successfully downloaded the project from GitHub, extracted its contents, placed the executable chrome driver in the folder, and created new files "cookies.json" and ".env". You are now ready to proceed with using the project.

### LinkedIn profile Cookies Setup Guide

#### Prerequisites:

1. **Create a Dummy LinkedIn Account**: It's recommended to create a dummy LinkedIn account to mitigate the risk of losing any valuable information in case the account is closed by LinkedIn authorities.

#### Steps:

1. **Install "Cookie-Editor" Chrome Extension**: 
   - Open your Chrome browser.
   - Navigate to [Cookie-Editor Chrome Extension](https://cookie-editor.com/) page.
   - Click on "Install" to install the extension.
   - Select "Chrome" from the list.
   - Click "Add to Chrome".

2. **Access and Export Cookies**:
   - Log in to your dummy LinkedIn account.
   - Once logged in, click on the Cookie Editor extension icon in your Chrome browser toolbar.

3. **Export Cookies as JSON**:
   - In the Cookie Editor window, navigate to the LinkedIn domain.
   - Export the cookies associated with LinkedIn.
   - Choose the export format as JSON.

4. **Copy JSON Text**:
   - Once the JSON export is complete, copy the entire text. (you already copied text automatically while you clicked Export as JSON button 😊)

5. **Update Cookies in the Project**:
   - Locate the `cookies.json` file in your LinkedIn scraper project.
   - Open the file.
   - Paste the copied JSON text into this file, replacing any existing content.

6. **Save and Test**:
   - Save the changes to the `cookies.json` file.
   - Test your LinkedIn scraper tool to ensure that it's working properly with the updated cookies.

By following these steps, you can set up the LinkedIn scraper tool with the necessary cookies obtained from your dummy LinkedIn account.

Remember to always use such tools responsibly and in compliance with LinkedIn's terms of service and any relevant laws and regulations.

_**Note: Don't share the `cookies.json` file with anyone.**_


### Example Input Excel File for LinkedIn Scraper Tool

#### Introduction
This Excel file serves as an example input for the LinkedIn scraper tool. It contains a template with specific columns where you can input LinkedIn profile URLs along with optional associated details.

#### Format Details
The Excel file follows a structured format with the following columns:

1. **PROFILE URL**: This column is reserved for the LinkedIn profile URLs that you want to scrape.
2. **FIRST NAME**: Use this column to input the first name of the LinkedIn user if available.
3. **LAST NAME**: Input the last name of the LinkedIn user in this column.
4. **COMPANY NAME**: If the LinkedIn user's current company information is available, enter it here.
5. **JOB TITLE**: Input the job title of the LinkedIn user if available.

PROFILE URL is mandatory, while other fields are optional. If no additional data is provided, leave the corresponding cells empty. The scraper will extract all available information based on the profile URLs provided.

#### Instructions
1. Open your preferred spreadsheet software such as Microsoft Excel or Google Sheets.
2. Create a new spreadsheet.
3. Label the columns as mentioned above: PROFILE URL, FIRST NAME, LAST NAME, COMPANY NAME, and JOB TITLE.
4. Input the LinkedIn profile URLs in the "PROFILE URL" column. Ensure each URL is in the correct cell under this column.
5. Optionally, fill in additional details such as first name, last name, company name, and job title in their respective columns if available.
6. Save the file with a `.xlsx` extension.
7. Place the saved Excel file in the project directory of the LinkedIn scraper tool.
8. The tool will use this file as input to scrape LinkedIn profiles based on the provided URLs and details.

#### Example
Here's an example of how the Excel file should look:

| PROFILE URL                               | FIRST NAME | LAST NAME | COMPANY NAME | JOB TITLE |
|-------------------------------------------|------------|-----------|--------------|-----------|
| https://www.linkedin.com/in/johndoe/      | John       | Doe       | ABC Company  | CEO       |
| https://www.linkedin.com/in/janesmith/    |            |           | XYZ Corp     | Engineer  |
| https://www.linkedin.com/in/alicejohnson/ |            |           |              |           |

#### Notes
- Ensure that each LinkedIn profile URL is valid and accessible.
- Profile URL is mandatory, while other fields are optional.
- Leaving fields empty will not affect the scraping process, as the tool will extract available data based on the profile URLs provided.

By following these instructions, you can create an input Excel file for the LinkedIn scraper tool, allowing you to organize and specify the profiles you want to scrape.


### Setting Up a Virtual Environment and Installing Requirements on macOS

#### Introduction
Setting up a virtual environment is a good practice to manage dependencies for your Python projects. This guide will walk you through creating a virtual environment and installing dependencies from a `requirements.txt` file on macOS.

#### Steps

1. **Open Terminal**
   - Launch the Terminal application on your macOS. You can find it in the Applications folder under Utilities, or you can use Spotlight search (Cmd + Space, then type "Terminal").

2. **Navigate to Your Project Directory**
   - Use the `cd` command to navigate to your project directory. For example:
     ```bash
     cd /path/to/your/project
     ```

3. **Create a Virtual Environment**
   - Once you're in your project directory, run the following command to create a virtual environment named `venv`:
     ```bash
     python3 -m venv venv
     ```

4. **Activate the Virtual Environment**
   - Activate the virtual environment by running the activation script. Use the following command:
     ```bash
     source venv/bin/activate
     ```

5. **Install Requirements**
   - With the virtual environment activated, you can now install the dependencies listed in the `requirements.txt` file. Run the following command:
     ```bash
     pip install -r requirements.txt
     ```

6. **Verify Installation**
   - After the installation is complete, you can verify that the dependencies were installed correctly by running:
     ```bash
     pip list
     ```
   - This will display a list of installed packages, including the ones from the `requirements.txt` file.

#### Conclusion
You have now successfully set up a virtual environment and installed dependencies from a `requirements.txt` file on macOS. This helps ensure that your project's dependencies are isolated and manageable.



### Insert Existing Dataset to the Database

To insert an existing dataset from an Excel file into your database, follow these steps:

#### Step 1: Python Script
You'll use a Python script to read the data from the Excel file and insert it into the database. Let's assume the script is named `insert_data_from_excel_to_db.py`.

#### Step 2: Execute the Script
Navigate to the directory where your Python script is located using the command line. Then, execute the script by running the following command:
```commandline
python3 insert_data_from_excel_to_db.py
```

### Running `linkedin_profile_scraper.py` to Scrape Profiles

To execute the `linkedin_profile_scraper.py` script and initiate the profile scraping process, follow these steps:

1. **Navigate to Project Directory:** Open your terminal and navigate to the directory where the `linkedin_profile_scraper.py` file is located.

2. **Run the Script:** Execute the following command in the terminal to run the script:

    ```commandline
    python3 linkedin_profile_scraper.py
    ```

3. **Scraping Process:** Upon execution, the script will start scraping LinkedIn profiles automatically. It may open a browser window to access the LinkedIn profiles and extract the required information.

4. **Automated Scraping:** Don't be alarmed if a browser window opens automatically during the scraping process. This is expected behavior as the script accesses the LinkedIn profiles for scraping.

5. **Completion:** Once the scraping process is complete, the script will automatically gather the necessary data from the profiles and store it as per the defined logic.

By following these steps, you can seamlessly execute the `linkedin_profile_scraper.py` script and initiate the automatic scraping of LinkedIn profiles.


## Example Output Excel(.xlsx) File

Here's an example of how the output Excel file containing scraped LinkedIn profile data might look like:

| PROFILE URL                                      | FIRST NAME | LAST NAME | COMPANY NAME | JOB TITLE |
|--------------------------------------------------|------------|-----------|--------------|-----------|
| https://www.linkedin.com/in/johndoe/             | John       | Doe       | Example Inc. | CEO       |
| https://www.linkedin.com/in/janesmith/           | Jane       | Smith     | ABC Corp.    | CFO       |
| https://www.linkedin.com/in/alicejohnson/        | Alice      | Johnson   | XYZ Ltd.     | CTO       |

This Excel file contains the scraped data from LinkedIn profiles, including the profile URL, first name, last name, company name, and job title.


---
## Connect with Me

<p align="center">
    <a href="https://www.buymeacoffee.com/mdminhaz2003"><img src="https://img.shields.io/badge/-Buy me a coffee-000000?style=for-the-badge&logo=buymeacoffee&logoColor=yellow"/></a>
    <a href="https://www.facebook.com/majesticminhaz/"><img src="https://img.shields.io/badge/-Md. Minhaz-3423A6?style=for-the-badge&logo=Facebook&logoColor=white"/></a>
    <a href="https://www.linkedin.com/in/majesticminhaz/"><img src="https://img.shields.io/badge/-Md. Minhaz-0077B5?style=for-the-badge&logo=Linkedin&logoColor=white"/></a>
    <a href="mailto:mdm047767@gmail.com"><img src="https://img.shields.io/badge/-Mail-D14836?style=for-the-badge&logo=Gmail&logoColor=white"/></a>
    <a href="https://instagram.com/majesticminhaz/"><img src="https://img.shields.io/badge/-Md. Minhaz-E4405F?style=for-the-badge&logo=Instagram&logoColor=white"/></a>
    <a href="https://twitter.com/majesticminhaz/"><img src="https://img.shields.io/badge/-MD. MINHAZ-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white"/></a>
</p>
