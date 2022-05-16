import datetime
import os
import random
import sys
import time
import easygui
import pygame
from random import randint
from sys import exit
import requests

pygame.init()
pygame.mixer.init()
pygame.key.set_repeat(10, 15)
setting_bg = pygame.Surface((400, 400))
setting_bg.fill((230, 230, 230))

version = "16.3.6"
black_move = 0
lan_move = 0
open_black = 0
going = 1
name_v = 1
last_name = eval("{'1':1}")
keep_key = False
rs_save = True
fcl_save = True
black_error = False
setting_x = 400
should_setting = 400
setting_open = False
ch_lan_x = 400
should_ch_lan = 400
ch_lan_open = False
rs_x = 400
should_rs = 400
rs_open = False
fcl_x = 400
should_fcl = 400
fcl_open = False
his_x = 400
should_his = 400
his_open = False
black_x = 400
should_black = 400
black_open = False

# bf = open("C:\\Draw\\data", "r")
# data_file = eval(bf.read())
# bf.close()

key_lan = ["您的软件已过期或许可证失效，请联系管理员。",
           "Your software has expired or your license has expired. Please contact your administrator.",
           "Votre logiciel a expiré ou votre licence a expiré, veuillez contacter votre administrateur.",
           "Su software ha expirado o su licencia ha expirado. Póngase en contacto con su administrador.",
           "Ваша программа уже просрочена или лицензия не действительна, обратитесь к администратору.",
           "ソフトウェアが期限切れになったり、ライセンスが期限切れになったりした場合は、管理者に連絡してください。"]
done_lan = ["完成。重启以生效。", "Done. Restart to take effect.", "Terminé. Redémarrer pour prendre effet.",
            "Hecho. Reiniciar para tener efecto.", "готово. перезагрузка вступает в силу.", "完了しました。再起動して有効にします。"]
ser_lan = ["您的本地序列号为:", "Your local serial number is:", "Votre numéro de série local est:",
           "Su número de serie local es:"
           "Ваш локальный серийный номер:", "ローカルシリアル番号:"]
input_lan = ["请输入您的密钥:", "Please enter your key:", "Veuillez saisir votre clé:", "Introduzca su clave:",
             "Введите ваш ключ:", "鍵を入力してください:"]
key_error_lan = ["您输入的密钥有误!", "The key you entered is incorrect!", "La clé que yous aver saisie est incorrecte!",
                 "Ha introducido la clave equivocada!", "Ошибка при вводе ключа!", "入力した鍵が間違っています。"]
buy_lan = ["购买", "Get it", "Achetez - le.", "Cómpralo.", "купить", "購入"]

try:
    lan_f = open("C:\\Draw\\lan", "r", encoding='utf-8')
    selected_language = lan_f.read()
    lan_f.close()
except FileNotFoundError:
    selected_language = easygui.buttonbox("Please choose the language:", "Setup",
                                          ["汉语", "English", "Français", "Español", "русский язык", "日本語"])
    if selected_language is None:
        sys.exit()
try:
    f16 = open("C:\\Draw\\lan", "w", encoding='utf-8')
except FileNotFoundError:
    os.mkdir("C:\\Draw\\")
    f16 = open("C:\\Draw\\lan", "w", encoding='utf-8')
f16.write(str(selected_language))
f16.close()

if selected_language == "汉语":
    e = 0
elif selected_language == "日本語":
    e = 5
elif selected_language == "English":
    e = 1
elif selected_language == "Français":
    e = 2
elif selected_language == "Español":
    e = 3
elif selected_language == "русский язык":
    e = 4
else:
    e = 1


class Key:
    def __init__(self):
        global key_lan
        try:
            ask1 = open("C:\\Draw\\asked.dll", "r")
            ask1.close()
        except FileNotFoundError:
            try:
                os.remove("C:\\Draw\\key")
            except FileNotFoundError:
                pass
            try:
                os.remove("C:\\Draw\\used.dll")
            except FileNotFoundError:
                pass
            try:
                os.mkdir("C:\\Draw\\")
            except FileExistsError:
                pass
            asked = open("C:\\Draw\\asked.dll", "w")
            asked.write("")
            asked.close()
            key_lan = ["欢迎使用抽号软件", "Welcome to Draw", "Bienvenue au logiciel flash",
                       "Bienvenido al software de numeración", "Добро пожаловать использовать программу",
                       "抽選ソフトをご利用ください"]

        # noinspection PyBroadException
        try:
            self.key_file = open("C:\\Draw\\key", "r")
            self.key = self.key_file.read()
            self.key_file.close()
            self.num_all = self.infer(self.key[0], self.key[1], self.key[2], self.key[3], self.key[4], self.key[5],
                                      self.key[6], self.key[7])
        except:
            self.key = ""
            for _ in range(8):
                self.key = self.key + str(random.randint(1, 9))
            self.key_file = open("C:\\Draw\\key", "w")
            self.key_file.write(str(self.key))
            self.key_file.close()
            self.num_all = self.infer(self.key[0], self.key[1], self.key[2], self.key[3], self.key[4], self.key[5],
                                      self.key[6], self.key[7])

    @staticmethod
    def infer(x1, x2, x3, x4, x5, x6, x7, x8):
        key_1 = int(x1)
        key_2 = int(x2)
        key_3 = int(x3)
        key_4 = int(x4)
        key_5 = int(x5)
        key_6 = int(x6)
        key_7 = int(x7)
        key_8 = int(x8)
        num_1 = key_1 * 2
        num_2 = key_2 * 7
        num_3 = key_3 * 4
        num_4 = key_4 * 9
        num_5 = key_5 * 3
        num_6 = key_6 * 1
        num_7 = key_7 * 5
        num_8 = key_8 * 6
        return str(num_1 + num_2 + num_3 + num_4 + num_5 + num_6 + num_7 + num_8)

    def welcome(self):
        global key_days, ser_lan, key_error_lan, input_lan
        qian_my = easygui.buttonbox(ser_lan[e] + self.key + "\n\n" + input_lan[e], "Setup", ["OK", buy_lan[e]])
        if qian_my is None:
            sys.exit()
        if qian_my == buy_lan[e]:
            os.system("start https://afdian.net/@yzkrz_Draw")
        my = easygui.enterbox(ser_lan[e] + self.key + "\n\n" + input_lan[e], "Setup")
        if my is None:
            sys.exit()
        try:
            if not (self.num_all == my[0:3]) or not (
                    self.infer(my[0], my[1], my[2], my[3], my[4], my[5], 0, 0) == my[6:9]):
                my2 = easygui.msgbox(key_error_lan[e])
                if my2 is None:
                    sys.exit()
                else:
                    return True
        except IndexError:
            my2 = easygui.msgbox(key_error_lan[e])
            if my2 is None:
                sys.exit()
            else:
                return True
        key_days = int(my[3:6])


