# Google Sheets Data Processor

This Python project utilizes the Google Sheets API to retrieve data from a Google Spreadsheet, process it using the math library, and update the spreadsheet with the results.

## Requirements

-Python 3.10.7 or above.
-PIP package management tool.
-Google account
-Ensure you have the required libraries installed. You can use the following command to install them:

```bash
pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
```
## Setup

    Google API Credentials:
        Create a project in the Google Cloud Console.
        Enable the Google Sheets API for the project.
        Create credentials (OAuth client ID).
        Download the JSON file of the credentials and save it as credentials.json in the project root.

    Install Dependencies:

    bash

pip install -r requirements.txt

Run the Project:

bash

    python main.py

    The application will guide you through the authentication process and demonstrate the data retrieval, processing, and updating steps.

Configuration

Ensure that you set up the necessary configuration in config.py: