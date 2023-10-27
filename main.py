from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time
import interceptor #Importa la funcion "respuesta_order" para obtener el los resultados del pedido (placa, nombre de conductor, tiempo de esperaa)
from codigo_sms import retrieve_phone_code #Importa la funcion para obtener el codigo del SMS
from interceptor import respuesta_order #Importa la funcion para obtener el body
from locators import UrbanRoutesLocators  #Importa los selectores desde el nuevo módulo
import data
class UrbanRoutesPage: # Clase que representa la página de Urban Routes
    def __init__(self, driver): # Inicialización de la clase con el controlador de Selenium (driver)
        self.driver = driver
        self.selectors = UrbanRoutesLocators #Instancia de la clase con los selectores

    #Funciones de esperas utilizadas:
    def espera_apertura_pagina(self): # Espera a que se cargue la página
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.selectors.campo_direccion_desde))

    def espera_cargar_mapa(self): # Espera a que el mapa sea visible
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.selectors.mapa))

    def espera_formulario_ruta_hasta_mostrar_placa(self): #Espera hasta que aparezca el elemento del número de placa al finalizar el contador del ultimo modal
        WebDriverWait(self.driver, 40).until(EC.visibility_of_element_located(self.selectors.etiqueta_placa_vehiculo))



    #Caso1: Funciones para configurar las direcciones
    def ingresar_direccion_desde(self, direccion_desde): # Ingresa la dirección de inicio
        self.driver.find_element(*self.selectors.campo_direccion_desde).send_keys(direccion_desde)

    def ingresar_direccion_hasta(self, direccion_hasta): # Ingresa la dirección del destino
        self.driver.find_element(*self.selectors.campo_direccion_hasta).send_keys(direccion_hasta)

    def click_boton_pedir_taxi(self): # Hace clic en el botón para pedir un taxi
        self.driver.find_element(*self.selectors.boton_pedir_taxi).click()
        time.sleep(1)
    def get_from(self) -> object:  #Obtiene la dirección desde
        return self.driver.find_element(*self.selectors.campo_direccion_desde).get_property('value')

    def get_to(self): #Obtiene la dirección hasta
        return self.driver.find_element(*self.selectors.campo_direccion_hasta).get_property('value')

        # Agrupa el ingreso de direcciones y clic en el botón de pedido de taxi

    def ingresar_login_direcciones(self, direccion_desde, direccion_hasta):
        # Agrupa el ingreso de direcciones y clic en el botón de pedido de taxi y llama a las esperas que estan en funciones
        self.espera_apertura_pagina()
        self.ingresar_direccion_desde(direccion_desde)
        self.ingresar_direccion_hasta(direccion_hasta)
        self.espera_cargar_mapa()
        self.click_boton_pedir_taxi()



    # Caso2:  funciones para seleccionar la tarifa comfort
    def seleccionar_tarifa_comfort(self): #Selecciona la tarifa comfort
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.selectors.tarifa_comfort))
        self.driver.find_element(*self.selectors.tarifa_comfort).click()

    def get_seleccionar_tarifa_comfort(self): # Obtiene la selección de la tarifa comfor
        return self.driver.find_element(*self.selectors.etiqueta_manta_panuelos).text

    #Caso:3  funciones para ingresar el telefono
    def click_numero_telefono(self): #Hace clic en el campo de número de teléfono que abre un modal
        self.driver.find_element(*self.selectors.entrada_numero_telefono).click()

    def ingresar_numero_telefono(self, entrada_telefono): # Ingresa el número de teléfono en el modal
        self.driver.find_element(*self.selectors.modal_entrada_numero_telefono).send_keys(entrada_telefono)

    def click_boton_modal_siguiente_numero_telefono(self): #Hace clic en el botón siguiente del modal
        self.driver.find_element(*self.selectors.boton_siguiente_modal_telefono).click()

    def ingresar_codigo_sms(self): # Ingresa el código SMS obtenido mediante la función retrieve_phone_code
        respuesta_sms = retrieve_phone_code(driver=self.driver) #Extraemos la función que obtiene el codigo SMS y la pasamos a una variable
        self.driver.find_element(*self.selectors.entrada_codigo_sms).send_keys(respuesta_sms) #Ubicamos el selector del campo y colocamos la variable donde almacena el codigo.

    def click_boton_confirmar_sms(self): # Hace clic en el botón para confirmar el código SMS
        self.driver.find_element(*self.selectors.boton_confirmar_sms).click()

    def get_numero_telefono(self):  # Obtiene el número de teléfono ingresado
        return self.driver.find_element(*self.selectors.modal_entrada_numero_telefono).get_property('value')

    def agrupando_ingreso_de_telefono(self, entrada_telefono): # Agrupa el proceso de ingreso de teléfono, código SMS y confirmación
        self.click_numero_telefono()
        self.ingresar_numero_telefono(entrada_telefono)
        self.click_boton_modal_siguiente_numero_telefono()
        self.ingresar_codigo_sms()
        self.click_boton_confirmar_sms()

    #Caso4: funciones para agregar tarjeta de credito
    def click_enlace_forma_de_pago(self): # Hace clic en el enlace de forma de pago
        self.driver.find_element(*self.selectors.enlace_forma_de_pago).click()

    def click_boton_modal_agregar_tarjeta(self): # Hace clic en el botón para agregar una tarjeta
        self.driver.find_element(*self.selectors.boton_modal_agregar_tarjeta).click()

    def ingresar_entrada_numero_tarjeta(self, numero_tarjeta): # Ingresa el número de tarjeta
        self.driver.find_element(*self.selectors.entrada_numero_tarjeta).send_keys(numero_tarjeta)
        time.sleep(1)

    def ingresar_entrada_cvv_tarjeta(self, codigo_tarjeta): # Ingresa el código CVV de la tarjeta
        self.driver.find_element(*self.selectors.entrada_cvv_numero_tarjeta).send_keys(codigo_tarjeta)
        time.sleep(1)

    def click_formulario_tarjeta_espacio_blanco(self): # Hace clic en el espacio en blanco del formulario de tarjeta
        self.driver.find_element(*self.selectors.formulario_tarjeta_espacio_blanco).click()

    def click_boton_agregar_tarjeta_enlace(self): # Hace clic en el botón para agregar la tarjeta
        self.driver.find_element(*self.selectors.boton_agregar_tarjeta_enlace).click()

    def click_boton_cerrar_modal_agregar_tarjeta(self): # Hace clic en el botón para cerrar el modal de agregar tarjeta
        self.driver.find_element(*self.selectors.boton_cerrar_modal_agregar_tarjeta).click()

    def get_entrada_numero_tarjeta(self): # Obtiene el número de tarjeta ingresado
        numero_tarjeta = self.driver.find_element(*self.selectors.entrada_numero_tarjeta).get_property('value')
        return numero_tarjeta

    def get_entrada_cvv_tarjeta(self): # Obtiene el código CVV de la tarjeta ingresado
        cvv_numero_tarjeta = self.driver.find_element(*self.selectors.entrada_cvv_numero_tarjeta).get_property('value')
        return cvv_numero_tarjeta
    def agregar_tarjeta_funciones(self, numero_tarjeta, codigo_tarjeta):
        # Agrupa las funciones para agregar una tarjeta de crédito
        self.click_enlace_forma_de_pago()
        self.click_boton_modal_agregar_tarjeta()
        self.ingresar_entrada_numero_tarjeta(numero_tarjeta)
        self.ingresar_entrada_cvv_tarjeta(codigo_tarjeta)
        self.click_formulario_tarjeta_espacio_blanco()
        self.click_boton_agregar_tarjeta_enlace()
        self.click_boton_cerrar_modal_agregar_tarjeta()

    #Caso5: Comentario conductor
    def ingresar_entrada_comentario_conductor(self, mensaje_para_conductor): # Ingresa el comentario para el conductor
        self.driver.find_element(*self.selectors.entrada_comentario_conductor).send_keys(mensaje_para_conductor)

    def get_entrada_comentario_conductor(self): # Obtiene el comentario para el conductor ingresado
        return self.driver.find_element(*self.selectors.entrada_comentario_conductor).get_property('value')

    #Caso6: Añadir manta y pañuelo
    def agregar_requisitos_manta_panuelo(self): ## Hace clic en el checkbox para activar manta y pañuelo
        self.driver.find_element(*self.selectors.requisitos_manta_panuelo).click()

    def get_comprobar_seleccion_manta_panuelo(self): # Comprueba si el checkbox de manta y pañuelo está seleccionado
        checkbox = self.driver.find_element(*self.selectors.checkbox_manta_panuelo)
        return checkbox.is_selected()

    # Caso7: Añadir 2 helados
    def agregar_requisitos_dos_helados(self): # Hace clic en el checkbox 2 VECES para añadir helados
        self.driver.find_element(*self.selectors.requisitos_dos_helados).click()
        self.driver.find_element(*self.selectors.requisitos_dos_helados).click()

    def get_comprobar_seleccion_dos_helados(self): # Obtiene la cantidad de helados seleccionados
        contador_helado = self.driver.find_element(*self.selectors.contador_dos_helados)
        return int(contador_helado.text)


    # Caso8: Modal pedir taxi
    def click_boton_pedir_un_taxi_final(self):
        # Hace clic en el botón para pedir un taxi final
        self.driver.find_element(*self.selectors.boton_pedir_un_taxi_final).click()
        # Obtiene la respuesta de la orden a través de la función respuesta_order del archivo interceptor
        variable_respuesta_orden = respuesta_order(self.driver)
        return variable_respuesta_orden #lo retorna

    def obtener_nombre_conductor(self):
        # Funcion get que obtiene el nombre del conductor, la placa del vehículo y el mensaje de espera del vehículo
        nombre_conductor = self.driver.find_element(*self.selectors.etiqueta_nombre_conductor).text
        placa_vehiculo = self.driver.find_element(*self.selectors.etiqueta_placa_vehiculo).text
        mensaje_espera_vehiculo = self.driver.find_element(*self.selectors.etiqueta_minutos_espera_vehiculo).text
        return nombre_conductor, placa_vehiculo, mensaje_espera_vehiculo


    def click_boton_detalles_de_la_ruta(self): # Hace clic en el botón para ver los detalles de la ruta
        self.driver.find_element(*self.selectors.boton_detalles_de_la_ruta).click()
        self.espera_formulario_ruta_hasta_mostrar_placa()
        time.sleep(2)


