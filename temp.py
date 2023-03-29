import pygame_widgets
import pygame
from pygame_widgets.textbox import TextBox
import datetime as dt
import time
import os
import sys

pygame.init()

W, H = 800, 600
screen = pygame.display.set_mode((W, H))
pygame.display.set_caption('School_siron')

pygame.mixer.init()
pygame.mixer.music.load('00101.mp3')

my_font = pygame.font.Font('fonts/shrift.otf', 40)

Les, Sm_sc_br, Bi_sc_br, Bb = None, None, None, None


def print_text(message, x, y, font_color=(0, 0, 0), font_type='fonts/shrift.otf', font_size=15):
    font_type = pygame.font.Font(font_type, font_size)
    text = font_type.render(message, True, font_color)
    screen.blit(text, (x, y))


class Button:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.enactive_color = (112, 102, 58)
        self.active_color = (23, 204, 58)

    def draw(self, x, y, text, action=None, font_size=30):
        try:
            mouse = pygame.mouse.get_pos()
            click = pygame.mouse.get_pressed()

            if x < mouse[0] < x + self.width and y < mouse[1] < y + self.height:
                # print('Зашёл в проверку x и y')

                pygame.draw.rect(screen, self.active_color, (x, y, self.width, self.height))

                if click[0] == 1:
                    # print('Ку-ку')
                    if action:
                        # print('Зашёл в action')
                        action()

            else:
                pygame.draw.rect(screen, self.enactive_color, (x, y, self.width, self.height))

            print_text(text, x + 10, y + 35)
        except:
            print('Ошибка в в методе draw класса Button')


def counter_siren(lesson=40, small_school_break=10, big_school_break=20, bbal=[4]):  # bbal => big_break_after_lessons
    try:

        print('Внутри counter_siren')

        flag = True
        list_start_action = ['8:00']
        hour = 8
        minutes = 0

        while len(list_start_action) < 30:
            if flag:
                print(lesson)
                minutes += lesson
                if minutes >= 60:
                    hour += 1
                    minutes = minutes % 60
                flag = not flag

                if minutes == 0:
                    list_start_action.append(':'.join((str(hour) + " " + (str(minutes) + '0')).split()))
                else:
                    list_start_action.append(':'.join((str(hour) + " " + str(minutes)).split()))
            else:
                for i in bbal:
                    if len(list_start_action) == i * 2:
                        minutes += big_school_break
                    else:
                        minutes += small_school_break
                if minutes >= 60:
                    hour += 1
                    minutes = minutes % 60
                flag = not flag

                if minutes == 0:
                    list_start_action.append(':'.join((str(hour) + " " + (str(minutes) + '0')).split()))
                else:
                    list_start_action.append(':'.join((str(hour) + " " + str(minutes)).split()))
        return list_start_action
    except Exception as e:
        print('Ошибка в функции counter_siren')
        print(e)


def main_window():
    try:

        print('Внутри main_window')
        show = True

        button = Button(100, 100)

        txt = 0

        while show:

            events = [event for event in pygame.event.get()]

            for event in events:
                if event.type == pygame.QUIT:
                    show = False
                    pygame.quit()

            if Les and ((Sm_sc_br or Bi_sc_br or Bb) is False):
                sp = counter_siren(lesson=Les)
            elif (Les and Sm_sc_br) and ((Bi_sc_br or Bb) is False):
                sp = counter_siren(lesson=Les, small_school_break=Sm_sc_br)
            elif (Les and Sm_sc_br and Bi_sc_br) and (Bb is False):
                sp = counter_siren(lesson=Les, small_school_break=Sm_sc_br, big_school_break=Bi_sc_br)
            elif Les and Sm_sc_br and Bi_sc_br and Bb:
                sp = counter_siren(lesson=Les, small_school_break=Sm_sc_br, big_school_break=Bi_sc_br, bbal=Bb)
            else:
                sp = counter_siren()

            # print(sp)
            # sp = ['14:22', '15:02', '15:42']
            print(sp)
            sp2 = []

            start_diap = 0  # Старт диапазона (урока)
            stop_diap = 0  # Конец диапазона (урока)

            my_time = dt.datetime.now()
            now_hour = my_time.hour
            now_minute = my_time.minute
            now_second = my_time.second
            correct_time = ':'.join([str(now_hour), str(now_minute)])

            if len(str(now_minute)) == 1:
                glue_time = int(str(now_hour) + '0' + str(now_minute))

            else:
                glue_time = int(str(now_hour) + str(now_minute))

            for element in sp:
                sp2.append(int(''.join(element.split(':'))))

            for i in sp2:
                if glue_time >= i:
                    start_diap = i
                else:
                    stop_diap = i
                    break
            temp = sp[sp2.index(stop_diap)].split(':')

            temp_h = int(temp[0]) * 60
            temp_m = int(temp[1])

            print(abs((now_hour * 60 + now_minute) - (temp_h + temp_m)))

            if correct_time in sp and now_second == 0:
                pygame.mixer.music.play()

            txt = abs((now_hour * 60 + now_minute) - (temp_h + temp_m))

            screen.fill((50, 115, 60))

            button.draw(10, 10, 'Настройки', switch)

            text_surface = my_font.render(f'До звонка осталось {txt} минуты', True, 'black')

            screen.blit(text_surface, (120, 150))

            # screen.blit(settings, (25, 25))

            pygame.display.update()

            pygame.display.flip()
    except Exception as e:
        print(e)
        print('Ошибка в функции main_window')


