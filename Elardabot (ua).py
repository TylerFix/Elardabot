# ,types.InlineKeyboardButton(text="Комментарий", callback_data="obr_zakaz")
# message.reply("Отличный выбор!", reply_markup=types.ReplyKeyboardRemove()) Удалить клавиатуру

import telebot
import time
from telebot import types
import pickle

bot = telebot.TeleBot('5353892055:AAEMEqLhJ6e-TMJjyxgn2nBkkkbXbQMhE4A')
# Id сравнение
id_res = 0
# Счётчики
#pepe_count = 0
#mari_count = 0
#marg_count = 0
#bbqbeef_count = 0
#grillchicken_count = 0
#cheesecake_count = 0
#sorbet_count = 0
zakaz_count = 0
zakaz_admin_count = 0
# Цены
pepe_cost = 110
mari_cost = 120
marg_cost = 90
bbqbeef_cost = 210
grillchicken_cost = 180
cheesecake_cost = 75
sorbet_cost = 50

global person_num 
person_num = 0
money = 0
person_list = []
zakaz_person_list = []
zakaz_money_list = []
zakaz_admin_list = []
zakaz_mess_list = []
zakaz_komm_list = []
zakaz_person_mari = []
zakaz_person_marg = []
zakaz_person_pepe = []
zakaz_person_bbqbeef = []
zakaz_person_grillchicken = []
zakaz_person_cheesecake = []
zakaz_person_sorbet = []
zakaz_person_mam = []
content = None
zakaz_admin_stat = []
zakaz_all_money = []
mam = ''
global_text = ''
zakaz_admin_id = 0

try :
    with open('data\\people.dat','rb') as pickle_file:
        content = pickle.load(pickle_file)
    with open('data\\person_num.dat','rb') as pickle_file:
        person_num = pickle.load(pickle_file)
    with open('data\\zakaz_admin_stat.dat','rb') as pickle_file:
        zakaz_admin_stat = pickle.load(pickle_file)
    with open('data\\zakaz_money_list.dat','rb') as pickle_file:
        zakaz_money_list = pickle.load(pickle_file)
    with open('data\\zakaz_person_bbqbeef.dat','rb') as pickle_file:
        zakaz_person_bbqbeef = pickle.load(pickle_file)
    with open('data\\zakaz_person_cheesecake.dat','rb') as pickle_file:
        zakaz_person_cheesecake = pickle.load(pickle_file)
    with open('data\\zakaz_person_grillchicken.dat','rb') as pickle_file:
        zakaz_person_grillchicken = pickle.load(pickle_file)
    with open('data\\zakaz_person_mam.dat','rb') as pickle_file:
        zakaz_person_mam = pickle.load(pickle_file)
    with open('data\\zakaz_person_marg.dat','rb') as pickle_file:
        zakaz_person_marg = pickle.load(pickle_file)
    with open('data\\zakaz_person_mari.dat','rb') as pickle_file:
        zakaz_person_mari = pickle.load(pickle_file)
    with open('data\\zakaz_person_pepe.dat','rb') as pickle_file:
        zakaz_person_pepe = pickle.load(pickle_file)
    with open('data\\zakaz_person_sorbet.dat','rb') as pickle_file:
        zakaz_person_sorbet = pickle.load(pickle_file)
    with open('data\\zakaz_person_list.dat','rb') as pickle_file:
        zakaz_person_list = pickle.load(pickle_file)
except:
    print(person_num)
    bot.send_message(346746037,'Помилка читання бази данних.')


@bot.message_handler(commands=['start'])


def start(m,res=False):
    # Наши меню
    global markup,service,menu,menu_zakaz,menu_pizza,etext,message,mam,service_dop_menu
    
    markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
    
    service=types.ReplyKeyboardMarkup(resize_keyboard=True)
    
    menu=types.ReplyKeyboardMarkup(resize_keyboard=True)

    menu_zakaz=types.ReplyKeyboardMarkup(resize_keyboard=True)

    menu_pizza=types.ReplyKeyboardMarkup(resize_keyboard=True)

    service_dop_menu = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item8=types.KeyboardButton('Start')
    markup.add(item8)
    
    bot.send_message(m.chat.id, 'Вас вітає Elarda\nДля початку роботи натисніть "Start"',reply_markup=markup )
    # Кнопки
    item0=types.KeyboardButton('Активні замовлення')
    item4=types.KeyboardButton('Завершені замовлення')
    item7=types.KeyboardButton('Завершити замовлення')
    item5=types.KeyboardButton('Загальна інформація')
    item6=types.KeyboardButton('Завершити роботу')
    item1=types.KeyboardButton('Меню')
    item2=types.KeyboardButton('Моє замовлення')
    item3=types.KeyboardButton('Інформація')
    item9=types.KeyboardButton('Відхилити')
    item10=types.KeyboardButton('Головне меню')
    item11=types.KeyboardButton('Підтвердити')
    item12=types.KeyboardButton('Піцца')
    item13=types.KeyboardButton('Бургери')
    item14=types.KeyboardButton('Десерти')
    item15=types.KeyboardButton('Додати коментар')
    item16=types.KeyboardButton('Змінити замовлення')
    item17=types.KeyboardButton('Вказати час')
    item18=types.KeyboardButton('Адмін меню')
    item19=types.KeyboardButton('Розсилка')
    # Полное меню
    menu.add(item1)
    menu.add(item2)
    menu.add(item3)
    # Сам заказ
    menu_zakaz.add(item16,item15)
    menu_zakaz.add(item1)
    menu_zakaz.add(item10)
    #menu_zakaz.add(item9)
    #menu_zakaz.add(item10)
    # Админка
    service.add(item0,item4)
    service.add(item5)
    service.add(item19)
    service.add(item6)
    # Подтверждение заказа, доп. меню
    service_dop_menu.add(item17)
    service_dop_menu.add(item18)

    menu_pizza.add(item12,item13,item14)
    menu_pizza.add(item2)
    menu_pizza.add(item10)
    global content
    global person_list

    if content != None :
        person_list = content

    if m.chat.id == 346746037 :
        global id_res
        id_res = m.chat.id
        #person_list.append(m.chat.id)
        #zakaz_person_mari.append(0)
        #zakaz_person_marg.append(0)
        #zakaz_person_pepe.append(0)
        #zakaz_person_bbqbeef.append(0)
        #zakaz_person_grillchicken.append(0)
        #zakaz_person_cheesecake.append(0)
        #zakaz_person_sorbet.append(0)
        #zakaz_person_mam.append(0)
        #zakaz_money_list.append(0)
        #zakaz_admin_stat.append(0)
    else:
        global person_num
        bot.send_message(346746037,('Новий користувач'+str(m.chat.id)))
        id_res = m.chat.id
        f = person_list.count(m.chat.id)
        if f == 0:
            person_list.append(m.chat.id)
            person_num = person_num+1
            zakaz_person_mari.append(0)
            with open("data\\zakaz_person_mari.dat","wb") as pickle_file:  
                pickle.dump(zakaz_person_mari,pickle_file,pickle.HIGHEST_PROTOCOL)
            zakaz_person_marg.append(0)
            with open("data\\zakaz_person_marg.dat","wb") as pickle_file:  
                pickle.dump(zakaz_person_marg,pickle_file,pickle.HIGHEST_PROTOCOL)
            zakaz_person_pepe.append(0)
            with open("data\\zakaz_person_pepe.dat","wb") as pickle_file:  
                pickle.dump(zakaz_person_pepe,pickle_file,pickle.HIGHEST_PROTOCOL)
            zakaz_person_bbqbeef.append(0)
            with open("data\\zakaz_person_bbqbeef.dat","wb") as pickle_file:  
                pickle.dump(zakaz_person_bbqbeef,pickle_file,pickle.HIGHEST_PROTOCOL)
            zakaz_person_grillchicken.append(0)
            with open("data\\zakaz_person_grillchicken.dat","wb") as pickle_file:  
                pickle.dump(zakaz_person_grillchicken,pickle_file,pickle.HIGHEST_PROTOCOL)
            zakaz_person_cheesecake.append(0)
            with open("data\\zakaz_person_cheesecake.dat","wb") as pickle_file:  
                pickle.dump(zakaz_person_cheesecake,pickle_file,pickle.HIGHEST_PROTOCOL)
            zakaz_person_sorbet.append(0)
            with open("data\\zakaz_person_sorbet.dat","wb") as pickle_file:  
                pickle.dump(zakaz_person_sorbet,pickle_file,pickle.HIGHEST_PROTOCOL)
            zakaz_person_mam.append(0)
            with open("data\\zakaz_person_mam.dat","wb") as pickle_file:  
                pickle.dump(zakaz_person_mam,pickle_file,pickle.HIGHEST_PROTOCOL)
            zakaz_money_list.append(0)
            with open("data\\zakaz_money_list.dat","wb") as pickle_file:  
                pickle.dump(zakaz_money_list,pickle_file,pickle.HIGHEST_PROTOCOL)
            zakaz_admin_stat.append(0)
            with open("data\\zakaz_admin_stat.dat","wb") as pickle_file:  
                pickle.dump(zakaz_admin_stat,pickle_file,pickle.HIGHEST_PROTOCOL)
            with open("data\\people.dat","wb") as pickle_file:  
                pickle.dump(person_list,pickle_file,pickle.HIGHEST_PROTOCOL)
            with open("data\\person_num.dat","wb") as pickle_file:  
                pickle.dump(person_num,pickle_file,pickle.HIGHEST_PROTOCOL)

