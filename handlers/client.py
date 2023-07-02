from aiogram import types, Dispatcher
from aiogram.types import UserProfilePhotos
from create_bot import dp, bot
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.filters import Text
from data_base import sqlite_db
from keyboards import kb_client, inline_kb_quest, inline_kb_succses, inline_kb_go, inline_kb_buy, inline_kb_buy_only,\
                      inline_kb_menu, inline_kb_back_menu, kb_menuchange, inline_kb_menu_buy, inline_kb_quest_format, inline_kb_change_format,\
                      inline_kb_quest_social, inline_kb_expect, thx_next, accept_photo, kb_purpose, kb_gender, kb_username, kb_back_change, kb_history,\
                      kb_only_prev, kb_only_next, inline_promo, inline_menu_promo
from aiogram.types.message import ContentType
from text import *
from work_with_pairs import similarity
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import os
import datetime
import validators

PAYMENT_TOKEN = os.getenv('PAYMENT_TOKEN')
PRICE_MONTH = types.LabeledPrice(label='Подписка на 1 месяц', amount=100*500)
PRICE_YEAR = types.LabeledPrice(label='Подписка на 1 год', amount=100*5000)

TOWNS = ['Абаза', 'Абакан', 'Абдулино', 'Абинск', 'Агидель', 'Агрыз', 'Адыгейск', 'Азнакаево', 'Азов', 'Ак-Довурак', 'Аксай', 'Алагир', 'Алапаевск', 'Алатырь', 'Алдан', 'Алейск', 'Александров', 'Александровск-Сахалинский', 'Александровск', 'Алексеевка', 'Алексин', 'Алзамай', 'Алупка', 'Алушта', 'Альметьевск', 'Амурск', 'Анадырь', 'Анапа', 'Ангарск', 'Андреаполь', 'Анжеро-Судженск', 'Анива', 'Апатиты', 'Апрелевка', 'Апшеронск', 'Арамиль', 'Аргун', 'Ардатов', 'Ардон', 'Арзамас', 'Аркадак', 'Армавир', 'Армянск', 'Арсеньев', 'Арск', 'Артём', 'Артёмовск', 'Артёмовский', 'Архангельск', 'Асбест', 'Асино', 'Астрахань', 'Аткарск', 'Ахтубинск', 'Ачинск', 'Аша', 'Бабаево', 'Бабушкин', 'Бавлы', 'Багратионовск', 'Байкальск', 'Баймак', 'Бакал', 'Баксан', 'Балабаново', 'Балаклава', 'Балаково', 'Балахна', 'Балашиха', 'Балашов', 'Балей', 'Балтийск', 'Барабинск', 'Барнаул', 'Барыш', 'Батайск', 'Бахчисарай', 'Бежецк', 'Белая Калитва', 'Белая Холуница', 'Белгород', 'Белебей', 'Белинский', 'Белово', 'Белогорск', 'Белогорск', 'Белозерск', 'Белокуриха', 'Беломорск', 'Белоозёрский', 'Белорецк', 'Белореченск', 'Белоусово', 'Белоярский', 'Белый', 'Белёв', 'Бердск', 'Березники', 'Берёзовский', 'Берёзовский', 'Беслан', 'Бийск', 'Бикин', 'Билибино', 'Биробиджан', 'Бирск', 'Бирюсинск', 'Бирюч', 'Благовещенск', 'Благовещенск', 'Благодарный', 'Бобров', 'Богданович', 'Богородицк', 'Богородск', 'Боготол', 'Богучар', 'Бодайбо', 'Бокситогорск', 'Болгар', 'Бологое', 'Болотное', 'Болохово', 'Болхов', 'Большой Камень', 'Бор', 'Борзя', 'Борисоглебск', 'Боровичи', 'Боровск', 'Бородино', 'Братск', 'Бронницы', 'Брянск', 'Бугульма', 'Бугуруслан', 'Будённовск', 'Бузулук', 'Буинск', 'Буй', 'Буйнакск', 'Бутурлиновка', 'Валдай', 'Валуйки', 'Велиж', 'Великие Луки', 'Великий Новгород', 'Великий Устюг', 'Вельск', 'Венёв', 'Верещагино', 'Верея', 'Верхнеуральск', 'Верхний Тагил', 'Верхний Уфалей', 'Верхняя Пышма', 'Верхняя Салда', 'Верхняя Тура', 'Верхотурье', 'Верхоянск', 'Весьегонск', 'Ветлуга', 'Видное', 'Вилюйск', 'Вилючинск', 'Вихоревка', 'Вичуга', 'Владивосток', 'Владикавказ', 'Владимир', 'Волгоград', 'Волгодонск', 'Волгореченск', 'Волжск', 'Волжский', 'Вологда', 'Володарск', 'Волоколамск', 'Волосово', 'Волхов', 'Волчанск', 'Вольск', 'Воркута', 'Воронеж', 'Ворсма', 'Воскресенск', 'Воткинск', 'Всеволожск', 'Вуктыл', 'Выборг', 'Выкса', 'Высоковск', 'Высоцк', 'Вытегра', 'Вышний Волочёк', 'Вяземский', 'Вязники', 'Вязьма', 'Вятские Поляны', 'Гаврилов Посад', 'Гаврилов-Ям', 'Гагарин', 'Гаджиево', 'Гай', 'Галич', 'Гатчина', 'Гвардейск', 'Гдов', 'Геленджик', 'Георгиевск', 'Глазов', 'Голицыно', 'Горбатов', 'Горно-Алтайск', 'Горнозаводск', 'Горняк', 'Городец', 'Городище', 'Городовиковск', 'Гороховец', 'Горячий Ключ', 'Грайворон', 'Гремячинск', 'Грозный', 'Грязи', 'Грязовец', 'Губаха', 'Губкин', 'Губкинский', 'Гудермес', 'Гуково', 'Гулькевичи', 'Гурьевск', 'Гурьевск', 'Гусев', 'Гусиноозёрск', 'Гусь-Хрустальный', 'Давлеканово', 'Дагестанские Огни', 'Далматово', 'Дальнегорск', 'Дальнереченск', 'Данилов', 'Данков', 'Дегтярск', 'Дедовск', 'Демидов', 'Дербент', 'Десногорск', 'Джанкой', 'Дзержинск', 'Дзержинский', 'Дивногорск', 'Дигора', 'Димитровград', 'Дмитриев', 'Дмитров', 'Дмитровск', 'Дно', 'Добрянка', 'Долгопрудный', 'Долинск', 'Домодедово', 'Донецк', 'Донской', 'Дорогобуж', 'Дрезна', 'Дубна', 'Дубовка', 'Дудинка', 'Духовщина', 'Дюртюли', 'Дятьково', 'Евпатория', 'Егорьевск', 'Ейск', 'Екатеринбург', 'Елабуга', 'Елец', 'Елизово', 'Ельня', 'Еманжелинск', 
'Емва', 'Енисейск', 'Ермолино', 'Ершов', 'Ессентуки', 'Ефремов', 'Железноводск', 'Железногорск-Илимский', 'Железногорск', 'Железногорск', 'Жердевка', 'Жигулёвск', 'Жиздра', 'Жирновск', 'Жуков', 'Жуковка', 'Жуковский', 'Завитинск', 'Заводоуковск', 'Заволжск', 'Заволжье', 'Задонск', 'Заинск', 'Закаменск', 'Заозёрный', 'Заозёрск', 'Западная Двина', 'Заполярный', 'Зарайск', 'Заречный', 'Заречный', 'Заринск', 'Звенигово', 'Звенигород', 'Зверево', 'Зеленогорск', 'Зеленогорск', 'Зеленоград', 'Зеленоградск', 'Зеленодольск', 'Зеленокумск', 'Зерноград', 'Зея', 'Зима', 'Златоуст', 'Злынка', 'Змеиногорск', 'Знаменск', 'Зубцов', 'Зуевка', 'Ивангород', 'Иваново', 'Ивантеевка', 'Ивдель', 'Игарка', 'Ижевск', 'Избербаш', 'Изобильный', 'Иланский', 'Инза', 'Инкерман', 'Иннополис', 'Инсар', 'Инта', 'Ипатово', 'Ирбит', 'Иркутск', 'Исилькуль', 'Искитим', 'Истра', 'Ишим', 'Ишимбай', 'Йошкар-Ола', 'Кадников', 'Казань', 'Калач-на-Дону', 'Калач', 'Калачинск', 'Калининград', 'Калининск', 'Калтан', 'Калуга', 'Калязин', 'Камбарка', 'Каменка', 'Каменногорск', 'Каменск-Уральский', 'Каменск-Шахтинский', 'Камень-на-Оби', 'Камешково', 'Камызяк', 'Камышин', 'Камышлов', 'Канаш', 'Кандалакша', 'Канск', 'Карабаново', 'Карабаш', 'Карабулак', 'Карасук', 'Карачаевск', 'Карачев', 'Каргат', 'Каргополь', 'Карпинск', 'Карталы', 'Касимов', 'Касли', 'Каспийск', 'Катав-Ивановск', 'Катайск', 'Качканар', 'Кашин', 'Кашира', 'Кедровый', 'Кемерово', 
'Кемь', 'Керчь', 'Кизел', 'Кизилюрт', 'Кизляр', 'Кимовск', 'Кимры', 'Кингисепп', 'Кинель', 'Кинешма', 'Киреевск', 'Киренск', 'Киржач', 'Кириллов', 'Кириши', 'Киров', 'Киров', 'Кировград', 'Кирово-Чепецк', 'Кировск', 'Кировск', 'Кирс', 'Кирсанов', 'Киселёвск', 'Кисловодск', 'Клин', 'Клинцы', 'Княгинино', 'Ковдор', 'Ковров', 'Ковылкино', 'Когалым', 'Кодинск', 'Козельск', 'Козловка', 'Козьмодемьянск', 'Кола', 'Кологрив', 'Коломна', 'Колпашево', 'Колпино', 'Кольчугино', 'Коммунар', 'Комсомольск-на-Амуре', 'Комсомольск', 'Конаково', 'Кондопога', 'Кондрово', 'Константиновск', 'Копейск', 'Кораблино', 'Кореновск', 'Коркино', 'Королёв', 'Короча', 'Корсаков', 'Коряжма', 'Костерёво', 'Костомукша', 'Кострома', 'Котельники', 'Котельниково', 'Котельнич', 'Котлас', 'Котово', 'Котовск', 'Кохма', 'Красавино', 'Красноармейск', 'Красноармейск', 'Красновишерск', 'Красногорск', 'Краснодар', 'Красное Село', 'Краснозаводск', 'Краснознаменск', 'Краснознаменск', 'Краснокаменск', 'Краснокамск', 'Красноперекопск', 'Краснослободск', 'Краснослободск', 'Краснотурьинск', 'Красноуральск', 'Красноуфимск', 'Красноярск', 'Красный Кут', 'Красный Сулин', 'Красный Холм', 'Кремёнки', 'Кронштадт', 'Кропоткин', 'Крымск', 'Кстово', 'Кубинка', 'Кувандык', 'Кувшиново', 'Кудрово', 'Кудымкар', 'Кузнецк', 'Куйбышев', 'Кукмор', 'Кулебаки', 'Кумертау', 'Кунгур', 'Купино', 'Курган', 'Курганинск', 'Курильск', 'Курлово', 'Куровское', 'Курск', 'Куртамыш', 'Курчалой', 'Курчатов', 'Куса', 'Кушва', 'Кызыл', 'Кыштым', 'Кяхта', 'Лабинск', 'Лабытнанги', 'Лагань', 'Ладушкин', 'Лаишево', 'Лакинск', 'Лангепас', 'Лахденпохья', 'Лебедянь', 'Лениногорск', 'Ленинск-Кузнецкий', 'Ленинск', 'Ленск', 'Лермонтов', 'Лесной', 'Лесозаводск', 'Лесосибирск', 'Ливны', 'Ликино-Дулёво', 'Липецк', 'Липки', 'Лиски', 'Лихославль', 'Лобня', 'Лодейное Поле', 'Ломоносов', 'Лосино-Петровский', 'Луга', 'Луза', 'Лукоянов', 'Луховицы', 'Лысково', 'Лысьва', 'Лыткарино', 'Льгов', 'Любань', 'Люберцы', 'Любим', 'Людиново', 'Лянтор', 'Магадан', 'Магас', 'Магнитогорск', 'Майкоп', 'Майский', 'Макаров', 'Макарьев', 'Макушино', 'Малая Вишера', 'Малгобек', 'Малмыж', 'Малоархангельск', 'Малоярославец', 'Мамадыш', 'Мамоново', 'Мантурово', 'Мариинск', 'Мариинский Посад', 'Маркс', 'Махачкала', 'Мглин', 'Мегион', 'Медвежьегорск', 'Медногорск', 'Медынь', 'Межгорье', 'Междуреченск', 'Мезень', 'Меленки', 'Мелеуз', 'Менделеевск', 'Мензелинск', 'Мещовск', 'Миасс', 'Микунь', 'Миллерово', 'Минеральные Воды', 'Минусинск', 'Миньяр', 'Мирный', 'Мирный', 'Михайлов', 'Михайловка', 'Михайловск', 'Михайловск', 'Мичуринск', 'Могоча', 'Можайск', 'Можга', 'Моздок', 'Мончегорск', 'Морозовск', 'Моршанск', 'Мосальск', 'Москва', 'Московский', 'Муравленко', 'Мураши', 'Мурино', 'Мурманск', 'Муром', 'Мценск', 'Мыски', 'Мытищи', 'Мышкин', 'Набережные Челны', 'Навашино', 'Наволоки', 'Надым', 'Назарово', 'Назрань', 'Называевск', 'Нальчик', 'Нариманов', 'Наро-Фоминск', 'Нарткала', 'Нарьян-Мар', 'Находка', 'Невель', 'Невельск', 'Невинномысск', 'Невьянск', 'Нелидово', 'Неман', 'Нерехта', 'Нерчинск', 'Нерюнгри', 'Нестеров', 'Нефтегорск', 'Нефтекамск', 'Нефтекумск', 'Нефтеюганск', 'Нея', 'Нижневартовск', 'Нижнекамск', 'Нижнеудинск', 'Нижние Серги', 'Нижний Ломов', 'Нижний Новгород', 'Нижний Тагил', 'Нижняя Салда', 'НижняяТура', 'Николаевск-на-Амуре', 'Николаевск', 'Никольск', 'Никольск', 'Никольское', 'Новая Ладога', 'Новая Ляля', 'Новоалександровск', 'Новоалтайск', 'Новоаннинский', 'Нововоронеж', 'Новодвинск', 'Новозыбков', 'Новокубанск', 'Новокузнецк', 'Новокуйбышевск', 'Новомичуринск', 'Новомосковск', 'Новопавловск', 'Новоржев', 'Новороссийск', 'Новосибирск', 'Новосиль', 'Новосокольники', 'Новотроицк', 'Новоузенск', 
'Новоульяновск', 'Новоуральск', 'Новохопёрск', 'Новочебоксарск', 'Новочеркасск', 'Новошахтинск', 'Новый Оскол', 'Новый Уренгой', 'Ногинск', 'Нолинск', 'Норильск', 'Ноябрьск', 'Нурлат', 'Нытва', 'Нюрба', 
'Нягань', 'Нязепетровск', 'Няндома', 'Облучье', 'Обнинск', 'Обоянь', 'Обь', 'Одинцово', 'Озёрск', 'Озёрск', 'Озёры', 'Октябрьск', 'Октябрьский', 'Окуловка', 'Оленегорск', 'Олонец', 'Олёкминск', 'Омск', 'Омутнинск', 'Онега', 'Опочка', 'Оренбург', 'Орехово-Зуево', 'Орлов', 'Орск', 'Орёл', 'Оса', 'Осинники', 'Осташков', 'Остров', 'Островной', 'Острогожск', 'Отрадное', 'Отрадный', 'Оха', 'Оханск', 'Очёр', 'Павлово', 'Павловск', 'Павловск', 'Павловский Посад', 'Палласовка', 'Партизанск', 'Певек', 'Пенза', 'Первомайск', 'Первоуральск', 'Перевоз', 'Пересвет', 'Переславль-Залесский', 'Пермь', 'Пестово', 'Петергоф', 'Петров Вал', 'Петровск-Забайкальский', 'Петровск', 'Петрозаводск', 'Петропавловск-Камчатский', 'Петухово', 'Петушки', 'Печора', 'Печоры', 'Пикалёво', 'Пионерский', 'Питкяранта', 'Плавск', 'Пласт', 'Плёс', 'Поворино', 'Подольск', 'Подпорожье', 'Покачи', 'Покров', 'Покровск', 'Полевской', 'Полесск', 'Полысаево', 'Полярные Зори', 'Полярный', 'Поронайск', 'Порхов', 'Похвистнево', 'Почеп', 'Починок', 
'Пошехонье', 'Правдинск', 'Приволжск', 'Приморск', 'Приморск', 'Приморско-Ахтарск', 'Приозерск', 'Прокопьевск', 'Пролетарск', 'Протвино', 'Прохладный', 'Псков', 'Пугачёв', 'Пудож', 'Пустошка', 'Пучеж', 'Пушкин', 'Пушкино', 'Пущино', 'Пыталово', 'Пыть-Ях', 'Пятигорск', 'Радужный', 'Радужный', 'Райчихинск', 'Раменское', 'Рассказово', 'Ревда', 'Реж', 'Реутов', 'Ржев', 'Родники', 'Рославль', 'Россошь', 'Ростов-на-Дону', 'Ростов', 'Рошаль', 'Ртищево', 'Рубцовск', 'Рудня', 'Руза', 'Рузаевка', 'Рыбинск', 'Рыбное', 'Рыльск', 'Ряжск', 'Рязань', 'Саки', 'Салават', 'Салаир', 'Салехард', 'Сальск', 'Самара', 'Санкт-Петербург', 'Саранск', 'Сарапул', 'Саратов', 'Саров', 'Сасово', 'Сатка', 'Сафоново', 'Саяногорск', 'Саянск', 'Светлогорск', 'Светлоград', 'Светлый', 'Светогорск', 'Свирск', 'Свободный', 'Себеж', 'Севастополь', 'Северо-Курильск', 'Северобайкальск', 'Северодвинск', 'Североморск', 'Североуральск', 'Северск', 'Севск', 'Сегежа', 'Сельцо', 'Семикаракорск', 'Семилуки', 'Семёнов', 'Сенгилей', 'Серафимович', 'Сергач', 'Сергиев Посад', 'Сердобск', 'Серов', 'Серпухов', 'Сертолово', 'Сестрорецк', 'Сибай', 'Сим', 'Симферополь', 'Сковородино', 'Скопин', 'Славгород', 'Славск', 'Славянск-на-Кубани', 'Сланцы', 'Слободской', 'Слюдянка', 'Смоленск', 'Снежинск', 'Снежногорск', 'Собинка', 'Советск', 'Советск', 'Советск', 'Советская Гавань', 'Советский', 'Сокол', 'Солигалич', 'Соликамск', 'Солнечногорск', 'Соль-Илецк', 'Сольвычегодск', 'Сольцы', 'Сорочинск', 'Сорск', 'Сортавала', 'Сосенский', 'Сосновка', 'Сосновоборск', 'Сосновый Бор', 'Сосногорск', 'Сочи', 'Спас-Деменск', 'Спас-Клепики', 'Спасск-Дальний', 'Спасск-Рязанский', 'Спасск', 'Среднеколымск', 'Среднеуральск', 'Сретенск', 'Ставрополь', 'Старая Купавна', 'Старая Русса', 'Старица', 'Стародуб', 'Старый Крым', 'Старый Оскол', 'Стерлитамак', 'Стрежевой', 'Строитель', 'Струнино', 'Ступино', 'Суворов', 'Судак', 'Суджа', 'Судогда', 'Суздаль', 'Сунжа', 'Суоярви', 'Сураж', 'Сургут', 'Суровикино', 'Сурск', 'Сусуман', 'Сухиничи', 'Сухой Лог', 'Сызрань', 'Сыктывкар', 'Сысерть', 'Сычёвка', 'Сясьстрой', 'Тавда', 'Таганрог', 'Тайга', 'Тайшет', 'Талдом', 'Талица', 'Тамбов', 'Тара', 'Тарко-Сале', 'Таруса', 'Татарск', 'Таштагол', 'Тверь', 'Теберда', 'Тейково', 'Темников', 'Темрюк', 'Терек', 'Тетюши', 'Тимашёвск', 'Тихвин', 'Тихорецк', 'Тобольск', 'Тогучин', 'Тольятти', 'Томари', 'Томмот', 'Томск', 'Топки', 'Торжок', 'Торопец', 'Тосно', 'Тотьма', 'Троицк', 'Троицк', 'Трубчевск', 'Трёхгорный', 'Туапсе', 'Туймазы', 'Тула', 'Тулун', 'Туран', 'Туринск', 'Тутаев', 'Тында', 'Тырныауз', 'Тюкалинск', 'Тюмень', 'Уварово', 'Углегорск', 'Углич', 'Удачный', 'Удомля', 'Ужур', 'Узловая', 'Улан-Удэ', 'Ульяновск', 'Унеча', 'Урай', 'Урень', 'Уржум', 'Урус-Мартан', 'Урюпинск', 'Усинск', 'Усмань', 'Усолье-Сибирское', 'Усолье', 'Уссурийск', 'Усть-Джегута', 'Усть-Илимск', 'Усть-Катав', 'Усть-Кут', 'Усть-Лабинск', 'Устюжна', 'Уфа', 'Ухта', 'Учалы', 'Уяр', 'Фатеж', 'Феодосия', 'Фокино', 'Фокино', 'Фролово', 'Фрязино', 'Фурманов', 'Хабаровск', 'Хадыженск', 'Ханты-Мансийск', 'Харабали', 'Харовск', 'Хасавюрт', 'Хвалынск', 'Хилок', 'Химки', 'Холм', 'Холмск', 'Хотьково', 'Цивильск', 'Цимлянск', 'Циолковский', 'Чадан', 'Чайковский', 'Чапаевск', 'Чаплыгин', 'Чебаркуль', 'Чебоксары', 'Чегем', 'Чекалин', 
'Челябинск', 'Чердынь', 'Черемхово', 'Черепаново', 'Череповец', 'Черкесск', 'Черноголовка', 'Черногорск', 'Чернушка', 'Черняховск', 'Чехов', 'Чистополь', 'Чита', 'Чкаловск', 'Чудово', 'Чулым', 'Чусовой', 'Чухлома', 'Чёрмоз', 'Шагонар', 'Шадринск', 'Шали', 'Шарыпово', 'Шарья', 'Шатура', 'Шахты', 'Шахунья', 'Шацк', 'Шебекино', 'Шелехов', 'Шенкурск', 'Шилка', 'Шимановск', 'Шиханы', 'Шлиссельбург', 'Шумерля', 'Шумиха', 'Шуя', 'Щербинка', 'Щигры', 'Щучье', 'Щёкино', 'Щёлкино', 'Щёлково', 'Электрогорск', 'Электросталь', 'Электроугли', 'Элиста', 'Энгельс', 'Эртиль', 'Югорск', 'Южа', 'Южно-Сахалинск', 'Южно-Сухокумск', 'Южноуральск', 'Юрга', 'Юрьев-Польский', 'Юрьевец', 'Юрюзань', 'Юхнов', 'Ядрин', 'Якутск', 'Ялта', 'Ялуторовск', 'Янаул', 'Яранск', 'Яровое', 'Ярославль', 'Ярцево', 'Ясногорск', 'Ясный', 'Яхрома']

