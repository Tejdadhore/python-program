#contect book

contects = {}

def add_con():
    name = input("enter you name : ")
    number = int(input("enter you number : "))
    mail = input("enter you mail : ")
    add = input("enter you adderess : ")
    contects[name] ={"number":number,"mail":mail,"add":add}
    print("contect added successfully ! ")

def viwe_con():
    print("contect book")
    '''for name,number,mail,add in contects.items():
        print(f"{name}:({number}\n\t-{mail}\n\t-{add})")'''
    print(contects)

def search_con():
    name_s = input("enter search name : ")
    if name_s in contects:
        print(f"{name_s}:{contects[name_s]['number']}\n('mail -->'{contects[name_s]['mail']} ,\n'add. -->' {contects[name_s]['add']})")
    else:
        print("contect not found !")
def delete_con():
    name = input("enter you delet contect : ")
    if name in contects:
        del contects[name]
        print("contect deleted successfully ")
    else:
        print("contect not found")
def update_con():
    name = input("enter name to update contect :")
    if name in contects:
        del contects[name]
        name = input("enter you name : ")
        number = int(input("enter you number : "))
        mail = input("enter you mail : ")
        add = input("enter you adderess : ")
        contects[name] ={"number":number,"mail":mail,"add":add}
        print("contect updated successfully ! ")
    else:
        ("contect not update !")

print("--- select one option ---")
print("1. add contect")
print("2. viwe contect")
print("3. search contect")
print("4. update contect")
print("5. delete contect")
print("6. quite")

while True:
    choices = ('1','2','3','4','5','6')
    chooce = input("enter you choice : ")
    if chooce in choices:
        if chooce == '1':
            add_con()
        elif chooce == '2':
            viwe_con()
        elif chooce == '3':
            search_con()
        elif chooce == '4':
            update_con()
        elif chooce == '5':
            delete_con()
        elif chooce == '6':
            break
        else:
            print("invalid choice")

    else:
        print("choise corect option !")
        