@bot.message_handler(content_types=['text'])
def handle_text(message):

#
# СООБЩЕНИЕ ПОЛЬЗОВАТЕЛЯ
#
    
    if message.chat.id != 346746037:
        global id_res
        #d = person_list.index(message.chat.id)
        #marg_count = zakaz_person_marg[d]
        #mari_count = zakaz_person_mari[d]
        #pepe_count = zakaz_person_pepe[d]
        #bbqbeef_count = zakaz_person_bbqbeef[d]
        #grillchicken_count = zakaz_person_grillchicken[d]
        #cheesecake_count = zakaz_person_cheesecake[d]
        #sorbet_count = zakaz_person_sorbet[d]
        answer = 'test'
        img = 1
        if message.text.strip() == 'Start':
            if id_res == 346746037 :
                bot.send_message(346746037,'Привіт Валера!',reply_markup=service)
            else :
                bot.send_message(message.chat.id,'Для взаємодії зі мною оберіть один із варіантів нижче.', reply_markup=menu)
            
        if message.text.strip() == 'Меню':
            img = open('25.png','rb')
            bot.send_photo(message.chat.id, img)
            bot.send_message(message.chat.id,'Оберіть страву.',reply_markup=menu_pizza)
# Меню
        elif message.text.strip() == 'Піцца':
            d = person_list.index(message.chat.id)
            marg_count = zakaz_person_marg[d]
            mari_count = zakaz_person_mari[d]
            pepe_count = zakaz_person_pepe[d]
            bbqbeef_count = zakaz_person_bbqbeef[d]
            grillchicken_count = zakaz_person_grillchicken[d]
            cheesecake_count = zakaz_person_cheesecake[d]
            sorbet_count = zakaz_person_sorbet[d]
            img1 = open('pizza-margarita.jpg','rb')
            bot.send_photo(message.chat.id,img1)
            bot.send_message(message.chat.id,"Піцца Маргарита — традиційна італійська страва,\nІнгрідієнти: сир моцарелла, стиглі помідори та листя свіжого базиліку, які надають їй неперевершений смак і аромат.\n\nЦіна : 90 грн.", reply_markup=key_pizza_marg(marg_count))

            img2 = open('26.jpg','rb')
            bot.send_photo(message.chat.id,img2)
            bot.send_message(message.chat.id,"Піцца Пепероні\nГастрономічна візитна картка сонячного півдня Італії.\n\nЦіна : 110 грн", reply_markup=key_pizza_pepe(pepe_count))

            img3 = open('pizza-marinara.jpg','rb')
            bot.send_photo(message.chat.id,img3)
            bot.send_message(message.chat.id,"Піцца Марінара\nМорський соус Марінара не залишить нікого байдужим. Ингрідиенти : стиглі томати, часник, оливкова олія, базилік, пармезан, чорні оливки.\n\nЦіна : 120 грн.", reply_markup=key_pizza_mari(mari_count))

        elif message.text.strip() == 'Бургери':
            global bbq_item
            d = person_list.index(message.chat.id)
            marg_count = zakaz_person_marg[d]
            mari_count = zakaz_person_mari[d]
            pepe_count = zakaz_person_pepe[d]
            bbqbeef_count = zakaz_person_bbqbeef[d]
            grillchicken_count = zakaz_person_grillchicken[d]
            cheesecake_count = zakaz_person_cheesecake[d]
            sorbet_count = zakaz_person_sorbet[d]
            img4 = open('bbqbeef.jpg','rb')
            bot.send_photo(message.chat.id,img4)
            bot.send_message(message.chat.id,"BBQ BEEF BURGER\n,Дві соковиті котлети з мармурової яловичини,стиглі томати, корнішони, червона цибуля, сир чеддер, салат айсберг і соус BBQ у булочці з кунжутом\n\nЦіна : 210 грн.", reply_markup=key_burg_bbq(bbqbeef_count))

            img5 = open('grilled-chicken-breast-burger.jpg','rb')
            bot.send_photo(message.chat.id,img5)
            bot.send_message(message.chat.id,"Grill Chicken Burger\nКуряче філе, бекон, сир моцарелла, томати, салат айсберг, мариновані огірки, соус Цезар, картопля фрі.\n\nЦіна : 180 грн.", reply_markup=key_burg(grillchicken_count))

        elif message.text.strip() == 'Десерти':
            d = person_list.index(message.chat.id)
            marg_count = zakaz_person_marg[d]
            mari_count = zakaz_person_mari[d]
            pepe_count = zakaz_person_pepe[d]
            bbqbeef_count = zakaz_person_bbqbeef[d]
            grillchicken_count = zakaz_person_grillchicken[d]
            cheesecake_count = zakaz_person_cheesecake[d]
            sorbet_count = zakaz_person_sorbet[d]
            img6 = open('gluten-free-new-york-cheesecake-1450985-hero-01-dc54f9daf38044238b495c7cefc191fa.jpg','rb')
            bot.send_photo(message.chat.id,img6)
            bot.send_message(message.chat.id,"Cheesecake\nДесерт європейської та американської кухні, зроблений з ніжного сиру та соковитої полуниці.\n\nЦіна : 75 грн.", reply_markup=key_desert_cheesecake(cheesecake_count))

            img7 = open('AdobeStock_85136925.jpg','rb')
            bot.send_photo(message.chat.id,img7)
            bot.send_message(message.chat.id,"Сорбет\nРізновид фруктово-ягідного морозива.\n\nЦіна 50 грн.", reply_markup=key_desert_sorbet(sorbet_count))
        
        elif message.text.strip() == 'Моє замовлення':
            global etext,money
            d = person_list.index(message.chat.id)
            marg_count = zakaz_person_marg[d]
            mari_count = zakaz_person_mari[d]
            pepe_count = zakaz_person_pepe[d]
            bbqbeef_count = zakaz_person_bbqbeef[d]
            grillchicken_count = zakaz_person_grillchicken[d]
            cheesecake_count = zakaz_person_cheesecake[d]
            sorbet_count = zakaz_person_sorbet[d]
            money = 0
            etext = ''
            if zakaz_person_pepe[d] or zakaz_person_marg[d] or zakaz_person_mari[d] or zakaz_person_bbqbeef[d] or zakaz_person_grillchicken[d] or zakaz_person_cheesecake[d] or zakaz_person_sorbet[d] > 0 :
                if pepe_count > 0 :
                    etext = etext+('Піцца Пепероні - '+str(zakaz_person_pepe[d])+',шт.\n')
                    money = money+(pepe_cost*zakaz_person_pepe[d])
                if marg_count  > 0 :
                    etext = etext+('Піцца Маргарита - '+str(zakaz_person_marg[d])+',шт.\n')
                    money = money+(marg_cost*zakaz_person_marg[d])
                if mari_count > 0:
                    etext = etext+('Піцца Марінара - '+str(zakaz_person_mari[d])+',шт.\n')
                    money = money+(mari_cost*zakaz_person_mari[d])
                if bbqbeef_count > 0 :
                    etext = etext+('BBQ BEEF Burger - '+str(zakaz_person_bbqbeef[d])+",шт.\n")
                    money = money+(bbqbeef_cost*zakaz_person_bbqbeef[d])
                if grillchicken_count > 0 :
                    etext = etext+('Grill Chicken Burger - '+str(zakaz_person_grillchicken[d])+",шт.\n")
                    money = money+(grillchicken_cost*zakaz_person_grillchicken[d])
                if cheesecake_count > 0 :
                    etext = etext+('Cheesecake - '+str(zakaz_person_cheesecake[d])+",шт.\n")
                    money = money+(cheesecake_cost*zakaz_person_cheesecake[d])
                if sorbet_count > 0 :
                    etext = etext+('Sorbet - '+str(zakaz_person_sorbet[d])+",шт.\n")
                    money = money+(sorbet_cost*zakaz_person_sorbet[d])
            global_text = etext
            if etext != '':
                keyboard4 = types.InlineKeyboardMarkup()
                keyboard4.add(types.InlineKeyboardButton(text="✅Підтвердити", callback_data="yes_zakaz"),types.InlineKeyboardButton(text="Відхилити", callback_data="no_zakaz"))
                bot.send_message(message.chat.id,str(etext+'\nВартість замовлення - '+str(money)+' грн.'+'\nКоментар : '+str(zakaz_person_mam[d])), reply_markup=keyboard4)
                bot.send_message(message.chat.id,'Підтвердіть, будь ласка, ваше замовлення',reply_markup = menu_zakaz)
            else:
                bot.send_message(message.chat.id,'У Вас немає активних замовлень.')

        #bot.send_message(message.chat.id,'Заказы:',reply_markup=menu_zakaz)

        elif message.text.strip() == 'Інфо':
            bot.send_message(message.chat.id,"Розробник бота - Антонніков В.В. Для зв'язку звертайтесь :\nПошта - raoautomatik@gmail.com\nТелеграм - @TylerFix",reply_markup=menu)
        

        elif message.text.strip() == 'Головне меню':
            bot.send_message(message.chat.id,'Ви у головному меню!',reply_markup=menu)


        elif message.text.strip() == 'Додати коментар':
            bot.send_message(message.chat.id,'Введіть Ваш коментар')
            bot.register_next_step_handler(message, zakaz_komm)

        elif message.text.strip() == 'Змінити замовлення':
            d = person_list.index(message.chat.id)
            if zakaz_person_pepe[d] or zakaz_person_marg[d] or zakaz_person_mari[d] or zakaz_person_bbqbeef[d] or zakaz_person_grillchicken[d] or zakaz_person_cheesecake[d] or zakaz_person_sorbet[d] > 0 :
                if pepe_count > 0 :
                    keyboard8 = types.InlineKeyboardMarkup()
                    keyboard8.add(types.InlineKeyboardButton(text="➖", callback_data="mone_peperoni"),types.InlineKeyboardButton(text="➕", callback_data="one_peperoni"))
                    bot.send_message(message.chat.id,"Піцца Пепероні - "+str(zakaz_person_pepe[d]), reply_markup=keyboard8)
                if marg_count > 0 :
                    keyboard9 = types.InlineKeyboardMarkup()
                    keyboard9.add(types.InlineKeyboardButton(text="➖", callback_data="mone_margarita"),types.InlineKeyboardButton(text="➕", callback_data="one_margarita"))
                    bot.send_message(message.chat.id,"Піцца Маргарита - "+str(zakaz_person_marg[d]), reply_markup=keyboard9)
                if mari_count > 0:
                    keyboard10 = types.InlineKeyboardMarkup()
                    keyboard10.add(types.InlineKeyboardButton(text="➖", callback_data="mone_marinara"),types.InlineKeyboardButton(text="➕", callback_data="one_marinara"))
                    bot.send_message(message.chat.id,"Піцца Марінара - "+str(zakaz_person_mari[d]), reply_markup=keyboard10)
                if bbqbeef_count > 0 :
                    keyboard11 = types.InlineKeyboardMarkup()
                    keyboard11.add(types.InlineKeyboardButton(text="➖", callback_data="mone_bbqbeef"),types.InlineKeyboardButton(text="➕", callback_data="one_bbqbeef"))
                    bot.send_message(message.chat.id,"BBQ BEEF Burger - "+str(zakaz_person_bbqbeef[d]), reply_markup=keyboard11)
                if grillchicken_count > 0 :
                    keyboard12 = types.InlineKeyboardMarkup()
                    keyboard12.add(types.InlineKeyboardButton(text="➖", callback_data="mone_grillchicken"),types.InlineKeyboardButton(text="➕", callback_data="one_grillchicken"))
                    bot.send_message(message.chat.id,"GRILL CHICKEN Burger - "+str(zakaz_person_grillchicken[d]), reply_markup=keyboard12)
                if cheesecake_count > 0 :
                    keyboard13 = types.InlineKeyboardMarkup()
                    keyboard13.add(types.InlineKeyboardButton(text="➖", callback_data="mone_cheesecake"),types.InlineKeyboardButton(text="➕", callback_data="one_cheesecake"))
                    bot.send_message(message.chat.id,"Cheesecake - "+str(zakaz_person_cheesecake[d]), reply_markup=keyboard13)
                if sorbet_count > 0 :
                    keyboard14 = types.InlineKeyboardMarkup()
                    keyboard14.add(types.InlineKeyboardButton(text="➖", callback_data="mone_sorbet"),types.InlineKeyboardButton(text="➕", callback_data="one_sorbet"))
                    bot.send_message(message.chat.id,"Sorbet - "+str(zakaz_person_sorbet[d]), reply_markup=keyboard14)

        else:
            bot.send_message(message.chat.id,'Вибачте, я Вас не розумію. Будь ласка, скористайтеся функціями меню.')
