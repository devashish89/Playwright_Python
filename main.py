# -- playwright in python -- #
import time

from playwright.sync_api import sync_playwright
firstname_loc = "input[name=\"firstname\"]"
lastname_loc = "input[name=\"lastname\"]"
DOB_loc = ":nth-match(input[type=\"text\"], 4)"
male_loc = ":nth-match(input[name=\"sex\"], 1)"
female_loc = ":nth-match(input[name=\"sex\"], 2)"
exp_loc = "text=YRS >> input[name=\"exp\"]"
continent_loc = "select[name=\"continents\"]"
selenium_command_loc = "select[name=\"selenium_commands\"]"
choose_file_loc = "input[name=\"photo\"]"
tool_loc = "text=TOOLNAME >> input[name=\"tool\"]"
profession = "text=TYPETESTER >> input[name=\"profession\"]"
drag_loc = "text=Draggable NUM"
drop_loc = "#mydropzone"

iframe_id = "mce_0_ifr"
edit_btn = "button[role=\"menuitem\"]:has-text(\"Edit\")"
select_all_btn = "div[role=\"menu\"] div:has-text(\"Select allCtrl+A\")"
cut_btn = "text=Cut"
bold_btn = "[aria-label=\"Bold\"]"

def handle_dialog(dialog):
    print(dialog.type)
    print(dialog.message)
    dialog.accept()

pwSync = sync_playwright().start()
browser = pwSync.chromium.launch(headless=False, downloads_path='main_downloads', slow_mo=100)
context = browser.new_context(
    accept_downloads=True,
    viewport={"width":1920, "height":1080},
    record_video_dir="main_videos",
    record_video_size={"width":640, "height":480}
)

page1 = context.new_page()
page1.goto("https://www.tutorialspoint.com/selenium/selenium_automation_practice.htm")
# -- wait for element to be visible -- #
page1.wait_for_selector(firstname_loc, state='visible', timeout=30000)
page1.fill(firstname_loc, "Devashish")
page1.fill(lastname_loc, "Nigam")
# --- radio button and checkboxes we can use page.check(locator) -- #
page1.check(female_loc)
page1.check(exp_loc.replace("YRS", "5"))
page1.fill(DOB_loc, "30/10/1989")
#--  3 methods - easiest method to upload file -- #
page1.set_input_files(choose_file_loc, r"C:\Users\91836\Documents\GitHub\Devashish-Resume-CL\DEVASHISH NIGAM resume e.pdf")
# --- radio button and checkboxes we can use page.check(locator) -- #
page1.check(tool_loc.replace("TOOLNAME", "RC"))
page1.check(tool_loc.replace("TOOLNAME", "Selenium IDE"))
page1.check(profession.replace("TYPETESTER", "Manual Tester"))
# -- handle dropdown -- #
page1.select_option(continent_loc, "Europe")
page1.select_option(selenium_command_loc, ["Switch Commands", "Wait Commands"])

# -- button click was not working to scroll to btn and then click --#
page1.click("//button[text()=\"Button\"]", delay=1000)
page1.press("//button[text()=\"Button\"]", "Enter")
# -- handle browser Dialog/ javascript kind Alert -- #
page1.on("dialog", handle_dialog)
page1.screenshot(path='form.jpg', full_page=True)
page1.close()
# -- drag and drop -- #
page2 = context.new_page()
page2.goto("http://demo.seleniumeasy.com/drag-and-drop-demo.html")
for i in range(1,4):
    page2.drag_and_drop(drag_loc.replace("NUM", str(i)), drop_loc)
time.sleep(5)
page2.close()

# -- iframe -- #
page3 = context.new_page()
page3.goto("https://the-internet.herokuapp.com/iframe")
page3.click(edit_btn)
page3.click(select_all_btn)
page3.click(edit_btn)
page3.click(cut_btn)
page3.frame(name=iframe_id).fill("p", "Hello RPA Developers")
page3.click(edit_btn)
page3.click(select_all_btn)
page3.click(bold_btn)
time.sleep(5)
page3.close()
context.close()
browser.close()
pwSync.stop()