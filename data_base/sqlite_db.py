import sqlite3 as sq
from aiogram import types
from create_bot import bot
from aiogram.dispatcher import FSMContext
import psycopg2 as ps
import datetime, calendar, os
from urllib.parse import urlparse
from aiogram.dispatcher.webhook import SendMessage

def start_sql():
    global base, cursor
    result = urlparse(os.environ.get('DATABASE_URL'))
    username = result.username
    password = result.password
    database = result.path[1:]
    hostname = result.hostname
    port = result.port
    base = ps.connect(
        port=port,
        host=hostname,
        user=username,
        password=password,
        database=database
    )
    cursor = base.cursor()
    if base:
        print('Data base connected') 
    cursor.execute('CREATE TABLE IF NOT EXISTS users(id BIGINT PRIMARY KEY,\
    tg TEXT, name TEXT, photo TEXT, town TEXT, social_network TEXT, work TEXT,\
    hooks TEXT, expect TEXT, online BOOL, born_date TEXT, purpose TEXT, gender TEXT,\
    email TEXT, is_sub_active BOOL, date_out_active TEXT, last_pairs BIGINT[], all_pairs BIGINT[], impress_of_meet INT[], active BOOL)')
    base.commit()
    
    cursor.execute('CREATE TABLE IF NOT EXISTS promo(code TEXT PRIMARY KEY, amount INT, count INT, active_id BIGINT[])')
    base.commit()  
    
    cursor.execute('CREATE TABLE IF NOT EXISTS temp_users(user_id BIGINT)')
    base.commit()
    
    cursor.execute('CREATE TABLE IF NOT EXISTS demo_users(user_id BIGINT)')
    base.commit()

async def close_db():
    base.close()
    
async def check_promo(message : types.Message):
    cursor.execute('SELECT * FROM promo WHERE code = %s', (message.text, ))
    promo = cursor.fetchone()
    if promo == None:
        await message.answer('Введённый промокод не найден!')  
        return 0
    if promo[2] < 1:
        await message.answer('Введённый промокод закончился!')
        cursor.execute('DELETE FROM promo WHERE code = %s', (promo[0], ))
        base.commit()
        return 0
    for id in promo[3]:
        if id == message.from_user.id:
            await message.answer('Вы уже активировали этот промокод ранее!')
            return 0
    
    cursor.execute('UPDATE promo SET count = %s, active_id = array_append(active_id, %s) WHERE code = %s', (promo[2] - 1, message.from_user.id, promo[0]))
    base.commit()
    await message.answer(f'Размер скидки введённого промокода равен {promo[1]}%!')
    return promo[1]

async def insert_promo(message : types.Message):
    array_values = message.text.split(' ')
    array_values.append('{ }')
    if len(array_values) != 4 or int(array_values[1]) > 100 or int(array_values[1]) < 1:
        return 'Промокод введён некорректно!'
        return
    cursor.execute('SELECT code FROM promo')
    codes = []
    promo = cursor.fetchall()
    for code in promo:
        codes.append(code[0])
    if array_values[0] in codes:
        return 'Промокод был добавлен ранее!'
    else:
        cursor.execute('INSERT INTO promo VALUES (%s, %s, %s, %s)', array_values)
        base.commit()
        return  'Промокод успешно добавлен!'
    
async def remove_promo(message : types.Message):    
    cursor.execute('SELECT * FROM promo WHERE code = %s', (message.text, ))
    if cursor.fetchone() == None:
        return 'Удаляемый промокод не найден'
    cursor.execute('DELETE FROM promo WHERE code = %s', (message.text, ))
    base.commit()
    return 'Промокод успешно удалён!'