# класс, который отвечает за анкетирование пользователя
class Client(StatesGroup): 
    # заполнение анкеты
    id = State()
    name = State()  # должны быть только буквы
    photo = State()
    username = State()
    town = State()  # дополнительная проверка на корректный город
    social_network = State()
    work = State()
    hooks = State()
    expect = State()
    format = State()
    born = State()
    purpose = State()
    gender = State()
    email = State()
     
    start_pay = State()
    buy_month = State()
    buy_year = State()
    promo_month = State()
    promo_year = State()
    get_promocode = State()
    
class Change(StatesGroup):  
    change_start = State()
    change_state = State()
    
class Menu(StatesGroup):
    menu = State()
    menu_point = State()

class Menu_buy(StatesGroup):
    get_promocode = State()
    start_pay = State()

#вернуться к предыдущему вопросу
async def back(callback_query : types.CallbackQuery, state : FSMContext):
    await callback_query.answer()
    current_state = await state.get_state()
    async with state.proxy() as data:
        if current_state != Client.buy_month.state and current_state != Client.buy_year.state and current_state != Client.get_promocode.state :
            msg : types.Message = types.Message.to_object(data['Last_message'])
            await msg.edit_reply_markup(None)
            await msg.delete()
    if current_state == Client.town.state or current_state == Client.username.state:
        async with state.proxy() as data:    
            msg = await bot.send_message(callback_query.from_user.id, GET_NAME)
            data['Last_message'] = msg.to_python()
        await Client.previous()
        if current_state == Client.town.state:
            await Client.previous()
    elif current_state == Client.social_network.state:
        async with state.proxy() as data:
            msg = await bot.send_message(callback_query.from_user.id, GET_TOWN, reply_markup=inline_kb_quest)
            data['Last_message'] = msg.to_python()
    elif current_state == Client.work.state:
        async with state.proxy() as data:
            msg = await bot.send_message(callback_query.from_user.id, GET_SOCIAL, reply_markup=inline_kb_quest_social) 
            data['Last_message'] = msg.to_python()
    elif current_state == Client.hooks.state:
        async with state.proxy() as data:
            msg = await bot.send_message(callback_query.from_user.id, GET_WORK, reply_markup=inline_kb_quest) 
            data['Last_message'] = msg.to_python()
    elif current_state == Client.expect.state:
        async with state.proxy() as data:
            msg = await bot.send_message(callback_query.from_user.id, GET_HOBBY, reply_markup=inline_kb_quest)
            data['Last_message'] = msg.to_python()  
    elif current_state == Client.format.state:
        async with state.proxy() as data:
            msg = await bot.send_message(callback_query.from_user.id, GET_EXPECT, reply_markup=inline_kb_expect) 
            data['Last_message'] = msg.to_python()
    elif current_state == Client.born.state:
        async with state.proxy() as data:
            msg = await bot.send_message(callback_query.from_user.id, GET_FORMAT, reply_markup=inline_kb_quest_format) 
            data['Last_message'] = msg.to_python()
    elif current_state == Client.purpose.state:
        async with state.proxy() as data:
            msg = await bot.send_message(callback_query.from_user.id, GET_DATA, reply_markup=inline_kb_quest) 
            data['Last_message'] = msg.to_python()            
    elif current_state == Client.gender.state:
        async with state.proxy() as data:
            msg = await bot.send_message(callback_query.from_user.id, CHOOSE_FORMAT, reply_markup=kb_purpose) 
            data['Last_message'] = msg.to_python() 
    elif current_state == Client.email.state:
        async with state.proxy() as data:
            msg = await bot.send_message(callback_query.from_user.id, CHOOSE_GENDER, reply_markup=kb_gender) 
            data['Last_message'] = msg.to_python()           
    elif current_state == Client.get_promocode.state:
        async with state.proxy() as data:
            msg = types.Message.to_object(data['Last_message'])
            if data['buy_type'] == 0:
                await msg.edit_text('Вы выбрали подписку на месяц. Цена составит 500 рублей, есть ли у вас промокод?', reply_markup=inline_promo)
                await Client.buy_month.set()
            else:
                await msg.edit_text('Вы выбрали подписку на год. Цена составит 5000 рублей, есть ли у вас промокод?', reply_markup=inline_promo)
                await Client.buy_year.set()     
            return
    elif current_state == Client.buy_month.state or current_state == Client.buy_year.state:
        async with state.proxy() as data:
            msg = types.Message.to_object(data['Last_message'])
            await msg.edit_text(ABOUT_SUB, reply_markup=inline_kb_buy)
        await Client.start_pay.set()
        return
    else:
        return
    await Client.previous()

