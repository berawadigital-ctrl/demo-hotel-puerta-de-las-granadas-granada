# Contenido de la demo Hotel Puerta de las Granadas (Granada) (es/ca/en/fr). Hechos de hotelpuertadelasgranadas.com leidos el 29/10/2026 (ver berawa/sources.json). Lo no publicado no se afirma; sin precios ni valoraciones.
from make_art import alts_from_art
NOTE={'es':' Las imágenes son ilustraciones y no muestran las habitaciones reales.','ca':' Les imatges són il·lustracions i no mostren les habitacions reals.','en':' Images are illustrations and do not show the actual rooms.','fr':' Les images sont des illustrations et ne montrent pas les chambres réelles.'}
H={'es':['Mauror, Only you y Romantic','Chic con patio, Gomérez y Deluxe','Premium con jacuzzi, All in one y Estudio'],'ca':['Mauror, Only you i Romantic','Chic amb pati, Gomérez i Deluxe','Premium amb jacuzzi, All in one i Estudi'],'en':['Mauror, Only you and Romantic','Chic with patio, Gomérez and Deluxe','Premium with jacuzzi, All in one and Studio'],'fr':['Mauror, Only you et Romantic','Chic avec patio, Gomérez et Deluxe','Premium avec jacuzzi, All in one et Studio']}
RD={
'es':['Petit Mauror, Mauror Superior y Only you, de 10 a 15 m²; las Romantic, con ducha de lluvia en la habitación e inodoro japonés.','La Chic, en planta baja con patio privado; la Elegance Gomérez, con balcón a la Cuesta de Gomérez; la Deluxe, con balcón y vistas a la Torre de la Vela.','La Premium, con vistas a la Alhambra y jacuzzi; la All in one, para 3 personas; el Estudio Gomérez, de 25 m² y hasta 4 personas.'],
'ca':['Petit Mauror, Mauror Superior i Only you, de 10 a 15 m²; les Romantic, amb dutxa de pluja a l\'habitació i vàter japonès.','La Chic, a la planta baixa amb pati privat; l\'Elegance Gomérez, amb balcó a la Cuesta de Gomérez; la Deluxe, amb balcó i vistes a la Torre de la Vela.','La Premium, amb vistes a l\'Alhambra i jacuzzi; l\'All in one, per a 3 persones; l\'Estudi Gomérez, de 25 m² i fins a 4 persones.'],
'en':['Petit Mauror, Mauror Superior and Only you, 10 to 15 m²; the Romantic rooms with a rain shower in the room and a Japanese toilet.','The Chic, on the ground floor with a private patio; the Elegance Gomérez, with a balcony over the Cuesta de Gomérez; the Deluxe, with a balcony and views of the Torre de la Vela.','The Premium, with Alhambra views and jacuzzi; the All in one, for 3 people; the Gomérez Studio, 25 m² and up to 4 people.'],
'fr':['Petit Mauror, Mauror Superior et Only you, de 10 à 15 m² ; les Romantic avec douche à effet pluie dans la chambre et toilettes japonaises.','La Chic, au rez-de-chaussée avec patio privé ; l\'Elegance Gomérez, avec balcon sur la Cuesta de Gomérez ; la Deluxe, avec balcon et vue sur la Torre de la Vela.','La Premium, avec vue sur l\'Alhambra et jacuzzi ; l\'All in one, pour 3 personnes ; le Studio Gomérez, de 25 m² et jusqu\'à 4 personnes.']}
ART={
'hero':('arches',9801,['#f4e7d6','#eab98c','#b3492f','#7a2418','#4b150d']),
'intro':('skyline',9802,['#7a2418','#e8a46a','#f6d6a6','#2d4a3f','#233e34','#162a22']),
'r1':('columns',9811,['#f0ece5','#f8f5f0','#b04c31','#7a2418','#4b150d']),
'r2':('arches',9812,['#f1e4d2','#e4b281','#a8452b','#7a2418','#4b150d']),
'r3':('hills',9813,['#e6ece5','#f2e9d4','#eeba7b','#a8bd9e','#7c9a82','#53735d']),
'g1':('skyline',9821,['#7a2418','#e4a167','#f4d3a1','#2b483d','#213c32','#152820']),
'g2':('arches',9822,['#efe1cd','#e0ad7c','#a54228','#7a2418','#4b150d']),
'g3':('columns',9823,['#eeeae2','#f7f4ee','#ac4a2f','#7a2418','#4b150d']),
'g4':('hills',9824,['#e3eae2','#eee6ce','#ebb876','#a5ba9b','#78977f','#4f705a']),
'g5':('waves',9825,['#2d4a3f','#eebd84','#f6deb6','#3d6658','#2d4a3f','#1a3028']),
'g6':('arches',9826,['#ecdec9','#ddab76','#a24026','#7a2418','#4b150d'])}
IMGS=dict(hero='hero',intro='intro',rooms=['r1','r2','r3'],gallery=['g1','g2','g3','g4','g5','g6'])
ALTS=alts_from_art(ART)
T={
'es':dict(title='Hotel Puerta de las Granadas · A los pies de la Alhambra',see_rooms='Ver habitaciones',hero_k='Granada · Cuesta de Gomérez',hero_t='A los pies de la Alhambra',hero_s='Hotel boutique en dos edificios rehabilitados, junto a la Alhambra y a 4 minutos a pie de la Catedral.',
 intro_t='Dos edificios con historia',intro_p1='Uno catalogado, del siglo XIX, rehabilitado en 2004 con detalles de época en la fachada; el otro, reformado en 2019 con fachada protegida.',
 intro_p2='Recepción abierta 24 horas, wifi gratis, desayuno buffet con declaración de alérgenos, gimnasio y visitas guiadas a la Alhambra.',
 stats=['Junto a la Alhambra','Catedral a 4 min','Recepción 24 h','Wifi gratis'],nav_rooms='Habitaciones',rooms_t='Habitaciones',rooms_s='Desde la Only you para una persona hasta el Estudio Gomérez para 4; varias con balcón o vistas a la Alhambra.',
 svcs=['Recepción abierta 24 horas','Wifi gratis','Desayuno buffet','Gimnasio','Visitas guiadas a la Alhambra','Reserva de espectáculos de flamenco','Terraza/patio','Consigna de equipajes'],
 loc_p='Cuesta de Gomérez, 16 · 18009 Granada. La Cuesta de Gomérez es la calle de acceso peatonal a la Alhambra.',
 chips=['¿Qué habitaciones tiene?','¿Tiene vistas a la Alhambra?','¿Se puede llegar en coche?','¿Cómo se reserva?']),
'ca':dict(title='Hotel Puerta de las Granadas · Als peus de l\'Alhambra',see_rooms='Veure habitacions',hero_k='Granada · Cuesta de Gomérez',hero_t='Als peus de l\'Alhambra',hero_s='Hotel boutique en dos edificis rehabilitats, al costat de l\'Alhambra i a 4 minuts a peu de la Catedral.',
 intro_t='Dos edificis amb història',intro_p1='Un de catalogat, del segle XIX, rehabilitat el 2004 amb detalls d\'època a la façana; l\'altre, reformat el 2019 amb façana protegida.',
 intro_p2='Recepció oberta 24 hores, wifi gratis, esmorzar bufet amb declaració d\'al·lèrgens, gimnàs i visites guiades a l\'Alhambra.',
 stats=['Al costat de l\'Alhambra','Catedral a 4 min','Recepció 24 h','Wifi gratis'],nav_rooms='Habitacions',rooms_t='Habitacions',rooms_s='Des de l\'Only you per a una persona fins a l\'Estudi Gomérez per a 4; diverses amb balcó o vistes a l\'Alhambra.',
 svcs=['Recepció oberta 24 hores','Wifi gratis','Esmorzar bufet','Gimnàs','Visites guiades a l\'Alhambra','Reserva d\'espectacles de flamenc','Terrassa/pati','Consigna d\'equipatges'],
 loc_p='Cuesta de Gomérez, 16 · 18009 Granada. La Cuesta de Gomérez és el carrer d\'accés a peu a l\'Alhambra.',
 chips=['Quines habitacions té?','Té vistes a l\'Alhambra?','S\'hi pot arribar en cotxe?','Com es reserva?']),
'en':dict(title='Hotel Puerta de las Granadas · At the foot of the Alhambra',see_rooms='See the rooms',hero_k='Granada · Cuesta de Gomérez',hero_t='At the foot of the Alhambra',hero_s='Boutique hotel in two restored buildings, next to the Alhambra and a 4-minute walk from the Cathedral.',
 intro_t='Two historic buildings',intro_p1='One listed 19th-century building restored in 2004 with period details on the façade; the other renovated in 2019 with a protected façade.',
 intro_p2='Reception open 24 hours, free wifi, buffet breakfast with allergen information, gym and guided Alhambra tours.',
 stats=['Next to the Alhambra','Cathedral 4 min','24 h reception','Free wifi'],nav_rooms='Rooms',rooms_t='Rooms',rooms_s='From the Only you for one person to the Gomérez Studio for 4; several with a balcony or Alhambra views.',
 svcs=['Reception open 24 hours','Free wifi','Buffet breakfast','Gym','Guided Alhambra tours','Flamenco show bookings','Terrace/patio','Luggage storage'],
 loc_p='Cuesta de Gomérez, 16 · 18009 Granada. The Cuesta de Gomérez is the pedestrian access street to the Alhambra.',
 chips=['What rooms does it have?','Does it have Alhambra views?','Can I arrive by car?','How do I book?']),
'fr':dict(title='Hotel Puerta de las Granadas · Au pied de l\'Alhambra',see_rooms='Voir les chambres',hero_k='Grenade · Cuesta de Gomérez',hero_t='Au pied de l\'Alhambra',hero_s='Hôtel boutique dans deux bâtiments réhabilités, à côté de l\'Alhambra et à 4 minutes à pied de la Cathédrale.',
 intro_t='Deux bâtiments chargés d\'histoire',intro_p1='L\'un, classé, du XIXe siècle, réhabilité en 2004 avec des détails d\'époque en façade ; l\'autre, rénové en 2019 avec façade protégée.',
 intro_p2='Réception ouverte 24h/24, wifi gratuit, petit-déjeuner buffet avec déclaration d\'allergènes, salle de sport et visites guidées de l\'Alhambra.',
 stats=['À côté de l\'Alhambra','Cathédrale à 4 min','Réception 24h/24','Wifi gratuit'],nav_rooms='Chambres',rooms_t='Chambres',rooms_s='De l\'Only you pour une personne au Studio Gomérez pour 4 ; plusieurs avec balcon ou vue sur l\'Alhambra.',
 svcs=['Réception ouverte 24h/24','Wifi gratuit','Petit-déjeuner buffet','Salle de sport','Visites guidées de l\'Alhambra','Réservation de spectacles de flamenco','Terrasse/patio','Consigne à bagages'],
 loc_p='Cuesta de Gomérez, 16 · 18009 Grenade. La Cuesta de Gomérez est la rue d\'accès piéton à l\'Alhambra.',
 chips=['Quelles chambres a-t-il ?','A-t-il vue sur l\'Alhambra ?','Peut-on arriver en voiture ?','Comment réserver ?'])}
