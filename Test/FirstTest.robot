*** Settings ***
Documentation    My first tests file
Resource    ../Library/Helper/CommonHelper.robot
Resource    ../Library/Helper/PageHelper.robot
## command to run on terminal>>robot -d report FirstTest.robot ##

Suite Setup    Launch Browser Choice
Suite Teardown    Quit Opened Browser

Test Setup    Open Selenium Easy Application
Test Teardown    Close Selenium Easy Application

#Test Setup    Open Website Herokuapp
#Test Teardown  Close Website Herokuapp

*** Test Cases ***
#My First Test Case
#    LOG    'This is first test case'
#    Menu.Navigate Menu to Table  Table Sort & Search
#    ${data}=  Table.Get Data From Sort Column  Age
#    ${flag}=  Is List Sorted Ascending  ${data}
#    Should be True  ${flag}
#
#My Second Test Case
#    LOG    'This is my second test case'
#    Menu.Navigate Menu to Table  Table Sort & Search
#    ${data}=  Table.Search And Get Data From Column  London  Office
#    ${flag}=  is lst contain same data  ${data}
#    Should be True  ${flag}
#
#My Third Test Case
#    LOG  This is my third test case
#    Menu.Navigate Menu to Alerts  File Download
#    ${filepath}=    FileDownload.Generate Link And Download File  Hi my name is devashish nigam  myfile.txt
#    LOG  ${filepath}
#
#My Fourth Test Case
#    LOG  This is my fourth test case
#    Menu.Navigate Menu to Others  Drag and Drop
#    ${dropped_items}=  DragAndDrop.Drag Items And Verify List
#
#My Fifth Test Case
#    LOG  My fifth test case
#    Menu.Navigate Menu to Alerts  Javascript Alerts
#    Dialog.Initialization Dialog Accept
#    Dialog.Alert Box
#    Dialog.Confirm Box
#    Dialog.Prompt Box
#    Sleep  10

# --- new website : https://the-internet.herokuapp.com/ ---#

#My Sixth Test Case
#    LOG  My sixth test case
#    FileUpload.Navigate File Upload Menu Page
#    FileUpload.Silent Mode File Upload
#    Sleep  5
#
#My Seventh Test Case
#    LOG  My sixth test case
#    FileUpload.Navigate File Upload Menu Page
#    FileUpload.Interactive Mode File Upload
#    Sleep  5
#
#My Eight Test Case
#    LOG  My sixth test case
#    FileUpload.Navigate File Upload Menu Page
#    FileUpload.Listener Mode File Upload
#    Sleep  5

#My Ninth Test Case
#    LOG  My ninth test case
#    IframeHandling.Enter Text In TextArea
#
#My Tenth Test Case
#    LOG  My tenth test case
#    ${lst_firstnames}=  Response.Get List All Users FirstName
#    LOG MANY  ${lst_firstnames}

My Eleventh Test Case
    LOG  http://demo.seleniumeasy.com/
    menu.navigate menu to alerts  Window Popup Modal
    PagePopUp.handle_pop_up_main_page_tasks