try:
    ask = open("C:\\Draw\\asked.dll", "r")
    ask.close()
except FileNotFoundError:
    try:
        os.remove("C:\\Draw\\key")
    except FileNotFoundError:
        pass
    try:
        os.remove("C:\\Draw\\used.dll")
    except FileNotFoundError:
        pass
    key_lan = ["欢迎使用抽号软件", "Welcome to Draw", "Bienvenue au logiciel flash", "Bienvenido al software de numeración",
               "Добро пожаловать использовать программу Cat", "抽選ソフトをご利用ください"]

# noinspection PyBroadException
try:
    used_file = open(r"C:\\Draw\\used.dll", "r")
    used = used_file.read()
    used_file.close()
    key_time = time.strptime(used, "%Y-%m-%d")
    now_time = time.strptime(time.strftime("%Y-%m-%d"), "%Y-%m-%d")
    d1 = datetime.datetime(key_time[0], key_time[1], key_time[2])  # 第一个日期
    d2 = datetime.datetime(now_time[0], now_time[1], now_time[2])  # 第二个日期
    interval = d1 - d2  # 两日期差距
    days = interval.days
except:
    days = -1
if days <= 0:
    a_a = easygui.msgbox(key_lan[e])
    if a_a is None:
        sys.exit()
    while Key().welcome():
        pass
    _T1 = datetime.date.today()
    # noinspection PyUnboundLocalVariable
    _T2 = _T1 + datetime.timedelta(key_days)
    u = open("C:\\Draw\\used.dll", "w")
    u.write(str(_T2))
    u.close()
    easygui.msgbox(done_lan[e])
    os.remove("C:\\Draw\\key")
    sys.exit()
elif days <= 14:
    warning = True
    SCREEN_Y = 450
else:
    warning = False
    SCREEN_Y = 400

state = "start"
installed_language = {
    "汉语": ["抽号软件", "抽号结果", "停止抽号", "继续抽号", "开始抽号", "设置", "语言", "请选择语言：", "人数", "请输入人数：", "完成。", "防重率", "历史记录", "关闭",
           "清空", f"您的软件还有{days}天过期。", "按←与→键以移动。", " 按↑与↓键以移动，左键减少，右键增加。", "用户协议", "更多"],
    "English": ['Draw', "Result", "Pause", "Continue", "Start", "Settings ", "Language", "Please select a language: ",
                "Number of people", "Please enter the number of people:", "Done.", "Frequency of prevent repetition",
                "History", "Close", "Empty", f"Your software will expire in {days} day(s).",
                "Press the ← and → keys to move.",
                "Press the ↑ and ↓ keys to move. The left key decreases and the right key increases.", "User agreement",
                "More"], "Français": ["Tombola", "Results", "Stop", "Continue", "Start", "Settings ", "Language",
                                      "Veuillez sélectionner une langue: ", "Nombre de personnes",
                                      "Veuillez entrer le nombre de personnes:", "Terminé.",
                                      "Fréquence de prévention des répétitions", "Historique", "Fermer", "Vide",
                                      f"Votre logiciel a encore {days} jour(s) pour expirer.",
                                      "Appuyez sur les touches ← et → pour déplacer.",
                                      "Appuyez sur les touches ↑ et ↓ pour déplacer,"
                                      " la touche gauche diminue, la touche"
                                      " droite augmente.", "Accord de l’utilisateur", "Plus"],
    "Español": ["Draft", "Result", "Stop", "Continue", "Start", "Setting", "Language", "Seleccione el idioma: ",
                "Número de personas", "Introduzca el número de personas:", "Hecho.",
                "Frecuencia de prevención de la repetición", "Historia", "Cerrar", "Vacío",
                f"Su software todavía tiene {days} día(s) para expirar.", "Pulse ← y → para moverse.",
                "Pulse las teclas ↑ y ↓ para moverse, disminuir la tecla izquierda, aumentar la tecla derecha",
                "Acuerdo de usuario", "Más"],
    "русский язык": ["софт - качалка", "результаты лотереи", "прекрати", "Продолжайте", "начинай", "Настройка", "язык",
                     "пожалуйста, выберите язык:", "количество людей", "пожалуйста, введите количество:", "готово.",
                     "частота предупреждения повторения", "исторические записи", "закрыть", "очистить",
                     "ваше программное обеспечение все еще", "нажать ← и → клавишам.",
                     "нажать ↑ и ↓ клавишам., уменьшить левую, увеличить правую.", "Протокол пользователя", "больше"],
    "日本語": ["抽選ソフト", "結果", "ていし", "続行", "スタート", "設定", "言語", "言語を,選択:", "人数", "人数を入力してください。", "完了しました。", "防止された繰返し率",
            "履歴", "閉じる", "クリア", f"あなたのソフトウェアはあと{days}日で期限切れになります。", "←と→キーを押して移動します。",
            " ↑と↓ボタンを押して移動し、左ボタンが減少し、右ボタンが増加します。", "加入者契約", "より多く"]}
languages = list(installed_language.keys())

settings = pygame.image.load("settings.png")

try:
    d_f = open("C:\\Draw\\data", "r")
    df = eval(d_f.read())
    d_f.close()
except FileNotFoundError:
    df = {"1": 1, "2": 1, "3": 1, "4": 1, "5": 1}
    d_f2 = open("C:\\Draw\\data", "w")
    d_f2.write(str(df))
    d_f2.close()

screen = pygame.display.set_mode((400, SCREEN_Y))
try:
    pygame.display.set_caption(installed_language[selected_language][0] + '   V' + version)
except KeyError:
    selected_language = "English"
    pygame.display.set_caption(installed_language[selected_language][0] + '   V' + version)


