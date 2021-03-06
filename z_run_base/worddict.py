# Dictionary for adding data to the database
main_table = [{'id': 1, 'section': 'index', 'link': '/', 'title_page': 'Главная', 'name_link': 'Главная',
               'data_page': '<p> Вставленный в <br>базу текст с html <b> Главная.</b> </p>'},
              {'id': 2, 'section': 'about', 'link': '/about', 'title_page': 'О нас', 'name_link': 'О нас',
               'data_page': '<p> Вставленный в базу текст с html <br><b> О нас.</b> </p>'},
              {'id': 3, 'section': 'articles.more_info', 'link': '/articles', 'title_page': 'Описание', 'name_link': 'Описание',
               'data_page': '<p> <b> Описание.</b> <br>Вставленный в базу текст с html </p>'},
              {'id': 4, 'section': 'products.product', 'link': '/products', 'title_page': 'Товары', 'name_link': 'Товары',
               'data_page': '<p> <b> Продукт.</b> <br>Вставленный в базу текст с html </p>'},
              {'id': 5, 'section': 'services.index', 'link': '/products', 'title_page': 'Установка', 'name_link': 'Поставить',
               'data_page': '<p> <b> Монтаж.</b> Вставленный в базу текст<br> с html </p>'}
              ]
#####################################################################################################################################
nickname = ["3D Waffle", "Hightower", "Papa Smurf", "57 Pixels", "Hog Butcher", "Pepper Legs", "101", "Houston",
            "Pinball Wizard", "Accidental Genius", "Hyper", "Pluto", "Alpha", "Jester", "Pogue", "Airport Hobo",
            "Jigsaw", "Prometheus", "Bearded Angler", "Joker's Grin", "Psycho Thinker", "Beetle King", "Judge", "Pusher",
            "Bitmap", "Junkyard Dog", "Riff Raff", "Blister", "K-9", "Roadblock", "Bowie", "Keystone",
            "Rooster", "Bowler", "Kickstart", "Sandbox", "Breadmaker", "Kill Switch", "Scrapper", "Broomspun",
            "Kingfisher", "Screwtape", "Buckshot", "Kitchen", "Sexual Chocolate", "Bugger", "Knuckles", "Shadow Chaser",
            "Cabbie", "Lady Killer", "Sherwood Gladiator", "Candy Butcher", "Liquid Science", "Shooter", "Capital F", "Little Cobra",
            "Sidewalk Enforcer", "Captain Peroxide", "Little General", "Skull Crusher", "Celtic Charger", "Lord Nikon", "Sky Bully", "Cereal Killer",
            "Lord Pistachio", "Slow Trot", "Chicago Blackout", "Mad Irishman", "Snake Eyes", "Chocolate Thunder", "Mad Jack", "Snow Hound",
            "Chuckles", "Mad Rascal", "Sofa King", "Commando", "Manimal", "Speedwell", "Cool Whip", "Marbles",
            "Spider Fuji", "Cosmo", "Married Man", "Springheel Jack", "Crash Override", "Marshmallow", "Squatch", "Crash Test",
            "Mental", "Stacker of Wheat", "Crazy Eights", "Mercury Reborn", "Sugar Man", "Criss Cross", "Midas", "Suicide Jockey",
            "Racy Lady", "Lightweight", "Duchess", "Abiss", "Sneaky Lady", "Moxie", "Heavenly Connection", "Contrary Mary",
            "Tomcat", "Raggedy Ann", "Little Drunk Girl", "Eerie", "Acid Queen", "Soiled Dove", "Necessary Momentum", "Hemlock",
            "Cool Whip", "Toy Town", "Roller Girl", "Loot", "Easy Street", "Alley Cat", "Solitaire", "New York Mood",
            "Highway", "Cream", "Trash", "Romance Princess", "Low Voltage", "Emerald Goddess", "All Natural", "Spellbinder",
            "Nibbler", "Hoboken Nightingale", "Crumb Cake", "Treasure Devil", "Rook", "Mafia Princess", "Essex", "Backstreet",
            "Spitfire", "Noisy Girl", "Homerun Diva", "Curio", "Trixie", "Rope", "Magenta", "Eye Candy Kitten",
            "Barbwire", "Spoiler", "Nola", "Impulse", "Dahlia", "Troubled Chick", "Runway Darling", "Manly",
            "Feline Devil", "Bleach", "Spooky Electric", "Nutmeg", "Indigo Red", "Dandelion", "Tweety", "Santa's Little Helper",
            "Marshmallow Treat", "Feral Filly", "Bleachers", "Spunky Chick", "Oblivion", "Innocent Ghost", "Darkside Hooker", "Twinkle",
            "Saturn Extreme", "Metal Lady", "Find It Girl", "Bleeker", "Star Jammer", "Opulent Gamer", "Instant Star", "Delicious",
            "Undergrad", "Sassy Muffin", "Microwave", "Firecracker", "Blink", "Star Killer", "Palomino", "Intimidating Presence",
            "Digital Goddess", "Video Game Heroine", "Scratch", "Mirage", "Firefly", "Bliss", "Steel Heart", "Peanut Butter Woman",
            "Iron Butterfly", "Delirium", "Vixen", "Scuffs", "Miss Fix It", "Flashpoint", "Boost", "Stickers",
            "Pepper", "Jade Fox", "Demo", "Voodoo Queen", "Serendipity", "Miss Lucky", "Freesia", "Burn",
            "Stick Shift", "Petite Beauty", "Jersey", "Demolition Queen", "Whipsaw", "Shady Lady", "Miss Murder", "Frenzy",
            "Call Back Queen", "Succubus In Training", "Pink Nightmare", "Kabuki", "Despair", "Whistler", "Shamrock", "Miss Mustard",
            "Frosty", "Campfire Mama", "Sugar Hiccup", "Pinup Diva", "Kamikaze Granny", "Devine Melon", "White Swan", "Shivers",
            "Moon Cricket", "Fuzzy Logic Hottie", "Canary Apple Red",  "Pitfall", "Kimono Goddess", "Dewdrop Doll", "Wiccan Trouble",
            "Show Off", "Moonflower", "Gentle Avenger", "Chameleon", "Sweetness", "Pixie", "Ladybird", "Dez",
            "Wildcat Talent", "Silver Cup", "Moon Orchid", "Chapstick",  "Pockets"]

