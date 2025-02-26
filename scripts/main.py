from selenium import webdriver

from AppOpener import open


def open_browser():
    driver = webdriver.Chrome()
    return driver

def main():
    print("1. 'devmode' - vscode, chrome, sqlsrv")
    print("2. 'no database - devmode' - vscode, chrome & lofi")
    print("3. 'gamemode' - valorant")
    print("4. 'comuncationmode' - whatsapp, discord")

    while True:
        userInput = input("Selecione sua aplicação: ")
        
        if "1" in userInput: 
            app_name = 'visual studio code, sql server management studio'
            
            driver = open_browser()
            driver.get("https://www.youtube.com/watch?v=q1T8tGb_A1M")
            open(app_name, match_closest=True)

        elif "2" in userInput: 
            app_name = 'visual studio code'

            driver = open_browser()
            driver.get("https://www.youtube.com/watch?v=q1T8tGb_A1M")
            app_name = 'visual studio code'
            open(app_name, match_closest=True)

        elif "3" in userInput: 
            app_name = 'cliente riot'
            open(app_name, match_closest=True)

        elif "4" in userInput: 
            app_name = 'whatsapp, discord'
            open(app_name, match_closest=True)

main()