def exe_exit():
    global name, last, l_list, selected_language, useLast
    f1 = open("C:\\Draw\\last_data", "w", encoding='utf-8')
    f1.write(str(name))
    f1.close()
    f2 = open("C:\\Draw\\last", "w", encoding='utf-8')
    f2.write(str(last))
    f2.close()
    f3 = open("C:\\Draw\\l_list", "w", encoding='utf-8')
    for f3_i in l_list:
        f3.write(str(f3_i) + "\n")
    f3.close()
    f17 = open("C:\\Draw\\lan", "w", encoding='utf-8')
    selected_language = f17.write(str(selected_language))
    f17.close()
    f19 = open("C:\\Draw\\useLast", "w", encoding='utf-8')
    f19.write(str(useLast))
    f19.close()
    exit(0)


def get():
    global SCREEN_X, SCREEN_Y, screen, state, name_range, name, last, black_move, going, keep_key, rs_save, black_error
    global selected_language, l_list, useLast, SCREEN_Y, open_black, data_file, inputting, fcl_inputting, fcl_save
    global lan_move, df, should_setting, setting_open, should_ch_lan, ch_lan_open, ch_lan_x, should_rs, rs_open, rs_x
    global fcl_x, should_fcl, fcl_open, his_x, should_his, his_open, black_x, should_black, black_open
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            if state == "blacking":
                if not black_error:
                    pygame.quit()
                    exe_exit()
                else:
                    pygame.mixer.music.load("Error.wav")
                    pygame.mixer.music.play()
            else:
                pygame.quit()
                exe_exit()
        x, y = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONUP:
            if state in ("randing", "result", "start"):
                if 75 <= x <= 325 and 295 <= y <= 370:
                    if state != "randing" and state != "setting":
                        state = "randing"
                        break
                    elif state == "randing":
                        state = "result"
                        name_range = 0
                        main()
                if 360 <= x <= 400 and 0 <= y <= 40:
                    setting_open = True
                    should_setting = 0
                if new_version:
                    if 370 <= x <= 400 and 370 <= y <= 400:
                        os.system("start https://www.github.com/yzkrz/Draw/releases/latest")
            if setting_open:
                if setting_x <= 0:
                    if 0 <= x <= 50 and 0 <= y <= 50:
                        if (not ch_lan_open) and (not rs_open) and (not fcl_open) and (not his_open) and (
                                not black_open):
                            should_setting = 400
                            state = "start"
                    if 310 <= x <= 335 and 90 <= y <= 115:
                        should_ch_lan = 0
                        ch_lan_open = True
                        state = "ch_lan"
                    if 310 <= x <= 335 and 165 <= y <= 190:
                        should_rs = 0
                        rs_open = True
                        state = "rs"
                    if 310 <= x <= 335 and 245 <= y <= 270:
                        should_fcl = 0
                        fcl_open = True
                        state = "fcl"

                    if selected_language in ("汉语", "English", "Español", "日本語"):
                        his_x_max = 100
                    elif selected_language == "Français":
                        his_x_max = 115
                    elif selected_language == "русский язык":
                        his_x_max = 220
                    else:
                        his_x_max = 110
                    if 0 <= x <= his_x_max and 360 <= y <= 400:
                        should_his = 0
                        his_open = True
                        state = "his"
                        continue

                    if xy_x <= x <= 400 and 360 <= y <= 400:
                        if selected_language == "汉语":
                            xyz = "1"
                        elif selected_language == "English":
                            xyz = "2"
                        elif selected_language == "Français":
                            xyz = "3"
                        elif selected_language == "Español":
                            xyz = "4"
                        elif selected_language == "русский язык":
                            xyz = "5"
                        elif selected_language == "日本語":
                            xyz = "6"
                        else:
                            xyz = 2
                        os.system('start https://gitee.com/yzkrz/Draw_files/blob/main/xy/' + xyz + '.md')

                    if 50 <= x <= 350 and 150 <= y <= 200:
                        open_black += 1
                        if open_black >= 10:
                            should_black = 0
                            black_open = True
                            state = "blacking"
                            open_black = 0
                    else:
                        open_black = 0
            if state == "rs":
                if 0 <= x <= 50 and 0 <= y <= 50:
                    should_rs = 400
                if 150 <= x <= 250 and 250 <= y <= 300:
                    rs_ok()
            if state == "fcl":
                if 0 <= x <= 50 and 0 <= y <= 50:
                    should_fcl = 400
                if 150 <= x <= 250 and 250 <= y <= 300:
                    fcl_ok()
            if state == "history":
                if 0 <= x <= 50 and 0 <= y <= 50:
                    should_his = 400
                if 150 <= x <= 250 and 250 <= y <= 300:
                    history_ok()
                if 0 <= x <= 90 and 360 <= y <= 400:
                    mor_his = open("more_his.html", "w")
                    mor_his.write(str(l_list))
                    mor_his.close()
                    os.system('"more_his.html"')
            if state == "blacking":
                if 0 <= x <= 50 and 0 <= y <= 50:
                    if not black_error:
                        should_black = 400
                        bfc = open("C:\\Draw\\data", "w")
                        bfc.write(str(df))
                        bfc.close()
                        name = df
                    else:
                        pygame.mixer.music.load("Error.wav")
                        pygame.mixer.music.play()
            if state == "ch_lan":
                if 0 <= x <= 50 and 0 <= y <= 50:
                    should_ch_lan = 400
        if event.type == pygame.MOUSEBUTTONDOWN:
            if state == "blacking":
                if 40 <= x <= 360:
                    for i in range(len(df)):
                        # title_height + i * height + (i + 1) * margin
                        if 70 * i + 100 + black_move <= y <= 70 * i + 150 + black_move:
                            if event.button == 1:
                                df[str(i + 1)] -= 1
                            if event.button == 3:
                                df[str(i + 1)] += 1
                            if df[str(i + 1)] < 0:
                                df[str(i + 1)] = 0
            if state == "ch_lan":
                if 250 <= y <= 300:
                    for i in range(len(list(languages))):
                        if 180 * i + 30 + lan_move <= x <= 180 * i + 180 + lan_move:
                            selected_language = list(languages)[i]
                            pygame.display.set_caption(installed_language[selected_language][0] + '   V' + version)
            if warning:
                if 370 <= x <= 380 and 420 <= y <= 430:
                    SCREEN_Y = 450
                    for _ in range(10):
                        SCREEN_Y -= 2
                        screen = pygame.display.set_mode((400, SCREEN_Y))
                        SCREEN_Y -= 3
                        screen = pygame.display.set_mode((400, SCREEN_Y))
        if event.type == pygame.KEYDOWN:
            if state == "blacking":
                if event.key == pygame.K_DOWN:
                    black_move += going
                if event.key == pygame.K_UP:
                    black_move -= going
                going += 0.25

                sum_data = len(df)
                title_height = 80
                margin = 20
                height = 50
                if black_move <= -(title_height * 2 + margin * (sum_data + 1) + height * (sum_data - 1) - 400):
                    black_move = -(title_height * 2 + margin * (sum_data + 1) + height * (sum_data - 1) - 400)

                if black_move > 0:
                    black_move = 0

            if state == "rs":
                if not keep_key:
                    if len(inputting) < 3:
                        if event.key == pygame.K_0:
                            if inputting != "":
                                inputting = inputting + "0"
                                rs_save = False
                        elif event.key == pygame.K_1:
                            inputting = inputting + "1"
                            rs_save = False
                        elif event.key == pygame.K_2:
                            inputting = inputting + "2"
                            rs_save = False
                        elif event.key == pygame.K_3:
                            inputting = inputting + "3"
                            rs_save = False
                        elif event.key == pygame.K_4:
                            inputting = inputting + "4"
                            rs_save = False
                        elif event.key == pygame.K_5:
                            inputting = inputting + "5"
                            rs_save = False
                        elif event.key == pygame.K_6:
                            inputting = inputting + "6"
                            rs_save = False
                        elif event.key == pygame.K_7:
                            inputting = inputting + "7"
                            rs_save = False
                        elif event.key == pygame.K_8:
                            inputting = inputting + "8"
                            rs_save = False
                        elif event.key == pygame.K_9:
                            inputting = inputting + "9"
                            rs_save = False
                    if event.key == pygame.K_BACKSPACE:
                        inputting = inputting[:-1]
                        rs_save = False
            if state == "fcl":
                if not keep_key:
                    if len(fcl_inputting) < 2:
                        if fcl_inputting != "0":
                            if event.key == pygame.K_0:
                                fcl_inputting = fcl_inputting + "0"
                                fcl_save = False
                            elif event.key == pygame.K_1:
                                fcl_inputting = fcl_inputting + "1"
                                fcl_save = False
                            elif event.key == pygame.K_2:
                                fcl_inputting = fcl_inputting + "2"
                                fcl_save = False
                            elif event.key == pygame.K_3:
                                fcl_inputting = fcl_inputting + "3"
                                fcl_save = False
                            elif event.key == pygame.K_4:
                                fcl_inputting = fcl_inputting + "4"
                                fcl_save = False
                            elif event.key == pygame.K_5:
                                fcl_inputting = fcl_inputting + "5"
                                fcl_save = False
                            elif event.key == pygame.K_6:
                                fcl_inputting = fcl_inputting + "6"
                                fcl_save = False
                            elif event.key == pygame.K_7:
                                fcl_inputting = fcl_inputting + "7"
                                fcl_save = False
                            elif event.key == pygame.K_8:
                                fcl_inputting = fcl_inputting + "8"
                                fcl_save = False
                            elif event.key == pygame.K_9:
                                fcl_inputting = fcl_inputting + "9"
                                fcl_save = False
                    if event.key == pygame.K_BACKSPACE:
                        fcl_inputting = fcl_inputting[:-1]
                        fcl_save = False
            if state == "ch_lan":
                if event.key == pygame.K_LEFT:
                    lan_move += going
                if event.key == pygame.K_RIGHT:
                    lan_move -= going
                going *= 1.03

                if lan_move >= 0:
                    lan_move = 0
                sum_lan = len(list(languages))
                if lan_move <= -(sum_lan * 180 - 370):
                    lan_move = -(sum_lan * 180 - 370)
            if going >= 1000:
                going = 1000
            keep_key = True
        if event.type == pygame.KEYUP:
            keep_key = False
            going = 1