#############################################################################################################################
articles = [{'title': "Установка шумоизоляции",
             ######################################
             'body': ''' Услуги по установке автомобильной шумоизоляции. Цена на установку шумоизоляции указана с учетом работы и стоимости материалов.
Опубликованы оптимальные наборки материалов, но возможен и индивидуальный подход к подбору шумоизоляции,
с учетом особенностей Вашего авто и желаемого уровня звукоизоляции, и в зависимости от мощности акустической системы Время установки шумоизоляции
в среднем занимает два дня.  ''',
             #######################################
             'specification': ''' Приобрести материалы Вы можете или у нас на сайте или непосредственно на СТО, где будет производиться монтаж шумоизоляции
Преимущества установки шумоизоляции у нас Качество работы – у наших установщиков огромный опыт работы в области монтажа виброизоляции и шумоизоляции.
Звукоизоляция — снижение уровня шума, проникающего в помещения извне. Количественная мера звукоизоляции ограждающих конструкций
выражается в децибелах. Степень необходимости звукоизоляции перекрытий зависит от характеристик используемых в строительстве материалов и соблюдения
всех технологических норм. К примеру, в случае сооружения перекрытий из качественных заводских бетонных плит при тщательном и аккуратном их монтаже
звукоизоляция может не потребоваться на протяжении нескольких лет.
Термин звукоизоляция всегда считался синонимом термина шумоизоляция. Но сейчас термин звукоизоляция чаще всего относят
к защите от шума в помещениях, в то время как шумоизоляция чаще используется при разговоре о защите от шума в автомобилях ''',
             ############################################################
             'image': "718744352_ustanovka_shumoizolyatsii.jpg"
             },
            ################################################################
            {'title': "Материалы для шумоизоляции авто",
             ##################################################
             'body': ''' Шумоизоляция автомобиля условно делится на несколько этапов. Первичный – это проклейка виброизоляции.
Ну и вторым слоем устанавливается шумоизоляция. Виды шумоизоляции авто Шумоизоляция автомобильная производится на различных основах,
на основе вспененного полиэтилена, вспененного каучука, или вспененного пенополиуретана .
Ну и самый древний материал для шумоизоляции – войлок Вспененный полиэтилен (Сплен)  ''',
             #####################################
             'specification': ''' Цена на материалы для шумоизоляции авто на основе полиэтилена ниже чем у каучука и пенополиуретана.
Благодаря чему шумоизоляция сплен очень популярна. Основная особенность материалов для шумоизоляции авто на основе
вспененного полиэтилена – чрезвычайно высокая влагостойкость.
Звукоизоляция — снижение уровня шума, проникающего в помещения извне. Количественная мера звукоизоляции ограждающих конструкций
выражается в децибелах. Степень необходимости звукоизоляции перекрытий зависит от характеристик используемых в строительстве материалов и соблюдения
всех технологических норм. К примеру, в случае сооружения перекрытий из качественных заводских бетонных плит при тщательном и аккуратном их монтаже
звукоизоляция может не потребоваться на протяжении нескольких лет.
Термин звукоизоляция всегда считался синонимом термина шумоизоляция. Но сейчас термин звукоизоляция чаще всего относят
к защите от шума в помещениях, в то время как шумоизоляция чаще используется при разговоре о защите от шума в автомобилях ''',
             #########################################################
             'image': "678860678_raschet_rashoda.jpg"
             },
            ##############################################################
            {'title': "Шумоизоляция автомобиля - это...",
             'body': '''Шумоизоляция автомобиля состоит из двух основных этапов:
Виброизоляция салона автомобиля
Шумоизоляция салона автомобиля''',
             ####################################
             'specification': '''Виброизоляция автомобиля
Виброизоляция это первичная, основная обработка. Процесс виброизоляции ― это проклейка вибропоглощяющих листов виброизоляции
на металл и иногда пластик салона автомобиля. Виброизоляция убирает гул металла, устраняя низкочастотные шумы,
которые являются основными в автомобиле. Так же дает качественную антикоррозионную обработку и консервацию металла.
К примеру срок службы самых лучших антикор материалов не более 5ти лет, а у виброизоляции наклеенной на металл срок службы
практически не ограничен. Перед проклейкой необходим прогрев и обезжиривание поверхности обработки. На основные источники шума
проклеивается самая мощная, толстая виброизоляция от 3мм до 4мм. Шум и вибрация из главных источников передается по цепи на другие детали,
усиливая их гул. Виброизоляция этих проблемных мест уберет более 60% всех шумов автомобиля.
К основным источникам шума в автомобиле относятся:
Щит моторного отсека и передние колесные арки
Коробка переключения передач
Тоннель (Если автомобиль заднеприводной)
Задние колесные арки, стаканы
При тюнинге автозвука область установки сабвуфера
К областям со средней вибронагрузкой применяется в зависимости от толщины металла виброизоляция толщиной от 1,8мм до 2,3мм. К ним относятся:
Филенки дверей автомобиля
Пол салона автомобиля
Днище багажника
Стойки крыши
Крылья, боковины
Капот
Ляда, или пятая дверь
К местам со слабой вибронагрузкой принято относить крышу автомобиля. Тут используется виброизоляция толщиной от 1,5мм до 1,8мм. На бусах и автомобилях с толстым металлом крыши 2,3мм. Но это условно, так как во время дождя, или при более-менее скоростной езде по нашим, простите за выражение, дорогам, металл крыши все же раздражающе гудит.
Шумоизоляция автомобиля
Шумоизоляция автомобиля это вторичный процесс утепления салона автомобиля, который следует после виброизоляции. Шумоизоляция клеится вторым слоем, сверху на виброизоляцию. Материалы шумоизоляции делятся на несколько типов, по их основе:
Вспененный полиэтилен (Сплен)
Вспененный каучук
Войлок, войлок с битумной пропиткой
Антискрип, изоляция проводки
Все материалы для шумоизоляции автомобиля отличаются по плотности, толщине, широте диапазона подавления шумов, наличию или отсутствию клеевого слоя. Перед установкой необходима обезжировка поверхности проклейки. В холодное время так же используется прогрев феном клеевого слоя.
Самый распространенный, относительно недорогой и широкоприменяемый материал шумоизоляции это  вспененный полиэтилен.
Пол автомобиля
Для шумоизоляции пола автомобиля применяется полиэтилен толщиной 8мм на клеевой основе, и без нее. Шумоизоляция без клеевой основы устанавливается на слой свежей автомобильной мастики. Для усиленной шумоизоляции днища применяется вспененный каучук, который убирает высокие и средние частоты шума. При решении сделать шумоизоляцию пола войлоком следует помнить о необходимости извлечения и просушки войлочной шумоизоляции два раза в год, весной и осенью. Войлок отлично давит шум, но тянет влагу даже из воздуха, что ведет к риску загнивания материала и коррозии металла пола.
Боковины и двери
Шумоизоляция дверей производится вспененным полиэтиленом толщиной 4мм или каучуком 6мм. Шумоизоляция клеится непосредственно на обшивку дверей. Если клеить на монтажную панель, возникнут сложности с доступом к внутренностям дверей. При установке не штатного усиленного автозвука при шумоизоляции используется звукопоглощяющий материал. За счет пористой структуры он не отражает а поглощает шумы. Места стыка пластика обрабатываются антискрипом. В следствии чего гуляющий при езде пластик трется о механикоустойчивое полотно антискрипа, и ходит беззвучно.
Крыша автомобиля
Для шумоизоляции крыши автомобиля мы рекомендуем использовать вспененный каучук. Он хоть и дорог, но за счет относительно небольшой площади обработки не ударит по карману. Зато у вспененного каучука лучшая клеевая основа из всех шумоизоляций, стойкая к жаре и холоду. Лучшие показатели теплоизоляции, он жаростойкий. К примеру если во вспененный каучук завернуть палец и поджечь, то Вы не почувствуете жара. Летом крыша обработанная каучуком не сильно нагревается, что позволяет усесться в салон без длительного проветривания. К тому же у каучука широкий диапазон шумоподавления.''',
             ##################################################
             'image': "678860678_raschet_rashoda.jpg"
             }]

