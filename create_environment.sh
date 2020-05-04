echo "curl command for Chromedriver"
# Chromedriver needs to be in opt/WebDriver/bin
# TODO: curl chromedriver latest version

echo "Adding WebDrivers to PATH"
export PATH=$PATH:/opt/WebDriver/bin >> ~/.profile