# Clase de prueba que contiene los test utilizando Selenium
class TestUrbanRoutes:

    driver = None
    @classmethod
    def setup_class(cls): # Configuración inicial de la clase de prueba
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("perfLoggingPrefs", {'enableNetwork': True, 'enablePage': True})
        chrome_options.set_capability("goog:loggingPrefs", {'performance': 'ALL'})
        cls.driver = webdriver.Chrome(options=chrome_options)
        cls.driver.maximize_window()
        cls.driver.get(data.urban_routes_url)
        cls.routes_page = UrbanRoutesPage(cls.driver)

    def test_1_configurar_direccion(self): #OK
        self.direccion_desde = data.direccion_desde
        self.direccion_hasta = data.direccion_hasta

        # Llama a la función para configurar ambas direcciones y verifica los resultados
        self.routes_page.ingresar_login_direcciones(self.direccion_desde, self.direccion_hasta) #Llamamos a la funcion que llama a funcion de ingreso direcciones y clic en boton pedir taxi y pasamos las variables
        assert self.routes_page.get_from() == self.direccion_desde
        assert self.routes_page.get_to() == self.direccion_hasta

    def test_2_seleccionar_tarifa_confort(self): #OK
        self.routes_page.seleccionar_tarifa_comfort() #Realiza la seleccion tarifa comfort
        assert self.routes_page.get_seleccionar_tarifa_comfort() == data.manta_panuelos #Comprueba la seleccion de tarifa comfort con la habilitacion del elemento manta y pañuelos

    def test_3_ingresar_telefono(self): #OK
        numero_telefono = data.numero_telefono

        # Llama a la función para ingresar el número de teléfono y verifica el resultado
        self.routes_page.agrupando_ingreso_de_telefono(numero_telefono)
        assert self.routes_page.get_numero_telefono() == numero_telefono

    def test_4_ingresar_tarjeta(self): # Caso de prueba: Ingresar detalles de la tarjeta de crédito
        numero_tarjeta = data.numero_tarjeta
        codigo_tarjeta = data.codigo_tarjeta

        # Llama a la función para ingresar detalles de la tarjeta y verifica los resultados
        self.routes_page.agregar_tarjeta_funciones(numero_tarjeta, codigo_tarjeta)
        assert self.routes_page.get_entrada_numero_tarjeta() == numero_tarjeta
        assert self.routes_page.get_entrada_cvv_tarjeta() == codigo_tarjeta
        #time.sleep(1)

    def test_5_ingresar_mensaje_conductor(self): ## Caso de prueba: Ingresar mensaje a conductor
        mensaje_para_conductor = data.mensaje_para_conductor

        # Llama a la función para ingresar detalles de la tarjeta y verifica los resultados
        self.routes_page.ingresar_entrada_comentario_conductor(mensaje_para_conductor)
        assert self.routes_page.get_entrada_comentario_conductor() == mensaje_para_conductor

    def test_6_agregar_requisitos_manta_panuelos(self): ## Caso de prueba: Activar opción de manta y pañuelo
        self.routes_page.agregar_requisitos_manta_panuelo()
        # Verifica que la opción esté seleccionada
        assert self.routes_page.get_comprobar_seleccion_manta_panuelo()

    def test_7_agregar_requisitos_2_helados(self): ## Caso de prueba: Añadir opción de 2 helados
        self.routes_page.agregar_requisitos_dos_helados()
        # Verifica que se hayan seleccionado 2 helados
        assert self.routes_page.get_comprobar_seleccion_dos_helados() == data.numero_helados

    def test_8_aparecer_modal_buscar_taxi(self): #Aparecer modal para buscar taxi
        self.routes_page.click_boton_pedir_un_taxi_final() #Llama al metodo para hacer clic al boton "pedir taxi final"
        self.routes_page.click_boton_detalles_de_la_ruta() #Llama al metodo para hacer clic al boton "detalles del pedido"

        # Obtiene información del conductor
        nombre_conductor, placa_vehiculo, mensaje_espera_vehiculo = self.routes_page.obtener_nombre_conductor()

        # Obtiene datos de la ruta a través de la función interceptor.respuesta_order
        datos_ruta = interceptor.respuesta_order(self.driver)
        eta = datos_ruta['eta']

        # Realiza las afirmaciones (assertions) para verificar la información
        detallado_datos_ruta = f'El conductor llegará en {eta} min.'
        assert nombre_conductor == datos_ruta['name']
        assert placa_vehiculo == datos_ruta['number']
        assert mensaje_espera_vehiculo == detallado_datos_ruta


    # Método para realizar acciones después de todos los tests de la clase
    @classmethod
    def teardown_class(cls):
        cls.driver.quit()  # Cierra el navegador al finalizar todos los tests

