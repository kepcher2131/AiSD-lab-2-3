with open ('t.txt',encoding='utf-8') as f:
    text=f.read()                           #открываем и считываем файл
    
    input_word=input('Введите слово:')      #просим ввести слово с клавиатуры
    word=' '+input_word                     #отделяем слово пробелом
    Word=' '+input_word.capitalize()        #тоже самое, только с заглавной буквы
    sent=text.split('.')                    #разделяем текст по предложениям
    
    for i in range(len(sent)-1):            #ставим пробел перед предложением,  
        sent[i]=' '+sent[i]                 #чтоб считывать первое слово
    
    for i in range(len(sent)-1):            #поиск и подсчет слов с помощью метода
        count_small=sent[i].count(word)     #str.count(sub)
        count_big=sent[i].count(Word)       
        count=count_small+count_big
        sent[i]=sent[i]+'.'+'['+str(count)+']'#приписываем кол-во слов после предл.
    
    for i in range(len(sent)-1):            
        sent[i]=sent[i].lstrip()            #удаляем пробел в начале предложения
    
    txt=' '.join(sent)                      #обьединяем предложения в строку 
    print(txt)                              #выводим редактированный текст