async def next_step(callback_query : types.CallbackQuery, state : FSMContext):    
    await callback_query.answer()
    async with state.proxy() as data:
        try:
            msg = types.Message.to_object(data['Last_message'])
            await msg.edit_text(msg.text + f'\n\n➡️ Поехали 🚀', reply_markup=None)
        except:
            pass
        try:
            msg = types.Message.to_object(data['Last_message'])
            await msg.delete_reply_markup()
        except:
            pass
        try:
            msg = types.Message.to_object(data['Main_message'])
            await msg.delete_reply_markup()
        except:
            pass
    is_reg = await sqlite_db.is_register(callback_query.from_user.id)
    if is_reg:
        date = await sqlite_db.check_paid(callback_query.from_user.id)
        if date[0] == True:
            date_paid = date[1].split('-')
            month_dict = {1 : 'Января', 2 : 'Февраля', 3 : 'Марта', 4 : 'Апреля', 5 : 'Мая',
                          6 : 'Июня', 7 : 'Июля', 8 : 'Августа', 9 : 'Сенятбря', 10 : 'Октября',
                          11 : 'Ноября', 12 : 'Декабря'}               
            await bot.send_message(callback_query.from_user.id, f'Вы уже зарегестрированы в нашей системе✅\n\
Подписка действует до {date_paid[0]} {month_dict[int(date_paid[1])]} {date_paid[2]} года⏳')
            async with state.proxy() as data:
                msg = await bot.send_message(callback_query.from_user.id, MENU, reply_markup=inline_kb_menu)
                data['Main_message'] = msg.to_python()
            await Menu.menu.set()
            return
        await bot.send_message(callback_query.from_user.id, 'Вы уже зарегестрированы в нашей системе, данные которые вы заполнили:\n')
        # await Client.expect.set()
        await sqlite_db.load_info(callback_query.from_user.id, state)         
        values = list(await sqlite_db.get_profile(callback_query.from_user.id))
        age = datetime.datetime.now().year - int(values[10].split('.')[2])
        format = str()
        if values[9]:
            format = 'Онлайн'
        else :
            format = 'Оффлайн'
        card = f'{values[2]} из города {values[4]}\nВозраст: {age}\n\nTelegram: {values[1]}\nСоциальная сеть: {values[5]}\n\nЧем занимается: \
{values[6]}\n\nЗацепки для начала разговора: {values[7]}\n\nЦель использования PRIDE CONNECT: {values[11]}\n\nФормат встречи: {format}\nОт встречи ожидает: {values[8]}'      
        async with state.proxy() as data:
            msg = await bot.send_message(callback_query.from_user.id, TEXT_PROFILE + card, reply_markup=inline_kb_succses)
            data['Last_message'] = msg.to_python()
        return    
    await bot.send_message(callback_query.from_user.id, DESCRIBE_WORK)
    video = open('./content/videos/vid1.mp4', 'rb')
    async with state.proxy() as data:
        msg = await bot.send_video(callback_query.from_user.id, video, reply_markup=thx_next)
        data['Last_message'] = msg.to_python()

async def start_ask(callback_query : types.CallbackGame, state : FSMContext):
    await callback_query.answer()
    async with state.proxy() as data:
        msg = types.Message.to_object(data['Last_message'])
        await msg.delete_reply_markup()
        msg = await bot.send_message(callback_query.from_user.id, GET_NAME)
        data['Last_message'] = msg.to_python()
    await Client.name.set()

async def menu(message : types.Message, state : FSMContext):
    async with state.proxy() as data:
        if 'Main_message' in data.keys():
            msg : types.Message = types.Message.to_object(data['Main_message'])
            try:
                await msg.delete()
            except:
                pass
        if await sqlite_db.is_register(message.from_user.id) == False:
            await message.answer('Для того, чтобы перейти в главное меню вы должны заполнить анкету!\nВведите /start, чтобы начать заполнение или воспользуйтесь опцией /help')
            return
        msg = await message.answer(MENU, reply_markup=inline_kb_menu)
        data['Main_message'] = msg.to_python()
    await Menu.menu.set()

async def help(message : types.Message):
    await message.answer(HELP_MESSAGE)

# обработка старта бота и получения id
async def start(message : types.Message, state : FSMContext):
    await Client.id.set()
    async with state.proxy() as data:
        user_name = message.from_user.first_name
        msg = await message.answer(f'Привет, {user_name}⚡️!\n' + START_MESSAGE, reply_markup=inline_kb_go)
        data['Last_message'] = msg.to_python()
    
    
async def get_name(message : types.Message, state : FSMContext):
    async with state.proxy() as data:
        data['id'] = message.from_user.id
        data['Телеграм'] = f'@{message.from_user.username}' 
        data['Имя'] = message.text
        msg = types.Message.to_object(data['Last_message'])
        photos: UserProfilePhotos = await bot.get_user_profile_photos(message.from_user.id)
        if photos.total_count == 0:
            await bot.send_message(message.from_user.id, 'У вас нет ни одной фотографии профиля!\nПожалуйста, отправьте вашу фотографию')
            await Client.photo.set()
        else:
            await bot.send_photo(message.from_user.id, photos.photos[0][0].file_id)
            data['Фото'] = photos.photos[0][0].file_id
            msg = await bot.send_message(message.from_user.id, 'Вот Ваша первая фотография в профиле, мы будем отправлять её Вашему партнёру каждую неделю', reply_markup=accept_photo)
            data['Last_message'] = msg.to_python()

