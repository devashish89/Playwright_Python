*** Settings ***
# --- install robotframewok-pabot library to run processes parallely -- #
# --- command: pabot --processes 2 --outputdir report *.robot ---#

Documentation    Fill Form https://www.tutorialspoint.com/selenium/selenium_automation_practice.htm
Resource    ../Library/Helper/CommonHelper.robot
Resource    ../Library/Helper/PageHelper.robot

Suite Setup    Launch Browser Choice  chromium  True
Suite Teardown    Quit Opened Browser

Test Setup    Open Website Herokuapp
Test Teardown  Close Website Herokuapp
*** Test Cases ***
My Iframe Test Case
    LOG  Iframe Test Case
    IframeHandling.Enter Text In TextArea