async def insert_sql(state : FSMContext):
    user_data = list()
    async with state.proxy() as data:
        user_data.append(data['id'])
        user_data.append(data['Телеграм'])
        user_data.append(data['Имя'])
        user_data.append(data['Фото'])
        user_data.append(data['Город'])
        user_data.append(data['Социальные сети'])    
        user_data.append(data['Работа'])
        user_data.append(data['Зацепки'])
        user_data.append(data['Ожидания'])
        user_data.append(data['Формат'])
        user_data.append(data['Дата'])
        user_data.append(data['Цель'])
        user_data.append(data['Гендер'])
        user_data.append(data['Email'])
        user_data.append(data['Оплачено'])
        user_data.append(data['Дата_окончания_подписки'])
        user_data.append('{ }')
        user_data.append('{ }')
        user_data.append('{ }')
        user_data.append('true')
        
    cursor.execute('SELECT * FROM users WHERE id = %s', (user_data[0], ))
    user = cursor.fetchone()
    if user != None:
        print(user_data)
        if user[14] == True:
            print(user[14])
            user_data[14] = 'true'
            user_data[15] = user[15]
        user_data[16] = user[16]
        user_data[17] = user[17]
        user_data[18] = user[18]
        cursor.execute('DELETE FROM users WHERE id = %s', (user[0], ))
        base.commit()
    cursor.execute('INSERT INTO users VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)', tuple(user_data))
    base.commit()
    
async def insert_point(column : str, id : int, text : str):
    if column == 'name':
        cursor.execute('UPDATE users SET name = %s WHERE id = %s', (text, id))
    elif column == 'photo':
        cursor.execute('UPDATE users SET photo = %s WHERE id = %s', (text, id))
    elif column == 'town':
        cursor.execute('UPDATE users SET town = %s WHERE id = %s', (text, id))
    elif column == 'social_network':
        cursor.execute('UPDATE users SET social_network = %s WHERE id = %s', (text, id))
    elif column == 'work':
        cursor.execute('UPDATE users SET work = %s WHERE id = %s', (text, id))
    elif column == 'hooks':
        cursor.execute('UPDATE users SET hooks = %s WHERE id = %s', (text, id))
    elif column == 'expect':
        cursor.execute('UPDATE users SET expect = %s WHERE id = %s', (text, id))
    elif column == 'online':
        cursor.execute('UPDATE users SET online = %s WHERE id = %s', (text, id))
    elif column == 'data':
        cursor.execute('UPDATE users SET born_date = %s WHERE id = %s', (text, id))
    elif column == 'purpose':
        cursor.execute('UPDATE users SET purpose = %s WHERE id = %s', (text, id))
    elif column == 'email':
        cursor.execute('UPDATE users SET email = %s WHERE id = %s', (text, id))
    base.commit()
        
async def remove_sql(text):
    cursor.execute('DELETE FROM users WHERE tg = %s', (text, ))
    base.commit()    
    
async def show_sql(user_id):
    try:
        cursor.execute('SELECT * FROM users WHERE id = %s', (user_id, ))
        data = cursor.fetchone()
        await bot.send_message(user_id, f'Телеграм : {data[1]}\n\
Имя : {data[2]}\nГород : {data[3]}\nСоциальные сети : \n{data[4]}\n\
Работа/увлечения : {data[5]}\nИнтересы/хобби : {data[6]}\nОжидания от встречи: {data[7]}\n')
    except:
        await bot.send_message(user_id, 'Ваша анкета удалена или ещё не заполнена!')
        
async def read_sql(id):
    cursor.execute('SELECT * FROM users')
    for data in cursor.fetchall():
        await bot.send_message(id, f'id : {data[0]}\nТелеграм : {data[1]}\n\
Имя : {data[2]}\nГород : {data[3]}\nСоциальные сети : {data[4]}\
\nРабота/увлечения : {data[5]}\nИнтересы/хобби : {data[6]}\nОжидания от встречи: {data[7]}\n')
    
async def send_message(message : types.Message):
    cursor.execute('SELECT id FROM users')
    users_id = cursor.fetchall()
    counter = 0
    num = 0
    for id in users_id:
        num += 1
        try:
            # await bot.send_message(555581588, message.text)
            # await bot.send_message(id[0], message.text)
            counter += 1
        except:
            print(f'Я в блоке {num}')
    return counter
