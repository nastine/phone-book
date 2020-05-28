import textwrap

class Contact:
    def __init__(self, name, surname, phone_number, fav=False, **kwargs):
        self.name = name 
        self.surname = surname
        self.phone_number = phone_number
        self.fav = fav
        self.__dict__.update(kwargs)
    

    def __str__(self):
        kwargs = ['%s: %s' % (key, val) for (key, val) in self.__dict__.items()]
        nl = '\n\t'
        return f"Имя: {self.name}\nФамилия: {self.surname}\nТелефон: {self.phone_number}\nВ избранных: {'нет' if self.fav==False else 'да'}\nДополнительная информация:\n\t{(nl.join(kwargs[4:]))}\n"

            
jhon = Contact('Jhon', 'Smith', '+71234567809', telegram='@jhony', email='jhony@smith.com')
derek = Contact('Derek', 'Nolan', '+71234560987', fav=True, instagram='@dnolan', email='derek@gmail.com')
# print(jhon)
# print(derek)


class PhoneBook:

    def __init__(self, name, contact_list, **kwags):
        self.name = name
        self.contact_list = contact_list


    def show_contacts(self):
        for contact in self.contact_list:
            print(contact)


    def add_new(self, contact):
        if contact not in self.contact_list:
            self.contact_list.append(contact)
            print(f'Контакт {contact.name} {contact.surname} успешно добавлен.')
        else:
            print(f'Контакт {contact.name} {contact.surname} уже существует.')


    def delete_contact(self, number):
        found_numbers =[]
        for contact in self.contact_list:
            if contact.phone_number == number:
                print(f'Контакт {contact.name} {contact.surname} успешно удален.')
                self.contact_list.remove(contact)
                found_numbers.append('1')
        if len(found_numbers)==0:
            print('Контакт с данным номером телефона не найден.')


    def show_favs(self):
        found_contacts =[]
        for contact in self.contact_list:
            if contact.fav == True:
                print(contact)
                found_contacts.append('1')
        if len(found_contacts)==0:
            print('В вашей телефонной книге ни один контакт не добавлен в избранные.')


    def search_contact(self, person):
        found_contacts =[]
        for contact in self.contact_list:
            if contact.name == person.split()[0] and contact.surname == person.split()[1]:
                print(contact)
                found_contacts.append('1')
        if len(found_contacts)==0:
            print('Данный контакт не найден.')
        

if __name__ == "__main__":
    
    contact_list = []
    my_phonebook = PhoneBook("Фоунбук", contact_list)
    my_phonebook.add_new(jhon)
    my_phonebook.add_new(derek)
    my_phonebook.show_favs()
    my_phonebook.delete_contact('+71234567809')
    my_phonebook.show_contacts()
    my_phonebook.search_contact('Derek Nolan')

#Задание №3

def adv_print(*args, **kwargs):
    params = {'start':'\n', 'in_file':False, 'max_line':'80'} 
    params.update(kwargs)
    
    for item in args:
        if len(item) <= int(params['max_line']):
            result = item
        else:
            result = textwrap.fill(item, width=int(params['max_line']))
        
        if params['in_file'] == False:
            
                print(params['start'])
                print(result)
        else:
            with open('result.txt', 'w') as f:
                f.write(params['start'])  
                f.write(result)              




adv_print("Oublie ton passé qu'il soit simple ou composé, participe au présent et ton futur sera plus que parfait.", max_line=10)
    