#
# СООБЩЕНИЯ АДМИНКИ
#
    elif message.chat.id == 346746037:

        if message.text.strip() == 'Start':
            bot.send_message(346746037,'Привіт',reply_markup=service)
        
        elif message.text.strip() == 'Вказати час':
            bot.send_message(message.chat.id,'Введіть час очикування')
            bot.register_next_step_handler(message, testing)

        elif message.text.strip() == 'Адмін меню':
            bot.send_message(message.chat.id,'Ви повернулись в адміністраційне меню.',reply_markup=service)

        elif message.text.strip() == 'Активні замовлення' :
            global zakaz_count,zakaz_admin_count,zakaz_person_list,zakaz_admin_list,zakaz_money_list,zakaz_mess_list,zakaz_komm_list
            try:
                i = 0
                if zakaz_admin_count != 0:
                    while i <= zakaz_admin_count-1:
                        if zakaz_admin_stat[i] != 2:
                            keyboard = types.InlineKeyboardMarkup()
                            keyboard.add(types.InlineKeyboardButton(text="✅Підтвердити", callback_data="zakaz_admin_yes"),types.InlineKeyboardButton(text="❌Відхилити", callback_data="zakaz_admin_none"))
                            keyboard.add(types.InlineKeyboardButton(text='Завершити замовлення',callback_data='zakaz_admin_finish'))
                            bot.send_message(346746037,zakaz_mess_list[i], reply_markup=keyboard)
                            if zakaz_admin_stat[i] == 1 :
                                bot.send_message(346746037,'\nСтатус замовлення : Підтверджений.')
                            elif zakaz_admin_stat[i] == 0 :
                                bot.send_message(346746037,'\nСтатус замовлення : Не підтверджений.')
                            x = person_list[i]
                            i = i+1
                        else:
                            bot.send_message(346746037,'Активних замовлень немає.')
                            i = i+1
                else:
                    bot.send_message(346746037,'Активних замовлень немає.')
            except:
                bot.send_message(346746037,'Помилка замовлень.')

        elif message.text.strip() == 'Загальна інформація':
            bot.send_message(message.chat.id,str('Зареєстрованих користувачів - '+str(len(person_list))+'\nЗамовлень виконано - '+'\n\nСума доходу за весь час = '+str(sum(zakaz_all_money))))

        elif message.text.strip() == 'Завершені замовлення' :
            #global zakaz_count,zakaz_admin_count,zakaz_person_list,zakaz_admin_list,zakaz_money_list,zakaz_mess_list,zakaz_komm_list
            i = 0
            while i <= zakaz_admin_count-1:
                if zakaz_admin_stat[i] == 2:
                    #keyboard = types.InlineKeyboardMarkup()
                    #keyboard.add(types.InlineKeyboardButton(text="✅Подтвердить", callback_data="zakaz_admin_yes"),types.InlineKeyboardButton(text="❌Отменить", callback_data="zakaz_admin_none"))
                    #keyboard.add(types.InlineKeyboardButton(text='Завершить заказ',callback_data='zakaz_admin_finish'))
                    bot.send_message(346746037,zakaz_mess_list[i])
                    bot.send_message(346746037,'\nСтатус замовлення : Завершений.')
                i = i+1
        elif message.text.strip() == 'Розсилка':
            bot.send_message(346746037,'Введіть текст.')
            bot.register_next_step_handler(message, reklama)
    else:
        bot.send,essage(message.chat.id,'Прошу вибачення, сталася помилка. Звеніться до розробника.')

