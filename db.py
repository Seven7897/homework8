import sqlite3
import datetime

def add():
    base = sqlite3.connect('new.db')
    cur = base.cursor()

    base.execute('CREATE TABLE IF NOT EXISTS data(name, surname, phonenumber PRIMARY KEY, comment)')
    base.commit
    name = input("name : ")
    surname = input("surname : ")
    phonenumber = input("phone number : ")
    comment = input("comment : ")
    cur.execute('INSERT INTO data VALUES(?, ?, ?, ?)',(name, surname, phonenumber, comment))
    x = datetime.datetime.now()
    data = open('story.txt','a' , encoding='utf-8')
    data.writelines(f"{x} Добавлен : {name}, {surname}, {phonenumber}, {comment}\n")
    data.close()

    base.commit()

def delete():
    base = sqlite3.connect('new.db')
    cur = base.cursor()
    variant = int(input("Удаляем по : \n 1 если по name \n 2 если по surname \n 3 если по phone number \n 4 если по comment : "))
    if variant == 1:
        name = input("Введите имя кого удаляем ? ")
        m = datetime.datetime.now()
        data = open('story.txt','a' , encoding='utf-8')
        data.writelines(f"{m} Удален пользователь с именем : {name}\n")
        data.close()
        cur.execute('DELETE FROM data WHERE name == ?', (name,)) 
        base.commit()
    if variant == 2:
        surname = input("Введите фалидию кого удаляем ? ")
        x = datetime.datetime.now()
        data = open('story.txt','a' , encoding='utf-8')
        data.writelines(f"{x} Удален пользователь с фамилией : {surname}\n")
        data.close()
        cur.execute('DELETE FROM data WHERE surname == ?', (surname,)) 
        base.commit()
    if variant == 3:
        phonenumber = input("Введите телефоном кого удаляем ? ")
        x = datetime.datetime.now()
        data = open('story.txt','a' , encoding='utf-8')
        data.writelines(f"{x} Удален пользователь с телефоном : {phonenumber} \n")
        data.close()
        cur.execute('DELETE FROM data WHERE phonenumber == ?', (phonenumber,)) 
        base.commit()
    if variant == 4:
        comment = input("Введите комментарий кого удаляем ? ")
        x = datetime.datetime.now()
        data = open('story.txt','a' , encoding='utf-8')
        data.writelines(f"{x} Удален пользователь с именем : {comment}\n")
        data.close()
        cur.execute('DELETE FROM data WHERE comment == ?', (comment,)) 
        base.commit()

def update():
    base = sqlite3.connect('new.db')
    cur = base.cursor()
    variant = int(input("Что обновляем ? \n 1 если name \n 2 если surname  \n 3 если phonenumber \n 4 если comment : "))
    variant_1 = int(input("На что обновляем ? \n 1 если name \n 2 если surname \n 3 если phonenumber \n 4 если comment : "))
    if variant == 1 and variant_1 == 1:
        new_name = input("Введите на которое нужно поменять  : ")
        old_name = input("Введите у которого нужно поменять  : ")
        x = datetime.datetime.now()
        data = open('story.txt','a' , encoding='utf-8')
        data.writelines(f"{x} Обновлен пользователь с именем : {old_name}  на  {new_name} \n")
        data.close()
        cur.execute('UPDATE data SET name == ? WHERE name == ?', (new_name, (old_name))) 
        base.commit()
    if variant == 1 and variant_1 == 2:
        new_name = input("Введите на которое нужно поменять  : ")
        surename = input("Введите на которое нужно поменять  : ")
        x = datetime.datetime.now()
        data = open('story.txt','a' , encoding='utf-8')
        data.writelines(f"{x} Обновлен имя пользователя с фамилией : {surename}  на  {new_name} \n")
        data.close()
        cur.execute('UPDATE data SET name == ? WHERE surname == ?', (new_name, (surename))) 
        base.commit()
    if variant == 1 and variant_1 == 3:
        new_name = input("Введите на которое нужно поменять  : ")
        phonenumber = input("Введите на которое нужно поменять  : ")
        x = datetime.datetime.now()
        data = open('story.txt','a' , encoding='utf-8')
        data.writelines(f"{x} Обновлен имя пользователь с телефоном : {phonenumber}  на  {new_name} \n")
        data.close()
        cur.execute('UPDATE data SET name == ? WHERE phonenumber == ?', (new_name, (phonenumber))) 
        base.commit()
    if variant == 1 and variant_1 == 4:
        new_name = input("Введите на которое нужно поменять  : ")
        comment = input("Введите на которое нужно поменять  : ")
        x = datetime.datetime.now()
        data = open('story.txt','a' , encoding='utf-8')
        data.writelines(f"{x} Обновлен имя пользователь с коментарием : {new_name}  на  {comment} \n")
        data.close()
        cur.execute('UPDATE data SET name == ? WHERE comment == ?', (new_name, (comment))) 
        base.commit()
    if variant == 2 and variant_1 == 1:
        new_surename = input("Введите на которое нужно поменять  : ")
        name = input("Введите на которое нужно поменять  : ")
        x = datetime.datetime.now()
        data = open('story.txt','a' , encoding='utf-8')
        data.writelines(f"{x} Обновлен фамилия пользователь с именем : {name}  на  {new_surename} \n")
        data.close()
        cur.execute('UPDATE data SET surname == ? WHERE name == ?', (new_surename, (name))) 
        base.commit()
    if variant == 2 and variant_1 == 2:
        new_surename = input("Введите на которое нужно поменять  : ")
        surname = input("Введите на которое нужно поменять  : ")
        x = datetime.datetime.now()
        data = open('story.txt','a' , encoding='utf-8')
        data.writelines(f"{x} Обновлен пользователь с фамилией : {surname}  на  {new_surename} \n")
        data.close()
        cur.execute('UPDATE data SET surname == ? WHERE surname == ?', (new_surename, (surname))) 
        base.commit()
    if variant == 2 and variant_1 == 3:
        new_surename = input("Введите на которое нужно поменять  : ")
        phonenumber = input("Введите на которое нужно поменять  : ")
        x = datetime.datetime.now()
        data = open('story.txt','a' , encoding='utf-8')
        data.writelines(f"{x} Обновлен фамилия пользователь с телефоном : {phonenumber}  на  {new_surename} \n")
        data.close()
        cur.execute('UPDATE data SET surname == ? WHERE phonenumber == ?', (new_surename, (phonenumber))) 
        base.commit()
    if variant == 2 and variant_1 == 4:
        new_surename = input("Введите на которое нужно поменять  : ")
        comment = input("Введите на которое нужно поменять  : ")
        x = datetime.datetime.now()
        data = open('story.txt','a' , encoding='utf-8')
        data.writelines(f"{x} Обновлен фамилия пользователь с комментарием : {comment}  на {new_surename} \n")
        data.close()
        cur.execute('UPDATE data SET surname == ? WHERE comment == ?', (new_surename, (comment))) 
        base.commit()
    if variant == 3 and variant_1 == 3:
        new_phonenumber = input("Введите на которое нужно поменять  : ")
        phonenumber = input("Введите на которое нужно поменять  : ")
        x = datetime.datetime.now()
        data = open('story.txt','a' , encoding='utf-8')
        data.writelines(f"{x} Обновлен пользователь с телефоном : {phonenumber}  на  {new_phonenumber} \n")
        data.close()
        cur.execute('UPDATE data SET phonenumber == ? WHERE phonenumber == ?', (new_phonenumber, (phonenumber))) 
        base.commit()
    if variant == 4 and variant_1 == 4:
        new_comment = input("Введите на которое нужно поменять  : ")
        old_comment = input("Введите на которое нужно поменять  : ")
        x = datetime.datetime.now()
        data = open('story.txt','a' , encoding='utf-8')
        data.writelines(f"{x} Обновлен пользователь с комментарием : {old_comment}  на  {new_comment} \n")
        data.close()
        cur.execute('UPDATE data SET comment == ? WHERE comment == ?', (new_comment, (old_comment))) 
        base.commit()