async def accept(callback_query : types.CallbackQuery, state : FSMContext):
    await callback_query.answer()
    async with state.proxy() as data:
        msg = types.Message.to_object(data['Last_message'])
        await msg.edit_text(msg.text + '\n\n➡️ Хорошо, далее✅', reply_markup=None)
        if callback_query.from_user.username == None:
            msg = await bot.send_message(callback_query.from_user.id, GET_USER_NAME, reply_markup=kb_username) 
            data['Last_message'] = msg.to_python()
            await Client.username.set()
            return
        msg = await bot.send_message(callback_query.from_user.id, GET_TOWN, reply_markup=inline_kb_quest) 
        data['Last_message'] = msg.to_python() 
    await Client.town.set()
    
          
async def other(callback_query : types.CallbackQuery, state : FSMContext):
    await callback_query.answer()
    async with state.proxy() as data:
        msg = types.Message.to_object(data['Last_message'])
        await msg.edit_text(msg.text + '\n\n➡️ Хочу отправить другую фотографию!', reply_markup=None)
    await bot.send_message(callback_query.from_user.id, 'Пожалуйста, отправьте вашу фотографию!')
    await Client.photo.set()

async def get_photo(message : types.Message, state : FSMContext):
    async with state.proxy() as data:
        data['Фото'] = message.photo[0].file_id
        if message.from_user.username == None:
            msg = await bot.send_message(message.from_user.id, GET_USER_NAME, reply_markup=kb_username) 
            data['Last_message'] = msg.to_python() 
            await Client.username.set()
            return
        msg = await message.answer(GET_TOWN, reply_markup=inline_kb_quest) 
        data['Last_message'] = msg.to_python()    
    await Client.town.set()
    
async def check_username(callback_query : types.CallbackQuery, state : FSMContext):
    await callback_query.answer()
    async with state.proxy() as data:   
        if callback_query.from_user.username == None:
            msg = types.Message.to_object(data['Last_message'])
            await msg.delete_reply_markup()
            msg = await bot.send_message(callback_query.from_user.id, 'Юзернэйм не был добавлен!\n\n' + GET_USER_NAME, reply_markup=kb_username) 
            data['Last_message'] = msg.to_python()   
            return
            
        data['Телеграм'] = f'@{callback_query.from_user.username}'
        msg = types.Message.to_object(data['Last_message'])
        await msg.edit_text(msg.text + f'\n\n➡️Ваш Юзернэйм @{callback_query.from_user.username}')
        msg = await bot.send_message(callback_query.from_user.id, GET_TOWN, reply_markup=inline_kb_quest) 
        data['Last_message'] = msg.to_python() 
   
    await Client.next()
    
# обработка получения города
async def get_town(message : types.Message, state : FSMContext):    
    async with state.proxy() as data:
        if message.text in TOWNS:
            msg = types.Message.to_object(data['Last_message'])
            data['Город'] = message.text
            await msg.delete_reply_markup()
            msg = await message.answer(GET_SOCIAL, reply_markup=inline_kb_quest_social) 
            data['Last_message'] = msg.to_python()    
        else:
            user_town = message.text
            sim = 0
            index = 0
            for i in range(len(TOWNS)):
                cur_sim = similarity(user_town, TOWNS[i])
                if cur_sim > sim:
                    index = i
                    sim = cur_sim
            kb_town = InlineKeyboardMarkup(resize_keyboard=True).row(InlineKeyboardButton(text=str(TOWNS[index]), callback_data='maybe_town')).row(
                                                             InlineKeyboardButton(text=user_town, callback_data='enter_town')).row(
                                                             InlineKeyboardButton(text='Ввести город ещё раз', callback_data='again_town'))
            msg = types.Message.to_object(data['Last_message'])
            if msg.reply_markup != None:
                await msg.edit_reply_markup(None)
            data['Город'] = message.text
            data['maybe_town'] = TOWNS[index]
            msg = await message.answer('К сожалению ваш город не удалось найти в списке городов\nВыберите максимально схожий или оставьте введённый город!', reply_markup=kb_town)
            data['Last_message'] = msg.to_python()  
            return
    await Client.next()
   
async def again_town(callback_query : types.CallbackQuery, state : FSMContext):
    await callback_query.answer()  
    async with state.proxy() as data:
        msg = types.Message.to_object(data['Last_message'])
        await msg.edit_reply_markup(None)
        msg = await bot.send_message(callback_query.from_user.id, GET_TOWN, reply_markup=inline_kb_quest) 
        data['Last_message'] = msg.to_python()  
    
async def maybe_town(callback_query : types.CallbackQuery, state : FSMContext):
    await callback_query.answer()
    async with state.proxy() as data:
        data['Город'] = data['maybe_town']
        msg = types.Message.to_object(data['Last_message'])
        await msg.delete_reply_markup()
        msg = await bot.send_message(callback_query.from_user.id, GET_SOCIAL, reply_markup=inline_kb_quest_social) 
        data['Last_message'] = msg.to_python()   
    await Client.social_network.set()
    
async def enter_town(callback_query : types.CallbackQuery, state : FSMContext):
    await callback_query.answer()
    async with state.proxy() as data:
        msg = types.Message.to_object(data['Last_message'])
        await msg.delete_reply_markup()
        msg = await bot.send_message(callback_query.from_user.id, GET_SOCIAL, reply_markup=inline_kb_quest_social) 
        data['Last_message'] = msg.to_python() 
    await Client.social_network.set()

# обработка получения социальной сети
async def get_social_network(message : types.Message, state : FSMContext):
    async with state.proxy() as data:
        if not validators.url(message.text):
            msg = types.Message.to_object(data['Last_message'])
            await msg.delete_reply_markup()
            msg = await bot.send_message(message.from_user.id, 'Ваше сообщение не является ссылкой! Пожалуйста отправьте ссылку на вашу социальную сеть.\n Например: Вконтакте, Инстаграм', reply_markup=inline_kb_quest_social) 
            data['Last_message'] = msg.to_python()             
            return
        data['Социальные сети'] = message.text
        msg = types.Message.to_object(data['Last_message'])
        await msg.delete_reply_markup()
        msg = await message.answer(GET_WORK, reply_markup=inline_kb_quest)  
        data['Last_message'] = msg.to_python()    
    await Client.next()
    
    
# обработка получения занятий
async def get_work(message : types.Message, state : FSMContext):
    async with state.proxy() as data:
        data['Работа'] = message.text
        msg = types.Message.to_object(data['Last_message'])
        await msg.delete_reply_markup()
        msg = await message.answer(GET_HOBBY, reply_markup=inline_kb_quest) 
        data['Last_message'] = msg.to_python()    
    await Client.next()

# обработка получения зацепок
async def get_hooks(message : types.Message, state : FSMContext): 
    async with state.proxy() as data:
        data['Зацепки'] = message.text
        msg = types.Message.to_object(data['Last_message'])
        await msg.delete_reply_markup()
        msg = await message.answer(GET_EXPECT, reply_markup=inline_kb_expect)
        data['Last_message'] = msg.to_python()                  
    await Client.next()
    
async def get_expect(callback_query : types.CallbackQuery, state : FSMContext):
    await callback_query.answer() 
    async with state.proxy() as data:
        data['Ожидания'] = callback_query.data
        msg = types.Message.to_object(data['Last_message'])
        await msg.edit_text(msg.text + f'\n\n➡️ {callback_query.data}', reply_markup=None)
        msg = await bot.send_message(callback_query.from_user.id, GET_FORMAT, reply_markup=inline_kb_quest_format)          
        data['Last_message'] = msg.to_python()      
    await Client.next() 
    
    
async def online(callback_query : types.CallbackQuery, state : FSMContext):
    await callback_query.answer()
    async with state.proxy() as data:
        msg = types.Message.to_object(data['Last_message'])
        await msg.edit_text(msg.text + '\n\n➡️ Онлайн', reply_markup=None)
        data['Формат'] = True
        msg = await bot.send_message(callback_query.from_user.id, GET_DATA, reply_markup=inline_kb_quest)
        data['Last_message'] = msg.to_python()
    await Client.next()

async def offline(callback_query : types.CallbackQuery, state : FSMContext):
    await callback_query.answer()
    async with state.proxy() as data:
        msg = types.Message.to_object(data['Last_message'])
        await msg.edit_text(msg.text + '\n\n➡️ Вживую', reply_markup=None)
        data['Формат'] = False
        msg = await bot.send_message(callback_query.from_user.id, GET_DATA, reply_markup=inline_kb_quest)
        data['Last_message'] = msg.to_python()
    await Client.next()
    
async def get_data(message : types.Message, state : FSMContext):
    async with state.proxy() as data:
        date = message.text.split('.')
        if len(date) < 3 or int(date[0]) < 0 or int(date[0]) > 31 or int(date[1]) < 1 or int(date[1]) > 12 or len(date[2]) != 4 or int(date[2]) < 1900 or int(date[2]) > 2020:
            msg = types.Message.to_object(data['Last_message'])
            await msg.delete_reply_markup()
            msg = await message.answer('Некорректная дата! Попробуйте снова', reply_markup=inline_kb_quest)
            data['Last_message'] = msg.to_python()
            return       
        msg = types.Message.to_object(data['Last_message'])
        await msg.delete_reply_markup()
        data['Дата'] = message.text
        msg = await message.answer(CHOOSE_FORMAT, reply_markup=kb_purpose)
        data['Last_message'] = msg.to_python()
    await Client.next()

async def get_purpose1(callback_query : types.CallbackQuery, state : FSMContext):
    await callback_query.answer()
    async with state.proxy() as data:
        data['Цель'] = 'Найти новые связи для решения задач по проектам'
        msg = types.Message.to_object(data['Last_message'])
        await msg.edit_text(msg.text + '\n\n➡️ Найти новые связи для решения задач по проектам', reply_markup=None)
        msg = await bot.send_message(callback_query.from_user.id, CHOOSE_GENDER, reply_markup=kb_gender)
        data['Last_message'] = msg.to_python()
    await Client.next()
    
async def get_purpose2(callback_query : types.CallbackQuery, state : FSMContext):
    await callback_query.answer()
    async with state.proxy() as data:
        data['Цель'] = 'Создать коллаборации и партнерства'
        msg = types.Message.to_object(data['Last_message'])
        await msg.edit_text(msg.text + '\n\n➡️ Создать коллаборации и партнерства', reply_markup=None)
        msg = await bot.send_message(callback_query.from_user.id, CHOOSE_GENDER, reply_markup=kb_gender)
        data['Last_message'] = msg.to_python()
    await Client.next() 
    
