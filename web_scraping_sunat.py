"""
Created on May 15, 2024 

Y@author: Rodrigo Silupú Peñaranda
"""
import os
import re
import time
from selenium import webdriver
import pandas as pd
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException

###################### CREAR TXT A PARTIR DE UN ARCHIVO CON LOS N  ROS DE DNI ###########################

archivo=f'D://Rodrigo Silupú//Lista DNIS'
file_name=f'{archivo}.xlsx'
bd = pd.read_excel(file_name, dtype=str) #Incluir, si es necesario, el nomrbre de la hoja de excel
dnis = bd[['nUserID']].rename(columns={'nUserID': 'dni'})
dnis=dnis['dni'].tolist()
dnis

# Ajustar la longitud de los DNIs
dnis_adjusted = []
for dni in dnis:
    if len(dni)==5:
        dni_adjusted = '000' + dni
    elif len(dni) == 6:
        dni_adjusted = '00' + dni
    elif len(dni) == 7:
        dni_adjusted = '0' + dni
    else:
        dni_adjusted = dni
    dnis_adjusted.append(dni_adjusted)

# Mostrar los DNIs ajustados
dnis=dnis_adjusted


results=[]
output_directory=f'D://Rodrigo Silupú'
prefs = {'download.default_directory': output_directory}

driver_path = 'D:\\Rodrigo Silupú\\edgedriver_win64\\msedgedriver.exe' #Install el indriver de microsoft edge

######################## SCRAPING ##########################
headless = 0
# Use Microsoft Edge WebDriver options
options = webdriver.EdgeOptions()
options.add_argument("--no-sandbox")
options.add_argument("--disable-gpu")
if headless == 1:
    options.add_argument("--headless")
options.add_experimental_option('prefs', prefs)


# Initialize Microsoft Edge WebDriver
service = Service(executable_path=driver_path)
b = webdriver.Edge(service=service, options=options)

# Set the window position and size
screen_width = b.execute_script("return window.screen.width;")
screen_height = b.execute_script("return window.screen.height;")
window_width = int(screen_width * 0.35)
window_height = int(screen_height * 0.968)  # Adjust the height as needed

b.set_window_position(screen_width - window_width, 0)
b.set_window_size(window_width, window_height)

for dni in dnis: 
    try:
        def Iniciar():
            b.get('https://e-consultaruc.sunat.gob.pe/cl-ti-itmrconsruc/FrameCriterioBusquedaWeb.jsp')
            time.sleep(1)

            validar_archivo = b.find_element("xpath", "//*[@id='btnPorDocumento']")
            validar_archivo.click()
            time.sleep(1)

        def Consultar(dni):
            input_dni = b.find_element("xpath", "//*[@id='txtNumeroDocumento']")
            input_dni.clear()
            input_dni.send_keys(dni)
            time.sleep(1)

            send = b.find_element("xpath", "//*[@id='btnAceptar']")
            send.click()
            time.sleep(1)

            try: 
                name_element = b.find_element('xpath', "/html/body/div/div[2]/div/div[3]/div[2]/a/h4[2]")
                name = name_element.text

                ruc_element = b.find_element('xpath', "/html/body/div/div[2]/div/div[3]/div[2]/a/h4[1]")
                ruc_text=ruc_element.text 
                ruc=re.search(r'RUC:\s*(\d+)', ruc_text)
                ruc=ruc.group(1) if ruc else None

                ubicacion_element = b.find_element('xpath', '/html/body/div/div[2]/div/div[3]/div[2]/a/p[1]')
                ubicacion = ubicacion_element.text

                estado_element = b.find_element('xpath', '/html/body/div/div[2]/div/div[3]/div[2]/a/p[2]/strong/span')
                estado = estado_element.text

                print(f'Datos encontrados para el DNI {dni}')
                results.append({'DNI': dni, 'Nombre': name, 'RUC': ruc, 'Ubicación': ubicacion, 'Estado': estado })

                back = b.find_element('xpath', "/html/body/div/div[2]/div/div[4]/button")
                back.click()
                time.sleep(1)
           


            except NoSuchElementException:
                print(f'No se encontraron datos para el DNI {dni}')
                results.append({'DNI': 'None', 'Nombre': 'None', 'RUC': 'None', 'Ubicación': 'None', 'Estado': 'None' })
                b.get('https://e-consultaruc.sunat.gob.pe/cl-ti-itmrconsruc/FrameCriterioBusquedaWeb.jsp')
                b.implicitly_wait(1) 
       

    except Exception as e:
        print(f"Error: {str(e)}")
        

# Iterar sobre los DNIs y realizar el scraping
try:
    for dni in dnis:
        Iniciar()
        Consultar(dni)

finally:
    b.quit()
print("b.quit")




df_results=pd.DataFrame(results)
df_results.to_excel(f'D://Rodrigo Silupú//Nombres.xlsx', index=False)