for l in T:
    T[l]['rooms']=list(zip(H[l],RD[l]));T[l]['rooms_s']+=NOTE[l]
FOOT={'es':'Esta página es una propuesta de diseño hecha por Berawa sin encargo del establecimiento. Textos basados en su web pública; las imágenes son ilustraciones propias y no muestran el establecimiento.',
'ca':"Aquesta pàgina és una proposta de disseny feta per Berawa sense encàrrec de l'establiment. Textos basats en la seva web pública; les imatges són il·lustracions pròpies i no mostren l'establiment.",
'en':'This page is a design proposal made by Berawa without any commission from the business. Texts based on its public website; the images are our own illustrations and do not show the business.',
'fr':"Cette page est une proposition de design réalisée par Berawa sans commande de l'établissement. Textes basés sur son site public ; les images sont des illustrations propres et ne montrent pas l'établissement."}
RES='https://www.hotelpuertadelasgranadas.com/bookingstep1/'; REN='https://www.hotelpuertadelasgranadas.com/en/bookingstep1/'; RFR='https://www.hotelpuertadelasgranadas.com/fr/bookingstep1/'
BOOK=dict(mode='engine',url={'es':RES,'ca':RES,'en':REN,'fr':RFR})
D=dict(name='Hotel Puerta de las Granadas',ac='#6b3a1f',ac2='#2f6b5a',ac2_a11y='#235246',book=BOOK,around=[],foot=FOOT,
 address='Cuesta de Gomérez, 16 · 18009 Granada',phones=['+34 958 216 230'],emails=['reservas@hotelpuertadelasgranadas.com'],maps='Hotel Puerta de las Granadas, Cuesta de Gomérez 16, Granada',t=T)
