import requests as rq
import xml.etree.ElementTree as ET


def create_dict(xml_root):
    # создает словарь {"название валюты": курс}
    dict = {}
    for i in range(len(xml_root)):
        dict[xml_root[i][3].text] = xml_root[i][4].text
    return dict
   
   
def user_action(curr_dict):

    # взаимодействие с пользователем
    
    while True:
    
        name = input("\nВведите название валюты: ")
        
        if name in curr_dict.keys():
        
            print("\n\tВы выбрали: ", name)
            print("\tТекущий курс: ", curr_dict[name])
            print("\n")
            break
        else:
            
            print("\nПо данной валюте нет данных. Проверьте, верно ли введено название валюты. \nОбратите внимание на верхний регистр. Допустимые варианты:\n")
            for key in curr_dict.keys():
                print("\t - ", key)
            ans = input("\n Попробуете ввести название ещё раз? да / нет: ")
            
            if ans in "ДАдаYESyes":
                continue
            else:
                break
                
    print("\n\tДо свидания!")
    print("\n")


def main():

    cbr_link = 'http://www.cbr.ru/scripts/XML_daily.asp'
    mirror_link = 'https://www.cbr-xml-daily.ru/daily.xml'
    
    fail = False

    try:
        cbr = rq.get(cbr_link) # сохраняет содержание страницы как объект           
        
        root = ET.fromstring(cbr.text) # получаем XML объект
        fail = False
        
    except:
        try:
            cbr = rq.get(mirror_link) # сохраняет содержание страницы как объект           
            
            root = ET.fromstring(cbr.text) # получаем XML объект
            fail = False
            
        except:
            fail = True
            
            print("\nК сожалению, данные сейчас не доступны. \nПроверьте соединение с интернетом или попробуйте позже.\n")
            
    # root.tag -> ValCurs
    '''
    
    Структура
    
    
    <ValCurs Date="10.02.2021" name="Foreign Currency Market">
        <Valute ID="R01010">
            <NumCode>036</NumCode>
            <CharCode>AUD</CharCode>
            <Nominal>1</Nominal>
            <Name>Австралийский доллар</Name>
            <Value>57,1385</Value>  
            
    '''
    
    if not fail:
        all_cm = create_dict(root) # получаем словарь название - курс
        
        print("\n\t Курсы валют ЦБ РФ\n")
        
        print("\t Дата актуальности информации: ", root.attrib['Date'])
        
        user_action(all_cm) # I - название валюты, O - выбранная валюта и её курс
    
    
   
if __name__=="__main__":
    main()