#
# ФУНКЦИИ МЕНЮ
#

def key_pizza_marg (marg_count):
    global keyboard1,item_pizza_marg1
    keyboard1 = types.InlineKeyboardMarkup()
    item_pizza_marg1 = types.InlineKeyboardButton(text=str("Обрано:"+str(marg_count)),callback_data='none')
    keyboard1.add(types.InlineKeyboardButton(text="➖", callback_data="mone_margarita"),types.InlineKeyboardButton(text="➕", callback_data="one_margarita"))
    keyboard1.add(item_pizza_marg1)
    return keyboard1

def key_pizza_pepe(pepe_count):
    global keyboard2,item_pizza_pepe2
    keyboard2 = types.InlineKeyboardMarkup()
    item_pizza_pepe2 = types.InlineKeyboardButton(text=str('Обрано:'+str(pepe_count)),callback_data='none')
    keyboard2.add(types.InlineKeyboardButton(text="➖", callback_data="mone_peperoni"),types.InlineKeyboardButton(text="➕", callback_data="one_peperoni"))
    keyboard2.add(item_pizza_pepe2)
    return keyboard2

def key_pizza_mari(mari_count):
    global keyboard3,item_pizza_mari3
    keyboard3 = types.InlineKeyboardMarkup()
    item_pizza_mari3 = types.InlineKeyboardButton(text=str("Обрано:"+str(mari_count)),callback_data='none')
    keyboard3.add(types.InlineKeyboardButton(text="➖", callback_data="mone_marinara"),types.InlineKeyboardButton(text="➕", callback_data="one_marinara"))
    keyboard3.add(item_pizza_mari3)
    return keyboard3