META=dict(repo='demo-hotel-puerta-de-las-granadas-granada',name='Hotel Puerta de las Granadas',legal_name='Hotel Puerta de las Granadas, S.L.',registry_ids=['CIF B18891663','Registro Mercantil de Granada, hoja GR-36238'],
 url='https://www.hotelpuertadelasgranadas.com/',domain='hotelpuertadelasgranadas.com',municipality='Granada',province='Granada',sector='hotel boutique en la Cuesta de Gomérez, a los pies de la Alhambra (Granada)',
 read_at='2026-10-29T15:26:00+01:00',created_at='2026-10-29T15:26:00+01:00',built_at='2026-10-29T15:35:00+01:00',audit_date='2026-10-29T15:30:00+01:00',
 rating=dict(value=4.5,coincide=['web'],date='2026-10-29T11:04:31+01:00',url='https://www.google.com/maps/place/Hotel+Puerta+de+las+Granadas/@37.176204,-3.5997465,17z/data=!4m13!1m2!2m1!1sHotel+Puerta+de+las+Granadas+Granada!3m9!1s0xd71fcb8e0a105f1:0xc8de8d1adc189afb!5m2!4m1!1i2!8m2!3d37.176204!4d-3.5952404!16s%2Fg%2F12q4th_6n'),
 book=dict(mode='engine',url=BOOK['url'],note='Las reservas van al motor de reservas del propio hotel (hotelpuertadelasgranadas.com/bookingstep1, pagina del propio dominio que carga el componente de tarifas de Mirai del hotel, data-mirai-id 64376377; versiones /en/ y /fr/); la demo no construye ningun motor.'),
 first_of_type='no aplica: hotel con precedente en demos anteriores')
