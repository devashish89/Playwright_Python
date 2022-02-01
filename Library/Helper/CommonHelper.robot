*** Settings ***
Documentation    Common helper file
Library    ../PyLib/PlaywrightCore.py
Library    ../Page/UtilityCore.py

*** Keywords ***
Launch Browser Choice
    launch browser

Quit Opened Browser
    close browser

Open Selenium Easy Application
    open application

Close Selenium Easy Application
    close application

Open Website Herokuapp
    open application herokuapp

Close Website Herokuapp
    close application herokuapp

Get Page Handle
    ${page_handle}     get page object
    [Return]    ${page_handle}

Get Herokuapp Page Handle
    ${page_handle}=  get herokuapp page
    [Return]  ${page_handle}

Is List Sorted Ascending
    [Arguments]  ${lst}
    ${flag}=  is lst ascending  ${lst}
    [Return]  ${flag}

Is List Contain Same Data
    [Arguments]  ${lst}
    ${flag}=  is lst contain same data  ${lst}
    [Return]  ${flag}