def switch():
    try:
        admin_window()
    except:
        print('Ошибка в функции switch')


class Txt:
    def __init__(self):
        try:
            self.Tb1, self.Tb2, self.Tb3, self.Tb4 = 40, 10, 20, [4]
        except:
            print('Ошибка при инициализации класса Txt')


def save():
    global Les, Sm_sc_br, Bi_sc_br, Bb

    print('Внутри save')

    try:
        if txt_xd.Tb1.getText() != '':
            Les = int(txt_xd.Tb1.getText())

        if txt_xd.Tb2.getText() != '':
            Sm_sc_br = int(txt_xd.Tb2.getText())

        if txt_xd.Tb3.getText() != '':
            Bi_sc_br = int(txt_xd.Tb3.getText())

        if txt_xd.Tb4.getText() != '':
            Bb = list(map(int, txt_xd.Tb4.getText().split()))

        # return txt_xd.Tb1.getText, txt_xd.Tb2.getText, txt_xd.Tb3.getText, txt_xd.Tb4.getText

    except Exception as e:
        print(e)
        print('Ошибка в функции save')


def admin_window():
    try:

        print('Внутри admin_window')

        def of1():
            # Get text in the textbox
            print(Tb1.getText())

        def of2():
            # Get text in the textbox
            print(Tb2.getText())

        def of3():
            # Get text in the textbox
            print(Tb3.getText())

        def of4():
            # Get text in the textbox
            print(Tb4.getText())

        show = True

        button_switch = Button(100, 100)

        button_save = Button(100, 100)

        Tb1 = TextBox(screen, 420, 55, 180, 40, fontSize=30,
                      borderColour=(255, 0, 0), textColour=(0, 200, 0),
                      onSubmit=of1, radius=10, borderThickness=2)

        Tb2 = TextBox(screen, 420, 150, 180, 40, fontSize=30,
                      borderColour=(255, 0, 0), textColour=(0, 200, 0),
                      onSubmit=of2, radius=10, borderThickness=2)

        Tb3 = TextBox(screen, 420, 245, 180, 40, fontSize=30,
                      borderColour=(255, 0, 0), textColour=(0, 200, 0),
                      onSubmit=of3, radius=10, borderThickness=2)

        Tb4 = TextBox(screen, 420, 340, 180, 40, fontSize=30,
                      borderColour=(255, 0, 0), textColour=(0, 200, 0),
                      onSubmit=of4, radius=10, borderThickness=2)

        txt_xd.Tb1 = Tb1
        txt_xd.Tb2 = Tb2
        txt_xd.Tb3 = Tb3
        txt_xd.Tb4 = Tb4

        while show:

            events = [event for event in pygame.event.get()]

            for event in events:
                if event.type == pygame.QUIT:
                    show = False
                    exit()

            screen.fill((0, 23, 57))

            print_text('Длина Урока:', 70, 65, font_color=(0, 255, 0), font_size=20)

            print_text('Длина перемены:', 50, 160, font_color=(0, 255, 0), font_size=20)

            print_text('Длина большой перемены:', 12, 255, font_color=(0, 255, 0), font_size=20)

            print_text('После каких уроков большая перемена:', 5, 350, font_color=(0, 255, 0), font_size=20)

            # print(Tb1.getText())

            button_switch.draw(690, 10, 'Назад', main_window)

            button_save.draw(690, 490, 'Сохранить', save)

            # screen.blit(settings, (25, 25))

            pygame.display.update()
            pygame_widgets.update(events)

            pygame.display.flip()
    except:
        print('Ошибка в функции admin_window')


if __name__ == '__main__':
    txt_xd = Txt()
    main_window()
