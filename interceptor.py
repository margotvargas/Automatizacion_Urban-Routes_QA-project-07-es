def respuesta_order(driver) -> str:
    ##Este código devuelve el body de la solicitud API del pedido de taxi (chofer, tiempo de espera, placa)

    import json
    import time
    from selenium.common import WebDriverException
    response = None
    for i in range(10):
        try:
            logs = [log["message"] for log in driver.get_log('performance') if log.get("message")
                    and 'api/v1/order' in log.get("message")]
            for log in reversed(logs):
                message_data = json.loads(log)["message"]
                body = driver.execute_cdp_cmd('Network.getResponseBody',
                                              {'requestId': message_data["params"]["requestId"]})
                response = body
        except WebDriverException:
            time.sleep(1)
            continue
        if not response:
            raise Exception("No se encontró el código de confirmación del body.\n"
                            "Utiliza 'respuesta_order' solo después de haber solicitado el código en tu aplicación.")
        response = json.loads(response['body'])
        return response