async def get_purpose3(callback_query : types.CallbackQuery, state : FSMContext):
    await callback_query.answer()
    async with state.proxy() as data:
        data['Цель'] = 'Найти подрядчиков в разных нишах'
        msg = types.Message.to_object(data['Last_message'])
        await msg.edit_text(msg.text + '\n\n➡️ Найти подрядчиков в разных нишах', reply_markup=None)
        msg = await bot.send_message(callback_query.from_user.id, CHOOSE_GENDER, reply_markup=kb_gender)
        data['Last_message'] = msg.to_python()
    await Client.next()
    
async def get_purpose4(callback_query : types.CallbackQuery, state : FSMContext):
    await callback_query.answer()
    async with state.proxy() as data:
        data['Цель'] = 'Познакомиться с интересными людьми со схожими интересами'
        msg = types.Message.to_object(data['Last_message'])
        await msg.edit_text(msg.text + '\n\n➡️ Познакомиться с интересными людьми со схожими интересами', reply_markup=None)
        msg = await bot.send_message(callback_query.from_user.id, CHOOSE_GENDER, reply_markup=kb_gender)
        data['Last_message'] = msg.to_python()
    await Client.next()  
    
async def get_purpose5(callback_query : types.CallbackQuery, state : FSMContext):
    await callback_query.answer()
    async with state.proxy() as data:
        data['Цель'] = 'Расширить свои возможности и влияние'
        msg = types.Message.to_object(data['Last_message'])
        await msg.edit_text(msg.text + '\n\n➡️ Расширить свои возможности и влияние', reply_markup=None)
        msg = await bot.send_message(callback_query.from_user.id, CHOOSE_GENDER, reply_markup=kb_gender)
        data['Last_message'] = msg.to_python()
    await Client.next()               

async def get_male(callback_query : types.CallbackQuery, state : FSMContext):
    await callback_query.answer()
    async with state.proxy() as data:
        data['Гендер'] = 'Мужчина'
        msg = types.Message.to_object(data['Last_message'])
        await msg.edit_text(msg.text + '\n\n➡️ Мужчина', reply_markup=None)
        msg = await bot.send_message(callback_query.from_user.id, GET_EMAIL, reply_markup=inline_kb_quest)
        data['Last_message'] = msg.to_python()
    await Client.next()
    
async def get_female(callback_query : types.CallbackQuery, state : FSMContext):
    await callback_query.answer()
    async with state.proxy() as data:
        data['Гендер'] = 'Женщина'
        msg = types.Message.to_object(data['Last_message'])
        await msg.edit_text(msg.text + '\n\n➡️ Женщина', reply_markup=None)
        msg = await bot.send_message(callback_query.from_user.id, GET_EMAIL, reply_markup=inline_kb_quest)
        data['Last_message'] = msg.to_python()
    await Client.next()    
    
async def get_email(message : types.Message, state : FSMContext):
    async with state.proxy() as data:
        msg = types.Message.to_object(data['Last_message'])
        # await msg.delete_reply_markup()
        await msg.delete_reply_markup()
        data['Email'] = message.text
        data['Оплачено'] = False
        data['Дата_окончания_подписки'] = None
    await sqlite_db.insert_sql(state)
    values = list(await sqlite_db.get_profile(message.from_user.id))
    age = datetime.datetime.now().year - int(values[10].split('.')[2])
    format = str()
    if values[9]:
        format = 'Онлайн'
    else :
        format = 'Оффлайн'
    card = f'{values[2]} из города {values[4]}\nВозраст: {age}\n\nTelegram: {values[1]}\nСоциальная сеть: {values[5]}\n\nЧем занимается: \
{values[6]}\n\nЗацепки для начала разговора: {values[7]}\n\nЦель использования PRIDE CONNECT: {values[11]}\n\nФормат встречи: {format}\nОт встречи ожидает: {values[8]}'    
    async with state.proxy() as data:
        msg = await message.answer(TEXT_PROFILE + card, reply_markup=inline_kb_succses)        
        data['Last_message'] = msg.to_python()  
   
async def fill_again(callback_query : types.CallbackQuery, state : FSMContext):
    await callback_query.answer()
    async with state.proxy() as data:
        msg = types.Message.to_object(data['Last_message'])
        await msg.delete_reply_markup()
        msg = await bot.send_message(callback_query.from_user.id, GET_NAME)
        data['Last_message'] = msg.to_python()
    await Client.name.set()
            
async def succses(callback_query : types.CallbackQuery, state : FSMContext):
    await callback_query.answer()    
    async with state.proxy() as data:
        msg = types.Message.to_object(data['Last_message'])
        try:
            await msg.delete_reply_markup()
        except:
            pass         
    
    user = await sqlite_db.check_paid(callback_query.from_user.id)
    if user[0]:
        async with state.proxy() as data:
            msg = await bot.send_message(callback_query.from_user.id, MENU, reply_markup=inline_kb_menu)
            data['Main_message'] = msg.to_python()
        await Menu.menu.set()
        return
    
    await Client.start_pay.set()
    async with state.proxy() as data:
        data['Promo'] = 0
        photo = open('./content/photo/pam1.png', 'rb')
        await bot.send_photo(callback_query.from_user.id, photo)
        msg = await bot.send_message(callback_query.from_user.id, ABOUT_SUB, reply_markup=inline_kb_buy)
        data['Last_message']  = msg.to_python()       
       
async def enter_promocode(callback_query : types.CallbackQuery, state : FSMContext):
    await callback_query.answer()
    async with state.proxy() as data:
        msg = types.Message.to_object(data['Last_message'])
        await msg.edit_text('Введите промокод:', reply_markup=inline_kb_quest)  
        data['Last_message']  = msg.to_python()
    await Client.get_promocode.set()

async def check_promo(message : types.Message, state : FSMContext):
    async with state.proxy() as data:
        data['Promo'] = await sqlite_db.check_promo(message)
        await message.delete()
        if data['Promo'] == 0:
            msg = types.Message.to_object(data['Last_message'])
            if data['buy_type'] == 0:
                await msg.edit_text('Введённый промокод закончился или не найден!\nВы выбрали подписку на месяц. Цена составит 500 рублей, есть ли у вас промокод?', reply_markup=inline_promo)
            else:
                await msg.edit_text('Введённый промокод закончился или не найден!\nВы выбрали подписку на год. Цена составит 5000 рублей, есть ли у вас промокод?', reply_markup=inline_promo)
            return
        if data['Promo'] == 100:
            await message.answer(ABOUT_UNIC_PROMO)
            await sqlite_db.add_user_paid(message.from_user.id)
            await sqlite_db.add_demo_paid(message.from_user.id)
            await state.finish()
            await Menu.menu.set()
            msg = await message.answer(MENU, reply_markup=inline_kb_menu)
            data['Main_message'] = msg.to_python()
            return
        promo_amount = data['Promo']
        msg = types.Message.to_object(data['Last_message'])
        if data['buy_type'] == 0:
            await msg.edit_text(f'С учётом вашего промокода цена составит {PRICE_MONTH.amount * (1 - float(promo_amount / 100)) // 100}', reply_markup=inline_kb_buy_only)
        else:
            await msg.edit_text(f'С учётом вашего промокода цена составит {PRICE_YEAR.amount * (1 - float(promo_amount / 100)) // 100}', reply_markup=inline_kb_buy_only)
    await Client.next()
    
async def buy_later(callbck_query : types.CallbackQuery, state : FSMContext):
    await callbck_query.answer()
    async with state.proxy() as data:
        msg = types.Message.to_object(data['Last_message'])
        await msg.edit_reply_markup(None)
        await bot.send_message(callbck_query.from_user.id, MENU, reply_markup=inline_kb_menu)
        data['Main_message'] = msg.to_python()
    await Menu.menu.set()
    
async def buy_month(callback_query : types.CallbackQuery, state : FSMContext):
    await callback_query.answer()
    async with state.proxy() as data:
        msg = types.Message.to_object(data['Last_message'])
        await msg.edit_text('Вы выбрали подписку на месяц. Цена составит 500 рублей, есть ли у вас промокод?', reply_markup=inline_promo)
        data['Last_message'] = msg.to_python()
        data['buy_type'] = 0
    await Client.buy_month.set()
    
async def buy_year(callback_query : types.CallbackQuery, state : FSMContext):
    await callback_query.answer()
    async with state.proxy() as data:
        msg = types.Message.to_object(data['Last_message'])
        await msg.edit_text('Вы выбрали подписку на год. Цена составит 5000 рублей, есть ли у вас промокод?', reply_markup=inline_promo)
        data['Last_message'] = msg.to_python()
        data['buy_type'] = 1
    await Client.buy_year.set()

async def buy(callback_query : types.CallbackQuery, state : FSMContext):
    await callback_query.answer()
    promo_amount = str()
    async with state.proxy() as data:
        promo_amount = data['Promo']
        msg = types.Message.to_object(data['Last_message'])
        await msg.delete_reply_markup()   
        if data['buy_type'] == 0:
            price = types.LabeledPrice(label='Подписка на 1 месяц', amount = int(PRICE_MONTH.amount * (1 - int(promo_amount) / 100)))
            await bot.send_invoice(callback_query.from_user.id,
                                   title='Подписка на месяц',
                                   description='Активация подписки!',
                                   provider_token=PAYMENT_TOKEN,
                                   currency='rub',
                                   is_flexible=False,
                                   prices=[price],
                                   start_parameter='one-month-sub',
                                   payload='test-invoice-payload')
        else:
            price = types.LabeledPrice(label='Подписка на год', amount = int(PRICE_YEAR.amount * (1 - int(promo_amount) / 100)))
            await bot.send_invoice(callback_query.from_user.id,
                                   title='Подписка на год',
                                   description='Активация подписки!',
                                   provider_token=PAYMENT_TOKEN,
                                   currency='rub',
                                   is_flexible=False,
                                   prices=[price],
                                   start_parameter='one-month-sub',
                                   payload='test-invoice-payload')
    await state.finish()
        
async def pre_checkout_query(pre_checkout_q : types.PreCheckoutQuery):
    await bot.answer_pre_checkout_query(pre_checkout_q.id, ok=True)
    
    
async def successful_payment(message : types.Message, state : FSMContext):
    await message.answer(f'Оплата на сумму {message.successful_payment.total_amount // 100} {message.successful_payment.currency} прошла успешно!✅\nВам добавлен месяц подписки на Pride Community!')    
    await sqlite_db.add_user_paid(message.from_user.id)
    await sqlite_db.remove_demo_user(message.from_user.id)
    await state.finish()
    async with state.proxy() as data:
        if 'Main_message' in data.keys():
            msg = types.Message.to_object(data['Main_message'])
            await msg.delete()
        msg = await message.answer(MENU, reply_markup=inline_kb_menu)
        data['Main_message'] = msg.to_python()
    await Menu.menu.set()
      
