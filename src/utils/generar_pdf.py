from src.utils.paleta_rojo import rojo
import matplotlib.pyplot as plt
from src.utils.helpers import cargar_datos_sin_filtros
from src.utils.paleta_rojo import rojo
from matplotlib import rcParams
from fpdf import FPDF
import os
import calmap
import pandas as pd
from matplotlib.colors import ListedColormap, Normalize
from matplotlib.ticker import MaxNLocator
import seaborn as sns

def generar_pdf(output_path="Resumen Estadístico.pdf"):
    df = cargar_datos_sin_filtros()
    # """
    # P: portrait(vertical)
    # L: landscape(horizontal)

    # A4: 210x297mm
    # Carta: 216x279mm
    # """
    tamaño_carta = (216, 279)
    pdf = FPDF(orientation='P', unit='mm', format=tamaño_carta)
    pdf.set_top_margin(25.4)
    pdf.set_left_margin(25.4)
    pdf.set_right_margin(25.4)

    # Portada
    pdf.add_page()

    pdf.set_font('Arial', 'B', 12)
    pdf.multi_cell(0, 8, txt="República Bolivariana de Venezuela \n Universidad Central de Venezuela \n Facultad de Ciencias Economicas y Sociales \n Escuela de Estadistica y Ciencias Actuariales", border=0, align="C")
    pdf.ln(55)

    pdf.set_font('Arial', 'B', 16)
    pdf.multi_cell(0, 8, txt="Diseño e Implementación de una Aplicación en lenguaje Python para el Control, Seguimiento y Gestión de la empresa de Transporte ACO Rent Car", align='C')
    pdf.ln(45)

    pdf.set_font('Arial', 'B', 12)
    pdf.multi_cell(0, 8, txt="Autores", align='R')
    pdf.ln(4)

    pdf.multi_cell(0, 8, txt="Cano Vielma Néstor Alirio", align='R')
    pdf.ln(2)

    pdf.multi_cell(0, 8, txt="Briceño Torres Carmen Emilia", align='R')
    pdf.ln(2)

    pdf.multi_cell(0, 8, txt="Maneiro Chirino Ronald Alejandro", align='R')
    pdf.ln(2)
    pdf.multi_cell(0, 8, txt="Profesor. Jesús Ochoa", align='L')
    pdf.ln(15)

    pdf.multi_cell(0, 8, txt="Caracas, marzo de 2025", align='C')

    # Capitulo Uno
    pdf.add_page()
    pdf.set_font('Arial', 'B', 12)
    pdf.cell(0, 8, txt="CAPITULO I", align='C')
    pdf.ln(8)
    pdf.cell(0, 8, txt="Planteamiento del Problema", align='C')

    pdf.ln(8)

    pdf.set_font('Arial', '', 12)
    pdf.multi_cell(0, 8, txt="     La empresa ACO Rent Car, desde su creación se ha caracterizado por el desarrollo de un modelo de negocio innovador, que les brinda a sus clientes atención personalizada, con el alquiler de vehículos adaptados a sus requerimientos y necesidades de transporte, facilitando la movilidad de turistas, ejecutivos y público en general, en aproximadamente 205 países a nivel mundial, según refleja la página web de la institución.  ", align='J', border=0,)

    pdf.ln(8)

    pdf.multi_cell(0, 8, txt="     Cabe destacar, que el alquiler de vehículos es un servicio clave dentro de la industria del transporte, al igual que ACO Rent Car, empresas ubicadas en el mismo sector como Uber Rent, AVIS, SIX, Hertz Digital, Enterprise, entre otras, han apostado como estrategia de negocio a la incorporación de la digitalización de los procesos, la implementación de aplicaciones móviles, uso de tecnologías como geolocalización, inteligencia artificial y pagos electrónicos. Estas plataformas incluyen módulos de registro de clientes, disponibilidad de vehículos, facturación, rastreo de unidades, soporte al usuario, reserva y administración de flotas, su aplicación ha permitido la reducción de los costos operativos y mejorado la relación con los usuarios.", align="J")

    pdf.ln(8)

    pdf.multi_cell(0, 8, txt="     De igual forma, la digitalización de los procesos suministra información relacionada con la detección de oportunidades de desarrollo adecuadas según el mercado, en algunos casos con opciones de ofertas económicas, de lujo o de transporte especializado (turismo, traslados corporativos), he inclusive, realizar inversiones en la incorporación de vehículos eléctricos que disminuyan su impacto en el tema ambiental, esta ha sido una de las fortalezas y evolución de la empresa.", align="J")

    pdf.ln(8)

    pdf.multi_cell(0, 8, txt="     La industria del alquiler de vehículos cada día es más competitiva, presenta retos como la definición de la presencia geográfica, hay que tomar decisiones de enfocarse en una sola región o ampliar a otros espacios de cada país menos atendidos, es el caso de mercados como Asia, África o América Latina. Aspectos como la consolidación de su presencia, centrando su inversión en un sector o diversificar su flota según indiquen los estudios. ", align="J")

    pdf.ln(8)

    pdf.multi_cell(0, 8, txt="     Ahora bien, fortalecerse como una marca que se distingue dentro de su nicho, o hacerse más competitivo e innovador, explorando espacios como el del alquiler por suscripción, incorporación de flotas de vehículos eléctricos, ofrecer precios más competitivos e inclusive personalizar servicios adaptados a sectores específicos del mercado, o el tema de desarrollar su visibilidad en las plataformas digitales, pasa por la realización de grandes campañas o de alianzas estratégicas con medios locales, sobre todo para dar a conocer los servicios en aeropuertos, turismo, asociaciones con aerolíneas, cadenas hoteleras. ", align="J")

    pdf.ln(8)

    pdf.multi_cell(0, 8, txt="     Sobre este aspecto, el desarrollo de una propuesta de aplicación en lenguaje Python, no solo depende del interfaz y funcionabilidad que tengan los usuarios con ella, esta debe suministrar suficiente información centralizada para el control y seguimiento administrativo, que vincule cada una de las 205 empresas adscritas a ACO Rent Car, permitiendo organizar, automatizar y sincronizar ventas, marketing, servicio al cliente, soporte técnico y datos para el diseño y ejecución de estrategias de gestión. ", align="J")

    pdf.ln(8)

    pdf.multi_cell(0, 8, txt="     Las estrategias que se decidan tomar serán siempre una acción sencillamente compleja, que requiere de suficiente información, al respecto Edward Deming expresa, 'sin datos, solo eres otra persona más dando su opinión', que, en algunos casos, implica cambios radicales, como por ejemplo salirse de sus métodos tradicionales de gestión. ", align="J")

    pdf.ln(8)

    pdf.multi_cell(0, 8, txt="     Partiendo del análisis antes descrito, surge la siguiente hipótesis: el diseño y desarrollo de una aplicación en lenguaje Python para la gestión de la empresa de alquiler de automóviles ACO Rent Car, permitirá optimizar el control y seguimiento de los procesos operativos, mejorar la toma de decisiones financieras y comerciales, y facilitar el diseño de estrategias de gestión mediante la implementación de inteligencia de negocios y análisis predictivo.  ", align="J")

    pdf.ln(8)

    pdf.multi_cell(
        0, 8, txt="A la luz de lo anteriormente expuesto, se plantea la siguiente interrogante.", align="J")

    pdf.ln(8)

    pdf.multi_cell(0, 8, txt="En qué medida el diseño y ejecución de una aplicación facilita suficiente información para el control, seguimiento de los procesos y el diseño de estrategias de desarrollo para la empresa ACO Rent Cars.", align="J")

    pdf.ln(8)

    # Pagina de Objetivos
    pdf.add_page()
    pdf.set_font('Arial', 'B', 12)

    pdf.multi_cell(0, 8, txt="Objetivo General ", align="C")
    pdf.ln(8)

    pdf.set_font('Arial', '', 12)
    pdf.multi_cell(0, 8, txt="     Diseñar y desarrollar una aplicación en lenguaje Python, para la gestión de la empresa de alquiler de automóviles ACO Rent Car, que permita el control, seguimiento y optimización de las estrategias operativas y comerciales.  ", align="J")

    pdf.ln(8)

    pdf.set_font('Arial', 'B', 12)
    pdf.multi_cell(0, 8, txt="Objetivos Especificos", align="C")
    pdf.ln(8)

    pdf.set_font('Arial', '', 12)
    pdf.multi_cell(0, 8, txt="     Caracterizar e identificar patrones o tendencias significativas en el registro de datos de la empresa ACO Rent Car.", align="J")

    pdf.ln(8)

    pdf.multi_cell(0, 8, txt="     Crear una interfaz intuitiva y funcional que facilite el control, seguimiento y toma de decisiones de gestión.", align="J")

    pdf.ln(8)

    pdf.multi_cell(
        0, 8, txt="    Desarrollar herramientas analíticas para la generación de reportes y estadísticas.", align="J")

    pdf.ln(8)

    pdf.multi_cell(
        0, 8, txt="     Incorporar una sección que genere un resumen automatizado que refleje la base de datos.", align="J")

    pdf.ln(8)

    # Justificacion y Delimitacion

    pdf.add_page()
    pdf.set_font('Arial', 'B', 12)

    pdf.multi_cell(0, 8, txt="Justificación", align="C")

    pdf.ln(8)

    pdf.set_font('Arial', '', 12)

    pdf.multi_cell(0, 8, txt="     El diseño de la aplicación busca proporcionar a la empresa ACO Rent Car, una herramienta de gestión empresarial, que le permita organizar, automatizar y sincronizar la información de sus empresas filiales para la toma de decisiones según sus necesidades, con la posibilidad de integrarse con otras plataformas, basada en datos suministrados por estas.", align="J")

    pdf.ln(8)

    pdf.multi_cell(0, 8, txt="     A nivel personal, su realización permite la experiencia práctica en la aplicación de las técnicas estadísticas y el diseño de aplicaciones en lenguaje Python impartidas en la universidad, facilitando una comprensión más amplia de como estas pueden ser utilizadas para el análisis de datos reales informadas en el ámbito laboral. Desde el punto de vista académico, sus resultados pueden ser de gran utilidad para futuros estudiantes, investigadores e instituciones, en virtud que este estudio permitirá crear conocimiento, con el cual se justifique la realización de trabajos posteriores.", align="J")

    pdf.ln(8)

    pdf.set_font('Arial', 'B', 12)
    pdf.multi_cell(0, 8, txt="Delimitación", align="C")
    pdf.ln(8)

    pdf.set_font('Arial', '', 12)

    pdf.multi_cell(0, 8, txt="     El alcance y delimitación se suscribe al análisis de 1.265 registros presentes en la base de datos suministrada, ubicados en diferentes países a nivel mundial, se recurre al lenguaje Python por su versatilidad y facilidad para el manejo en las ciencias de datos, inteligencia artificial, desarrollo de web y automatización de procesos.", align="J")

    # Marco Teorico
    pdf.add_page()
    pdf.set_font('Arial', 'B', 12)
    pdf.cell(0, 10, txt='CAPITULO II', align="C")
    pdf.ln(8)

    pdf.cell(0, 10, txt='Marco Teórico', align="C")
    pdf.ln(8)

    pdf.set_font('Arial', '', 12)

    pdf.multi_cell(0, 8, txt="     El desarrollo del marco teórico relacionado con el análisis de los servicios prestados por cada una de las oficinas de la empresa ACO Rent Car presentes en la base de datos, se realiza con el propósito de situar al problema objeto de estudio dentro de un conjunto de conocimientos, lo más sólido posible, a fin de orientar la búsqueda y ofrecer una conceptualización adecuada de los términos utilizados, pudiendo ser manejados y convertidos en acciones concretas.", align="J")

    pdf.ln(8)

    pdf.multi_cell(
        0, 8, txt="Al respecto, Balestrini (2006), define el marco teórico como: ", align="J")
    pdf.ln(8)

    pdf.multi_cell(0, 6, txt="'el resultado de la selección de aquellos aspectos más relacionados del cuerpo teórico epistemológico que se asume, referidos al tema específico para su estudio' (p.91). De allí pues, que su racionalidad, estructura lógica y consistencia interna, va a permitir el análisis de los hechos conocidos, así como, orientar la búsqueda de otros datos relevantes.", align="C")
    pdf.ln(8)

    pdf.multi_cell(0, 8, txt="     Para realizar el análisis, el trabajo se fundamenta en diversas teorías estudios empíricos que permiten comprender la dinámica y el comportamiento del servicio de alquiler de automóviles. Este enfoque sostiene que las empresas generan productos o brindan servicios en aquellos espacios donde presentan mayor rentabilidad. ", align="J")
    pdf.ln(8)

    pdf.multi_cell(0, 8, txt="     Al respecto, la teoría comparativa, sugiere fundamentar el desarrollo de las empresas de acuerdo producción de bienes y servicios en los cuales se poseen ventajas comparativas, y desde ese punto de vista la aplicación propuesta pretende dar respuesta a las estrategias de inversión.", align="J")
    pdf.ln(8)

    # Reseña Historica
    pdf.add_page()
    pdf.set_font('Arial', 'B', 12)
    pdf.multi_cell(0, 8, txt="Reseña Histórica", align="J")
    pdf.ln(8)

    pdf.set_font('Arial', '', 12)
    pdf.multi_cell(0, 8, txt="ACO RENT A CAR, se ha caracterizado por ofrecer un servicio de alquiler de vehículos, que tiene presencia en el mercado por más de 40 años. La empresa se distingue por brindar flexibilidad y comodidad, ideales para vacaciones en familia o viajes de negocios. A lo largo de su trayectoria, ha mantenido un enfoque en la satisfacción del cliente, asegurando que sus vehículos se encuentren en excelentes condiciones y proporcionando asistencia en carretera de alta calidad.", align="J")
    pdf.ln(8)

    pdf.set_font('Arial', 'B', 12)
    pdf.multi_cell(0, 8, txt="Visión", align="J")
    pdf.ln(8)

    pdf.set_font('Arial', '', 12)
    pdf.multi_cell(0, 8, txt="Ser una empresa líder con una marca internacional reconocida por su tecnología de punta y por la alta calidad de sus servicios.", align="J")
    pdf.ln(8)

    pdf.set_font('Arial', 'B', 12)
    pdf.multi_cell(0, 8, txt="Misión", align="J")
    pdf.ln(8)

    pdf.set_font('Arial', '', 12)
    pdf.multi_cell(0, 8, txt="Somos una empresa de alquiler de vehículos sin chofer a nivel nacional e internacional, orientada a satisfacer las expectativas de los clientes, con capital humano competente, motivado y comprometido con la mejora continua de la gestión de la calidad, en un ambiente de trabajo seguro y estable, fomentando la innovación, utilizando la última tecnología, creando valor y bienestar para nuestros empleados, accionistas y las sociedades donde operamos.", align="J")
    pdf.ln(8)

    pdf.set_font('Arial', 'B', 12)
    pdf.multi_cell(0, 8, txt="Políticas de Calidad", align="J")
    pdf.ln(8)

    pdf.set_font('Arial', '', 12)
    pdf.multi_cell(0, 8, txt="- Adquirir los mejores vehículos.", align="J")
    pdf.ln(8)

    pdf.multi_cell(
        0, 8, txt="- Mantener los vehículos en condiciones óptimas de funcionamiento y apariencia.", align="J")
    pdf.ln(8)

    pdf.multi_cell(
        0, 8, txt="- Entregar vehículos limpios y totalmente equipados.", align="J")
    pdf.ln(8)

    pdf.multi_cell(0, 8, txt="- Ofrecer atención cordial e información oportuna y confiable durante todo el proceso de alquiler de vehículos.", align="J")
    pdf.ln(8)

    pdf.multi_cell(0, 8, txt="- Dar asistencia oportuna.", align="J")
    pdf.ln(8)

    pdf.multi_cell(
        0, 8, txt="- Mantener compromiso con la mejora continua de la eficacia del sistema de gestión de la calidad.", align="J")
    pdf.ln(8)

    pdf.multi_cell(
        0, 8, txt="- Capacitar, motivar y comprometer a nuestro capital humano para mantener su competencia.", align="J")
    pdf.ln(8)

    pdf.multi_cell(0, 8, txt="- Honrar nuestros compromisos.", align="J")
    pdf.ln(8)

    pdf.multi_cell(
        0, 8, txt="- Cumplir con los requerimientos legales y reglamentarios.", align="J")
    pdf.ln(8)

    pdf.multi_cell(
        0, 8, txt="- Adquirir y mantener una plataforma tecnológica robusta.", align="J")
    pdf.ln(8)

    pdf.multi_cell(
        0, 8, txt="- Mantener procesos administrativos confiables y oportunos.", align="J")
    pdf.ln(8)

    pdf.multi_cell(
        0, 8, txt="- Mantener y mejorar la presencia de nuestra marca en el mercado nacional e internacional.", align="J")
    pdf.ln(8)

    pdf.multi_cell(0, 8, txt="- Mantener operaciones rentables.", align="J")
    pdf.ln(8)

    pdf.add_page()
    pdf.set_font('Arial', 'B', 12)
    pdf.multi_cell(0, 8, txt="Valores", align="J")
    pdf.ln(8)

    pdf.multi_cell(0, 8, txt="Trabajo en Equipo", align="J")
    pdf.ln(8)

    pdf.set_font('Arial', '', 12)
    pdf.multi_cell(0, 8, txt="- La calidad de nuestro trabajo es vital para la organización. Nos enfocamos en ser los mejores en nuestros puestos de trabajo.", align="J")
    pdf.ln(8)

    pdf.multi_cell(
        0, 8, txt="- Nos comunicamos de manera sincera, directa y cordial, para resolver los problemas lo más rápido posible.", align="J")
    pdf.ln(8)

    pdf.multi_cell(0, 8, txt="- Solicitamos y proporcionamos información precisa, veraz y oportuna. Es mejor decir 'no sé', que inventar una respuesta.", align="J")
    pdf.ln(8)

    pdf.multi_cell(0, 8, txt="- Utilizamos las palabras adecuadas y eliminamos el uso de aquellas coloquiales y genéricas (cosa, bicho, perol, cuestiones, broma, etc.)", align="J")
    pdf.ln(8)

    pdf.set_font('Arial', 'B', 12)
    pdf.multi_cell(0, 8, txt="Compromiso", align="J")
    pdf.ln(8)

    pdf.set_font('Arial', '', 12)
    pdf.multi_cell(0, 8, txt="- Reconocemos la importancia de la puntualidad en nuestro trabajo. Entregamos a tiempo los requerimientos de nuestros clientes internos y externos.", align="J")
    pdf.ln(8)

    pdf.multi_cell(
        0, 8, txt="- Cumplimos con las políticas y procedimientos establecidos para el desempeño de nuestros cargos.", align="J")
    pdf.ln(8)

    pdf.multi_cell(0, 8, txt="- Entendemos que la presencia en nuestros puestos de trabajo es indispensable para lograr los objetivos de la organización.", align="J")
    pdf.ln(8)

    pdf.multi_cell(
        0, 8, txt="- Innovamos continuamente para ser los mejores en nuestro negocio.", align="J")
    pdf.ln(8)

    pdf.multi_cell(0, 8, txt="- Nos ocupamos de que las fallas de nuestra organización sean corregidas lo antes posible y tomamos acciones para que no se repitan.", align="J")
    pdf.ln(8)

    pdf.multi_cell(
        0, 8, txt="- No contratamos a terceros para que hagan lo que nosotros debemos.", align="J")
    pdf.ln(8)

    pdf.multi_cell(
        0, 8, txt="- Siempre conseguimos un medio para lograr los objetivos. Las excusas no sirven de nada.", align="J")
    pdf.ln(8)

    pdf.multi_cell(
        0, 8, txt="- Tenemos sentido de urgencia en todo lo que hacemos.", align="J")
    pdf.ln(8)

    pdf.multi_cell(
        0, 8, txt="- Desarrollamos habilidades y capacidades para ser exitosos en un mercado desigual.", align="J")
    pdf.ln(8)

    pdf.multi_cell(
        0, 8, txt="- Innovamos en nuestros productos, servicios y procesos para obtener el mejor resultado.", align="J")
    pdf.ln(8)

    pdf.multi_cell(
        0, 8, txt="- Implementamos buenas ideas sin importar de donde vengan y nos enfocamos en mejorarlas.", align="J")
    pdf.ln(8)

    pdf.set_font('Arial', 'B', 12)
    pdf.multi_cell(0, 8, txt="Honestidad", align="J")
    pdf.ln(8)

    pdf.set_font('Arial', '', 12)
    pdf.multi_cell(0, 8, txt="- Decimos la verdad.", align="J")
    pdf.ln(8)

    pdf.multi_cell(0, 8, txt="- Utilizamos el tiempo laboral para realizar las tareas propias del cargo, haciendo buen uso de los recursos y evitando el desperdicio.", align="J")
    pdf.ln(8)

    pdf.multi_cell(
        0, 8, txt="- Honramos los compromisos de la organización.", align="J")
    pdf.ln(8)

    pdf.add_page()
    pdf.set_font('Arial', 'B', 12)
    pdf.multi_cell(0, 8, txt="Respeto", align="J")
    pdf.ln(8)

    pdf.set_font('Arial', '', 12)
    pdf.multi_cell(
        0, 8, txt="1.	Ofrecemos a nuestros clientes un servicio excelente y justo.", align="J")
    pdf.ln(8)

    pdf.multi_cell(0, 8, txt="2.	Valoramos el tiempo de los demás.", align="J")
    pdf.ln(8)

    pdf.multi_cell(
        0, 8, txt="3.	No interrumpimos a nuestros compañeros con asuntos que no conciernen a la actividad laboral.", align="J")
    pdf.ln(8)

    pdf.multi_cell(
        0, 8, txt="4.	Rechazamos la hipocresía y el chisme. Promovemos relaciones de confianza.", align="J")
    pdf.ln(8)

    pdf.multi_cell(0, 8, txt="5.	Evitamos la crítica negativa.", align="J")
    pdf.ln(8)

    pdf.multi_cell(0, 8, txt="6.	Siempre damos las 'gracias'.", align="J")
    pdf.ln(8)

    pdf.set_font('Arial', 'B', 12)
    pdf.multi_cell(0, 8, txt="Coherencia", align="J")
    pdf.ln(8)

    pdf.set_font('Arial', '', 12)
    pdf.multi_cell(
        0, 8, txt="- Somos consistentes entre lo que decimos, lo que hacemos y lo que escribimos.", align="J")
    pdf.ln(8)

    pdf.multi_cell(
        0, 8, txt="- Tomamos decisiones efectivas basadas en el análisis de la información.", align="J")
    pdf.ln(8)

    # Antecedente de la Investigacion
    pdf.add_page()
    pdf.set_font('Arial', 'B', 12)
    pdf.multi_cell(0, 8, txt="Antecendetes de la Investigación", align="C")
    pdf.ln(8)

    pdf.set_font('Arial', '', 12)
    pdf.multi_cell(0, 8, txt="     Para respaldar el análisis y los datos proporcionados en la base de datos, se debe mencionar que existen múltiples investigaciones que abordan lo referente al alquiler de autos y de la industria automotriz, a continuación, se presenta una serie de estas usadas como referencias:", align="J")
    pdf.ln(8)

    pdf.multi_cell(0, 8, txt="     La empresa Hertz Digital (2022), realizó un trabajo cuyo objetivo principal era el desarrollo de su aplicación para mejorar la experiencia del usuario mediante una integración efectiva con tecnologías digitales, incluyendo inteligencia artificial (IA). Con esto buscó ofrecer una reserva y alquiler más personalizados y eficientes. Esta propuesta consistió en; 1. trabajar con empresas como Google para mejorar el marketing basado en datos. 2. Crear aplicaciones móviles que permitan a los usuarios alquilar vehículos fácilmente. Y 3. La integración de IA, Utilizando datos para personalizar mensajes y servicios según las preferencias del cliente.", align="J")
    pdf.ln(8)

    pdf.multi_cell(0, 8, txt="     Dicha estrategia trajo como consecuencia para la empresa, mayor eficiencia en las reservas gracias a la aplicación móvil, mejora en la relación del cliente mediante servicios personalizados y el incremento en los ingresos por unidad debido a un mejor uso de los canales digitales.", align="J")
    pdf.ln(8)

    pdf.multi_cell(0, 8, txt="     Así ismo Uber Rent (2021), implementó la estrategia que permitía el alquiler de vehículos mediante alianzas con empresas locales. A través de esta, la empresa buscaba expandir sus servicios con alianzas locales como AVIS y HERZ, ofrecía no solo el alquiler del auto, incorporaba el concepto de integrar al conductor. La aplicación permitía al usuario reservar directamente, y los precios los asignaban las empresas asociadas y a Uber se le reconocía una comisión por servicio brindado. La aplicación de esta estrategia, evidenció mayor accesibilidad por parte del usuario, procesos más expeditos, la oferta de promociones de descuentos. ", align="J")
    pdf.ln(8)

    pdf.multi_cell(0, 8, txt="     Por su parte, el informe Global del Mercado de Alquiler de Vehículos (2023), (Research and Markets), analiza las dinámicas de crecimiento del mercado, las tendencias de innovación, y las estrategias de las empresas líderes como Enterprise, Hertz y Avis. Además, detalla una visión integral de la industria del transporte y el comportamiento de la empresa ACO Rent Car. (https://www.researchandmarkets.com)", align="J")
    pdf.ln(8)

    pdf.multi_cell(0, 8, txt="     En este mismo orden de ideas, el estudio del Mercado Global de Alquiler de Automóviles, (Grand View Research), ofrece datos sobre la valoración actual y futura del mercado, con énfasis en la segmentación por tipo de vehículo, ubicación geográfica y tendencias emergentes, como los vehículos eléctricos. (https://www.grandviewresearch.com)", align="J")
    pdf.ln(8)

    pdf.multi_cell(0, 8, txt="     Por su parte, el trabajo sobre las tendencias del Mercado Automotriz Global 2023-2028, (Statista), proporciona estadísticas detalladas sobre el crecimiento y las tendencias en el alquiler de automóviles, abordando la competencia y el impacto de las tecnologías emergentes. (https://www.statista.com)", align="J")
    pdf.ln(8)

    pdf.multi_cell(0, 8, txt="     Sobre el tema del diseño de aplicaciones en lenguaje Python, existe una profusa información sobre este tema en manuales y tutoriales, al respecto Summerfield (2019), ofrece una guía completa práctica, denominada 'Introducción al lenguaje Python', un estudio amigable y fácil de entender, que incluye procesos y conceptos básicos.", align="J")
    pdf.ln(8)

    pdf.add_page()
    pdf.set_font('Arial', 'B', 12)
    pdf.multi_cell(0, 8, txt="CAPITULO III", align="C")
    pdf.ln(8)

    pdf.multi_cell(0, 8, txt="Marco Metodológico", align="C")
    pdf.ln(8)

    pdf.set_font('Arial', '', 12)
    pdf.multi_cell(
        0, 8, txt="     El trabajo es de tipo estadístico descriptivo, según Lincoln Chao (1975) lo define como: ", align="J")
    pdf.ln(8)

    pdf.multi_cell(0, 6, txt="     La parte de la estadística que se ocupa del resumen y descripción de los datos. Este resumen puede ser tabular, gráfico o numérico. El análisis se limita a los datos recolectados y no se realizan inferencias o generalizaciones sobre la población de la cual provienen estas observaciones. Es decir, la estadística descriptiva no es más que el trabajo preliminar para la inferencia", align="C")
    pdf.ln(8)

    pdf.multi_cell(0, 8, txt="     De igual forma, permite el uso de un conjunto de técnicas para la recopilación, presentación y caracterización de datos con el fin de describir sus principales características de manera cuantitativa. Utiliza medidas como la media, mediana, moda, desviación estándar, entre otras, para resumir y analizar datos, facilitando su interpretación y comprensión sin hacer inferencias sobre un grupo más amplio.", align="J")
    pdf.ln(8)

    pdf.multi_cell(0, 8, txt="     Dado que el investigador no está recolectando datos de primera mano, sino que está utilizando un registro de información ya recopilado por otras fuentes, en este sentido, el trabajo se clasifica como una investigación indirecta (secundaria). De acuerdo a su concepción, se hace necesario incorporar la descripción de los procesos, los resultados, las conclusiones y las recomendaciones. Al respecto la Universidad Experimental Libertador (2003), que el estudio es considerado de factible, al respecto expresa:", align="J")
    pdf.ln(8)

    pdf.multi_cell(0, 6, txt="El proyecto factible, consiste en la elaboración de una propuesta de un modelo operativo viable, o una solución posible a un problema de tipo práctico para satisfacer las necesidades de una institución o grupo social. La propuesta debe tener apoyo, bien sea una investigación de tipo documental y debe referirse a la formulación de políticas, programas, métodos y procesos.", align="C")
    pdf.ln(8)

    pdf.set_font('Arial', 'B', 12)
    pdf.multi_cell(0, 8, txt="Población", align="J")
    pdf.ln(8)

    pdf.set_font('Arial', '', 12)
    pdf.multi_cell(0, 8, txt="     El universo a estudiar o población lo conforman 1265 registros, ubicados en 23 regiones a nivel mundial, en los cuales la empresa ACO Rent Car tiene presencia. En virtud de esto, no se hace una selección muestral, sino que se analiza toda la base de datos.", align="J")
    pdf.ln(8)

    pdf.set_font('Arial', 'B', 12)
    pdf.multi_cell(
        0, 8, txt="Método e intrumentos de recolección de datos", align="J")
    pdf.ln(8)

    pdf.set_font('Arial', '', 12)
    pdf.multi_cell(0, 8, txt="     Para el procesamiento de los datos se recurre al método estadístico descriptivo, caracterizado por permitir la recopilación, organización, presentación y la síntesis de la información numérica, mediante técnicas estadísticas descriptivas, así como representaciones visuales como gráficos y diagramas para ilustrar la distribución y las relaciones entre los datos, con el fin de facilitar su comprensión y análisis. Se basa en la utilización de técnicas como la distribución de frecuencias, las medidas de tendencia central y las medidas de dispersión, resúmenes numéricos que ofrecen medidas como la media, mediana y moda para comprender el comportamiento central de los datos.", align="J")
    pdf.ln(8)


    pdf.multi_cell(0, 8, txt="     Para la revisión de los datos provenientes de material impreso y digital, se emplean técnicas de análisis de contenido y observación documental, resumen, subrayado, así mismo, se recurre a técnicas operacionales como son: citas, bibliográficas, fichaje y notas de referencia todo esto con la finalidad de organizar la información, extraer las ideas básicas y descubrir la estructura de los documentos.", align="J")
    pdf.ln(8)

    pdf.add_page()
    pdf.set_font('Arial', 'B', 12)
    pdf.multi_cell(
        0, 8, txt="Técnicas de procesamiento y análisis de datos", align="J")
    pdf.ln(8)

    pdf.set_font('Arial', '', 12)
    pdf.multi_cell(0, 8, txt="     Luego de obtener los datos con los instrumentos citados, se procede al análisis crítico de la información documental obtenida, mediante el uso de técnicas de carácter cuantitativo, tal como lo refiere Balestrini (2002), este proceso tiene como fin último 'reducir los datos de una manera comprensible, para poder poner a prueba algunas relaciones de los problemas estudiados'. En síntesis, se trata de resumir y agrupar los datos para establecer alguna relación entre ellos. Para ello se emplea el siguiente proceso:", align="J")
    pdf.ln(8)

    pdf.multi_cell(0, 8, txt="     La recopilación de los datos, incluye información previamente compilada en la base de datos de la empresa ACO Rent Car, que incluye variables de clientes, reserva y negocio, así como estudios realizados sobre el comportamiento del sector alquiler de vehículos en la industria automotriz. Posteriormente para la clasificación, resumen, procesamiento y cálculo de los datos, se recurre a las de técnicas de tendencia central como son: Calculo de la media, mediana y moda. De igual forma se recurrirá a medidas de dispersión como desviación estándar, varianza y rango de la información, para comprender la variabilidad y comportamiento de la información.", align="J")
    pdf.ln(8)

    pdf.multi_cell(0, 8, txt="     Para la representación gráfica se recurre al uso de Tablas y gráficas que resuman los datos anuales y gráficos (como histogramas, gráficos de barras y líneas), para visualizar las tendencias y patrones a lo largo de los años para identificar el comportamiento de aumento o disminución.", align="J")
    pdf.ln(8)

    pdf.multi_cell(0, 8, txt="     Este enfoque metodológico permite: identificar patrones o tendencias significativas en los datos registrados. Toda la información obtenida a través del análisis de contexto, la caracterización del fenómeno estudiado, el análisis de los resultados, sirven para identificar, predecir, e interpretar el comportamiento generado y relacionado con el problema planteado.", align="J")
    pdf.ln(8)

    pdf.multi_cell(0, 8, txt="     Una vez, realizado el análisis inicial e identificar las necesidades, oportunidades de negocio y requerimientos técnicos, se establecen una arquitectura estandarizada (framework), esta incluye las herramientas, bibliotecas y reglas predefinidas que facilitan el desarrollo del software. Su diseño incorpora entre otros elementos la protección contra vulnerabilidad, los módulos son reutilizables, facilita el uso de componentes ya creados, establece reglas, convenciones relacionadas con la legalidad y mantenibilidad del código, permite el uso de bibliotecas externas para mejorar su funcionabilidad, esto redunda en la reducción de tiempo y esfuerzos.", align="J")
    pdf.ln(8)

    pdf.multi_cell(0, 8, txt="     El proceso anteriormente descrito brinda información clave, permite optimizar la operación, mejorar la experiencia del cliente y aumentar la rentabilidad del negocio, es decir, facilita la interpretación del hecho a estudiar, alcanzar estos procesos implica la clasificación de las variables en diferentes categorías, para una mejor comprensión. Según Arias (2004): ", align="J")
    pdf.ln(8)

    pdf.multi_cell(0, 6, txt="Las variables se definen, como la cualidad susceptible de sufrir cambios y, un sistema de variables como una serie de características por estudiar, definidas de manera operacional, es decir en función de sus indicadores o unidades de medida. Su operacionalización implica la desagregación.", align="C")
    pdf.ln(8)

    # Cuadro de Operacionalizacion de Varibles
    pdf.add_page()
    pdf.set_font('Arial', 'B', 12)
    pdf.multi_cell(
        0, 8, txt="Cuadro de Operacionalización de Variables", align="C")
    pdf.ln(8)

    pdf.multi_cell(0, 8, txt="Objetivo General", align="J")
    pdf.ln(8)

    pdf.set_font('Arial', '', 12)
    pdf.multi_cell(0, 8, txt="     Diseñar y desarrollar una aplicación para la gestión integral de la empresa ACO Rent Car, que permita el control, seguimiento y optimización de las estrategias operativas y comerciales.  ", align="J")
    pdf.ln(8)

    pdf.image("./assets/images/cuadro1.png", x=24, y=85, w=180)

    pdf.add_page()

    pdf.image("./assets/images/cuadro2.png", x=24, y=26, w=180)


    # Graficos
    pdf.add_page()
    pdf.set_font('Arial', "B", 12)
    pdf.ln(8)

    pdf.cell(0, 8, txt="Graficos y Análisis", align="C")
    pdf.ln(12)

    # Grafico de Vehiculos rentados segun su clasificacion

    image_folder = os.path.abspath("assets/images")


    def generar_grafico_clasificacion():
        if "Class" not in df.columns:
            print("Error: La columna 'Class' no está en los datos.")
            return None

        class_counts = df["Class"].value_counts()

        colores = rojo()
        colores = colores[:len(class_counts)]
        rcParams["font.family"] = "Arial"

        plt.figure(figsize=(10, 6))
        barras = class_counts.plot(kind="bar", color=colores, edgecolor="black")
        plt.xlabel("Clasificación de Vehículo")
        plt.ylabel("Vehículos Rentados")
        plt.title("Gráfico de Barras de Vehiculos Rentados según su Clasificación",
                fontsize=14, fontweight="bold", fontname="Arial")
        plt.xticks(rotation=45)
        plt.grid(axis="y", linestyle="--", alpha=0.7)

        for barra in barras.patches:
            height = barra.get_height()
            plt.text(barra.get_x() + barra.get_width() / 2, height + 0.5,
                    f"{int(height)}",
                    ha='center', va='bottom', fontsize=10, fontweight='bold')

        graph_path = os.path.join(
            image_folder, "vehiculos_rentados_clasificacion.png")
        plt.savefig(graph_path, bbox_inches="tight")
        plt.close()

        if os.path.exists(graph_path):
            print(f"✅ Gráfico guardado en: {graph_path}")
        else:
            print("❌ Error al guardar el gráfico")
            return None
    

        # Agregar imagen del gráfico al PDF
        pdf.image(graph_path, x=10, w=180)

        return graph_path

    # Grafico de Promedio de Rentas


    def generar_grafico_promedio_rentas():
        if not all(col in df.columns for col in ['Class', 'TotalBill', 'RDays']):
            print("❌ Error: Faltan columnas en los datos.")
            return None

        df['AvgRentalCost'] = df['TotalBill'] / df['RDays']
        gasto_promedio = df.groupby('Class')['AvgRentalCost'].mean()
        colores = rojo()
        plt.figure(figsize=(12, 6))
        barras = plt.bar(gasto_promedio.index, gasto_promedio.values,

                        color=colores[:len(gasto_promedio)])
        plt.xlabel("Clasificación", fontsize=12, fontname="Arial")
        plt.ylabel("Gasto Promedio ($USD)", fontsize=12, fontname="Arial")
        plt.title("Gráfico de Barra de Gasto Promedio Diario ($USD) según la Clasificación de los Vehículos",
                fontsize=14, fontweight="bold", fontname="Arial")
        plt.xticks(rotation=45, fontsize=12, fontname="Arial")
        plt.yticks(fontsize=12, fontname="Arial")

        for barra in barras:
            height = barra.get_height()
            plt.text(barra.get_x() + barra.get_width() / 2, height + 2,
                    f"${height:.2f}",
                    ha='center', va='bottom', fontsize=10, fontweight='bold')

        plt.grid(axis="y", linestyle="--", alpha=0.7)

        graph_path = os.path.abspath("assets/images/gasto_promedio_rentas.png")
        plt.savefig(graph_path, bbox_inches="tight")
        plt.close()

        if os.path.exists(graph_path):
            print(f"✅ Gráfico guardado en: {graph_path}")
            return graph_path
        else:
            print("❌ Error al guardar el gráfico")
            return None

    # Grafico de rentas generadas por empresa


    def generar_grafico_rentas_por_empresa():
        if 'Source' not in df.columns:
            print("❌ Error: La columna 'Source' no está en los datos.")
            return None
        rentas_por_empresa = df['Source'].value_counts()

        colores = rojo()

        plt.figure(figsize=(12, 6))
        plt.bar(rentas_por_empresa.index, rentas_por_empresa.values,
                color=colores[:len(rentas_por_empresa)])

        plt.xlabel("Empresa", fontsize=12, fontname="Arial")
        plt.ylabel("Cantidad de Vehiculos Rentados", fontsize=12, fontname="Arial")
        plt.title("Rentas Generadas según la Empresa", fontsize=14,
                fontweight="bold", fontname="Arial")
        plt.xticks(rotation=45, fontsize=10, fontname="Arial")
        plt.yticks(fontsize=10, fontname="Arial")

        for i, v in enumerate(rentas_por_empresa.values):
            plt.text(i, v + 5, str(v), ha='center', fontsize=10, fontweight='bold')

        plt.grid(axis="y", linestyle="--", alpha=0.7)

        graph_path = os.path.abspath("assets/images/rentas_por_empresa.png")
        plt.savefig(graph_path, bbox_inches="tight")
        plt.close()

        if os.path.exists(graph_path):
            print(f"✅ Gráfico guardado en: {graph_path}")
            return graph_path
        else:
            print("❌ Error al guardar el gráfico")
            return None

    # Cantidad Generado por la tarifa total


    def generar_grafico_tarifa_total_por_empresa():
        if not all(col in df.columns for col in ['Source', 'TotalBill']):
            print("✕ Error: Faltan columnas en los datos.")
            return None

        tarifa_total_por_empresa = df.groupby('Source')['TotalBill'].sum()

        colores = rojo()

        plt.figure(figsize=(12, 6))
        plt.bar(tarifa_total_por_empresa.index, tarifa_total_por_empresa.values,
                color=colores[:len(tarifa_total_por_empresa)])

        plt.xlabel("Empresa", fontsize=12, fontname="Arial")
        plt.ylabel("Monto ($USD)", fontsize=12, fontname="Arial")
        plt.title("Dinero Recaudado por Tarifa Total según la Empresa",
                fontsize=14, fontweight="bold", fontname="Arial")

        plt.xticks(rotation=45, fontsize=10, fontname="Arial")
        plt.yticks(fontsize=10, fontname="Arial")

        for i, v in enumerate(tarifa_total_por_empresa.values):
            plt.text(i, v + 1000, f"${v:,.2f}",
                    ha='center', fontsize=10, fontweight='bold')

        plt.grid(axis="y", linestyle="--", alpha=0.7)

        graph_path = os.path.abspath("assets/images/tarifa_total_por_empresa.png")
        plt.savefig(graph_path, bbox_inches="tight")
        plt.close()

        if os.path.exists(graph_path):
            print(f"✔ Gráfico guardado en: {graph_path}")
            return graph_path
        else:
            print("✕ Error al guardar el gráfico")
            return None


    # Tasa Porcentual de los Pre-Depositos
    def generar_grafico_pre_depositos():

        if 'res_prepagos' not in df.columns:
            print("❌ Error: La columna 'res_prepagos' no está en los datos.")
            return None

        hizo_predeposito = df[df['res_prepagos'] > 0].shape[0]
        no_hizo_predeposito = df[df['res_prepagos'] == 0].shape[0]

        sizes = [hizo_predeposito, no_hizo_predeposito]
        labels = ['Hizo Pre-Depósito', 'No hizo Pre-Depósito']
        colors = ['#2E9449', '#C0392B']

        fig, ax = plt.subplots(figsize=(6, 4))
        wedges, texts, autotexts = ax.pie(
            sizes,
            labels=None,
            autopct='%1.1f%%',
            startangle=90,
            colors=colors,
            textprops={'fontsize': 12, 'fontname': "Arial"},

        )

        for autotext in autotexts:
            autotext.set_fontsize(12)
            autotext.set_fontweight('bold')
            autotext.set_color('white')

        plt.title("Tasa Porcentual de los Pre-Depósitos",
                fontsize=14, fontweight="bold", fontname="Arial")

        plt.legend(wedges, labels, title="Leyenda", loc="center left",
                bbox_to_anchor=(1, 0, 0.5, 1), prop={'size': 10})

        graph_path = os.path.abspath("assets/images/pre_depositos_pie_chart.png")
        plt.savefig(graph_path, bbox_inches='tight')
        plt.close()

        if os.path.exists(graph_path):
            print(f"✅ Gráfico guardado en: {graph_path}")
            return graph_path
        else:
            print("❌ Error al guardar el gráfico")
            return None

    # Calendario de Rentas


    image_folder = os.path.abspath("assets/images")
    os.makedirs(image_folder, exist_ok=True)


    def generar_calendario_transacciones_rentas(year=2024):
        df = cargar_datos_sin_filtros()
        df['Pickupd'] = pd.to_datetime(df['Pickupd'], errors='coerce')
        df = df[df['Pickupd'].dt.year == year]

        reservas_diarias = df.groupby(df['Pickupd'].dt.date).size()

        if reservas_diarias.empty:
            print(f"❌ No hay datos disponibles para el año {year}.")
            return None

        reservas_diarias = pd.Series(
            reservas_diarias.values, index=pd.to_datetime(reservas_diarias.index))

        colores = ListedColormap([
            '#fff5f0', '#fee0d2', '#fcbba1', '#fc9272', '#fb6a4a',
            '#ef3b2c', '#cb181d', '#a50f15', '#67000d'
        ])

        fig, ax = plt.subplots(figsize=(15, 4))
        calmap.yearplot(reservas_diarias, year=year,
                        cmap=colores, linewidth=0.2, ax=ax)

        ax.set_title(f"Calendario de Renta de los Vehículos {year}", fontsize=14,
                    fontweight="bold", fontname="Arial", pad=15)

        mappable = plt.cm.ScalarMappable(cmap=colores, norm=Normalize(
            vmin=reservas_diarias.min(), vmax=reservas_diarias.max()))
        cbar = fig.colorbar(
            mappable, ax=ax, orientation='vertical', fraction=0.03, pad=0.05)
        cbar.set_label("Número de Reservas", fontsize=10, labelpad=10)
        cbar.ax.tick_params(labelsize=8)
        cbar.ax.yaxis.set_major_locator(MaxNLocator(integer=True))

        image_folder = os.path.abspath("assets/images")
        os.makedirs(image_folder, exist_ok=True)
        graph_path = os.path.join(image_folder, f"calendario_reservas_{year}.png")

        try:
            plt.savefig(graph_path, bbox_inches="tight", dpi=300)
            plt.close()
            print(f"✅ Gráfico guardado en: {graph_path}")
            return graph_path
        except Exception as e:
            print(f"❌ Error al guardar el gráfico: {str(e)}")
            return None

    # Grafico de ingresos por ubicacion segun codigo IATA


    image_folder = os.path.abspath("assets/images")
    os.makedirs(image_folder, exist_ok=True)

    colores = rojo()


    def generar_grafico_ingresos_por_ubicacion():
        df = cargar_datos_sin_filtros()

        if "LocOut" not in df.columns or "TotalBill" not in df.columns:
            print("❌ Error: La base de datos no contiene las columnas requeridas.")
            return None

        df['TotalBill'] = pd.to_numeric(df['TotalBill'], errors='coerce')
        df = df.dropna(subset=['TotalBill'])

        ingresos_por_ubicacion = df.groupby('LocOut')['TotalBill'].sum().sort_values(ascending=False)

        if ingresos_por_ubicacion.empty:
            print("❌ No hay datos disponibles para generar el gráfico.")
            return None

        plt.figure(figsize=(12, 6))
        ax = sns.barplot(
            x=ingresos_por_ubicacion.index,
            y=ingresos_por_ubicacion.values,
            palette=colores
        )

        plt.xlabel("Ubicación (IATA)", fontsize=12, fontweight="bold")
        plt.ylabel("Ingresos Totales ($USD)", fontsize=12, fontweight="bold")
        plt.title("Ingresos Totales por Ubicación (IATA)", fontsize=14, fontweight="bold", pad=15)

        plt.xticks(rotation=45, ha="right", fontsize=10)
        plt.yticks(fontsize=10)
        plt.grid(axis="y", linestyle="--", alpha=0.7)

        # Agregar etiquetas encima de las barras
        for bar in ax.patches:
            height = bar.get_height()
            ax.text(
                bar.get_x() + bar.get_width() / 2,  # Posición en X (centrado)
                height + (height * 0.02),  # Posición en Y (ligeramente por encima de la barra)
                f"${height:,.2f}",  # Formato de dinero
                ha="center", va="bottom", fontsize=9, fontweight="bold", color="black"
            )

        graph_path = os.path.join(image_folder, "ingresos_por_ubicacion.png")

        try:
            plt.savefig(graph_path, bbox_inches="tight", dpi=300)
            plt.close()
            print(f"✅ Gráfico guardado en: {graph_path}")
            return graph_path
        except Exception as e:
            print(f"❌ Error al guardar el gráfico: {str(e)}")
            return None


    # Añadiendo los graficos


    graph_path_1 = generar_grafico_clasificacion()
    if graph_path_1 and os.path.exists(graph_path_1):
        pdf.image(graph_path_1.replace("\\", "/"), x=10, y=50, w=180)
    else:
        print(" No se pudo agregar el gráfico de clasificación al PDF.")

    pdf.add_page()

    graph_path_2 = generar_grafico_promedio_rentas()
    if graph_path_2 and os.path.exists(graph_path_2):
        pdf.image(graph_path_2.replace("\\", "/"), x=10, y=30, w=180)

    else:
        print("❌ No se pudo agregar el gráfico de gasto promedio al PDF.")

    pdf.add_page()

    graph_path_3 = generar_grafico_rentas_por_empresa()
    if graph_path_3 and os.path.exists(graph_path_3):
        pdf.image(graph_path_3.replace("\\", "/"), x=10, y=30, w=180)
    else:
        print("❌ No se pudo agregar el gráfico de rentas por empresa al PDF.")

    pdf.add_page()

    graph_path_4 = generar_grafico_tarifa_total_por_empresa()
    if graph_path_4 and os.path.exists(graph_path_4):
        pdf.image(graph_path_4.replace("\\", "/"), x=10, y=30, w=180)
    else:
        print("✕ No se pudo agregar el gráfico de tarifa total al PDF.")

    pdf.add_page()

    graph_path_5 = generar_grafico_pre_depositos()
    if graph_path_5 and os.path.exists(graph_path_5):
        pdf.image(graph_path_5.replace("\\", "/"), x=10, y=30, w=180)
    else:
        print("❌ No se pudo agregar el gráfico de gasto promedio al PDF.")

    pdf.add_page()

    graph_path_6 = generar_calendario_transacciones_rentas()
    if graph_path_6 and os.path.exists(graph_path_6):
        pdf.image(graph_path_6.replace("\\", "/"), x=10, y=30, w=180)
    else:
        print("❌ No se pudo agregar el gráfico de gasto promedio al PDF.")

    pdf.add_page()

    graph_path_8 = generar_grafico_ingresos_por_ubicacion()
    if graph_path_8 and os.path.exists(graph_path_8):
        pdf.image(graph_path_8.replace("\\", "/"), x=10, y=30, w=180)
    else:
        print("❌ No se pudo agregar el gráfico de rentas por empresa al PDF.")

    # Agregar una página de conclusión antes de las referencias bibliográficas
    pdf.add_page()
    pdf.set_font('Arial', 'B', 12)
    pdf.multi_cell(0, 8, txt="Conclusión", align="C")
    pdf.ln(8)

    pdf.set_font('Arial', '', 12)
    pdf.multi_cell(0, 8, txt="     El presente estudio ha demostrado la importancia de la digitalización en la industria del alquiler de vehículos. "
                            "Mediante el desarrollo de una aplicación en lenguaje Python, se ha logrado optimizar la gestión de datos, "
                            "facilitando la toma de decisiones basada en información estadística precisa. "
                            "El análisis realizado refleja cómo las tendencias del mercado y el comportamiento del consumidor pueden ser "
                            "mejor comprendidos y aprovechados para mejorar la eficiencia operativa y comercial de la empresa ACO Rent Car. ", align="J")

    pdf.ln(8)

    pdf.multi_cell(0, 8, txt="     Además, la implementación de herramientas estadísticas y la visualización de datos ha permitido identificar "
                            "patrones clave en la demanda de vehículos, la duración de los alquileres y la rentabilidad de diferentes categorías. "
                            "Estos hallazgos no solo aportan valor a la empresa, sino que también pueden servir como referencia para futuras "
                            "investigaciones en el área del análisis de datos aplicados a la industria del transporte y la movilidad. ", align="J")

    pdf.ln(8)

    pdf.multi_cell(0, 8, txt="     En conclusión, la integración de tecnología y análisis de datos en la gestión de alquiler de vehículos es "
                            "un factor clave para el crecimiento y la competitividad del sector. La digitalización y el uso de modelos "
                            "estadísticos avanzados permiten a las empresas adaptarse a los cambios del mercado y mejorar la experiencia "
                            "del cliente, asegurando así su sostenibilidad a largo plazo. ", align="J")

    pdf.ln(8)


    # Referencias Bibliograficas
    pdf.add_page()
    pdf.set_font('Arial', 'B', 12)

    pdf.multi_cell(0, 8, txt='Referencias Bibliográficas', align='C')
    pdf.ln(8)

    pdf.set_font('Arial', '', 12)
    pdf.multi_cell(
        0, 8, txt="Arias Fidias (2001). Investigación previa en el campo de interés. Editorial Limusa ", align="J")
    pdf.ln(8)

    pdf.multi_cell(0, 8, txt="Calderón, J. (2018). Evolución y tendencias del mercado de alquiler de vehículos. Editorial Transporte Global.  ", align="J")
    pdf.ln(8)

    pdf.multi_cell(0, 8, txt="Balestrini, Acuna María (2006). Cómo se elabora el proyecto de investigación. Consultores Asociados Servicios Editoriales. Caracas, Venezuela.", align="J")
    pdf.ln(8)


    pdf.multi_cell(0, 8, txt="Chao, L. L. (1975). Estadística para las ciencias administrativas (2ª ed., trad. J. M. Castaño). México: McGraw-Hill.", align="J")
    pdf.ln(8)

    pdf.multi_cell(0, 8, txt="Chilton, K. (2020). Disrupción digital en la industria de alquiler de automóviles. Revista de Investigación en Transporte, 45(2), 102-118. https://doi.org/xxxx  ", align="J")
    pdf.ln(8)

    pdf.multi_cell(0, 8, txt="García, M., & López, R. (2021). Aplicaciones móviles para la gestión de flotas en empresas de transporte. Revista de Movilidad Inteligente, 14(2), 78-92. https://doi.org/xxxx  ", align="J")
    pdf.ln(8)

    pdf.multi_cell(
        0, 8, txt="García, J. L. (2017). Implementación de aplicación web para la gestión de rutas de transporte público [Tesis de grado, Universidad Politécnica Salesiana].", align="J")
    pdf.ln(8)

    pdf.multi_cell(
        0, 8, txt="González, M. (2015). Adopción de aplicaciones móviles para el Sistema de Transporte público en Querétaro [Tesis de maestría, Universidad Autónoma de Querétaro].", align="J")
    pdf.ln(8)

    pdf.multi_cell(0, 8, txt="Hertz. (2022). Hertz Digital: Experiencia de alquiler de autos mejorada con IA. Hertz Corporation. https://www.hertz.com  ", align="J")
    pdf.ln(8)

    pdf.multi_cell(0, 8, txt="Lyft. (2020). Lyft Rentals: Expansión de los servicios de movilidad. Lyft Inc. https://www.lyft.com/rentals", align="J")
    pdf.ln(8)

    pdf.multi_cell(0, 8, txt="Organización Mundial del Turismo. (2021). Informe sobre transporte y turismo sostenible. OMT.Porqué contar con ACO Rent Car. Consultado en: https://www.acorentacar.com/why-aco-rent-a-car/indexES.aspx", align="J")
    pdf.ln(8)

    pdf.multi_cell(
        0, 8, txt="Pressman, R. S. (2010). Ingeniería de software: Un enfoque práctico (7.ª ed.). McGraw-Hill.", align="J")
    pdf.ln(8)

    pdf.multi_cell(0, 8, txt="Smith, J., & García, M. (2019). Aplicaciones móviles para el transporte inteligente. Revista de Movilidad Urbana, 12(3), 45-67. https://doi.org/xxxx  ", align="J")
    pdf.ln(8)

    pdf.multi_cell(
        0, 8, txt="ReportLab. (2025). Guía de usuario para la generación de PDF. Recuperado de [https://www.reportlab.com/docs/reportlab-userguide.pdf](https://www.reportlab.com/docs/reportlab-userguide.pdf).", align="J")
    pdf.ln(8)

    pdf.multi_cell(
        0, 8, txt="Sabino. Carlos (2002). El proceso de investigación. Editorial Panapo. Caracas Venezuela", align="J")
    pdf.ln(8)

    pdf.multi_cell(
        0, 8, txt="Sampieri, Roberto. Metodología de la investigación. McGraw-Hill. Cuarta edición. 2006. p. 3-26.", align="J")
    pdf.ln(8)

    pdf.multi_cell(
        0, 8, txt="Sommerville, I. (2011). Ingeniería de software (9.ª ed.). Pearson Educación.", align="J")
    pdf.ln(8)

    pdf.multi_cell(0, 8, txt="Summerfield, M. (2019). Programming in Python: A Complete Introduction to the Python Language. Addison-Wesley Professional.", align="J")
    pdf.ln(8)

    pdf.multi_cell(0, 8, txt="Tamayo y Tamayo, Mario (1999). El proceso de investigación científica. 3 edición. Editorial Limusa. Bogotá. De CV. ISBNI: 978-050-138-8", align="J")
    pdf.ln(8)

    pdf.multi_cell(0, 8, txt="Torres, J. (2020). Optimización de la movilidad urbana mediante aplicaciones de alquiler de vehículos. Transporte y Digitalización, 8(1), 33-47. https://doi.org/xxxx  ", align="J")
    pdf.ln(8)

    pdf.multi_cell(0, 8, txt="Uber. (2021). Uber Rent: Una nueva forma de alquilar un automóvil. Uber Technologies Inc. https://www.uber.com/rent.", align="J")
    pdf.ln(8)

    pdf.multi_cell(0, 8, txt="Universidad Pedagógica Experimental Libertador (2003): Manual de Trabajos de Grado Especialización y Maestría y Tesis Doctorales. Fedeupel. Caracas, Venezuela.", align="J")
    pdf.ln(8)


    pdf.output(output_path)
    return output_path