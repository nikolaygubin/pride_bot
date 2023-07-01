from create_bot import dp
from data_base import sqlite_db
from keyboards import inline_kb_impress, inline_kb_active
import difflib
import datetime
from aiogram.types import  InlineKeyboardButton, InlineKeyboardMarkup

def similarity(s1, s2):
  normalized1 = s1.lower()
  normalized2 = s2.lower()
  matcher = difflib.SequenceMatcher(None, normalized1, normalized2)
  return matcher.ratio()

async def send_invoice_message(user_id, send_id):
    values = list(await sqlite_db.get_profile(user_id))
    age = datetime.datetime.now().year - int(values[10].split('.')[2])
    format = str()
    if values[9]:
        format = 'Онлайн'
    else :
        format = 'Оффлайн'
    card = f'Поздравляем! Вам нашёлся собеседник, спишитесь с ним в удобной для вас соцсети, приятного общения🤝\n⏬\n\n{values[2]} из города {values[4]}\nВозраст: {age}\n\nTelegram: {values[1]}\nСоциальная сеть: {values[5]}\n\nЧем занимается: \
{values[6]}\n\nЗацепки для начала разговора: {values[7]}\n\nЦель использования PRIDE CONNECT: {values[11]}\n\nФормат встречи: {format}\nОт встречи ожидает: {values[8]}'      
    try:
        inline_keyboard = InlineKeyboardMarkup(resize_keyboard=True).row(InlineKeyboardButton(text=f'Написать {values[2]}', url='https://t.me/' + values[1][1::]))
        # await dp.bot.send_message(send_id, text + 'Вот твой собеседник, напиши сразу, чтобы не забыть:\n⏬\n\n' + card, reply_markup=inline_keyboard)
        await dp.bot.send_photo(send_id, photo=await sqlite_db.get_photo(user_id), caption=card, reply_markup=inline_keyboard)
        photo = open('./content/photo/right.jpeg', 'rb')
        await dp.bot.send_photo(send_id, photo=photo)
    except:
        print('Я в блоке')
    
async def make_pairs():
    try:
        # await sqlite_db.check_block()
        await sqlite_db.clear_temp_users()
        await sqlite_db.delete_current_pairs()
        offline_users = await sqlite_db.get_offline_users() # получаем всех оффлайн пользователей (id + town)
        online_users = await sqlite_db.get_online_users() # получаем всех онлайн пользователей (только id)
        dict_pairs = dict(str()) # словарь со всеми парами

        offline_dict = {} # инициализируем словарь и заносим туда всех оффлайн пользователей по городам
        for user in offline_users: 
            town = user[1].lower()
            if offline_dict.get(town) == None:
                offline_dict[town] = list()
            offline_dict[town].append(user[0])

        for town in offline_dict.keys(): # проходимся по всем городам и пытаемся сформировать пары
            town_id = list(offline_dict[town]) # иницализируем массив с пользователями в городе town
            for id in range(len(town_id)): # пытаемся подобрать пару каждому пользователю
                max_sim = -1    # максимальная схожесть
                max_index = id  # индекс с максимальной схожестью (по умолчанию ссылается на самого себя)
                for pair_id in range(len(town_id)):
                    if town_id[id] in dict_pairs.values():
                        break
                    if id == pair_id or town_id[pair_id] in dict_pairs.keys() or town_id[pair_id] in dict_pairs.values() or await sqlite_db.is_last_pair(town_id[id], town_id[pair_id]):
                        continue   
                    s1 = await sqlite_db.get_hooks(town_id[id])
                    s2 = await sqlite_db.get_hooks(town_id[pair_id])
                    sim = similarity(s1, s2) # процент схожести 2 строк 
                    if sim > max_sim:
                        max_index = pair_id
                        max_sim = sim
                if max_index != id:
                    dict_pairs[town_id[id]] = town_id[max_index]
                    await sqlite_db.append_pair(town_id[id], town_id[max_index]) # добавляем пары в базу данных
                    offline_dict[town].remove(town_id[id])
                    offline_dict[town].remove(town_id[max_index])

        online_id = list() # создаём список и добавляем туда все онлайн id
        for town in offline_dict.keys():
            users = offline_dict[town]
            for user in users:
                online_id.append(user)

        for user in online_users:
            online_id.append(user[0])

        for id in range(len(online_id)):
            max_sim = -1
            max_index = id
            for pair_id in range(len(online_id)):
                if online_id[id] in dict_pairs.values():
                    break
                if id == pair_id or online_id[pair_id] in dict_pairs.keys() or online_id[pair_id] in dict_pairs.values() or await sqlite_db.is_last_pair(online_id[id], online_id[pair_id]):
                    continue     
                s1 = await sqlite_db.get_hooks(online_id[id])
                s2 = await sqlite_db.get_hooks(online_id[pair_id])
                sim = similarity(s1, s2)
                if sim > max_sim:
                    max_index = pair_id
                    max_sim = sim
            if max_index != id:
                dict_pairs[online_id[id]] = online_id[max_index]
                await sqlite_db.append_pair(online_id[id], online_id[max_index])

        extra_pairs = 0
        if len(dict_pairs) * 2 != len(offline_users) + len(online_users):
            users_without_pair = await sqlite_db.find_users_without_pair()
            if users_without_pair == None:
                extra_pairs = 0
            else:
                for id in users_without_pair:
                    await sqlite_db.try_make_pair(id)
                    try:
                        await dp.bot.send_message(id, 'К сожалению на этой неделе вам не удалось подобрать пару сразу\nМы занесём вас в дополнительный список, и каждый день будем пытаться подобрать пару снова!')
                    except:
                        print('Я в блоке')
                extra_pairs = await make_extra_pairs()


        for key, value in dict_pairs.items():
            await send_invoice_message(key, value)
            await send_invoice_message(value, key)

        return len(dict_pairs) + extra_pairs
    except Exception:
        await dp.bot.send_message(555581588, 'Возникла ошибка при подборе пар')
