from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
import time


def testingBcafinance(harga_kendaraan, budget_baru, tipe_pembayaran, asuransi, wilayah):
    options = webdriver.ChromeOptions()
    options.add_argument("start-maximized")
    options.add_argument("disable-infobars")
    options.add_argument("--disable-extensions")
    driver = webdriver.Chrome(chrome_options=options, executable_path=r'C:\webdrivers\chromedriver.exe')

    driver.get("https://bcafinance.co.id/")
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//input[@class='form-control mr-sm-2']"))).click()
    search = driver.find_element_by_xpath("//input[@class='form-control mr-sm-2']")
    search.send_keys("Simulasi Budget")
    search.send_keys(Keys.RETURN)
    time.sleep(2)

    search3 = driver.find_element_by_xpath("//p[@class = 'font-weight-500 title'][1]")
    search3.click()
    time.sleep(2)

    search4 = driver.find_element_by_xpath("//input[@id ='hargaKendaraan-Baru']")
    search4.send_keys(harga_kendaraan)
    time.sleep(2)

    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//select[@id='typeBudget-Baru']"))).click()
    time.sleep(1)
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, tipe_pembayaran))).click()
    time.sleep(2)

    search5 = driver.find_element_by_xpath("//input[@id='budget-Baru']")
    search5.send_keys(budget_baru)
    time.sleep(2)

    driver.find_element_by_xpath("//select[@id='jenisAsuransi-Baru']").click()
    time.sleep(1)
    driver.find_element_by_xpath(asuransi).click()
    time.sleep(2)

    driver.find_element_by_xpath("//select[@id='zonaWilayah-Baru']")
    driver.find_element_by_xpath(wilayah).click()
    time.sleep(2)

    try:
        driver.find_element_by_xpath("//button[@id='btn-simulasiBudgetMobilBaru']").click()
    except:
        print("ADA ERROR")

    time.sleep(3)

    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "(//div[@class='is-desktop action--wrapper']/button[@class='download-result'][1])[1]"))).click()
    time.sleep(3)

    driver.close()


if __name__ == "__main__":
    list_harga_kendaraan = [350000000, 340000000, 360000000]
    list_tipe_budget = ["//select[@id='typeBudget-Baru']/option[2]", "//select[@id='typeBudget-Baru']/option[3]"]
    list_tipe_asuransi = ["//select[@id='jenisAsuransi-Baru']/option[2]",
                          "//select[@id='jenisAsuransi-Baru']/option[3]",
                          "//select[@id='jenisAsuransi-Baru']/option[4]"]
    list_tipe_zona = ["//select[@id='zonaWilayah-Baru']/option[2]", "//select[@id='zonaWilayah-Baru']/option[3]",
                      "//select[@id='zonaWilayah-Baru']/option[4]"]
    harga_total_pembayaran_pertama = 130000000
    harga_angsuran = 7500000
    for harga in list_harga_kendaraan:
        for tipe_pembayaran in list_tipe_budget:
            for asuransi in list_tipe_asuransi:
                for wilayah in list_tipe_zona:
                    if (tipe_pembayaran == "//select[@id='typeBudget-Baru']/option[2]"):
                        testingBcafinance(harga, harga_total_pembayaran_pertama, tipe_pembayaran, asuransi, wilayah)
                    else:
                        testingBcafinance(harga, harga_angsuran, tipe_pembayaran, asuransi, wilayah)