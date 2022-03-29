import os
import time
import sys

try:
    with open ('t.txt',encoding='utf-8') as f:
        text=f.read()                                       #открываем и считываем файл
        if text=='':                                        #если файл пуст, то просим...
            print("\nДобавьте текст в файл.")
            sys.exit()
            
        input_word=input('Введите слово:')                  #просим ввести слово с клавиатуры
        start = time.time()
        print("\n-----Результат работы программы-----\n-----Локальное время",time.ctime(),"-----")
        print()

        word=' '+input_word+' '                             #отделяем слово пробелом
        Word=' '+input_word.capitalize()+' '                #тоже самое, только с заглавной буквы
        
        text_c=text.replace('!', '.')                       #заменяем знаки конца предл. на "."
        text_c=text_c.replace('?', '.')                         
        text_c=text_c.replace('...', '.')
        sent=text_c.split('.')                              #разделяем текст по предложениям
        senten=sent.copy()                                  #делаем копию
        
        for i in range(len(sent)-1):                        #стираем перенос, запятую, скобки, 
            sent[i]=' '+sent[i].replace('\n', '')+' '       #кавычки, двоеточие
            senten[i]=' '+senten[i].replace('\n', '')+' '
            senten[i]=senten[i].replace(',', '')
            senten[i]=senten[i].replace('(', '')
            senten[i]=senten[i].replace(')', '')
            senten[i]=senten[i].replace('"', '')
            senten[i]=senten[i].replace(';', '')
            senten[i]=senten[i].replace(':', '')
              
        for i in range(len(sent)-1):                        #поиск и подсчет слов с помощью метода
            count_small=senten[i].count(word)               #str.count(sub)
            count_big=senten[i].count(Word)       
            count=count_small+count_big
            sent[i]=sent[i].strip()+'.'+'['+str(count)+']'  #приписываем кол-во слов после предложения
        
        
        txt=' '.join(sent)                                  #обьединяем предложения в строку 
        print(txt)                                          #выводим редактированный текст

    finish = time.time()
    result = finish - start                                 #определяем время и память работы программы
    print("\nProgram time: "+ str(result) +" seconds.")
    print("Program size: "+ str(os.path.getsize('lab_2-3.py')) +" bytes.")
    
except ValueError:
    print("\nэто не слово")

except FileNotFoundError:
    print("\nФайл t.txt не найден в директории проекта.\nДобавьте файл в директорию или переименуйте существующий файл.")
