<!DOCTYPE html>
<html>
<head>
    
</head>
<body>

<h1>Proyecto de Web Scraping de Sunat</h1>

<h2>Descripción del Proyecto</h2>
<p>Este proyecto tiene como objetivo realizar web scraping en la página web de la <a href="https://e-consultaruc.sunat.gob.pe/cl-ti-itmrconsruc/FrameCriterioBusquedaWeb.jsp">Superintendencia Nacional de Aduanas y de Administración Tributaria (Sunat)</a> de Perú. El propósito es obtener información de empresas a partir de sus números de RUC (Registro Único de Contribuyentes) mediante la búsqueda por DNI (Documento Nacional de Identidad).</p>

<h2>Input del Proyecto</h2>
<p>El input del proyecto es una base de datos que contiene un listado de DNIs. Esta base de datos fue obtenida del <a href="https://objectstorage.us-ashburn-1.oraclecloud.com/p/Ovj4ah5usLFDMxJZEj8Q1wmkP3ld9SVohrd3t7yhw5Hf0jle-D5RGMG9_fr1Zc9n/n/id08kfinkj3s/b/doccontraloria/o/uneteanuestroequipo/documentos/listado_acc.pdf">CONCURSO PÚBLICO DE MÉRITOS N° 01-2018-CG</a>, que es de acceso público.</p>


<h2>Ejecución del Proyecto</h2>
<ol>
    <li>El proyecto comienza leyendo la base de datos de DNIs desde un archivo Excel.</li>
    <li>Luego, ajusta la longitud de los DNIs según un estándar específico:</li>
        <ul>
            <li>Si el DNI tiene 6 números, se agregan 2 ceros al principio.</li>
            <li>Si el DNI tiene 7 números, se agrega 1 cero al principio.</li>
            <li>Si el DNI tiene 8 números, no se hace ningún ajuste.</li>
        </ul>
    <li>Se inicia un navegador web automatizado (en este caso, se utiliza Microsoft Edge) con WebDriver.</li>
    <li>Se realiza un loop sobre la lista de DNIs ajustados.</li>
    <li>Para cada DNI, se ejecuta una función para iniciar la búsqueda en la página web de Sunat.</li>
    <li>Luego, se ejecuta otra función para realizar la consulta del DNI en la página web y extraer la información de la empresa.</li>
    <li>La información obtenida se almacena en una lista de resultados.</li>
    <li>Finalmente, se crea un archivo Excel con los resultados obtenidos.</li>
</ol>

<h2>Dependencias del Proyecto</h2>
<p>El proyecto utiliza las siguientes bibliotecas de Python:</p>
<ul>
    <li>pandas: Para la manipulación de datos desde archivos Excel.</li>
    <li>selenium: Para la automatización del navegador web.</li>
    <li>time: Para pausas entre las acciones.</li>
    <li>os: Para operaciones del sistema operativo.</li>
    <li>re: Para el manejo de expresiones regulares.</li>
</ul>

<h2>Consideraciones Importantes</h2>
<p>Se recomienda ejecutar este proyecto con cuidado y dentro de los límites legales y éticos de web scraping. Este proyecto se desarrolló con fines educativos y prácticos. Es importante revisar y entender las políticas de uso del sitio web de Sunat antes de realizar el web scraping.</p>

<p>¡Disfruta explorando la información obtenida!</p>

</body>
</html>
