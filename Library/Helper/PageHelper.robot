*** Settings ***
Documentation    Helper File
Library    ../Page/Menu.py
Library    ../Page/TableSortAndSearchDemo.py
Library    ../Page/FileDownload.py
Library    ../Page/DragDrop.py
Library    ../Page/Dialog.py
Library    ../Page/FileUpload.py
Library    ../Page/IframeHandling.py
Library    ../Page/Response.py
Library    ../Page/PagePopUp.py
Resource    CommonHelper.robot


*** Keywords ***
# ---- Menu Item related Helper ---- #
Menu.Navigate Menu to Input Forms
    [Arguments]    ${second_menu_item}
    ${page}=    Get Page Handle
    navigate menu item    ${page}    Input Forms    ${second_menu_item}


Menu.Navigate Menu to Table
    [Arguments]    ${second_menu_item}
    ${page}=    Get Page Handle
    navigate menu item    ${page}    Table    ${second_menu_item}


Menu.Navigate Menu to Alerts
    [Arguments]    ${second_menu_item}
    ${page}=    Get Page Handle
    navigate menu item    ${page}    Alerts & Modals    ${second_menu_item}

Menu.Navigate Menu to Others
    [Arguments]    ${second_menu_item}
    ${page}=    Get Page Handle
    navigate menu item  ${page}  Others  ${second_menu_item}

# --- Table Related Helper --- #
Table.Get Data From Sort Column
    [Arguments]  ${column}
    ${page}=    Get Page Handle
    select table entries  ${page}  100
    Sort Table By Column  ${page}  ${column}
    ${data}=  Get Sorted Data List  ${page}
    [Return]  ${data}

Table.Search And Get Data From Column
    [Arguments]  ${search_val}  ${column}
    ${page}=    Get Page Handle
    select table entries  ${page}  100
    Search Table  ${page}  ${search_val}
    Sort Table By Column  ${page}  ${column}
    ${data}=  Get Sorted Data List  ${page}
    [Return]  ${data}

# --- File Download --- #
FileDownload.Generate Link And Download File
    [Arguments]  ${text}  ${filename}
    ${page}=  Get Page Handle
    enter text  ${page}  ${text}
    generate download link  ${page}
    download file  ${page}  ${filename}


# --- Drag and Drop --- #
DragAndDrop.Drag Items And Verify List
    ${page}=    Get Page Handle
    FOR  ${i}  IN RANGE  1  5
        LOG  ${i}
        ${num}=  Convert To String  ${i}
        drag item  ${page}  ${num}
    END
    ${dropped_items}=    get dropped items  ${page}
    [Return]  ${dropped_items}

 # --- Alerts --- #
Dialog.Initialization Dialog Accept
    ${page}  Get Page Handle
    init dialog accept  ${page}

Dialog.Alert Box
    ${page}  Get Page Handle
    click alert box btn  ${page}

Dialog.Confirm Box
    ${page}  Get Page Handle
    click confirm box btn  ${page}

Dialog.Prompt Box
    ${page}  Get Page Handle
    set prompt message  Hello my name is devashish nigam
    click prompt box btn  ${page}

# -- File Upload-- #
FileUpload.Navigate File Upload Menu Page
    ${page}  Get Herokuapp Page Handle
    navigate file upload page  ${page}

FileUpload.Silent Mode File Upload
    ${page}  Get Herokuapp Page Handle
    silent file upload  ${page}  C:/Users/91836/Downloads/Aadhar_card.jpeg
    ${status}=  check file uploaded  ${page}
    Should Be True  ${status}

FileUpload.Interactive Mode File Upload
    ${page}  Get Herokuapp Page Handle
    interactive file upload  ${page}  C:/Users/91836/Downloads/Aadhar_card.jpeg
    ${status}=  check file uploaded  ${page}
    Should Be True  ${status}

FileUpload.Listener Mode File Upload
    ${page}  Get Herokuapp Page Handle
    init listener file upload  ${page}
    set filepath  C:/Users/91836/Downloads/Aadhar_card.jpeg
    click file upload  ${page}
    ${status}=  check file uploaded  ${page}
    Should Be True  ${status}

# --- Iframe Page related handler --- #
IframeHandling.Enter Text In TextArea
    ${page}  Get Herokuapp Page Handle
    navigate to iframe menu  ${page}
    select all  ${page}
    cut text  ${page}
    enter text iframe  ${page}  I'm using Playwright here
    select all  ${page}
    bold text  ${page}

# --- reqres.in ----  Network HTTp request response --- #
Response.Get List All Users FirstName
    ${page}  Get Herokuapp Page Handle
    ${lst_firstnames}=  get list of all users firstname  ${page}
    [Return]  ${lst_firstnames}

# -- Window Popups http://demo.seleniumeasy.com/window-popup-modal-demo.html-- #
PagePopUp.handle_pop_up_main_page_tasks
    ${page}=  Get Page Handle
    work within popup main page also  ${page}