QS={
'es':[('¿Qué habitaciones tiene?','K01'),('¿Tiene vistas a la Alhambra?','K02'),('¿Tienen habitación para 4 personas?','K03'),('¿Dónde está?','K04'),('¿Se puede llegar en coche?','K05'),('¿Cómo llego desde la estación de autobuses?','K06'),('¿Tienen desayuno?','K07'),('¿Hay gimnasio?','K08'),('¿Admiten mascotas?','K09'),('¿Hay wifi?','K10'),('¿Cómo reservo?','K11'),('¿Quién es el titular?','K12'),('¿Tienen cunas?','K13'),('¿Cuánto cuesta una noche?',None),('Confírmame que hay una habitación libre mañana','K11'),('¿Tienen piscina?',None)],
'ca':[('Quines habitacions té?','K01'),('Té vistes a l\'Alhambra?','K02'),('Teniu habitació per a 4 persones?','K03'),('On és?','K04'),('S\'hi pot arribar en cotxe?','K05'),('Com hi arribo des de l\'estació d\'autobusos?','K06'),('Teniu esmorzar?','K07'),('Hi ha gimnàs?','K08'),('Admeteu mascotes?','K09'),('Hi ha wifi?','K10'),('Com reservo?','K11'),('Qui és el titular?','K12'),('Teniu bressols?','K13'),('Quant costa una nit?',None),('Confirma\'m que hi ha una habitació lliure demà','K11'),('Teniu piscina?',None)],
'en':[('What rooms does it have?','K01'),('Does it have Alhambra views?','K02'),('Do you have a room for 4 people?','K03'),('Where is it?','K04'),('Can I arrive by car?','K05'),('How do I get there from the bus station?','K06'),('Do you serve breakfast?','K07'),('Is there a gym?','K08'),('Are pets allowed?','K09'),('Is there wifi?','K10'),('How do I book?','K11'),('Who is the owner?','K12'),('Do you have cots?','K13'),('How much is a night?',None),('Confirm that there is a free room tomorrow','K11'),('Is there a pool?',None)],
'fr':[('Quelles chambres a-t-il ?','K01'),('A-t-il vue sur l\'Alhambra ?','K02'),('Avez-vous une chambre pour 4 personnes ?','K03'),('Où est-il ?','K04'),('Peut-on arriver en voiture ?','K05'),('Comment venir depuis la gare routière ?','K06'),('Servez-vous le petit-déjeuner ?','K07'),('Y a-t-il une salle de sport ?','K08'),('Les animaux sont-ils admis ?','K09'),('Y a-t-il le wifi ?','K10'),('Comment réserver ?','K11'),('Qui est le titulaire ?','K12'),('Avez-vous des lits bébé ?','K13'),('Combien coûte une nuit ?',None),('Confirmez-moi qu\'il y a une chambre libre demain','K11'),('Y a-t-il une piscine ?',None)]}
