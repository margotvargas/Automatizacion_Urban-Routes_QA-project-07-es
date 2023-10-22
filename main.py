import data
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time
from codigo_sms import retrieve_phone_code #Importa la funcion para obtener el codigo del SMS
from locators import UrbanRoutesLocators  #Importa los selectores desde el nuevo módulo

class UrbanRoutesPage:
    def __init__(self, driver):
        self.driver = driver
        self.selectors = UrbanRoutesLocators # Instancia de la clase con los selectores

    def espera_apertura_pagina(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.selectors.campo_direccion_desde))

    def espera_cargar_mapa(self):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.selectors.mapa))

    def espera_formulario_ruta(self):
        self.driver.implicitly_wait(35)
        time.sleep(35)

    def ingresar_direccion_desde(self, direccion_desde):
        self.driver.find_element(*self.selectors.campo_direccion_desde).send_keys(direccion_desde)

    def ingresar_direccion_hasta(self, direccion_hasta):
        self.driver.find_element(*self.selectors.campo_direccion_hasta).send_keys(direccion_hasta)

    def click_boton_pedir_taxi(self):
        self.driver.find_element(*self.selectors.boton_pedir_taxi).click()

    def click_tarifa_comfort(self):
        WebDriverWait(self.driver, 3).until(EC.element_to_be_clickable(self.selectors.tarifa_comfort))
        self.driver.find_element(*self.selectors.tarifa_comfort).click()

    def click_numero_telefono(self):
        self.driver.find_element(*self.selectors.entrada_numero_telefono).click()

    def ingresar_numero_telefono(self, entrada_telefono):
        self.driver.find_element(*self.selectors.modal_entrada_numero_telefono).send_keys(entrada_telefono)

    def click_boton_modal_siguiente_numero_telefono(self):
        self.driver.find_element(*self.selectors.boton_siguiente_modal_telefono).click()

    def ingresar_codigo_sms(self):
        respuesta_sms = retrieve_phone_code(driver=self.driver) #Extraemos la función que obtiene el codigo SMS y la pasamos a una variable
        self.driver.find_element(*self.selectors.entrada_codigo_sms).send_keys(respuesta_sms) #ubicamos el selector del campo y colocamos la variable donde almacena el codigo.

    def click_boton_confirmar_sms(self):
        self.driver.find_element(*self.selectors.boton_confirmar_sms).click()

    def click_enlace_forma_de_pago(self):
        self.driver.find_element(*self.selectors.enlace_forma_de_pago).click()

    def click_boton_modal_agregar_tarjeta(self):
        self.driver.find_element(*self.selectors.boton_modal_agregar_tarjeta).click()

    def ingresar_entrada_numero_tarjeta(self, numero_tarjeta, codigo_tarjeta):
        self.driver.find_element(*self.selectors.entrada_numero_tarjeta).send_keys(numero_tarjeta)
        self.driver.find_element(*self.selectors.entrada_cvv_numero_tarjeta).send_keys(codigo_tarjeta)
        time.sleep(1)
    def click_formulario_tarjeta_espacio_blanco(self):
        self.driver.find_element(*self.selectors.formulario_tarjeta_espacio_blanco).click()

    def click_boton_agregar_tarjeta_enlace(self):
        self.driver.find_element(*self.selectors.boton_agregar_tarjeta_enlace).click()

    def click_boton_cerrar_modal_agregar_tarjeta(self):
        self.driver.find_element(*self.selectors.boton_cerrar_modal_agregar_tarjeta).click()

    def ingresar_entrada_comentario_conductor(self, mensaje_para_conductor):
        self.driver.find_element(*self.selectors.entrada_comentario_conductor).send_keys(mensaje_para_conductor)

    def agregar_requisitos_manta_panuelo(self):
        self.driver.find_element(*self.selectors.requisitos_manta_panuelo).click()
        time.sleep(1)

    def agregar_requisitos_dos_helados(self):
        self.driver.find_element(*self.selectors.requisitos_dos_helados).click()
        self.driver.find_element(*self.selectors.requisitos_dos_helados).click()
        time.sleep(1)

    def click_boton_pedir_un_taxi_final(self):
        self.driver.find_element(*self.selectors.boton_pedir_un_taxi_final).click()

    def click_boton_detalles_de_la_ruta(self):
        self.driver.find_element(*self.selectors.boton_detalles_de_la_ruta).click()
        WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(self.selectors.formulario_detalles_de_la_ruta))

    def get_from(self):
        return self.driver.find_element(*self.selectors.campo_direccion_desde).get_property('value')

    def get_to(self):
        return self.driver.find_element(*self.selectors.campo_direccion_hasta).get_property('value')

    def get_numero_telefono(self):
        return self.driver.find_element(*self.selectors.modal_entrada_numero_telefono).get_property('value')

    def get_entrada_numero_tarjeta(self):
        numero_tarjeta = self.driver.find_element(*self.selectors.entrada_numero_tarjeta).get_property('value')
        cvv_numero_tarjeta = self.driver.find_element(*self.selectors.entrada_cvv_numero_tarjeta).get_property('value')
        return numero_tarjeta, cvv_numero_tarjeta

    def get_entrada_comentario_conductor(self):
        return self.driver.find_element(*self.selectors.entrada_comentario_conductor).get_property('value')


