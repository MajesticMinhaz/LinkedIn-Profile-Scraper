<p align="center"><img src="https://img.shields.io/badge/Version-1.0.0-brightgreen"></p>
<p align="center">
  <a href="https://github.com/majesticminhaz">
    <img src="https://img.shields.io/github/followers/majesticminhaz?label=Follow&style=social">
  </a>
</p>
<p align="center">
</p>

---

# LinkedIn Profile Scraper Docs
## `.env` file management
```
# LinkedIn Scraper Configuration

# Official LinkedIn website URL
LINKEDIN_WEBSITE_URL=https://www.linkedin.com/

# File path to store user cookies
COOKIES_FILE_PATH=cookies.json

# Database URL for storing scraped data
DATABASE_URL=sqlite:///linkedin_data.db

# Path to the Chrome WebDriver executable
DRIVER_PATH=./chrome-driver.exe

# Scraper start ID specification
SCRAP_START_ID=0

# Scraper end ID specification
SCRAP_END_ID=100

# Scraper browser window width (default: 1200, recommended)
SCRAP_WINDOW_WIDTH=1200

# Scraper browser window height (default: 900, recommended)
SCRAP_WINDOW_HEIGHT=900

# File path of the existing Excel file for data insertion
INSERT_EXCEL_FILE_PATH=Insert.xlsx

# Name of the sheet within the existing Excel file
INSERT_EXCEL_SHEET_NAME=Sheet1
```

## Installation
```commandline
pip install -r requirements.txt
```
## Insert existing dataset to the database
```commandline
python insert_data_from_excel_to_db.py
```

## Example Input Excel(.xlsx) file

| PROFILE URL                               | FIRST NAME | LAST NAME | COMPANY NAME | JOB TITLE |
|-------------------------------------------|------------|-----------|----------|-----------|
| https://www.linkedin.com/in/johndoe/      |||||
| https://www.linkedin.com/in/janesmith/    |||||
| https://www.linkedin.com/in/alicejohnson/ |||||


## Example Output Excel(.xlsx) file
| PROFILE URL                                      | FIRST NAME | LAST NAME | COMPANY NAME | JOB TITLE |
|--------------------------------------------------|------------|-----------|--------------|-----------|
| https://www.linkedin.com/in/johndoe/     | John       | Doe       | Example Inc. | CEO       |
| https://www.linkedin.com/in/janesmith/     | Jane       | Smith     | ABC Corp.    | CFO       |
| https://www.linkedin.com/in/alicejohnson/     | Alice      | Johnson   | XYZ Ltd.     | CTO       |


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