def paint_text(text: str, color: tuple[int, int, int], bg_color: tuple[int, int, int] or None, x: int, y: int, mod: str,
               aa: bool = True, size: int = 32):
    font = pygame.font.Font("msyh.ttc", size)

    text_surface_object = font.render(text, aa, color, bg_color)
    text_rect_object = text_surface_object.get_rect()
    if mod == "xy":
        text_rect_object.topleft = (x, y)
    elif mod == "center":
        text_rect_object.center = (x, y)
    screen.blit(text_surface_object, text_rect_object)


def input_rs():
    global name, inputting, last_name, name_v, rs_save, rs_open, rs_x, should_rs, state, setting_open

    if rs_x < should_rs:
        rs_x += 40
        clear_lan_move()
        if rs_x >= 400:
            state = "setting"
            rs_open = False
    elif rs_x > should_rs:
        rs_x -= 40
    if rs_x <= 0:
        state = "rs"
        setting_open = False
    else:
        setting_open = True

    screen.blit(setting_bg, (rs_x, 0))

    pygame.draw.rect(screen, (243, 243, 243), (-2 + rs_x, -20, 404, 70), 0, border_radius=21)
    pygame.draw.rect(screen, (150, 150, 150), (-2 + rs_x, -18, 404, 70), 2, border_radius=21)
    paint_text("<    " + installed_language[selected_language][8], (0, 0, 0), (243, 243, 243), 18 + rs_x, 7, "xy", True,
               23)
    pygame.draw.line(screen, (177, 177, 177), (50 + rs_x, 5), (50 + rs_x, 45))

    paint_text(installed_language[selected_language][9], (0, 0, 0), (230, 230, 230), 200 + rs_x, 100, "center", True,
               20)
    pygame.draw.rect(screen, (255, 255, 255), (50 + rs_x, 150, 300, 50), 0, 20)
    pygame.draw.rect(screen, (150, 150, 150), (50 + rs_x, 150, 300, 50), 2, 20)
    if inputting != "":
        if 0 < int(inputting) < 1000:
            if not rs_save:
                pygame.draw.rect(screen, (100, 150, 255), (150 + rs_x, 250, 100, 50), 0, 20)
                paint_text("OK", (255, 255, 255), (100, 150, 255), 200 + rs_x, 275, "center", True, 22)
    paint_text(str(inputting), (0, 0, 0), (255, 255, 255), 70 + rs_x, 160, "xy", True, 20)

    last_name = name
    try:
        name_v = int(inputting)
    except ValueError:
        name_v = 1