async def show_profile(callback_query : types.CallbackQuery, state = FSMContext):
    await callback_query.answer()
    await sqlite_db.load_info(callback_query.from_user.id, state)
    values = list(await sqlite_db.get_profile(callback_query.from_user.id))
    age = datetime.datetime.now().year - int(values[10].split('.')[2])
    format = str()
    if values[9]:
        format = 'Онлайн'
    else :
        format = 'Оффлайн'
    card = f'Вот так будет выглядеть твой профиль в сообщении,\
которое мы пришлем твоему собеседнику:\n⏬\n\n{values[2]} из города {values[4]}\nВозраст: {age}\n\nTelegram: {values[1]}\nСоциальная сеть: {values[5]}\n\nЧем занимается: \
{values[6]}\n\nЗацепки для начала разговора: {values[7]}\n\nЦель использования PRIDE CONNECT: {values[11]}\n\nФормат встречи: {format}\nОт встречи ожидает: {values[8]}'        

    async with state.proxy() as data:
        msg = types.Message.to_object(data['Main_message'])   
        await msg.edit_text(card, reply_markup=inline_kb_back_menu)
    await Menu.next()


async def change_profile(callback_query : types.CallbackQuery, state : FSMContext):
    await callback_query.answer()
    async with state.proxy() as data:
        msg = types.Message.to_object(data['Main_message'])
        await msg.edit_text('Выберите пункт, который хотите поменять : ', reply_markup=kb_menuchange)
    await Change.change_start.set()
    await sqlite_db.load_info(callback_query.from_user.id, state)
    # await Menu.next()

async def check_paid(callback_query : types.CallbackQuery, state : FSMContext):
    await callback_query.answer()
    date = await sqlite_db.check_paid(callback_query.from_user.id)
    async with state.proxy() as data:
        if date[0] == 1:
            paid_date = date[1].split('-')
            month_dict = {1 : 'Января', 2 : 'Февраля', 3 : 'Марта', 4 : 'Апреля', 5 : 'Мая',
                          6 : 'Июня', 7 : 'Июля', 8 : 'Августа', 9 : 'Сенятбря', 10 : 'Октября',
                          11 : 'Ноября', 12 : 'Декабря'}    
            msg = types.Message.to_object(data['Main_message'])        
            await msg.edit_text(f'Подписка действует до {paid_date[0]} {month_dict[int(paid_date[1])]} {paid_date[2]} года⏳', reply_markup=inline_kb_back_menu)
        else :
            if date[1] == None:
                msg = types.Message.to_object(data['Main_message'])
                await msg.edit_text('Ваша подписка ещё ни разу не была оплачена, вы можете сделать это в пункте меню "Оплатить подписку"', reply_markup=inline_kb_back_menu)
            else :
                paid_date = date[1].split('-')
                month_dict = {1 : 'Января', 2 : 'Февраля', 3 : 'Марта', 4 : 'Апреля', 5 : 'Мая',
                              6 : 'Июня', 7 : 'Июля', 8 : 'Августа', 9 : 'Сенятбря', 10 : 'Октября',
                              11 : 'Ноября', 12 : 'Декабря'}      
                msg = types.Message.to_object(data['Main_message'])         
                await msg.edit_text(f'Ваша подписка истекла {paid_date[0]} {month_dict[int(paid_date[1])]} {paid_date[2]} года⏳', reply_markup=inline_kb_back_menu)              
        
    await Menu.next()

async def buy_sub(callback_query : types.CallbackQuery, state : FSMContext):
    await callback_query.answer()  
    date = await sqlite_db.check_paid(callback_query.from_user.id)
    async with state.proxy() as data:
        data['Promo'] = 0
        if date[0] == True:
            date_paid = date[1].split('-')
            month_dict = {1 : 'Января', 2 : 'Февраля', 3 : 'Марта', 4 : 'Апреля', 5 : 'Мая',
                          6 : 'Июня', 7 : 'Июля', 8 : 'Августа', 9 : 'Сенятбря', 10 : 'Октября',
                          11 : 'Ноября', 12 : 'Декабря'}     
            msg = types.Message.to_object(data['Main_message'])          
            await msg.edit_text(f'Ваша подписка действует до {date_paid[0]} {month_dict[int(date_paid[1])]} {date_paid[2]} года⏳\nМожете заранее оплатить подписку на месяц вперёд🌟', reply_markup=inline_kb_menu_buy)
        else :
            if date[1] == None:
                msg = types.Message.to_object(data['Main_message'])
                await msg.edit_text('Ваша подписка ещё ни разу не была оплачена, нажмите на кнопку оплатить, чтобы купить месячную подписку', reply_markup=inline_kb_menu_buy)
            else :
                paid_date = date[1].split('-')
                month_dict = {1 : 'Января', 2 : 'Февраля', 3 : 'Марта', 4 : 'Апреля', 5 : 'Мая',
                              6 : 'Июня', 7 : 'Июля', 8 : 'Августа', 9 : 'Сенятбря', 10 : 'Октября',
                              11 : 'Ноября', 12 : 'Декабря'}   
                msg = types.Message.to_object(data['Main_message'])            
                await msg.edit_text(f'Ваша подписка истекла {paid_date[0]} {month_dict[int(paid_date[1])]} {paid_date[2]} года⏳', reply_markup=inline_kb_menu_buy) 
    await Menu_buy.start_pay.set()

async def current_buddy(callback_query : types.CallbackQuery, state : FSMContext):
    await callback_query.answer()
    current = await sqlite_db.current_buddies(callback_query.from_user.id)
    async with state.proxy() as data:
        msg = types.Message.to_object(data['Main_message'])
        await msg.edit_text(current, reply_markup=inline_kb_back_menu)
    await Menu.next()

async def get_new_buddy(callback_query : types.CallbackQuery, state : FSMContext):
    await callback_query.answer()
    async with state.proxy() as data:
        paid_data = await sqlite_db.check_paid(callback_query.from_user.id)
        if paid_data[0] == False:
            msg = types.Message.to_object(data['Main_message'])
            await msg.edit_text("Вы не можете получить дополнительного собеседника, пока не оплатите подписку!", reply_markup=inline_kb_back_menu)
        elif await sqlite_db.try_make_pair(callback_query.from_user.id):
            msg = types.Message.to_object(data['Main_message'])
            await msg.edit_text("Вы успешно занесены в очередь на дополнительную пару✅", reply_markup=inline_kb_back_menu)
        else:
            msg = types.Message.to_object(data['Main_message'])
            await msg.edit_text("У вас уже есть 2 собеседника на эту неделю или истекло время для дополнительной пары - допольнительную пару можно получить только с \
понедельника по среду\nВ понедельник в 10:00 мск вам автоматически подберётся новая пара\n", reply_markup=inline_kb_back_menu)
    await Menu.next()
    
async def get_history(callback_query : types.CallbackQuery, state : FSMContext):
    await callback_query.answer()
    async with state.proxy() as data:
        data['Page_num'] = 0
    async with state.proxy() as data:
        
        await sqlite_db.get_history(callback_query.from_user.id, state)
    await Menu.next()

async def next_history(callback_query: types.CallbackQuery, state : FSMContext):
    await callback_query.answer()
    async with state.proxy() as data:
        data['Page_num'] += 1
    async with state.proxy() as data:
        await sqlite_db.get_history(callback_query.from_user.id, state)
    #     msg = types.Message.to_object(data['Main_message'])
    #     if history != None:
    #         await msg.edit_text(history, reply_markup=kb_history)
    # async with state.proxy() as data:
    #     if cur_page == data['Page_num']:
    #         await msg.edit_reply_markup(kb_only_prev)

async def prev_history(callback_query: types.CallbackQuery, state : FSMContext):
    await callback_query.answer()
    async with state.proxy() as data:
        data['Page_num'] -= 1
    async with state.proxy() as data:
        await sqlite_db.get_history(callback_query.from_user.id, state)
        # msg = types.Message.to_object(data['Main_message'])
        # if history != None:
        #     await msg.edit_text(history, reply_markup=kb_history)
        # if data['Page_num'] <= 0:
        #     await msg.edit_reply_markup(kb_only_next)

async def back_main(callback_query : types.CallbackQuery, state : FSMContext):
    await callback_query.answer()
    async with state.proxy() as data:
        msg = types.Message.to_object(data['Main_message'])
        await msg.edit_text(MENU, reply_markup=inline_kb_menu)
    await Menu.previous()                     
    
async def change_name(callback_query : types.CallbackQuery, state : FSMContext):
    await callback_query.answer()
    async with state.proxy() as data:
        msg = types.Message.to_object(data['Main_message'])
        await msg.edit_text('Напиши свое имя и фамилию?', reply_markup=kb_back_change) 
        data['Change_object'] = 'name'
    await Change.next()
    
async def change_photo(callback_query : types.CallbackQuery, state : FSMContext):
    await callback_query.answer()
    async with state.proxy() as data:
        msg = types.Message.to_object(data['Main_message'])
        await msg.edit_text('Отправьте вашу фотографию', reply_markup=kb_back_change) 
        data['Change_object'] = 'photo'
    await Change.next()
    
async def change_town(callback_query : types.CallbackQuery, state : FSMContext):
    await callback_query.answer()
    async with state.proxy() as data:
        msg = types.Message.to_object(data['Main_message'])
        await msg.edit_text('💣Откуда ты? Напиши название города ответом на это сообщение 🤝🏽\n\n\
✅ Москва, Ростов-на-Дону, Екатеринбург\n\
❌ МСК , Ростов, Екб\n\n\
Мы будем назначать тебе встречи с собеседником выбранным по критериям заполненной тобой анкеты. \
С назначенным нетворкером, вы можете оказаться в разных городах, тогда вам подойдет online формат встречи ⚡️\n\n\
А если же Вы из одного города, то рекомендуем договориться на offline формат, но решение за вами 🙌🏽', reply_markup=kb_back_change) 
        data['Change_object'] = 'town'   
    await Change.next()
        
async def change_social_network(callback_query : types.CallbackQuery, state : FSMContext):
    await callback_query.answer()
    async with state.proxy() as data:
        msg = types.Message.to_object(data['Main_message'])
        await msg.edit_text('Отправь ссылку на свои социальные сети, так собеседник и ты сможете узнать немного больше друг о друге, и ваша встреча пройдёт наиболее эффективно 😉\n\n\
💣Мы рекомендуем отправлять кликабельные ссылки, чтобы было наиболее удобно переходить в ваш профиль 🙂', reply_markup=kb_back_change) 
        data['Change_object'] = 'social_network'
    await Change.next()
            
async def change_work(callback_query : types.CallbackQuery, state : FSMContext):
    await callback_query.answer()
    async with state.proxy() as data:
        msg = types.Message.to_object(data['Main_message'])
        await msg.edit_text('Из какой ты ниши? Чем занимаешься?', reply_markup=kb_back_change) 
        data['Change_object'] = 'work'
    await Change.next()
                    
async def change_hobby(callback_query : types.CallbackQuery, state : FSMContext):
    await callback_query.answer()
    async with state.proxy() as data:
        msg = types.Message.to_object(data['Main_message'])
        await msg.edit_text('Расскажи о сферах твоего интереса, чем увлекаешься как в личном, так и в профессиональном плане?🙌🏽', reply_markup=kb_back_change) 
        data['Change_object'] = 'hooks'                    
    await Change.next()

async def change_expect(callback_query : types.CallbackQuery, state : FSMContext):
    await callback_query.answer()
    async with state.proxy() as data:
        msg = types.Message.to_object(data['Main_message'])
        await msg.edit_text('Выберите соотношение фана и пользы от встречи', reply_markup=inline_kb_expect) 
        data['Change_object'] = 'expect'
    await Change.next()
    
    