class TestUrbanRoutes:

    driver = None

    @classmethod
    def setup_class(cls):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("perfLoggingPrefs", {'enableNetwork': True, 'enablePage': True})
        chrome_options.set_capability("goog:loggingPrefs", {'performance': 'ALL'})
        cls.driver = webdriver.Chrome(options=chrome_options)
        cls.driver.maximize_window()


    def test_set_route(self):
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)

        direccion_desde = data.direccion_desde
        direccion_hasta = data.direccion_hasta
        numero_telefono = data.numero_telefono
        numero_tarjeta = data.numero_tarjeta
        codigo_tarjeta = data.codigo_tarjeta
        mensaje_para_conductor = data.mensaje_para_conductor

        routes_page.espera_apertura_pagina()
        routes_page.ingresar_direccion_desde(direccion_desde)
        routes_page.ingresar_direccion_hasta(direccion_hasta)
        routes_page.espera_cargar_mapa()
        routes_page.click_boton_pedir_taxi()
        routes_page.click_tarifa_comfort()
        routes_page.click_numero_telefono()
        routes_page.ingresar_numero_telefono(numero_telefono)
        routes_page.click_boton_modal_siguiente_numero_telefono()
        routes_page.ingresar_codigo_sms()
        routes_page.click_boton_confirmar_sms()
        routes_page.click_enlace_forma_de_pago()
        routes_page.click_boton_modal_agregar_tarjeta()
        routes_page.ingresar_entrada_numero_tarjeta(numero_tarjeta, codigo_tarjeta)
        routes_page.click_formulario_tarjeta_espacio_blanco()
        routes_page.click_boton_agregar_tarjeta_enlace()
        routes_page.click_boton_cerrar_modal_agregar_tarjeta()
        routes_page.ingresar_entrada_comentario_conductor(mensaje_para_conductor)
        routes_page.agregar_requisitos_manta_panuelo()
        routes_page.agregar_requisitos_dos_helados()
        routes_page.click_boton_pedir_un_taxi_final()
        routes_page.click_boton_detalles_de_la_ruta()
        routes_page.espera_formulario_ruta()
        numero_tarjeta_value, cvv_numero_tarjeta_value = routes_page.get_entrada_numero_tarjeta()

        assert routes_page.get_from() == direccion_desde
        assert routes_page.get_to() == direccion_hasta
        assert routes_page.get_numero_telefono() == numero_telefono
        assert routes_page.get_entrada_comentario_conductor() == mensaje_para_conductor
        assert numero_tarjeta_value == numero_tarjeta
        assert cvv_numero_tarjeta_value == codigo_tarjeta

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()