def rs_ok():
    global name_v, last_name, name, data_error, rs_save, d_f, df
    if inputting != "":
        if int(inputting) < 1000:
            if not rs_save:
                rs_save = True
                try:
                    if name_v is None:
                        exe_exit()
                    if name_v > len(name):
                        for _ in range(name_v - len(name)):
                            name_j = 1 + len(name)
                            name[str(name_j)] = 1
                        for _ in range(name_v - len(last_name)):
                            name_j = 1 + len(last_name)
                            last_name[str(name_j)] = 1
                    elif name_v < len(name):
                        for _ in range(len(name) - name_v):
                            name.pop(str(len(name)))
                        for _ in range(len(last_name) - name_v):
                            last_name.pop(str(len(last_name)))
                    data_error = True
                except NameError:
                    pass
                ns_f = open("C:\\Draw\\data", "w")
                ns_f.write(str(last_name))
                ns_f.close()

                d_f = open("C:\\Draw\\data", "r")
                df = eval(d_f.read())
                d_f.close()


def input_fcl():
    global fcl_x, should_fcl, fcl_open, state, setting_open
    if fcl_x < should_fcl:
        fcl_x += 40
        if fcl_x >= 400:
            state = "setting"
            fcl_open = False
    elif fcl_x > should_fcl:
        fcl_x -= 40
    if fcl_x <= 0:
        state = "fcl"
        setting_open = False
    else:
        setting_open = True

    screen.blit(setting_bg, (fcl_x, 0))

    if selected_language == "English":
        fcl_title_text_sise = 22
        fcl_title_text_y = 2
    elif selected_language == "Français":
        fcl_title_text_sise = 17
        fcl_title_text_y = 7
    elif selected_language == "русский язык":
        fcl_title_text_sise = 17
        fcl_title_text_y = 5
    elif selected_language == "Español":
        fcl_title_text_sise = 16
        fcl_title_text_y = 7
    else:
        fcl_title_text_sise = 23
        fcl_title_text_y = 0

    pygame.draw.rect(screen, (243, 243, 243), (-2 + fcl_x, -20, 404, 70), 0, border_radius=21)
    pygame.draw.rect(screen, (150, 150, 150), (-2 + fcl_x, -18, 404, 70), 2, border_radius=21)
    paint_text("<    ", (0, 0, 0), (243, 243, 243), 18 + fcl_x, 7, "xy", True, 23)
    paint_text(installed_language[selected_language][11], (0, 0, 0), (243, 243, 243), 60 + fcl_x, 7 + fcl_title_text_y,
               "xy", True, fcl_title_text_sise)
    pygame.draw.line(screen, (177, 177, 177), (50 + fcl_x, 5), (50 + fcl_x, 45))

    paint_text(installed_language[selected_language][11], (0, 0, 0), (230, 230, 230), 200 + fcl_x, 100, "center", True,
               20)
    pygame.draw.rect(screen, (255, 255, 255), (50 + fcl_x, 150, 300, 50), 0, 20)
    pygame.draw.rect(screen, (150, 150, 150), (50 + fcl_x, 150, 300, 50), 2, 20)
    if fcl_inputting != "":
        if int(fcl_inputting) < 100:
            if not fcl_save:
                pygame.draw.rect(screen, (100, 150, 255), (150 + fcl_x, 250, 100, 50), 0, 20)
                paint_text("OK", (255, 255, 255), (100, 150, 255), 200 + fcl_x, 275, "center", True, 22)
    paint_text(str(fcl_inputting), (0, 0, 0), (255, 255, 255), 70 + fcl_x, 160, "xy", True, 20)
    paint_text("%", (0, 0, 0), None, 325 + fcl_x, 160, "xy", True, 20)


def fcl_ok():
    global name_v, last_name, name, data_error, fcl_save, useLast, fcl_inputting
    if inputting != "":
        if int(inputting) < 1000:
            if not fcl_save:
                fcl_save = True
                useLast = int(fcl_inputting) / 100
                ul = open("C:\\Draw\\useLast", "w")
                ul.write(str(useLast))
                ul.close()


def history():
    global his_x, should_his, state, setting_open, his_open, l_list
    if his_x < should_his:
        his_x += 40
        if his_x >= 400:
            state = "setting"
            his_open = False
    elif his_x > should_his:
        his_x -= 40
    if his_x <= 0:
        state = "history"
        setting_open = False
    else:
        setting_open = True

    screen.blit(setting_bg, (his_x, 0))

    j = 0
    txt_width = 0
    last_text = "0"
    txt_y = 100
    for i in l_list:
        if j == len(l_list) - 1:
            dun_hao = ""
        else:
            dun_hao = ","
        if len(str(last_text)) == 1:
            txt_width += 20
        elif len(str(last_text)) == 2:
            txt_width += 30
        else:
            txt_width += 40
        if len(str(i)) == 1:
            this_txt_width = 20
        elif len(str(i)) == 2:
            this_txt_width = 30
        else:
            this_txt_width = 40
        if txt_width + this_txt_width >= 360:
            txt_width = 20
            txt_y += 30
        if txt_y <= 220:
            paint_text(i + dun_hao, (0, 0, 0), (230, 230, 230), 20 + txt_width + his_x, txt_y, "xy", True, 18)
        j += 1
        last_text = i

    if l_list:
        pygame.draw.rect(screen, (100, 150, 255), (150 + his_x, 250, 100, 50), 0, 20)
        paint_text(installed_language[selected_language][14], (255, 255, 255), (100, 150, 255), 200 + his_x, 275,
                   "center", True, 22)

    pygame.draw.rect(screen, (243, 243, 243), (-2 + his_x, -20, 404, 70), 0, border_radius=21)
    pygame.draw.rect(screen, (150, 150, 150), (-2 + his_x, -18, 404, 70), 2, border_radius=21)
    paint_text("<    " + installed_language[selected_language][12], (0, 0, 0), (243, 243, 243), 18 + his_x, 7, "xy",
               True, 23)
    pygame.draw.line(screen, (177, 177, 177), (50 + his_x, 5), (50 + his_x, 45))

    if txt_y > 220:
        paint_text(installed_language[selected_language][19], (40, 123, 222), (230, 230, 230), 15 + his_x, 360, "xy",
                   True, 20)
        paint_text("...", (0, 0, 0), (230, 230, 230), 41 + his_x, 250, "xy", True, 18)