async def load_info(id, state : FSMContext):
    cursor.execute('SELECT * FROM users WHERE id = %s', (id, ))
    user = cursor.fetchone()
    async with state.proxy() as data:
        data['id'] = user[0]
        data['Телеграм'] = user[1]
        data['Имя'] = user[2] 
        data['Город'] = user[4]
        data['Социальные сети'] = user[5] 
        data['Работа'] = user[6]
        data['Зацепки'] = user[7]
        data['Ожидания'] = user[8]
        data['Формат'] = user[9]
        data['Оплачено'] = user[10]
        data['Дата_окончания_подписки'] = user[11]
        
async def count():
    cursor.execute('SELECT id, town FROM users')
    users = cursor.fetchall()
    return len(users)     
        
async def count_for_town():
    cursor.execute('SELECT id, town FROM users')
    users = cursor.fetchall()
    count_town = dict()
    for user in users:
        if count_town.get(user[1]) is None:
            count_town[user[1]] = 1
        else:
            count_town[user[1]] += 1
    users_town = str()
    for town in count_town:
        users_town += f'{town} : {count_town.get(town)}\n'        
    return users_town  
        
async def is_register(id):
    try:
        cursor.execute('SELECT * FROM users WHERE id = %s', (id, ))
        user = cursor.fetchone()
        if len(user) != 0:
            return True
        return False
    except:
        return False
    
async def count_paid_subs():
    cursor.execute('SELECT id FROM users WHERE is_sub_active = %s', ((True), ))
    return len(cursor.fetchall()) - await count_demo_subs()
    
async def add_user_paid(id):
    try:
        cursor.execute('SELECT * FROM users WHERE id = %s', (id, ))
        user = cursor.fetchone()
        if user[14] == True:
            mas_date = user[15].split('-')
            date = datetime.date(int(mas_date[2]), int(mas_date[1]), int(mas_date[0]))
            days_month = calendar.monthrange(int(mas_date[0]), int(mas_date[1]))[1]
            date += datetime.timedelta(days=days_month)
            str_date = str(date.day) + '-' + str(date.month) + '-' + str(date.year)
        else:
            date = datetime.datetime.now().date()
            days_month = calendar.monthrange(date.year, date.month)[1]
            date += datetime.timedelta(days=days_month)
            str_date = str(date.day) + '-' + str(date.month) + '-' + str(date.year)

        cursor.execute('UPDATE users SET is_sub_active = %s, date_out_active = %s WHERE id = %s', (True, str_date, id))
        base.commit()
        await bot.send_message(id, 'Данные об оплате успешно записаны!')
    except Exception as ex:
        print(ex)
        await bot.send_message(id, 'Не удалось записать данные об оплате!')
 
 
async def check_paid(id):
    cursor.execute('SELECT is_sub_active, date_out_active FROM users WHERE id = %s', (id,))
    return cursor.fetchone()

async def get_offline_users():
    cursor.execute("SELECT id, town FROM users WHERE online = %s and is_sub_active = %s and active = %s", (False, True, True))
    offline = cursor.fetchall()
    if offline == None:
        return list()
    return offline

async def get_online_users():
    cursor.execute("SELECT id, town FROM users WHERE online = %s and is_sub_active = %s and active = %s", (True, True, True))
    online = cursor.fetchall()
    if online == None:
        return list()
    return online

async def get_hooks(id):
    cursor.execute('SELECT hooks FROM users WHERE id = %s', (id, ))
    return cursor.fetchone()[0]

async def get_profile(id):
    cursor.execute('SELECT * FROM users WHERE id = %s', (id, ))
    return cursor.fetchone()

