import time

from selenium import webdriver

from selenium.webdriver.common.by import By


def get_temp_madrid():

    driver = webdriver.Chrome()

    driver.get("https://www.meteoblue.com/es/tiempo/semana/madrid_espa%C3%B1a_3117735")

    time.sleep(5)
    element_tempo = driver.find_element_by_css_selector("#header > div > a > div.current-picto-and-temp > div")


    tempera = element_tempo

    driver.close()

    return tempera


def get_rango_temp(temperatura):
    if temperatura < 25:
        return "Franja 1"
    elif temperatura <= 30:
        return "Franja 2"
    else:
        return "Franja 3"


def main():
    temperature = get_temp_madrid()
    temperature_rango = get_rango_temp(temperature)

    print("La temperatura en Madrid es de {} grados.".format(temperature))
    print("La franja de temperatura es {}.".format(temperature_rango))


main()
