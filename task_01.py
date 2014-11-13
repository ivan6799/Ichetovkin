import  math
# step-4 Инкапсуляция
# Инкапсуляция:
#1.языковая конструкция, позволяющая связать данные с методами, предназначенными для обработки этих данных;
#2.механизм языка, позволяющий ограничить доступ одних компонентов программы к други
# Геттеры/Сеттеры, рассмотренные в прошлом шаге, тоже относятся к парадигме "Инкапсуляция"
class Block:
    def __init__(self, coords, width, height, color):
        self.x = coords[0]
        self.y = coords[1]
        #self.coords = coords
        self.width = width
        self.height = height
        self.color = color

    def get_area(self):
        """
        Возвращает площадь данного блока
        """
        return self.width*self.height

    def set_width(self, new_width):
        """
        Установка нового значения высоты (проверка корректнсти звведенного значения)
        """
        if type(new_width) is not int:#Если тип не int
            print("Error: Попытка задать некорректный тип свойства width")
            return -1
        elif new_width<0:
            print("Error: Попытка задать отритцательное зачение свойства widht")
        else:
            self.width = new_width

    def set_coords(self, new_coords):
        """
        Задает новые координаты объекта
        """
        self.x = new_coords[0]
        self.y = new_coords[1]
        #self.coords = new_coords


    def change_color(self, new_color):# Изменение цвета
        if type(new_color) is not str:
            print("Error")
        else:
            self.color = new_color

    def set_nw_nh(self, new_width, new_height): #Изменения размера

            self.height = self.height + new_height
            self.width = new_width + self.width

    def move_on(self, move):#Перемещение

        self.x += move
        self.y += move



def sort_big_to_min(list): #Сортировка
    k = 0
    while k+1 < len(list):
        if list[k].width*list[k].height < list[k+1].height*list[k+1].width:
            list[k], list[k+1] = list[k+1], list[k]
            k = 0
        else:
            k +=1
    return list

def center_point(list, k):
    cord_1 = (list[k].x, list[k].y)
    cord_2 = (list[k].x+ list[k].width, list[k].y + list[k].height)
    cord_cp = ((cord_1[0]+cord_2[0])/2,(cord_1[1]+cord_2[1])/2)
    return cord_cp






redSmallBlock = Block((20,40),20,10,"red")
blueBigBlock = Block((60,10),120,100,"blue")
#Мы решили передвинуть наш прямоугольник на координаты (100,100). Можно конечно указать новые координаты напрямую:
redSmallBlock.x = 100
redSmallBlock.y = 100
#Но если мы решим изменить структуру хранения координат,
#напримем будем хранить координаты в виде кортежа self.coords = coords
#То вам придется переписывать весь код использующий ваш Класс, но можно поступить проще
#Создадим метод-сеттер для установки новых координат set_coorda()
#Теперь для изменения коорлинат пользователи вашего класса просто буду вызывать метод, а вы можете хранить координаты
# в люббом удобном вам виде
#На ЗАМЕТКУ: Не обязательно метод называть set_coord, по сути этот метод передвигает прямоугольник на указанные координаты,
#возможно гораздо удобнее будет назвать его move_to(...), это уж как вам удобнее, все зависит от целей и задачи.
redSmallBlock.set_coords((100,100)) #Вместо прямого обращения redSmallBlock.x = 100, redSmallBlock.y = 100

#ВАЖНО! Не злоупотребляйте сеттерами и геттрерами, не стоит их делать в огромнхы количествах для всех свойств!
#Где нужны методы, а где проще предоставлять прямой доступ к свойствам придет только с опытом.


object_list = []
i = 0
w = 160
h = 140
x = 0
y = 0
while i < 10:
    a = Block((x+i,y+i), w + 2*i, h + 2*i, "black")
    b = Block((x+2*i,y+2*i), w + 1*i, h + 1*i, "purple")
    c = Block((x+3*i,y+3*i), w + 3*i, h+ 3*i, "blue")
    d = Block((x+4*i,y+4*i), 4*w + 2*i, + 4*h + 2*i, "red")
    object_list.append(a)
    object_list.append(b)
    object_list.append(c)
    object_list.append(d)
    i +=1


k = 0
new_x = 20
new_y = 20

#while True: """Тест сортировки"""
   # print("До")
    #while k<39:
      #  print(object_list[k].width*object_list[k].height)
       # k +=1
   # print("После")
    #k = 0
    #while k<39:
        #print(sort_big_to_min(object_list)[k].width*sort_big_to_min(object_list)[k].height)
        #k+=1
    #k = 0
    #break

new_ccx = 150
new_ccy = 800

while k+1 < len(object_list):
    object_list[k].x = new_ccx - object_list[k].width
    object_list[k].y = new_ccy - object_list[k].height
    k +=1