async def change_format(callback_query : types.CallbackQuery, state : FSMContext):
    await callback_query.answer()
    async with state.proxy() as data:
        msg = types.Message.to_object(data['Main_message'])
        await msg.edit_text('Выберите формат встреч', reply_markup=inline_kb_change_format)
        data['Change_object'] = 'online'   
    await Change.next()
    
async def change_data(callback_query : types.CallbackQuery, state : FSMContext):
    await callback_query.answer()
    async with state.proxy() as data:
        msg = types.Message.to_object(data['Main_message'])
        await msg.edit_text('📅 Напиши дату своего рождения в формате дд.мм.гггг.', reply_markup=kb_back_change)
        data['Change_object'] = 'data'   
    await Change.next() 
    
async def change_purpose(callback_query : types.CallbackQuery, state : FSMContext):
    await callback_query.answer()
    async with state.proxy() as data:
        msg = types.Message.to_object(data['Main_message'])
        await msg.edit_text('⚡️Для каких запросов используют бот для нетворкинга Pride Connect?\n\n\
 ⁃ Найти новые связи для решения задач по проектам\
 ⁃ Создать коллаборации и партнерства \
 ⁃ Найти подрядчиков в разных нишах\
 ⁃ Познакомиться с интересными людьми со схожими интересами\
 ⁃ Расширить свои возможности и влияние\n\n\
Наш главный оффер нетворкеров - Связи решают ВСЕ и даже больше 💣\n\n\
За каким сейчас вариантом здесь ты? ', reply_markup=kb_purpose)
        data['Change_object'] = 'purpose'   
    await Change.next()    
    
async def change_email(callback_query : types.CallbackQuery, state : FSMContext):
    await callback_query.answer()
    async with state.proxy() as data:
        msg = types.Message.to_object(data['Main_message'])
        await msg.edit_text('Введи свой email, для эффективной работы бота⚡️\n\n\
Так мы сможем уведомлять тебя о новых событиях, если новости станут для тебя неактуальны, ты всегда сможешь отписаться.', reply_markup=kb_back_change)
        data['Change_object'] = 'email'   
    await Change.next()   
                            
async def change_exit(callback_query : types.CallbackQuery, state :  FSMContext):
    await callback_query.answer()
    async with state.proxy() as data:
        msg = types.Message.to_object(data['Main_message'])
        await msg.edit_text(MENU, reply_markup=inline_kb_menu)
    await Menu.previous()
    
async def set_change (message : types.Message, state : FSMContext):
    async with state.proxy() as data:
        if data['Change_object'] == 'photo':
            return
        text = message.text
        await sqlite_db.insert_point(data['Change_object'], message.from_user.id, text)  
        msg = types.Message.to_object(data['Main_message'])
        await msg.edit_text(SUCCSES_CHANGE, reply_markup=kb_menuchange)       
    await message.delete()  
    await Change.previous()
    
async def set_change_photo(message : types.Message, state : FSMContext):
    async with state.proxy() as data:
        if data['Change_object'] != 'photo':
            return
        await sqlite_db.insert_point(data['Change_object'], message.from_user.id, message.photo[0].file_id)  
        msg = types.Message.to_object(data['Main_message'])
        await msg.edit_text(SUCCSES_CHANGE, reply_markup=kb_menuchange)       
    await message.delete()  
    await Change.previous()
    
async def back_change(callback_query : types.CallbackQuery, state : FSMContext):
    await callback_query.answer()
    async with state.proxy() as data:
        msg = types.Message.to_object(data['Main_message'])
        await msg.edit_text(SUCCSES_CHANGE, reply_markup=kb_menuchange) 
    await Change.previous()
    

async def set_change_purpose(callback_query : types.CallbackQuery, state : FSMContext):
    await callback_query.answer()        
    async with state.proxy() as data:
        button_text = callback_query.data
        text = ''
        if button_text == '1_purpose':
            text = 'Найти новые связи для решения задач по проектам'
        elif button_text == '2_purpose':
            text = 'Создать коллаборации и партнерства'
        elif button_text == '3_purpose':
            text = 'Найти подрядчиков в разных нишах'
        elif button_text == '4_purpose':
            text = 'Познакомиться с интересными людьми со схожими интересами'
        elif button_text == '5_purpose':
            text = 'Расширить свои возможности и влияние'
        await sqlite_db.insert_point('purpose', callback_query.from_user.id, text)  
        msg = types.Message.to_object(data['Main_message'])
        await msg.edit_text(SUCCSES_CHANGE, reply_markup=kb_menuchange)           
    await Change.previous()
    
async def set_change_online(callback_query : types.CallbackQuery, state : FSMContext):
    await callback_query.answer()        
    async with state.proxy() as data:
        await sqlite_db.insert_point('online', callback_query.from_user.id, 'true')  
        msg = types.Message.to_object(data['Main_message'])
        await msg.edit_text(SUCCSES_CHANGE, reply_markup=kb_menuchange)           
    await Change.previous()
    
async def set_change_offline(callback_query : types.CallbackQuery, state : FSMContext):
    await callback_query.answer()
    async with state.proxy() as data: 
        await sqlite_db.insert_point('online', callback_query.from_user.id, 'false')           
        msg = types.Message.to_object(data['Main_message'])
        await msg.edit_text(SUCCSES_CHANGE, reply_markup=kb_menuchange)           
    await Change.previous()
    
async def set_change_expect(callback_query : types.CallbackQuery, state : FSMContext):
    await callback_query.answer()
    async with state.proxy() as data:
        data[data['Change_object']] = callback_query.data  
        await sqlite_db.insert_point('expect', callback_query.from_user.id, callback_query.data)           
        msg = types.Message.to_object(data['Main_message'])
        await msg.edit_text(SUCCSES_CHANGE, reply_markup=kb_menuchange)           
    await Change.previous()
              
async def menu_enter_promocode(callback_query : types.CallbackQuery, state : FSMContext):
    await callback_query.answer()
    async with state.proxy() as data:
        msg = types.Message.to_object(data['Main_message'])
        await msg.edit_text('Введите промокод')
    await Menu_buy.get_promocode.set()
        
async def menu_check_promo(message : types.Message, state : FSMContext):
    async with state.proxy() as data:
        data['Promo'] = await sqlite_db.check_promo(message)
        if data['Promo'] == 0:
            msg = types.Message.to_object(data['Main_message'])
            await msg.edit_text('Промокод недействительный')
            msg = await bot.send_message(message.from_user.id, 'Оплата подписки', reply_markup=inline_kb_menu_buy)
            data['Main_message'] = msg.to_python()
            await Menu_buy.next()
            return
        await message.delete()
        if data['Promo'] == 100:
            await sqlite_db.add_user_paid(message.from_user.id)
            await sqlite_db.add_demo_paid(message.from_user.id)
            msg = types.Message.to_object(data['Main_message'])
            await msg.edit_text('Вы ввели уникальный промокод, ваша подписка продлена на месяц!👌')
            msg = await message.answer(MENU, reply_markup=inline_kb_menu)
            data['Main_message'] = msg.to_python()
            await Menu.menu.set()
            return
        promo_amount = data['Promo']
        msg = types.Message.to_object(data['Main_message'])
        await msg.edit_text(f'С учётом вашего промокода цена составит {PRICE_MONTH.amount * (1 - float(promo_amount / 100)) // 100}', reply_markup=inline_kb_menu_buy)  
    await Menu_buy.next()
    
async def menu_buy(callback_query : types.CallbackQuery, state : FSMContext):
    await callback_query.answer()    
    promo_amount = str()
    async with state.proxy() as data:
        msg = types.Message.to_object(data['Main_message'])
        await msg.edit_reply_markup(None)
        promo_amount = data['Promo']
    price = types.LabeledPrice(label='Подписка на 1 месяц', amount = int(PRICE_MONTH.amount * (1 - int(promo_amount) / 100)))
    await bot.send_invoice(callback_query.from_user.id,
                           title='Подписка на месяц',
                           description='Активация подписки!',
                           provider_token=PAYMENT_TOKEN,
                           currency='rub',
                           is_flexible=False,
                           prices=[price],
                           start_parameter='one-month-sub',
                           payload='test-invoice-payload')
                    
async def impress_nice(callback_query: types.CallbackQuery, state : FSMContext):
    await callback_query.answer()
    tg_name = await sqlite_db.find_id_from_tg('@' + callback_query.message.text.split('@')[-1])
    await sqlite_db.make_impress(callback_query.from_user.id, tg_name, 2)
    await callback_query.message.edit_text(f'➡️ {callback_query.message.text}\nВпечатление : Отлично✅', reply_markup=None)
    
async def impress_bad(callback_query: types.CallbackQuery, state : FSMContext):
    await callback_query.answer()
    tg_name = await sqlite_db.find_id_from_tg('@' + callback_query.message.text.split('@')[-1])
    await sqlite_db.make_impress(callback_query.from_user.id, tg_name, 1)
    await callback_query.message.edit_text(f'➡️ {callback_query.message.text}\nВпечатление : Не понравилось🙅‍♂️', reply_markup=None)
        
async def impress_not(callback_query: types.CallbackQuery, state : FSMContext):
    await callback_query.answer()        
    tg_name = await sqlite_db.find_id_from_tg('@' + callback_query.message.text.split('@')[-1])
    await sqlite_db.make_impress(callback_query.from_user.id, tg_name, 0)
    await callback_query.message.edit_text(f'{callback_query.message.text}\n➡️Впечатление : Пока не встретились🔜', reply_markup=None)
       
async def active(callback_query: types.CallbackQuery, state : FSMContext):
    await callback_query.answer()      
    await sqlite_db.write_active(True, callback_query.from_user.id)
    await callback_query.message.edit_text(f'{callback_query.message.text}\n➡️Конечно✅', reply_markup=None)
                        
async def skip(callback_query: types.CallbackQuery, state : FSMContext):
    await callback_query.answer()      
    await sqlite_db.write_active(False, callback_query.from_user.id)
    await callback_query.message.edit_text(f'{callback_query.message.text}\n➡️Пропущу неделю🔜', reply_markup=None)
    
async def restart(message : types.Message, state : FSMContext):
    keyboard = InlineKeyboardMarkup(resize_keyboard=True).row(InlineKeyboardButton(text='Перезапуск', callback_data='restart')).row(
                                                              InlineKeyboardButton(text='Отмена', callback_data='cancel'))
    async with state.proxy() as data:
        msg = await message.answer('Вы действительно хотите перезаполнить анкету?\nМожете не беспокоиться за вашу оплату, она сохраняется в базе!', reply_markup=keyboard)
        data['Restart_message'] = msg.to_python()
    await message.delete()
  
async def at_start(callback_query: types.CallbackQuery, state : FSMContext):
    await callback_query.answer()
    async with state.proxy() as data:
        msg = types.Message.to_object(data['Restart_message'])
        await msg.delete()
        try:
            msg = types.Message.to_object(data['Last_message'])
            await msg.delete_reply_markup()
        except:
            pass
        try:
            msg = types.Message.to_object(data['Main_message'])
            await msg.delete_reply_markup()
        except:
            pass
        await bot.send_message(callback_query.from_user.id, DESCRIBE_WORK)
        video = open('./content/videos/vid1.mp4', 'rb')
        msg = await bot.send_video(callback_query.from_user.id, video, reply_markup=thx_next)
        data['Last_message'] = msg.to_python()
    await Client.name.set()
    
