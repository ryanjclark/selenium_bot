echo "Creating virtualenv 'selenium'"
virtualenv selenium
source selenium/bin/activate

echo "Installing requirements"
pip install -r requirements.txt

# TODO: curl chromedriver latest version
# echo "curl command for Chromedriver"
# Chromedriver needs to be in opt/WebDriver/bin

echo "Adding WebDrivers to PATH"
export PATH=$PATH:/opt/WebDriver/bin >> ~/.profile