def key_burg_bbq (bbqbeef_count):
    global keyboard4,item_burg4
    keyboard4 = types.InlineKeyboardMarkup()
    item_burg4 = types.InlineKeyboardButton(text=str("Обрано:"+str(bbqbeef_count)),callback_data='none')
    keyboard4.add(types.InlineKeyboardButton(text="➖", callback_data="mone_bbqbeef"),types.InlineKeyboardButton(text="➕", callback_data="one_bbqbeef"))
    keyboard4.add(item_burg4)
    return keyboard4

def key_burg (grillchicken_count):
    global keyboard5,item_burg5
    keyboard5 = types.InlineKeyboardMarkup()
    item_burg5 = types.InlineKeyboardButton(text=str("Обрано:"+str(grillchicken_count)),callback_data='none')
    keyboard5.add(types.InlineKeyboardButton(text="➖", callback_data="mone_grillchicken"),types.InlineKeyboardButton(text="➕", callback_data="one_grillchicken"))
    keyboard5.add(item_burg5)
    return keyboard5

def key_desert_cheesecake(cheesecake_count):
    global keyboard6,item_desert_cheesecake
    keyboard6 = types.InlineKeyboardMarkup()
    item_desert_cheesecake = types.InlineKeyboardButton(text=str('Обрано:'+str(cheesecake_count)),callback_data='none')
    keyboard6.add(types.InlineKeyboardButton(text="➖", callback_data="mone_cheesecake"),types.InlineKeyboardButton(text="➕", callback_data="one_cheesecake"))
    keyboard6.add(item_desert_cheesecake)
    return keyboard6

def key_desert_sorbet(sorbet_count):
    global keyboard7,item_desert_sorbet
    keyboard7 = types.InlineKeyboardMarkup()
    item_desert_sorbet = types.InlineKeyboardButton(text=str('Обрано:'+str(sorbet_count)),callback_data='none')
    keyboard7.add(types.InlineKeyboardButton(text="➖", callback_data="mone_sorbet"),types.InlineKeyboardButton(text="➕", callback_data="one_sorbet"))
    keyboard7.add(item_desert_sorbet)
    return keyboard7

def zakaz_komm(message):
#global mam
    d = person_list.index(message.chat.id)
    try:
        mam = message.text.strip()
        bot.send_message(message.chat.id,'Ваш коментар додано.')
        zakaz_person_mam[d] = mam
        with open("data\\zakaz_person_mam.dat","wb") as pickle_file:  
            pickle.dump(zakaz_person_mam,pickle_file,pickle.HIGHEST_PROTOCOL)
    except:
        bot.send_message(message.chat.id,'Введіть повідомлення коректно.')
        bot.register_next_step_handler(message, zakaz_komm)
    
def testing(message):
    global zakaz_admin_id,person_list
    try:
        time_zak = message.text.strip()
        print(zakaz_admin_id,time_zak)
        bot.send_message(zakaz_admin_id,time_zak)
        u = person_list.index(zakaz_admin_id)
        zakaz_admin_stat[u] = 1
        bot.send_message(message.chat.id,'Підтвердження було надіслано клієнту.')
    except:
        bot.send_message(message.chat.id,'Введіть час коректно.')
        bot.register_next_step_handler(message, testing)

def reklama (message):
    #try:
    text_reklama = message.text.strip()
    i=0
        #except:
        #    photo_reklama = message.photo
        #try:
        #    photo_reklama = message.photo
        #except:
        #    text_reklama = message.text.strip()
    print(person_num)
    while i <= (person_num - 1):
        next_id = person_list[i]
        bot.send_message(next_id,text_reklama)
        i=i+1
    #except:
    #    bot.send_message(346746037,'Произошла ошибка.')
def testing2(message):
    global papa
    papa = message.text.strip()
    bot.send_message(346746037,papa)
