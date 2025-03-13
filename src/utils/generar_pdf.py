"""Este modulo genera un PDF con diferentes configuraciones"""

import matplotlib.pyplot as plt
from src.utils.helpers import cargar_datos_sin_filtros
from fpdf import FPDF
import sys
import os

sys.path.append(os.path.abspath(os.path.join(
    os.path.dirname(__file__), "..", "..")))

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

pdf.multi_cell(0, 8, txt="Maneiro Chirino Ronald Alejandro", align='R')
pdf.ln(30)

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

pdf.multi_cell(0, 8, txt="     Establecer la seguridad y protección de datos mediante protocolos de autenticación y almacenamiento seguro.", align="J")
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
pdf.multi_cell(0, 8, txt="ACO RENT A CAR, se ha caracterizado por ofrecer un servicio de alquiler de vehículos, que tiene presencia en el mercado por más de 40 años. La empresa se distingue por brindar flexibilidad y comodidad, ideales para vacaciones en familia o viajes de negocios. A lo largo de su trayectoria, ha mantenido un enfoque en la satisfacción del cliente, asegurando que sus vehículos se encuentren en excelentes condiciones y proporcionando asistencia en carretera de alta calidad (página WEB).", align="J")
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
pdf.multi_cell(0, 8, txt="     Para respaldar el análisis y los datos proporcionados en la base de datos, se debe mencionar que existen múltiples investigaciones que abordan lo referente al alquiler de autos y de la industria automotriz, a continuación, se presenta una serie estas usadas como referencias:", align="J")
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

pdf.multi_cell(0, 6, txt="     la parte de la estadística que se ocupa del resumen y descripción de los datos. Este resumen puede ser tabular, gráfico o numérico. El análisis se limita a los datos recolectados y no se realizan inferencias o generalizaciones sobre la población de la cual provienen estas observaciones. Es decir, la estadística descriptiva no es más que el trabajo preliminar para la inferencia", align="C")
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


pdf.add_page()


# Graficos


def generarpdf():
    df = cargar_datos_sin_filtros()

    # Verificar que la columna 'Class' exista
    if "Class" not in df.columns:
        print("Error: La columna 'Class' no está en los datos.")
        return

    # Generar el gráfico de vehículos rentados por clasificación
    class_counts = df["Class"].value_counts()

    plt.figure(figsize=(10, 6))
    class_counts.plot(kind="bar", color="skyblue", edgecolor="black")

    plt.xlabel("Clasificación de Vehículo")
    plt.ylabel("Cantidad de Vehículos Rentados")
    plt.title("Cantidad de Vehículos Rentados por Clasificación")
    plt.xticks(rotation=45)
    plt.grid(axis="y", linestyle="--", alpha=0.7)

    # Guardar el gráfico como imagen
    graph_path = "vehiculos_rentados_clasificacion.png"
    plt.savefig(graph_path, bbox_inches="tight")
    plt.close()

    pdf.image(graph_path, x=10, y=30, w=180)


# Llamar a la función para ejecutar el proceso
generarpdf()


# pdf.multi_cell(100, 20, txt="adfshg", border=1, align="J")

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

pdf.multi_cell(
    0, 8, txt="Django REST Framework. (2025). Construcción de API con Django. Recuperado de [https://www.django-rest-framework.org](https://www.django-rest-framework.org).  ", align="J")
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

pdf.multi_cell(
    0, 8, txt="PostgreSQL. (2025). Documentación y tutoriales. Recuperado de [https://www.postgresql.org/docs/](https://www.postgresql.org/docs/).", align="J")
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

# pdf.multi_cell(0,8, txt= "",align= "J" )


pdf.output('Trabajo final.pdf')