def history_ok():
    try:
        os.remove("C:\\Draw\\last_data")
    except FileNotFoundError:
        pass


def blacking():
    global screen, black_move, black_error, selected_language, df, black_x, should_black, state, setting_open
    global black_open
    if black_x < should_black:
        black_x += 40
        if black_x >= 400:
            state = "setting"
            black_open = False
    elif black_x > should_black:
        black_x -= 40
    if black_x <= 0:
        state = "blacking"
        setting_open = False
    else:
        setting_open = True

    screen.blit(setting_bg, (black_x, 0))
    sum_data = len(df)
    title_height = 80
    margin = 20
    height = 50
    width = 320
    old_all_0_error = True

    for j in df:
        if df[j] == 0:
            all_0_error = True
        else:
            all_0_error = False
        old_all_0_error = old_all_0_error and all_0_error

    if old_all_0_error:
        error_color = (255, 0, 0)
        black_error = True
    else:
        black_error = False
        error_color = (0, 0, 0)

    for i in range(1, sum_data + 1):
        if 400 >= (title_height + margin * i + black_move + height * (i - 1)) >= -50:
            pygame.draw.rect(screen, (255, 255, 255), (
                margin * 2 + black_x, title_height + margin * i + black_move + height * (i - 1), width, height), 0,
                             border_radius=21)
            pygame.draw.rect(screen, (150, 150, 150), (
                margin * 2 + black_x, title_height + margin * i + black_move + height * (i - 1), width, height), 2,
                             border_radius=21)
            paint_text(str(i), (0, 0, 0), (255, 255, 255), int(margin * 2 + 20) + black_x,
                       int(title_height + margin * i + black_move + height * (i - 1) + 11), "xy", True, 20)
            vx = 300 - (len(str(df[str(i)])) * 10)
            paint_text(str(df[str(i)]), error_color, (255, 255, 255), int(margin * 2 + vx) + black_x,
                       int(title_height + margin * i + black_move + height * (i - 1) + 11), "xy", True, 20)

    if black_move > 0:
        black_move = 0
    if black_move <= -(title_height * 2 + margin * (sum_data + 1) + height * (sum_data - 1) - 400):
        black_move = -(title_height * 2 + margin * (sum_data + 1) + height * (sum_data - 1) - 400)

    small_title_y = int((400 - black_x) / 10) + 55
    if small_title_y >= 85:
        small_title_y = 85
    pygame.draw.rect(screen, (230, 230, 230), (-5, -5, 410, small_title_y))
    pygame.draw.rect(screen, (147, 147, 147), (-5, -5, 410, small_title_y), 1)
    if selected_language == "汉语":
        bla_size = 15
    elif selected_language == "English":
        bla_size = 10
    elif selected_language == "Français":
        bla_size = 8
    elif selected_language == "Español":
        bla_size = 9
    elif selected_language == "русский язык":
        bla_size = 12
    elif selected_language == "日本語":
        bla_size = 12
    else:
        bla_size = 15
    paint_text(installed_language[selected_language][17], (0, 0, 0), (230, 230, 230), 200, small_title_y - 20, "center",
               True, bla_size)

    pygame.draw.rect(screen, (243, 243, 243), (-2, -20, 404, 70), 0, border_radius=21)
    pygame.draw.rect(screen, (150, 150, 150), (-2, -18, 404, 70), 2, border_radius=21)
    paint_text("<    " + installed_language[selected_language][5], (0, 0, 0), (243, 243, 243), 18, 7, "xy", True, 23)
    pygame.draw.line(screen, (177, 177, 177), (50, 5), (50, 45))


def clear_lan_move():
    global lan_move
    if lan_move <= 0:
        lan_move_cha = int((0 - lan_move) / 10) + 1
        lan_move += lan_move_cha


def ch_lan():
    global lan_move, ch_lan_x, should_ch_lan, state, setting_open, ch_lan_open
    if ch_lan_x < should_ch_lan:
        ch_lan_x += 40
        clear_lan_move()
        if ch_lan_x >= 400:
            state = "setting"
            ch_lan_open = False
    elif ch_lan_x > should_ch_lan:
        ch_lan_x -= 40
    if ch_lan_x <= 0:
        state = "ch_lan"
        setting_open = False
    else:
        setting_open = True

    screen.blit(setting_bg, (ch_lan_x, 0))

    pygame.draw.rect(screen, (243, 243, 243), (-2 + ch_lan_x, -20, 404, 70), 0, border_radius=21)
    pygame.draw.rect(screen, (150, 150, 150), (-2 + ch_lan_x, -18, 404, 70), 2, border_radius=21)
    paint_text("<    " + installed_language[selected_language][6], (0, 0, 0), (243, 243, 243), 18 + ch_lan_x, 7, "xy",
               True, 23)
    pygame.draw.line(screen, (177, 177, 177), (50 + ch_lan_x, 5), (50 + ch_lan_x, 45))
    if selected_language == "Français":
        ch_size = 15
    else:
        ch_size = 20
    paint_text(installed_language[selected_language][7], (0, 0, 0), (230, 230, 230), 200 + ch_lan_x, 150, "center",
               True, 20)
    paint_text(installed_language[selected_language][16], (0, 0, 0), (230, 230, 230), 200 + ch_lan_x, 200, "center",
               True, ch_size)
    pygame.draw.line(screen, (177, 177, 177), (30 + ch_lan_x, 225), (370 + ch_lan_x, 225), 1)

    for i in range(0, len(languages)):
        pygame.draw.rect(screen, (255, 255, 255), (180 * i + 30 + lan_move + ch_lan_x, 250, 150, 50), 0, 20)
        pygame.draw.rect(screen, (150, 150, 150), (180 * i + 30 + lan_move + ch_lan_x, 250, 150, 50), 2, 20)
        paint_text(languages[i], (0, 0, 0), (255, 255, 255), 180 * i + 105 + lan_move + ch_lan_x, 275, "center", True,
                   20)