#def zakaz_komm2(message):
#    text = message.text
#    bot.send_message(346746037,str(text))

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
# Вызовы добавления из меню
    if call.message.chat.id != 346746037:
        d = person_list.index(call.message.chat.id)
        if call.data == 'one_margarita':
            marg_count = zakaz_person_marg[d]
            marg_count = marg_count+1
            zakaz_person_marg[d] = marg_count
            zakaz_money_list[d] = zakaz_money_list[d]+ marg_cost
            with open("data\\zakaz_money_list.dat","wb") as pickle_file:  
                    pickle.dump(zakaz_money_list,pickle_file,pickle.HIGHEST_PROTOCOL)
            with open("data\\zakaz_person_marg.dat","wb") as pickle_file:  
                pickle.dump(zakaz_person_marg,pickle_file,pickle.HIGHEST_PROTOCOL)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='Піцца Маргарита — традиційна італійська страва,\nІнгрідієнти: сир моцарелла, стиглі помідори та листя свіжого базиліку, які надають їй неперевершений смак і аромат.\n\nЦіна : 90 грн.', reply_markup=key_pizza_marg(marg_count))
        if call.data == 'mone_margarita':
            if marg_count > 0 :
                marg_count = zakaz_person_marg[d]
                marg_count = marg_count-1
                zakaz_person_marg[d] = marg_count
                with open("data\\zakaz_person_marg.dat","wb") as pickle_file:  
                    pickle.dump(zakaz_person_marg,pickle_file,pickle.HIGHEST_PROTOCOL)
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='Піцца Маргарита — традиційна італійська страва,\nІнгрідієнти: сир моцарелла, стиглі помідори та листя свіжого базиліку, які надають їй неперевершений смак і аромат.\n\nЦіна : 90 грн.', reply_markup=key_pizza_marg(marg_count))
                try:
                    zakaz_money_list[d] = zakaz_money_list[d]-marg_cost
                    with open("data\\zakaz_money_list.dat","wb") as pickle_file:  
                        pickle.dump(zakaz_money_list,pickle_file,pickle.HIGHEST_PROTOCOL)
                except:
                    print('')
            else :
                bot.send_message(call.message.chat.id, 'Піцца Маргарита не обрана.')

        if call.data == 'one_peperoni':
            pepe_count = zakaz_person_pepe[d]
            pepe_count = pepe_count+1
            zakaz_person_pepe[d] = pepe_count
            zakaz_money_list[d] = zakaz_money_list[d]+ pepe_cost
            with open("data\\zakaz_money_list.dat","wb") as pickle_file:  
                    pickle.dump(zakaz_money_list,pickle_file,pickle.HIGHEST_PROTOCOL)
            with open("data\\zakaz_person_pepe.dat","wb") as pickle_file:  
                pickle.dump(zakaz_person_pepe,pickle_file,pickle.HIGHEST_PROTOCOL)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Піцца Пепероні\nГастрономічна візитна картка сонячного півдня Італії.\n\nЦіна : 110 грн", reply_markup=key_pizza_pepe(pepe_count))
        if call.data == 'mone_peperoni':
            if pepe_count > 0 :
                pepe_count = zakaz_person_pepe[d]
                pepe_count = pepe_count-1
                zakaz_person_pepe[d] = pepe_count
                with open("data\\zakaz_person_pepe.dat","wb") as pickle_file:  
                    pickle.dump(zakaz_person_pepe,pickle_file,pickle.HIGHEST_PROTOCOL)
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Піцца Пепероні\nГастрономічна візитна картка сонячного півдня Італії.\n\nЦіна : 110 грн", reply_markup=key_pizza_pepe(pepe_count))
                try:
                    zakaz_money_list[d] = zakaz_money_list[d]-pepe_cost
                    with open("data\\zakaz_money_list.dat","wb") as pickle_file:  
                        pickle.dump(zakaz_money_list,pickle_file,pickle.HIGHEST_PROTOCOL)
                except:
                    print('')
            else:
                bot.send_message(call.message.chat.id,'Піцца Пепероні не обрана.')

        if call.data == 'one_marinara':
            mari_count = zakaz_person_mari[d]
            mari_count = mari_count+1
            zakaz_person_mari[d] = mari_count
            zakaz_money_list[d] = zakaz_money_list[d]+ mari_cost
            with open("data\\zakaz_money_list.dat","wb") as pickle_file:  
                    pickle.dump(zakaz_money_list,pickle_file,pickle.HIGHEST_PROTOCOL)
            with open("data\\zakaz_person_mari.dat","wb") as pickle_file:  
                pickle.dump(zakaz_person_mari,pickle_file,pickle.HIGHEST_PROTOCOL)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Піцца Марінара\nМорський соус Марінара не залишить нікого байдужим. Ингрідиенти : стиглі томати, часник, оливкова олія, базилік, пармезан, чорні оливки.\n\nЦіна : 120 грн.", reply_markup=key_pizza_mari(mari_count))
        if call.data == 'mone_marinara':
            if mari_count > 0 :
                mari_count = zakaz_person_mari[d]
                mari_count = mari_count-1
                zakaz_person_mari[d] = mari_count
                with open("data\\zakaz_person_mari.dat","wb") as pickle_file:  
                    pickle.dump(zakaz_person_mari,pickle_file,pickle.HIGHEST_PROTOCOL)
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Піцца Марінара\nМорський соус Марінара не залишить нікого байдужим. Ингрідиенти : стиглі томати, часник, оливкова олія, базилік, пармезан, чорні оливки.\n\nЦіна : 120 грн.", reply_markup=key_pizza_mari(mari_count))
                try:
                    zakaz_money_list[d] = zakaz_money_list[d]-mari_cost
                    with open("data\\zakaz_money_list.dat","wb") as pickle_file:  
                        pickle.dump(zakaz_money_list,pickle_file,pickle.HIGHEST_PROTOCOL)
                except:
                    print('')
            else:
                bot.send_message(call.message.chat.id,'Піцца Марінара не обрана.')
            
        if call.data == 'one_bbqbeef':
            bbqbeef_count = zakaz_person_bbqbeef[d]
            bbqbeef_count = bbqbeef_count+1
            zakaz_person_bbqbeef[d] = bbqbeef_count
            zakaz_money_list[d] = zakaz_money_list[d]+ bbqbeef_cost
            with open("data\\zakaz_money_list.dat","wb") as pickle_file:  
                    pickle.dump(zakaz_money_list,pickle_file,pickle.HIGHEST_PROTOCOL)
            with open("data\\zakaz_person_bbqbeef.dat","wb") as pickle_file:  
                pickle.dump(zakaz_person_bbqbeef,pickle_file,pickle.HIGHEST_PROTOCOL)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="BBQ BEEF BURGER\n,Дві соковиті котлети з мармурової яловичини,стиглі томати, корнішони, червона цибуля, сир чеддер, салат айсберг і соус BBQ у булочці з кунжутом\n\nЦіна : 210 грн.", reply_markup=key_burg_bbq(bbqbeef_count))
        if call.data == 'mone_bbqbeef':
            if bbqbeef_count > 0 :
                bbqbeef_count = zakaz_person_bbqbeef[d]
                bbqbeef_count = bbqbeef_count-1
                zakaz_person_bbqbeef[d] = bbqbeef_count
                with open("data\\zakaz_person_bbqbeef.dat","wb") as pickle_file:  
                    pickle.dump(zakaz_person_bbqbeef,pickle_file,pickle.HIGHEST_PROTOCOL)
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="BBQ BEEF BURGER\n,Дві соковиті котлети з мармурової яловичини,стиглі томати, корнішони, червона цибуля, сир чеддер, салат айсберг і соус BBQ у булочці з кунжутом\n\nЦіна : 210 грн.", reply_markup=key_burg_bbq(bbqbeef_count))
                try:
                    zakaz_money_list[d] = zakaz_money_list[d]-bbqbeef_cost
                    with open("data\\zakaz_money_list.dat","wb") as pickle_file:  
                        pickle.dump(zakaz_money_list,pickle_file,pickle.HIGHEST_PROTOCOL)
                except:
                    print('')
            else:
                bot.send_message(call.message.chat.id,'BBQ BEEF Burger не обраний.')

        if call.data == 'one_grillchicken':
            grillchicken_count = zakaz_person_grillchicken[d]
            grillchicken_count = grillchicken_count+1
            zakaz_person_grillchicken[d] = grillchicken_count
            zakaz_money_list[d] = zakaz_money_list[d]+grillchicken_cost
            with open("data\\zakaz_money_list.dat","wb") as pickle_file:  
                    pickle.dump(zakaz_money_list,pickle_file,pickle.HIGHEST_PROTOCOL)
            with open("data\\zakaz_person_grillchicken.dat","wb") as pickle_file:  
                pickle.dump(zakaz_person_grillchicken,pickle_file,pickle.HIGHEST_PROTOCOL)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Grill Chicken Burger\nКуряче філе, бекон, сир моцарелла, томати, салат айсберг, мариновані огірки, соус Цезар, картопля фрі.\n\nЦіна : 180 грн.", reply_markup=key_burg(grillchicken_count) )
        if call.data == 'mone_grillchicken':
            if grillchicken_count > 0 :
                grillchicken_count = zakaz_person_grillchicken[d]
                grillchicken_count = grillchicken_count-1
                zakaz_person_grillchicken[d] = grillchicken_count
                with open("data\\zakaz_person_grillchicken.dat","wb") as pickle_file:  
                    pickle.dump(zakaz_person_grillchicken,pickle_file,pickle.HIGHEST_PROTOCOL)
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Grill Chicken Burger\nКуряче філе, бекон, сир моцарелла, томати, салат айсберг, мариновані огірки, соус Цезар, картопля фрі.\n\nЦіна : 180 грн.", reply_markup=key_burg(grillchicken_count) )
                try:
                    zakaz_money_list[d] = zakaz_money_list[d]-grillchicken_cost
                    with open("data\\zakaz_money_list.dat","wb") as pickle_file:  
                        pickle.dump(zakaz_money_list,pickle_file,pickle.HIGHEST_PROTOCOL)
                except:
                    print('')
            else:
                bot.send_message(call.message.chat.id,'Grill Chicken Burger не обраний.')
            
        if call.data == 'one_cheesecake':
            cheesecake_count = zakaz_person_cheesecake[d]
            cheesecake_count = cheesecake_count+1
            zakaz_person_cheesecake[d] = cheesecake_count
            zakaz_money_list[d] = zakaz_money_list[d]+cheesecake_cost
            with open("data\\zakaz_money_list.dat","wb") as pickle_file:  
                    pickle.dump(zakaz_money_list,pickle_file,pickle.HIGHEST_PROTOCOL)
            with open("data\\zakaz_person_cheesecake.dat","wb") as pickle_file:  
                pickle.dump(zakaz_person_cheesecake,pickle_file,pickle.HIGHEST_PROTOCOL)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Cheesecake\nДесерт європейської та американської кухні, зроблений з ніжного сиру та соковитої полуниці.\n\nЦіна : 75 грн.", reply_markup=key_desert_cheesecake(cheesecake_count))
        if call.data == 'mone_cheesecake':
            if cheesecake_count > 0 :
                cheesecake_count = zakaz_person_cheesecake[d]
                cheesecake_count = cheesecake_count-1
                zakaz_person_cheesecake[d] = cheesecake_count
                with open("data\\zakaz_person_cheesecake.dat","wb") as pickle_file:  
                    pickle.dump(zakaz_person_cheesecake,pickle_file,pickle.HIGHEST_PROTOCOL)
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Cheesecake\nДесерт європейської та американської кухні, зроблений з ніжного сиру та соковитої полуниці.\n\nЦіна : 75 грн.", reply_markup=key_desert_cheesecake(cheesecake_count))
                try:
                    zakaz_money_list[d] = zakaz_money_list[d]-cheesecake_cost
                    with open("data\\zakaz_money_list.dat","wb") as pickle_file:  
                        pickle.dump(zakaz_money_list,pickle_file,pickle.HIGHEST_PROTOCOL)
                except:
                    print('')
            else:
                bot.send_message(call.message.chat.id,'Cheesecake не обраний.')

        if call.data == 'one_sorbet':
            sorbet_count = zakaz_person_sorbet[d]
            sorbet_count = sorbet_count+1
            zakaz_person_sorbet[d] = sorbet_count
            zakaz_money_list[d] = zakaz_money_list[d]+sorbet_cost
            with open("data\\zakaz_money_list.dat","wb") as pickle_file:  
                    pickle.dump(zakaz_money_list,pickle_file,pickle.HIGHEST_PROTOCOL)
            with open("data\\zakaz_person_sorbet.dat","wb") as pickle_file:  
                pickle.dump(zakaz_person_sorbet,pickle_file,pickle.HIGHEST_PROTOCOL)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Сорбет\nРізновид фруктово-ягідного морозива.\n\nЦіна 50 грн.", reply_markup=key_desert_sorbet(sorbet_count))
        if call.data == 'mone_sorbet':
            if sorbet_count > 0 :
                sorbet_count = zakaz_person_sorbet[d]
                sorbet_count = sorbet_count-1
                zakaz_person_sorbet[d] = sorbet_count
                with open("data\\zakaz_person_sorbet.dat","wb") as pickle_file:  
                    pickle.dump(zakaz_person_sorbet,pickle_file,pickle.HIGHEST_PROTOCOL)
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Сорбет\nРізновид фруктово-ягідного морозива.\n\nЦіна 50 грн.", reply_markup=key_desert_sorbet(sorbet_count))
                try:
                    zakaz_money_list[d] = zakaz_money_list[d]-sorbet_cost
                    with open("data\\zakaz_money_list.dat","wb") as pickle_file:  
                        pickle.dump(zakaz_money_list,pickle_file,pickle.HIGHEST_PROTOCOL)
                except:
                    print('')
            else:
                bot.send_message(call.message.chat.id,'Sorbet не обраний.')

