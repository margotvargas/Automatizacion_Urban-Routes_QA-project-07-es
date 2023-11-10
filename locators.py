
from selenium.webdriver.common.by import By

class UrbanRoutesLocators:
    campo_direccion_desde = (By.ID, 'from')
    campo_direccion_hasta = (By.ID, 'to')
    mapa = (By.CLASS_NAME, 'gm-style')
    boton_pedir_taxi = (By.XPATH, "//button[@class='button round' and text()='Pedir un taxi']")
    tarifa_comfort = (By.XPATH, "//div[@class='tcard-title' and text()='Comfort']")
    entrada_numero_telefono = (By.CLASS_NAME, 'np-text')
    modal_entrada_numero_telefono = (By.ID, 'phone')
    boton_siguiente_modal_telefono = (By.XPATH, "//button[@type='submit'][@class='button full']")
    entrada_codigo_sms = (By.ID, 'code')
    boton_confirmar_sms = (By.XPATH, "//button[@class='button full' and text()='Confirmar']")
    enlace_forma_de_pago = (By.CLASS_NAME, 'pp-value-text')
    boton_modal_agregar_tarjeta = (By.CLASS_NAME, "pp-plus")
    entrada_numero_tarjeta = (By.ID, 'number')
    entrada_cvv_numero_tarjeta = (By.CSS_SELECTOR, "input[placeholder='12']")
    formulario_tarjeta_espacio_blanco = (By.CLASS_NAME, 'card-wrapper')
    boton_agregar_tarjeta_enlace = (By.XPATH, "//button[@type='submit'][@class='button full' and text()='Enlace']")
    boton_cerrar_modal_agregar_tarjeta = (By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div[1]/button')
    entrada_comentario_conductor = (By.ID, 'comment')
    requisitos_manta_panuelo = (By.XPATH, "//*[@id='root']/div/div[3]/div[3]/div[2]/div[2]/div[4]/div[2]/div[1]/div/div[2]/div/span")
    checkbox_manta_panuelo = (By.XPATH, "//*[@id='root']/div/div[3]/div[3]/div[2]/div[2]/div[4]/div[2]/div[1]/div/div[2]/div/input")
    etiqueta_manta_panuelos = (By.XPATH, "//div[contains(text(),'Manta y pañuelos')]")
    requisitos_dos_helados = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[2]/div[2]/div[4]/div[2]/div[3]/div/div[2]/div[1]/div/div[2]/div/div[3]')
    contador_dos_helados = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[2]/div[2]/div[4]/div[2]/div[3]/div/div[2]/div[1]/div/div[2]/div/div[2]')
    boton_pedir_un_taxi_final = (By.CLASS_NAME, 'smart-button')
    boton_detalles_de_la_ruta = (By.XPATH, "//button[@class='order-button' and img[@alt='burger']]")
    formulario_detalles_de_la_ruta = (By.CLASS_NAME, 'order-body')
    etiqueta_formulario_buscando_taxi = (By.XPATH, "//div[@class='order-header-title' and text()='Buscar automóvil']")
    etiqueta_nombre_conductor = (By.XPATH, '//*[@id="root"]/div/div[5]/div[2]/div[2]/div[1]/div[1]/div[2]')
    etiqueta_placa_vehiculo = (By.XPATH, "//div[@class='number']")
    etiqueta_minutos_espera_vehiculo = (By.XPATH, "//div[@class='order-header-title']")