def find():
    base = sqlite3.connect('new.db')
    cur = base.cursor()
    variant = int(input("Выберите поиск чего : \n 1 если  name :  \n 2 если  surname :   \n 3 если  phone numbers : \n 4 если  comment : "))
    variant_2 = int(input("Выберите поиск по : \n 1 если по name :  \n 2 если по surname :   \n 3 если по phone numbers : \n 4 если по comment : "))
    if variant == 1 and variant_2 == 2 :
        read = cur.execute('SELECT name FROM data WHERE surname == ?', (input(': '),)).fetchone()  
        print(read)
    if variant == 1 and variant_2 == 3 :
        read = cur.execute('SELECT name FROM data WHERE phonenumber == ?', (input(': '),)).fetchone()  
        print(read)
    if variant == 1 and variant_2 == 4 :
        read = cur.execute('SELECT name FROM data WHERE comment == ?', (input(': '),)).fetchone()  
        print(read)
    if variant == 2 and variant_2 == 1 :
        read = cur.execute('SELECT surname FROM data WHERE name == ?', (input(': '),)).fetchone()  
        print(read)
    if variant == 2 and variant_2 == 3 :
        read = cur.execute('SELECT surname FROM data WHERE phonenumber == ?', (input(': '),)).fetchone()  
        print(read)
    if variant == 2 and variant_2 == 4 :
        read = cur.execute('SELECT surname FROM data WHERE comment == ?', (input(': '),)).fetchone()  
        print(read)
    if variant == 3 and variant_2 == 1 :
        read = cur.execute('SELECT phonenumber FROM data WHERE name == ?', (input(': '),)).fetchone()  
        print(read)
    if variant == 3 and variant_2 == 2 :
        read = cur.execute('SELECT phonenumber FROM data WHERE surname == ?', (input(': '),)).fetchone()  
        print(read)
    if variant == 3 and variant_2 == 4 :
        read = cur.execute('SELECT phonenumber FROM data WHERE comment == ?', (input(': '),)).fetchone()  
        print(read)
    if variant == 4 and variant_2 == 1 :
        read = cur.execute('SELECT comment FROM data WHERE name == ?', (input(': '),)).fetchone()  
        print(read)
    if variant == 4 and variant_2 == 2 :
        read = cur.execute('SELECT comment FROM data WHERE surname == ?', (input(': '),)).fetchone()  
        print(read)
    if variant == 4 and variant_2 == 3 :
        read = cur.execute('SELECT comment FROM data WHERE phonenumber == ?', (input(': '),)).fetchone()  
        print(read)


def find_oll():
    base = sqlite3.connect('new.db')
    cur = base.cursor()
    read = cur.execute('SELECT * FROM data').fetchall() 
    print(read)


