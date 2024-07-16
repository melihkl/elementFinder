# Web Element Locator Script

This project aims to facilitate the identification of web elements such as ID, name, class, and XPath for use in test automation. The script uses Selenium WebDriver in Python to open a specified web page, log in if required, and collect information about various elements on the page.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- You have installed Python 3.x.
- You have installed the necessary Python packages by running:
  ```sh
  pip install selenium

## Installation
Clone the repository or download the script and config file.
Ensure you have the correct WebDriver for your browser installed and accessible in your system's PATH. For Chrome, download ChromeDriver, and for Edge, download EdgeDriver.
Configuration

The script requires a config.json file to run. Below is an example configuration:
```javascript
{
  "browser_type": "Chrome",
  "login_required": false,
  "login_url": "",
  "username_element": "",
  "password_element": "",
  "login_button_element": "",
  "username": "",
  "password": "",
  "target_url": ""
}
```
`browser_type`: Choose between "Chrome" or "Edge" for the browser.

`login_required`: Set to true if login is needed, otherwise false.

`login_url`: URL of the login page.

`username_element`: The ID of the username input element.

`password_element`: The ID of the password input element.

`login_button_element`: The ID of the login button.

`username`: The username for login.

`password`: The password for login.

`target_url`: The URL of the target page.

## Usage
The script will perform the following actions:

- Load the browser specified in config.json.
- If login_required is true, navigate to the login URL, enter the username and password, and log in.
- Navigate to the target URL.
- Collect information about buttons, input fields, text areas, and select elements on the page.
- Save the collected information in elements_info.json.

## Output
The script generates an elements_info.json file with details about the web page elements, including their type, ID, name, class name, text, and XPath.

## License
This project is licensed under the [MIT](https://choosealicense.com/licenses/mit/) License - see the LICENSE file for details.