async def append_pair(user1, user2):
    cursor.execute('UPDATE users SET last_pairs = array_append(last_pairs, %s), all_pairs = array_append(all_pairs, %s), impress_of_meet = array_append(impress_of_meet, %s) WHERE id = %s', (user2, user2, 0, user1))
    cursor.execute('UPDATE users SET last_pairs = array_append(last_pairs, %s), all_pairs = array_append(all_pairs, %s), impress_of_meet = array_append(impress_of_meet, %s) WHERE id = %s', (user1, user1, 0, user2))
    base.commit()
    
async def is_last_pair(id, pair_id):
    cursor.execute('SELECT all_pairs FROM users WHERE id = %s', (id, ))
    last_id = cursor.fetchone()
    if last_id == None:
        return False
    if pair_id in list(last_id[0]):
        return True
    else:
        return False
    
async def find_users_without_pair():
    cursor.execute('SELECT id FROM users WHERE array_upper(last_pairs, 1) is null and active = true')
    users = cursor.fetchall()
    if users == None:
        return []
    users_id = []
    for user in users:
        users_id.append(user[0])
    return users_id

async def make_impress(user_id, pair_id, num_impress):
    cursor.execute('SELECT all_pairs FROM users WHERE id = %s', (user_id, ))
    id_list = cursor.fetchone()
    if id_list == None:
        return
    id_list = id_list[0]
    counter = 0
    for counter in range(len(id_list)):
        if pair_id == id_list[counter]:
            break
    if counter == len(id_list):
        # print('Пара не найдена в списке')
        return
    cursor.execute('UPDATE users SET impress_of_meet[%s] = %s WHERE id = %s', (counter + 1, num_impress, user_id))
    base.commit()
    
async def delete_current_pairs():
    brackets = '{ }'
    cursor.execute('UPDATE users SET last_pairs = %s', (brackets, ))
    base.commit()
    
async def get_history(id):
    cursor.execute('SELECT all_pairs, impress_of_meet FROM users WHERE id = %s', (id, ))
    data = cursor.fetchone()
    if data[0] == None or len(data[0]) == 0:
        return 'У вас ещё не было ни одной встречи'
    
    history_string = str()
    counter = 0
    for user_pair in data[0]:
        user = await get_profile(user_pair)
        impress = str()
        if len(data[1]) > counter:
            if data[1][counter] == 2:
                impress = 'Отлично✅'
            elif data[1][counter] == 1:
                impress = 'Не понравилось🙅‍♂️'
            else:
                impress = 'Отсутствует'
        else:
            impress = 'Отсутствует'
        history_string += f'{user[2]} из города {user[4]}\nВпечатление от встречи : {impress}\nTelegram : {user[1]}\n\n'
        counter += 1
    return history_string

async def current_buddies(id):
    cursor.execute('SELECT last_pairs FROM users WHERE id = %s', (id, ))
    current_pair_id = cursor.fetchone()
    if current_pair_id == None or len(current_pair_id[0]) == 0:
        return 'У вас нет пары на текущую неделю, дождитесь воскресенья, или нажмите на кнопку \'Новый собеседник\''
    pairs_info = str()
    count = 1
    for user_pair in current_pair_id[0]:
        pairs_info += f'Cобеседник №{str(count)} :\n'
        user = await get_profile(user_pair)
        if user[8]:
            format = 'Онлайн'
        else:
            format = 'Оффлайн'
        pairs_info += f'{user[2]}({user[4]})\n\nСвязь:\nTelegram: {user[1]}\n{user[5]}\n\nЧем занимается: \
{user[6]}\n\nЗацепки для начала разговора: {user[7]}\n\nОт встречи ожидает: {user[8]}\nФормат встречи: {format}\n\n'  
        count += 1
        
    return pairs_info

async def get_users():
    cursor.execute('SELECT id, last_pairs, impress_of_meet FROM users WHERE is_sub_active = true and active = true')
    return cursor.fetchall()
        