#################################################################################################################################

products = [{'title': "Вибропласт Vizol М1",
             ############################################################
             'body': ''' Вибропласт для виброизоляции автомобиля Недорогая автомобильная виброизоляция визол М1,
широкого спектра применения. Основная особенность - тонкая фольга в 50 микрон и специальный облегченный герметик,
и толщина 1,3мм делают Визол М1 отличной легкой виброизоляцией для деталей авто с низкой вибро нагрузкойнаших установщиков
огромный опыт работы в области монтажа виброизоляции и шумоизоляции. ''',

             'specification': ''' Звукоизоляция — снижение уровня шума, проникающего в помещения извне. Количественная мера звукоизоляции ограждающих конструкций
выражается в децибелах. Степень необходимости звукоизоляции перекрытий зависит от характеристик используемых в строительстве материалов и соблюдения
всех технологических норм. К примеру, в случае сооружения перекрытий из качественных заводских бетонных плит при тщательном и аккуратном их монтаже
звукоизоляция может не потребоваться на протяжении нескольких лет.
Термин звукоизоляция всегда считался синонимом термина шумоизоляция. Но сейчас термин звукоизоляция чаще всего относят
к защите от шума в помещениях, в то время как шумоизоляция чаще используется при разговоре о защите от шума в автомобилях ''',
             ############################################################
             'price': 17.5,
             ##########################################################################
             'image': "905838154_w640_h640_7.jpg"
             },
            ##########################################################################################
            {'title': "Виброизоляция Визол М2 Толщина 2мм",
             #########################################################################################
             'body': ''' Гремящий металл в авто раздражает, отвлекает водителя. Гул металла вызывает ощущение усталости.
Это может привести к очень нежелательным последствиям. Необработанный кузов авто подвержен коррозии, а мовиль и
мастика не устранют шум. К счастью, есть Визол М2. Недорогой способ избавиться не только от шума в салоне, но и
получить приличную антикор защиту кузова. Хорошо прикатанная виброизоляция избавляет и от звука гремящего металла и от коррозии! ''',
             ################################################
             'specification': ''' Звукоизоляция — снижение уровня шума, проникающего в помещения извне. Количественная мера звукоизоляции ограждающих конструкций
выражается в децибелах. Степень необходимости звукоизоляции перекрытий зависит от характеристик используемых в строительстве материалов и соблюдения
всех технологических норм. К примеру, в случае сооружения перекрытий из качественных заводских бетонных плит при тщательном и аккуратном их монтаже
звукоизоляция может не потребоваться на протяжении нескольких лет.
Термин звукоизоляция всегда считался синонимом термина шумоизоляция. Но сейчас термин звукоизоляция чаще всего относят
к защите от шума в помещениях, в то время как шумоизоляция чаще используется при разговоре о защите от шума в автомобилях ''',
             ####################################################
             'price': 20.3,
             ####################################################################
             'image': "905839834_w640_h640_1.jpg"
             },
            ###################
            {'title': "Шумоизоляция Визол 1,3мм 500*700мм",
             ################################
             'body': '''Виброизоляция Визол 1,3мм для дверей автомобиля Филенки дверей.
 При обработке филенок дверей автомобиля рекомендуется проклейка внахлест, с перекрытием в 3-4см.
Площадь обработки 70%. Виброизоляцией не обрабатываются усилители металла и верх филенки, что бы избежать трения стекла
при пользовании стеклоподъемниками ''',
             ######################################################
             'specification': ''' К основным источникам шума в автомобиле относятся:
Щит моторного отсека и передние колесные арки
Коробка переключения передач
Тоннель (Если автомобиль заднеприводной)
Задние колесные арки, стаканы
При тюнинге автозвука область установки сабвуфера
К областям со средней вибронагрузкой применяется в зависимости от толщины металла виброизоляция толщиной от 1,8мм до 2,3мм. К ним относятся:
Филенки дверей автомобиля
Пол салона автомобиля
Днище багажника
Стойки крыши
Крылья, боковины
Капот
Ляда, или пятая дверь
К местам со слабой вибронагрузкой принято относить крышу автомобиля. Тут используется виброизоляция толщиной от 1,5мм до 1,8мм. На бусах и автомобилях с толстым металлом крыши 2,3мм. Но это условно, так как во время дождя, или при более-менее скоростной езде по нашим, простите за выражение, дорогам, металл крыши все же раздражающе гудит.
Шумоизоляция автомобиля
Шумоизоляция автомобиля это вторичный процесс утепления салона автомобиля, который следует после виброизоляции. Шумоизоляция клеится вторым слоем, сверху на виброизоляцию. Материалы шумоизоляции делятся на несколько типов, по их основе:
Вспененный полиэтилен (Сплен)
Вспененный каучук
Войлок, войлок с битумной пропиткой
Антискрип, изоляция проводки
Все материалы для шумоизоляции автомобиля отличаются по плотности, толщине, широте диапазона подавления шумов, наличию или отсутствию клеевого слоя. Перед установкой необходима обезжировка поверхности проклейки. В холодное время так же используется прогрев феном клеевого слоя.
Самый распространенный, относительно недорогой и широкоприменяемый материал шумоизоляции это  вспененный полиэтилен.
Пол автомобиля
Для шумоизоляции пола автомобиля применяется полиэтилен толщиной 8мм на клеевой основе, и без нее. Шумоизоляция без клеевой основы устанавливается на слой свежей автомобильной мастики. Для усиленной шумоизоляции днища применяется вспененный каучук, который убирает высокие и средние частоты шума. При решении сделать шумоизоляцию пола войлоком следует помнить о необходимости извлечения и просушки войлочной шумоизоляции два раза в год, весной и осенью. Войлок отлично давит шум, но тянет влагу даже из воздуха, что ведет к риску загнивания материала и коррозии металла пола.
Боковины и двери
Шумоизоляция дверей производится вспененным полиэтиленом толщиной 4мм или каучуком 6мм. Шумоизоляция клеится непосредственно на обшивку дверей. Если клеить на монтажную панель, возникнут сложности с доступом к внутренностям дверей. При установке не штатного усиленного автозвука при шумоизоляции используется звукопоглощяющий материал. За счет пористой структуры он не отражает а поглощает шумы. Места стыка пластика обрабатываются антискрипом. В следствии чего гуляющий при езде пластик трется о механикоустойчивое полотно антискрипа, и ходит беззвучно.
Крыша автомобиля
Для шумоизоляции крыши автомобиля мы рекомендуем использовать вспененный каучук.
Он хоть и дорог, но за счет относительно небольшой площади обработки не ударит по карману.
Зато у вспененного каучука лучшая клеевая основа из всех шумоизоляций, стойкая к жаре и холоду.
Лучшие показатели теплоизоляции, он жаростойкий. К примеру если во вспененный каучук завернуть палец и поджечь,
то Вы не почувствуете жара. Летом крыша обработанная каучуком не сильно нагревается, что позволяет усесться в салон без
длительного проветривания. К тому же у каучука широкий диапазон шумоподавления.''',
             #####################################################
             'price': 34.8,
             ########################################################
             'image': "892649168_w640_h640_vizol_13mm_1_1.jpg"
             }]