# Вызовы с МОЙ ЗАКАЗ            
        if call.data == 'no_zakaz':
            pepe_count= marg_count=mari_count=bbqbeef_count=grillchicken_count=cheesecake_count=sorbet_count = 0
            d = person_list.index(call.message.chat.id)
            zakaz_person_marg[d] = 0
            with open("data\\zakaz_person_marg.dat","wb") as pickle_file:  
                    pickle.dump(zakaz_person_marg,pickle_file,pickle.HIGHEST_PROTOCOL)
            zakaz_person_mari[d] = 0
            with open("data\\zakaz_person_mari.dat","wb") as pickle_file:  
                    pickle.dump(zakaz_person_mari,pickle_file,pickle.HIGHEST_PROTOCOL)
            zakaz_person_pepe[d] = 0
            with open("data\\zakaz_person_pepe.dat","wb") as pickle_file:  
                    pickle.dump(zakaz_person_pepe,pickle_file,pickle.HIGHEST_PROTOCOL)
            zakaz_person_bbqbeef[d] = 0
            with open("data\\zakaz_person_bbqbeef.dat","wb") as pickle_file:  
                    pickle.dump(zakaz_person_bbqbeef,pickle_file,pickle.HIGHEST_PROTOCOL)
            zakaz_person_grillchicken[d] = 0
            with open("data\\zakaz_person_grillchicken.dat","wb") as pickle_file:  
                    pickle.dump(zakaz_person_grillchicken,pickle_file,pickle.HIGHEST_PROTOCOL)
            zakaz_person_cheesecake[d] = 0
            with open("data\\zakaz_person_cheesecake.dat","wb") as pickle_file:  
                    pickle.dump(zakaz_person_cheesecake,pickle_file,pickle.HIGHEST_PROTOCOL)
            zakaz_person_sorbet[d] = 0
            with open("data\\zakaz_person_sorbet.dat","wb") as pickle_file:  
                    pickle.dump(zakaz_person_sorbet,pickle_file,pickle.HIGHEST_PROTOCOL)
            bot.send_message(call.message.chat.id,'Замовлення відхилено.')

        if call.data == 'yes_zakaz':
            global zakaz_count,zakaz_admin_count,zakaz_person_list,zakaz_admin_list,zakaz_mess_list,zakaz_komm_list,id_res
            zakaz_count = zakaz_count+1
            zakaz_person_list.append(id_res)
            zakaz_admin_list.append(zakaz_count)
            zakaz_mess_list.append('Номер замовлення - '+str(zakaz_count)+'\nЗамовлення :\n'+str(etext)+'\nКоментар :'+str(zakaz_person_mam[d])+'\nВартість замовлення : '+str(zakaz_money_list[d])+' грн.')
            pepe_count=marg_count=mari_count=bbqbeef_count=grillchicken_count=cheesecake_count=sorbet_count = 0
            bot.send_message(346746037,'Номер замовлення - '+str(zakaz_count)+'\nЗамовлення :\n'+str(etext)+'\nКоментар :'+str(zakaz_person_mam[d])+'\nВартість замовлення : '+str(zakaz_money_list[d])+' грн.') 
            bot.send_message(call.message.chat.id,'Очікуйте підтвердження замовлення.')
            with open("data\\zakaz_person_list.dat","wb") as pickle_file:  
                    pickle.dump(zakaz_person_list,pickle_file,pickle.HIGHEST_PROTOCOL)
            mam = ''
            money = 0
            zakaz_admin_count = zakaz_admin_count+1
        if call.data == 'obr_zakaz':
            bot.send_message(call.message.chat.id,'Напишіть Ваш коментар до замовлення')
    elif call.message.chat.id == 346746037:
# Вызовы с АКТИВНЫЕ ЗАКАЗЫ
        if call.data == 'zakaz_admin_yes':
            global service_dop_menu,zakaz_admin_id
            bot.send_message(call.message.chat.id,'Ви у меню підтвердження замовлення.',reply_markup=service_dop_menu)
            x = zakaz_mess_list.index(call.message.text)
            zakaz_admin_id = person_list[x]
            print(zakaz_admin_id)
        if call.data == 'zakaz_admin_none':
            bot.send_message(call.message.chat.id,'Замовлення відхилено. Повідомлення клієнту надіслано.')
            x = zakaz_mess_list.index(call.message.text)
            zakaz_person_mari[x] = 0
            with open("data\\zakaz_person_mari.dat","wb") as pickle_file:  
                    pickle.dump(zakaz_person_mari,pickle_file,pickle.HIGHEST_PROTOCOL)
            zakaz_person_marg[x] = 0
            with open("data\\zakaz_person_marg.dat","wb") as pickle_file:  
                    pickle.dump(zakaz_person_marg,pickle_file,pickle.HIGHEST_PROTOCOL)
            zakaz_person_pepe[x] = 0
            with open("data\\zakaz_person_pepe.dat","wb") as pickle_file:  
                    pickle.dump(zakaz_person_pepe,pickle_file,pickle.HIGHEST_PROTOCOL)
            zakaz_person_bbqbeef[x] = 0
            with open("data\\zakaz_person_bbqbeef.dat","wb") as pickle_file:  
                    pickle.dump(zakaz_person_bbqbeef,pickle_file,pickle.HIGHEST_PROTOCOL)
            zakaz_person_grillchicken[x] = 0
            with open("data\\zakaz_person_grillchicken.dat","wb") as pickle_file:  
                    pickle.dump(zakaz_person_grillchicken,pickle_file,pickle.HIGHEST_PROTOCOL)
            zakaz_person_cheesecake[x] = 0
            with open("data\\zakaz_person_cheesecake.dat","wb") as pickle_file:  
                    pickle.dump(zakaz_person_cheesecake,pickle_file,pickle.HIGHEST_PROTOCOL)
            zakaz_person_sorbet[x] = 0
            with open("data\\zakaz_person_sorbet.dat","wb") as pickle_file:  
                    pickle.dump(zakaz_person_sorbet,pickle_file,pickle.HIGHEST_PROTOCOL)
            zakaz_person_mam[x] = 0
            with open("data\\zakaz_person_mam.dat","wb") as pickle_file:  
                    pickle.dump(zakaz_person_mam,pickle_file,pickle.HIGHEST_PROTOCOL)
            zakaz_money_list[x] = 0
            with open("data\\zakaz_money_list.dat","wb") as pickle_file:  
                    pickle.dump(zakaz_money_list,pickle_file,pickle.HIGHEST_PROTOCOL)
            zakaz_admin_stat[x] = 0
            with open("data\\zakaz_admin_stat.dat","wb") as pickle_file:  
                    pickle.dump(zakaz_admin_stat,pickle_file,pickle.HIGHEST_PROTOCOL)
            zakaz_admin_id = person_list[x]
            bot.send_message(zakaz_admin_id,'Ваше замовлення відхилено адміністратором.')
        if call.data == 'zakaz_admin_finish':
            bot.send_message(call.message.chat.id,'Замовлення виконано. Повідомлення клієнту надіслано.')
            x = zakaz_mess_list.index(call.message.text)
            zakaz_all_money.append(zakaz_money_list[x])
            with open("data\\zakaz_all_money.dat","wb") as pickle_file:  
                    pickle.dump(zakaz_all_money,pickle_file,pickle.HIGHEST_PROTOCOL)
            zakaz_person_mari[x] = 0
            with open("data\\zakaz_person_mari.dat","wb") as pickle_file:  
                    pickle.dump(zakaz_person_mari,pickle_file,pickle.HIGHEST_PROTOCOL)
            zakaz_person_marg[x] = 0
            with open("data\\zakaz_person_marg.dat","wb") as pickle_file:  
                    pickle.dump(zakaz_person_marg,pickle_file,pickle.HIGHEST_PROTOCOL)
            zakaz_person_pepe[x] = 0
            with open("data\\zakaz_person_pepe.dat","wb") as pickle_file:  
                    pickle.dump(zakaz_person_pepe,pickle_file,pickle.HIGHEST_PROTOCOL)
            zakaz_person_bbqbeef[x] = 0
            with open("data\\zakaz_person_bbqbeef.dat","wb") as pickle_file:  
                    pickle.dump(zakaz_person_bbqbeef,pickle_file,pickle.HIGHEST_PROTOCOL)
            zakaz_person_grillchicken[x] = 0
            with open("data\\zakaz_person_grillchicken.dat","wb") as pickle_file:  
                    pickle.dump(zakaz_person_grillchicken,pickle_file,pickle.HIGHEST_PROTOCOL)
            zakaz_person_cheesecake[x] = 0
            with open("data\\zakaz_person_cheesecake.dat","wb") as pickle_file:  
                    pickle.dump(zakaz_person_cheesecake,pickle_file,pickle.HIGHEST_PROTOCOL)
            zakaz_person_sorbet[x] = 0
            with open("data\\zakaz_person_sorbet.dat","wb") as pickle_file:  
                    pickle.dump(zakaz_person_sorbet,pickle_file,pickle.HIGHEST_PROTOCOL)
            zakaz_person_mam[x] = 0
            with open("data\\zakaz_person_mam.dat","wb") as pickle_file:  
                    pickle.dump(zakaz_person_mam,pickle_file,pickle.HIGHEST_PROTOCOL)
            zakaz_money_list[x] = 0
            with open("data\\zakaz_money_list.dat","wb") as pickle_file:  
                    pickle.dump(zakaz_money_list,pickle_file,pickle.HIGHEST_PROTOCOL)
            zakaz_admin_stat[x] = 2
            with open("data\\zakaz_admin_stat.dat","wb") as pickle_file:  
                    pickle.dump(zakaz_admin_stat,pickle_file,pickle.HIGHEST_PROTOCOL)
            zakaz_admin_id = person_list[x]
            bot.send_message(zakaz_admin_id,'Ваше замовлення виконано. Гарного дня')

     
bot.polling(none_stop=True,interval=0)


