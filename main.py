import time

from selenium import webdriver
import interceptor #Importa la funcion "respuesta_order" para obtener el los resultados del pedido (placa, nombre de conductor, tiempo de esperaa)
import data
from UrbanRoutesPage import UrbanRoutesPage
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

    def test_1_configurar_direccion(self):

        self.direccion_desde = data.direccion_desde
        self.direccion_hasta = data.direccion_hasta

        # Llama a la función para configurar ambas direcciones y verifica los resultados
        self.routes_page.ingresar_login_direcciones(self.direccion_desde, self.direccion_hasta) #Llamamos a la funcion que llama a funcion de ingreso direcciones y clic en boton pedir taxi y pasamos las variables
        assert self.routes_page.obtener_direccion_desde() == self.direccion_desde
        assert self.routes_page.obtener_direccion_hasta() == self.direccion_hasta

    def test_2_seleccionar_tarifa_confort(self): #OK
        self.routes_page.seleccionar_tarifa_comfort() #Realiza la seleccion tarifa comfort
        assert self.routes_page.obtener_seleccionar_tarifa_comfort() == 'Manta y pañuelos' #Comprueba la seleccion de tarifa comfort con la habilitacion del elemento manta y pañuelos

    def test_3_ingresar_telefono(self): #OK
        numero_telefono = data.numero_telefono

        # Llama a la función para ingresar el número de teléfono y verifica el resultado
        self.routes_page.agrupando_ingreso_de_telefono(numero_telefono)
        assert self.routes_page.obtener_numero_telefono() == numero_telefono

    def test_4_ingresar_tarjeta(self): # Caso de prueba: Ingresar detalles de la tarjeta de crédito
        numero_tarjeta = data.numero_tarjeta
        codigo_tarjeta = data.codigo_tarjeta

        # Llama a la función para ingresar detalles de la tarjeta y verifica los resultados
        self.routes_page.agregar_tarjeta_funciones(numero_tarjeta, codigo_tarjeta)
        assert self.routes_page.obtener_entrada_numero_tarjeta() == numero_tarjeta
        assert self.routes_page.obtener_entrada_cvv_tarjeta() == codigo_tarjeta

    def test_5_ingresar_mensaje_conductor(self): ## Caso de prueba: Ingresar mensaje a conductor
        mensaje_para_conductor = data.mensaje_para_conductor

        # Llama a la función para ingresar detalles del conductor y verifica los resultados
        self.routes_page.ingresar_entrada_comentario_conductor(mensaje_para_conductor)
        assert self.routes_page.obtener_entrada_comentario_conductor() == mensaje_para_conductor

    def test_6_agregar_requisitos_manta_panuelos(self): ## Caso de prueba: Activar opción de manta y pañuelo
        self.routes_page.agregar_requisitos_manta_panuelo()
        # Verifica que la opción checkbox manta pañuelos esté seleccionada
        assert self.routes_page.obtener_comprobar_seleccion_manta_panuelo()

    def test_7_agregar_requisitos_2_helados(self): ## Caso de prueba: Añadir opción de 2 helados
        self.routes_page.agregar_requisitos_dos_helados()
        # Verifica que se hayan seleccionado 2 helados
        assert self.routes_page.obtener_comprobar_seleccion_dos_helados() == data.numero_helados

    def test_8_aparecer_modal_buscar_taxi(self): #Aparecer modal para buscar taxi
        self.routes_page.click_boton_pedir_un_taxi_final() #Llama al metodo para hacer clic al boton "pedir taxi final"
        assert self.routes_page.obtener_texto_buscando_taxi() == 'Buscar automóvil' #Comprobamos que al hacer clic se abre el formulario en donde empieza la Busqueda del automovil (aparece el elemento Buscar automovil)

    def test_9_detalles_del_pedido(self):
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