# ______________________________________________________________________________________________________________________


total = 0
name_range = 0
f8 = open("C:\\Draw\\data", "r", encoding='utf-8')
name = eval(f8.read())
f8.close()
lim = []
try:
    f9 = open("C:\\Draw\\last", "r", encoding='utf-8')
    last = int(f9.read())
    f9.close()
except FileNotFoundError:
    last = 0
except ValueError:
    last = 0

try:
    f10 = open("C:\\Draw\\useLast", "r", encoding='utf-8')
    useLast = float(f10.read())
    f10.close()
except FileNotFoundError:
    useLast = 0
fcl_inputting = str(int(useLast * 100))

if not (last >= len(name) * useLast):
    # noinspection PyBroadException
    try:
        f11 = open("C:\\Draw\\last_data", "r", encoding='utf-8')
        name = eval(f11.read())
        f11.close()
    except:
        f12 = open("C:\\Draw\\data", "r", encoding='utf-8')
        name = eval(f12.read())
        f12.close()
else:
    last = 0
inputting: str = str(len(name))

last_temp = 0
for last_i in range(len(name)):
    if name[str(last_i + 1)] == 0:
        last_temp += 1
if last_temp > last:
    last = last_temp

try:
    f13 = open("C:\\Draw\\l_list", "r", encoding='utf-8')
    l_list = f13.read().split("\n")
    new_list = [i for i in l_list if i != '']
    l_list = new_list
    f13.close()
except FileNotFoundError:
    l_list = []

for i in range(len(name)):
    txt = total + 1
    total += name[str(1 + i)]
    lim.append([txt, txt + name[str(1 + i)] - 1])


def isin(x, y, value):
    if x <= value <= y:
        return True
    else:
        return False


def ran():
    global r, name_range, lim, last, name, total
    r = randint(1, total)
    for event in lim:
        name_range += 1
        if isin(event[0], event[1], r):
            name[str(name_range)] = 0
            last += 1
            l_list.append(str(name_range))
            if last >= len(name) * useLast:
                f14 = open("C:\\Draw\\data", "r", encoding='utf-8')
                name = eval(f14.read())
                f14.close()
                last = 0
            break


def main():
    global state
    if state != "start":
        ran()


main()

if selected_language == "汉语":
    xy_x = 311
    xy_s = 20
    xy_y = 360
elif selected_language == "日本語":
    xy_x = 290
    xy_s = 20
    xy_y = 360
elif selected_language == "Français":
    xy_x = 170
    xy_s = 20
    xy_y = 360
elif selected_language == "Español":
    xy_x = 200
    xy_s = 20
    xy_y = 360
elif selected_language == "русский язык":
    xy_x = 240
    xy_s = 12
    xy_y = 370
elif selected_language == "English":
    xy_x = 235
    xy_s = 20
    xy_y = 360
else:
    xy_x = 280
    xy_s = 20
    xy_y = 360

# ______________________________________________________________________________________________________________________
old_FPS_time = time.time()
web = "https://api.github.com/repos/yzkrz/Draw/releases/latest"
try:
    all_web_info = requests.get(web, timeout=1).json()
    latest = all_web_info["tag_name"][8:]
    if latest > version:
        print("Up")
        new_version = True
    else:
        new_version = False
except requests.exceptions.ConnectTimeout:
    print("Timeout")
    new_version = False