async def find_id_from_tg(tg):
    cursor.execute('SELECT id FROM users WHERE tg = %s', (tg, ))
    return cursor.fetchone()[0]
        
async def try_make_pair(id):
    cursor.execute("SELECT last_pairs FROM users WHERE id = %s", (id, ))
    last_pairs = cursor.fetchone()[0]
    if len(last_pairs) < 2:
        cursor.execute('SELECT user_id FROM temp_users')
        user_array = cursor.fetchall()
        users = []
        for user in user_array:
            users.append(user[0])
        if id not in users:
            cursor.execute('INSERT INTO temp_users VALUES(%s)', (id, ))
            base.commit()
        return True
    else:
        return False
    
async def get_extra_users():
    cursor.execute('SELECT user_id FROM temp_users')
    users = cursor.fetchall()
    if users == None:
        return []
    all_id = []
    for user in users:
        all_id.append(user[0])
        
    return all_id

async def delete_from_temp_users(id):
    cursor.execute('DELETE FROM temp_users WHERE user_id = %s', (id, ))
    base.commit()

async def clear_temp_users():
    cursor.execute('DELETE from temp_users')
    base.commit()
    
async def active_users():
    cursor.execute('SELECT * FROM users WHERE active = true')
    return len(cursor.fetchall())
        
async def get_paid_users():
    cursor.execute('SELECT id FROM users where is_sub_active = true')
    id_list = []
    users = cursor.fetchall()
    if users == None:
        return []
    for user in users:
        id_list.append(user[0])
    return id_list

async def write_active(active : bool, id : int):
    cursor.execute('UPDATE users SET active = %s WHERE id = %s', (active, id))
    base.commit()

async def get_promocodes():
    cursor.execute('SELECT * FROM promo')
    promocodes = cursor.fetchall()
    if promocodes == None:
        return []
    return promocodes
    
async def remove_active(id : int):
    cursor.execute('UPDATE users SET is_sub_active = false WHERE id = %s', (id, ))
    base.commit()
    
async def update():
    cursor.execute('SELECT id, date_out_active FROM users WHERE is_sub_active = true')
    paid_users = cursor.fetchall()
    present = datetime.datetime.now().date()
    counter = 0
    for user in paid_users:
        mas_date = user[1].split('-')
        date_out = datetime.date(int(mas_date[2]), int(mas_date[1]), int(mas_date[0]))
        if date_out < present:
            counter += 1
            await remove_active(user[0])
            await bot.send_message(user[0], 'Ваша подписка истекла, чтобы дальше продолжать подбор собеседников совершите оплату')
    return counter
    
    
async def add_demo_paid(id : int):
    cursor.execute('SELECT * FROM demo_users')
    users = cursor.fetchall()
    for user in users:
        if user[0] == id:
            return
    cursor.execute('INSERT INTO demo_users VALUES(%s)', (id, ))
    base.commit()

async def remove_demo_user(id : int):
    cursor.execute('SELECT * FROM demo_users WHERE user_id = %s', (id, ))
    
    user = cursor.fetchone()
    if user == None:
        return
    cursor.execute('DELETE FROM demo_users WHERE user_id = %s', (id, ))
    base.commit()
    
async def count_demo_subs():
    cursor.execute('SELECT * FROM demo_users')
    return len(cursor.fetchall())

async def get_photo(id):
    cursor.execute('SELECT photo FROM users WHERE id = %s', (id, ))
    return cursor.fetchone()[0]

async def check_block():
    cursor.execute('SELECT id FROM users WHERE is_sub_active = true')
    users = cursor.fetchall()
    
    text = ''
    for user in users:
        try:
            await bot.send_chat_action(user[0], types.ChatActions.TYPING)
            # await bot.send_chat_action(user[0], None)      
        except:
            text += f'юзер {user[0]} в блоке'
            cursor.execute('UPDATE users SET active = false WHERE id = %s', (user[0], ))
            base.commit()
            
    await bot.send_message(555581588, text)