async def cancel(callback_query: types.CallbackQuery, state : FSMContext):
    await callback_query.answer()
    async with state.proxy() as data:
        msg = types.Message.to_object(data['Restart_message'])
        await msg.delete()

async def unknown(message : types.Message):
    await message.answer('Неизвестная команда!\nДля навигации в боте импользуйте Меню.\n\
Введите команду /help если у вас возникли проблемы с ботом')

def register_handlers_client(dp : Dispatcher):
    dp.register_callback_query_handler(next_step, Text(equals='next', ignore_case=True), state='*')
    dp.register_callback_query_handler(back, Text(equals='back_mes', ignore_case=True), state=Client.all_states)
    
    dp.register_message_handler(start, Text(equals='/start', ignore_case=True), state='*') 
    dp.register_message_handler(menu, Text(equals='/menu', ignore_case=True), state='*') 
    dp.register_message_handler(help, Text(equals='/help', ignore_case=True), state='*') 
    dp.register_message_handler(restart, Text(equals='/restart', ignore_case=True), state='*') 
    dp.register_callback_query_handler(at_start, Text(equals='restart', ignore_case=True), state='*')
    dp.register_callback_query_handler(cancel, Text(equals='cancel', ignore_case=True), state='*')
    
    dp.register_callback_query_handler(start_ask, Text(equals='thx_next', ignore_case=True), state='*')
    
    dp.register_message_handler(get_name, state=Client.name)
    
    dp.register_message_handler(get_photo, content_types=['photo'], state=Client.photo)
    
    dp.register_callback_query_handler(accept, Text(equals='accept', ignore_case=True), state='*')
    dp.register_callback_query_handler(other, Text(equals='other', ignore_case=True), state='*')
    
    dp.register_callback_query_handler(check_username, Text(equals='check_username', ignore_case=True), state='*')
    
    dp.register_message_handler(get_town, state=Client.town)
    dp.register_callback_query_handler(maybe_town, Text(equals='maybe_town', ignore_case=True), state=Client.town)
    dp.register_callback_query_handler(enter_town, Text(equals='enter_town', ignore_case=True), state=Client.town)
    dp.register_callback_query_handler(again_town, Text(equals='again_town', ignore_case=True), state=Client.town)
    
    dp.register_message_handler(get_social_network, state=Client.social_network)
    
    dp.register_message_handler(get_work, state=Client.work)
    
    dp.register_message_handler(get_hooks, state=Client.hooks)
    
    dp.register_callback_query_handler(get_expect, Text(equals='100% польза', ignore_case=True), state=Client.expect)
    dp.register_callback_query_handler(get_expect, Text(equals='70% польза - 30% фан', ignore_case=True), state=Client.expect)
    dp.register_callback_query_handler(get_expect, Text(equals='50% польза - 50% фан', ignore_case=True), state=Client.expect)
    dp.register_callback_query_handler(get_expect, Text(equals='30% польза - 70% фан', ignore_case=True), state=Client.expect)
    dp.register_callback_query_handler(get_expect, Text(equals='100% фан', ignore_case=True), state=Client.expect)
    
    dp.register_callback_query_handler(online, Text(equals='online', ignore_case=True), state=Client.format)
    dp.register_callback_query_handler(offline, Text(equals='offline', ignore_case=True), state=Client.format)
    
    dp.register_message_handler(get_data, state=Client.born)
    
    dp.register_callback_query_handler(get_purpose1, Text(equals='1_purpose', ignore_case=True), state=Client.purpose)
    dp.register_callback_query_handler(get_purpose2, Text(equals='2_purpose', ignore_case=True), state=Client.purpose)
    dp.register_callback_query_handler(get_purpose3, Text(equals='3_purpose', ignore_case=True), state=Client.purpose)
    dp.register_callback_query_handler(get_purpose4, Text(equals='4_purpose', ignore_case=True), state=Client.purpose)
    dp.register_callback_query_handler(get_purpose5, Text(equals='5_purpose', ignore_case=True), state=Client.purpose)
    
    dp.register_callback_query_handler(get_male, Text(equals='male', ignore_case=True), state=Client.gender)
    dp.register_callback_query_handler(get_female, Text(equals='female', ignore_case=True), state=Client.gender)
    
    dp.register_message_handler(get_email, state=Client.email)

    dp.register_callback_query_handler(succses, Text(equals='succses', ignore_case=True), state='*')
    dp.register_callback_query_handler(fill_again, Text(equals='fill_again', ignore_case=True), state='*')

    # payment
    dp.register_message_handler(check_promo, state=Client.get_promocode)
    dp.register_callback_query_handler(enter_promocode, Text(equals='promocode', ignore_case=True), state='*')
    dp.register_callback_query_handler(buy, Text(equals='buy', ignore_case=True), state='*')
    dp.register_callback_query_handler(buy_month, Text(equals='buy_month', ignore_case=True), state='*')
    dp.register_callback_query_handler(buy_year, Text(equals='buy_year', ignore_case=True), state='*')
    dp.register_callback_query_handler(buy_later, Text(equals='buy_later', ignore_case=True), state='*')
    dp.register_pre_checkout_query_handler(pre_checkout_query, lambda query : True, state='*')
    dp.register_message_handler(successful_payment, content_types=[ContentType.SUCCESSFUL_PAYMENT], state='*')    
    
    # menu
    dp.register_callback_query_handler(show_profile, Text(equals='show_profile', ignore_case=True), state=Menu.menu)
    dp.register_callback_query_handler(change_profile, Text(equals='change_profile', ignore_case=True), state=Menu.menu)
    dp.register_callback_query_handler(check_paid, Text(equals='check_paid', ignore_case=True), state=Menu.menu)
    dp.register_callback_query_handler(buy_sub, Text(equals='buy_sub', ignore_case=True), state=Menu.menu)
    dp.register_callback_query_handler(current_buddy, Text(equals='current_buddy', ignore_case=True), state=Menu.menu)
    dp.register_callback_query_handler(get_new_buddy, Text(equals='get_new_buddy', ignore_case=True), state=Menu.menu)

    dp.register_callback_query_handler(get_history, Text(equals='get_history', ignore_case=True), state=Menu.menu)
    dp.register_callback_query_handler(next_history, Text(equals='next_history', ignore_case=True), state=Menu.menu_point)
    dp.register_callback_query_handler(prev_history, Text(equals='prev_history', ignore_case=True), state=Menu.menu_point)
    
    dp.register_callback_query_handler(back_main, Text(equals='back_main', ignore_case=True), state='*')
    
    # change menu profile
    dp.register_callback_query_handler(change_name, Text(equals='change_name', ignore_case=True), state=Change.change_start)
    
    dp.register_callback_query_handler(change_photo, Text(equals='change_photo', ignore_case=True), state=Change.change_start)
    
    dp.register_callback_query_handler(change_town, Text(equals='change_town', ignore_case=True), state=Change.change_start)
    
    dp.register_callback_query_handler(change_social_network, Text(equals='change_social_network', ignore_case=True), state=Change.change_start)
    
    dp.register_callback_query_handler(change_work, Text(equals='change_work', ignore_case=True), state=Change.change_start)
    
    dp.register_callback_query_handler(change_hobby, Text(equals='change_hobby', ignore_case=True), state=Change.change_start)
    
    dp.register_callback_query_handler(change_expect, Text(equals='change_expect', ignore_case=True), state=Change.change_start)
    dp.register_callback_query_handler(set_change_expect, Text(equals='100% польза', ignore_case=True), state=Change.change_state)
    dp.register_callback_query_handler(set_change_expect, Text(equals='70% польза - 30% фан', ignore_case=True), state=Change.change_state)
    dp.register_callback_query_handler(set_change_expect, Text(equals='50% польза - 50% фан', ignore_case=True), state=Change.change_state)
    dp.register_callback_query_handler(set_change_expect, Text(equals='30% польза - 70% фан', ignore_case=True), state=Change.change_state)
    dp.register_callback_query_handler(set_change_expect, Text(equals='100% фан', ignore_case=True), state=Change.change_state)
    
    dp.register_callback_query_handler(change_format, Text(equals='change_format', ignore_case=True), state=Change.change_start)
    dp.register_callback_query_handler(set_change_offline, Text(equals='offline', ignore_case=True), state=Change.change_state)
    dp.register_callback_query_handler(set_change_online, Text(equals='online', ignore_case=True), state=Change.change_state)
    
    dp.register_callback_query_handler(change_data, Text(equals='change_data', ignore_case=True), state=Change.change_start) 
    
    dp.register_callback_query_handler(change_purpose, Text(equals='change_purpose', ignore_case=True), state=Change.change_start) 
    dp.register_callback_query_handler(set_change_purpose, Text(equals='1_purpose', ignore_case=True), state=Change.change_state)
    dp.register_callback_query_handler(set_change_purpose, Text(equals='2_purpose', ignore_case=True), state=Change.change_state)
    dp.register_callback_query_handler(set_change_purpose, Text(equals='3_purpose', ignore_case=True), state=Change.change_state)
    dp.register_callback_query_handler(set_change_purpose, Text(equals='4_purpose', ignore_case=True), state=Change.change_state)
    dp.register_callback_query_handler(set_change_purpose, Text(equals='5_purpose', ignore_case=True), state=Change.change_state)    
    
    dp.register_callback_query_handler(change_email, Text(equals='change_email', ignore_case=True), state=Change.change_start)    
    
    dp.register_message_handler(set_change, content_types=ContentType.TEXT, state=Change.change_state)
    
    dp.register_message_handler(set_change_photo, content_types=ContentType.PHOTO, state=Change.change_state)
    
    dp.register_callback_query_handler(back_change, Text(equals='back_mes', ignore_case=True), state='*')   
    
    dp.register_callback_query_handler(change_exit, Text(equals='change_exit', ignore_case=True), state=Change.change_start)
    
    
    #payment from menu
    dp.register_callback_query_handler(menu_enter_promocode, Text(equals='menu_promocode', ignore_case=True), state='*')
    dp.register_message_handler(menu_check_promo, state=Menu_buy.get_promocode)
    dp.register_callback_query_handler(menu_buy, Text(equals='menu_buy', ignore_case=True), state=Menu_buy.start_pay)
      
    #ask_impress
    dp.register_callback_query_handler(impress_nice, Text(equals='nice', ignore_case=True), state='*')
    dp.register_callback_query_handler(impress_bad, Text(equals='bad', ignore_case=True), state='*')
    dp.register_callback_query_handler(impress_not, Text(equals='not_meet', ignore_case=True), state='*')
    
    #ask_active
    dp.register_callback_query_handler(active, Text(equals='active_user', ignore_case=True), state='*')
    dp.register_callback_query_handler(skip, Text(equals='skip_week', ignore_case=True), state='*')

    dp.register_message_handler(unknown, state='*')