while True:
    last_txt = 0
    for i in range(len(name)):
        if name[str(i + 1)] == 0:
            last_txt += 1
    if last_txt > last:
        last = last_txt

    screen.fill((230, 230, 230))

    total = 0
    lim = []
    for i in range(len(name)):
        txt = total + 1
        total += name[str(1 + i)]
        lim.append([txt, txt + name[str(1 + i)] - 1])
    if last >= len(name) * useLast:
        f15 = open("C:\\Draw\\data", "r", encoding='utf-8')
        name = eval(f15.read())
        f15.close()
        last = 0

    if state == "randing":
        screen.blit(settings, (355, 0))
        pygame.draw.rect(screen, (100, 150, 255), (75, 300, 250, 75), 0, border_radius=20)
        pygame.draw.rect(screen, (125, 125, 125), (50, 40, 300, 230), 2, border_radius=20)
        paint_text(installed_language[selected_language][1], (0, 0, 0), (230, 230, 230), 70, 26, "xy", True, 20)
        paint_text(str(randint(1, len(name))), (255, 0, 0), (230, 230, 230), 200, 150, "center", True, 150)
        paint_text(installed_language[selected_language][2], (255, 255, 255), (100, 150, 255), 200, 336, "center", True,
                   32)
        if new_version:
            pygame.draw.circle(screen, (255, 200, 15), (380, 380), 15)
            paint_text("!", (255, 255, 255), None, 380, 380, "center", True, 22)
    elif state == "result":
        screen.blit(settings, (355, 0))
        pygame.draw.rect(screen, (100, 150, 255), (75, 300, 250, 75), 0, border_radius=20)
        pygame.draw.rect(screen, (125, 125, 125), (50, 40, 300, 230), 2, border_radius=20)
        paint_text(installed_language[selected_language][1], (0, 0, 0), (230, 230, 230), 70, 26, "xy", True, 20)
        paint_text(str(name_range), (255, 0, 0), (230, 230, 230), 200, 150, "center", True, 150)
        paint_text(installed_language[selected_language][3], (255, 255, 255), (100, 150, 255), 200, 336, "center", True,
                   32)
        if new_version:
            pygame.draw.circle(screen, (255, 200, 15), (380, 380), 15)
            paint_text("!", (255, 255, 255), None, 380, 380, "center", True, 22)
    elif state == "start":
        screen.blit(settings, (355, 0))
        pygame.draw.rect(screen, (100, 150, 255), (75, 300, 250, 75), 0, border_radius=20)
        pygame.draw.rect(screen, (125, 125, 125), (50, 40, 300, 230), 2, border_radius=20)
        paint_text(installed_language[selected_language][1], (0, 0, 0), (230, 230, 230), 70, 26, "xy", True, 20)
        paint_text(installed_language[selected_language][4], (255, 255, 255), (100, 150, 255), 200, 336, "center", True,
                   32)
        if new_version:
            pygame.draw.circle(screen, (255, 200, 15), (380, 380), 15)
            paint_text("!", (255, 255, 255), None, 380, 380, "center", True, 22)
    if setting_open:
        if setting_x < should_setting:
            setting_x += 40
        elif setting_x > should_setting:
            setting_x -= 40
            if setting_x <= 0:
                state = "setting"
        if setting_x >= 400:
            setting_open = False

        screen.blit(setting_bg, (setting_x, 0))

        pygame.draw.rect(screen, (243, 243, 243), (-2 + setting_x, -20, 404, 70), 0, border_radius=21)
        pygame.draw.rect(screen, (150, 150, 150), (-2 + setting_x, -18, 404, 70), 2, border_radius=21)
        paint_text("<    " + installed_language[selected_language][5], (0, 0, 0), (243, 243, 243), 18 + setting_x, 7,
                   "xy", True, 23)
        pygame.draw.line(screen, (177, 177, 177), (50 + setting_x, 5), (50 + setting_x, 45))

        pygame.draw.rect(screen, (255, 255, 255), (50 + setting_x, 75, 300, 50), 0, border_radius=20)
        pygame.draw.rect(screen, (150, 150, 150), (50 + setting_x, 75, 300, 50), 1, border_radius=20)
        paint_text(installed_language[selected_language][6] + ": " + selected_language, (0, 0, 0), (255, 255, 255),
                   68 + setting_x, 88, "xy", True, 16)
        paint_text("∨", (100, 100, 100), (255, 255, 255), 315 + setting_x, 85, "xy", True, 20)

        pygame.draw.rect(screen, (255, 255, 255), (50 + setting_x, 150, 300, 50), 0, border_radius=20)
        pygame.draw.rect(screen, (150, 150, 150), (50 + setting_x, 150, 300, 50), 1, border_radius=20)
        paint_text(installed_language[selected_language][8] + ": " + str(len(name)), (0, 0, 0), (255, 255, 255),
                   68 + setting_x, 164, "xy", True, 16)
        paint_text("∨", (100, 100, 100), (255, 255, 255), 315 + setting_x, 160, "xy", True, 20)
        pygame.draw.rect(screen, (255, 255, 255), (50 + setting_x, 225, 300, 50), 0, border_radius=20)
        pygame.draw.rect(screen, (150, 150, 150), (50 + setting_x, 225, 300, 50), 1, border_radius=20)
        fcl_y = 0
        if selected_language == "汉语" or selected_language == "日本語":
            fcl_size = 16
            fcl_y = -2
        elif selected_language == "English":
            fcl_size = 13
            fcl_y = 1
        elif selected_language == "Français":
            fcl_size = 11
        elif selected_language == "Español" or selected_language == "русский язык":
            fcl_size = 11
            fcl_y = 1
        else:
            fcl_size = 11
            fcl_y = 0
        paint_text(installed_language[selected_language][11] + ": " + str(int(useLast * 100)) + "%", (0, 0, 0),
                   (255, 255, 255), 68 + setting_x, 241 + fcl_y, "xy", True, fcl_size)
        paint_text("∨", (100, 100, 100), (255, 255, 255), 315 + setting_x, 235, "xy", True, 20)
        paint_text(installed_language[selected_language][12], (40, 123, 222), (230, 230, 230), 15 + setting_x, 360,
                   "xy", True, 20)
        if selected_language == "汉语":
            xy_x = 311
            xy_s = 20
            xy_y = 360
        elif selected_language == "日本語":
            xy_x = 290
            xy_s = 20
            xy_y = 360
        elif selected_language == "Français":
            xy_x = 170
            xy_s = 20
            xy_y = 360
        elif selected_language == "Español":
            xy_x = 200
            xy_s = 20
            xy_y = 360
        elif selected_language == "русский язык":
            xy_x = 240
            xy_s = 12
            xy_y = 370
        elif selected_language == "English":
            xy_x = 235
            xy_s = 20
            xy_y = 360
        else:
            xy_x = 280
            xy_s = 20
            xy_y = 360
        paint_text(installed_language[selected_language][18], (40, 123, 222), (230, 230, 230), xy_x + setting_x, xy_y,
                   "xy", True, xy_s)
    if state == "blacking":
        blacking()
    elif rs_open:
        input_rs()
    elif fcl_open:
        input_fcl()
    elif his_open:
        history()
    elif ch_lan_open:
        ch_lan()
    pygame.draw.rect(screen, (248, 212, 212), (0, 400, 400, 50))
    pygame.draw.line(screen, (226, 101, 102), (0, 400), (400, 400))
    pygame.draw.circle(screen, (255, 0, 0), (26, 426), 20)
    paint_text("x", (255, 255, 255), None, 26, 421, "center", True, 36)
    if selected_language == "汉语":
        e_t = 20
        e_y = 0
    elif selected_language == "日本語":
        e_t = 12
        e_y = 7
    elif selected_language == "Français":
        e_t = 14
        e_y = 5
    elif selected_language == "Español":
        e_t = 14
        e_y = 5
    elif selected_language == "русский язык":
        e_t = 14
        e_y = -3
        paint_text(f"на {days} день", (0, 0, 0), (248, 212, 212), 55, 425, "xy", True, e_t)
    elif selected_language == "English":
        e_t = 16
        e_y = 4
    else:
        e_t = 16
        e_y = 4
        paint_text(f" просрочено на {days} дней.", (0, 0, 0), (248, 212, 212), 55, 422, "xy", True, e_t)
    paint_text(installed_language[selected_language][15], (0, 0, 0), (248, 212, 212), 55, 410 + e_y, "xy", True, e_t)
    paint_text("x", (100, 100, 100), (248, 212, 212), 375, 422, "center", True, 20)

    get()
    pygame.display.update()

    # new_FPS_time = time.time()  # FPS = new_FPS_time - old_FPS_time  # old_FPS_time = new_FPS_time  # print(1 / FPS)