async def ask_impress():
    users = await sqlite_db.get_users()
    if len(users) == 0:
        return
    count = 0
    for user in users:
        counter = 0
        for pair in reversed(user[1]):
            if user[2][-1 - counter] == 0:
                pair_user = await sqlite_db.get_profile(pair)
                try:
                    await dp.bot.send_message(user[0], f'Как прошла встреча с {pair_user[2]} из города {pair_user[4]}?\nTg : {pair_user[1]}', reply_markup=inline_kb_impress)
                    count += 1
                except:
                    pass
            counter += 1
    return count
            
async def make_extra_pairs():
    users = await sqlite_db.get_extra_users()
    dict_pairs = dict(str())
    for id in range(len(users)):
        max_sim = -1
        max_index = id
        for pair_id in range(len(users)):
            if users[id] in dict_pairs.values():
                break
            if id == pair_id or users[pair_id] in dict_pairs.keys() or users[pair_id] in dict_pairs.values() or await sqlite_db.is_last_pair(users[id], users[pair_id]):
                continue     
            s1 = await sqlite_db.get_hooks(users[id])
            s2 = await sqlite_db.get_hooks(users[pair_id])
            sim = similarity(s1, s2)
            if sim > max_sim:
                max_index = pair_id
                max_sim = sim
        if max_index != id:
            dict_pairs[users[id]] = users[max_index]
            await sqlite_db.append_pair(users[id], users[max_index])
    for key, value in dict_pairs.items():
        await sqlite_db.delete_from_temp_users(key)
        await sqlite_db.delete_from_temp_users(value)
        await send_invoice_message(key, value)
        await send_invoice_message(value, key)
    
    return len(dict_pairs)
    
    
async def is_active():
    users = await sqlite_db.get_paid_users()
    counter = 0
    for user in users:
        try:
            await dp.bot.send_message(user, 'Новая неделя - новые знакомства!\nИскать вам пару на следующую неделю?', reply_markup=inline_kb_active)
            counter += 1
        except:
            print('Я в блоке')
            
    return counter

async def update_paid():
    await sqlite_db.update()