import pygame


class character:
    def __init__(self, level_up):
        self.level_up = level_up

    def exp_need_fun(self):
        global exp_need_dic
        exp_need_dic = {20: "120,175", 40: "698,005", 50: "1,277,600",
                        60: "2,131,725", 70: "3,327,650", 80: "4,939,525", 90: "8,362,650"}
        global exp_need
        exp_need = exp_need_dic[self.level_up]
        return exp_need

    def money_need_fun(self):
        global money_need_dic
        money_need_dic = {20: "24,035", 40: "159,700", 50: "315,520",
                          60: "546,345", 70: "865,530", 80: "1,287,905", 90: "2,092,530"}
        global money_need
        money_need = money_need_dic[self.level_up]
        return money_need

    def stones_boss_need_fun(self):
        global stones_boss_need_dic
        stones_boss_need_dic = {20: ["0", "0", "0", "0", "0"], 40: ["1", "0", "0", "0", "0"], 50: ["1", "3", "0", "0", "2"],
                                60: ["1", "9", "0", "0", "6"], 70: ["1", "9", "3", "0", '14'], 80: ['1', '9', '9', '0', '26'],
                                90: ['1', '9', '9', '6', '46']}
        global stones_need_1
        stones_need_1 = stones_boss_need_dic[self.level_up][0]
        global stones_need_2
        stones_need_2 = stones_boss_need_dic[self.level_up][1]
        global stones_need_3
        stones_need_3 = stones_boss_need_dic[self.level_up][2]
        global stones_need_4
        stones_need_4 = stones_boss_need_dic[self.level_up][3]
        global boss_need
        boss_need = stones_boss_need_dic[self.level_up][4]

    def materials_need_fun(self):
        global materials_need_dic
        materials_need_dic = {20: ['0', '0', '0', '0'], 40: ['3', '3', '0', '0'], 50: ['13', '18', '0', '0'],
                              60: ['33', '18', '12', '0'], 70: ['63', '18', '30', '0'], 80: ['108', '18', '30', '12'],
                              90: ['168', '18', '30', '36']}
        global materials_special_need
        materials_special_need = materials_need_dic[self.level_up][0]
        global materials_normal_need_1
        materials_normal_need_1 = materials_need_dic[self.level_up][1]
        global materials_normal_need_2
        materials_normal_need_2 = materials_need_dic[self.level_up][2]
        global materials_normal_need_3
        materials_normal_need_3 = materials_need_dic[self.level_up][3]


def color(elem_name):
    if elem_name == "fire":
        return (240, 80, 57)
    if elem_name == "water":
        return (1, 160, 255)
    if elem_name == "wind":
        return (78, 240, 184)
    if elem_name == "elec":
        return (155, 100, 194)
    if elem_name == "ice":
        return (143, 206, 219)
    if elem_name == "stone":
        return (156, 115, 10)
    return (0, 0, 0)


def drawText1(content, form, size, color):
    pygame.font.init()
    my_font = pygame.font.SysFont(form, size)
    text_surface = my_font.render(content, True, color)
    return text_surface


def materials_need_fun(screen, n_num, p_num):
    list_n = ["huami", "huiji", "jiandai", "mianju", "shu",
              "slm", "yayin"]
    list_p = ["baihe", "dudulian", "fengcheju", "gougouguo", "jiaojiao",
              "liulidai", "luoluomei", "mogu", "nichang", "pogongyin",
              "qingxin", "saixiliya", "shipo", "xiaodengcao", "xingluo",
              "yeboshi"]

    address1 = "normal_materials/" + list_n[n_num-1] + "1.png"
    address2 = "normal_materials/" + list_n[n_num-1] + "2.png"
    address3 = "normal_materials/" + list_n[n_num-1] + "3.png"
    address_p = "local_specialty/" + list_p[p_num-1] + ".png"
    n_image_1 = pygame.image.load(address1)
    n_image_2 = pygame.image.load(address2)
    n_image_3 = pygame.image.load(address3)
    n_image_1 = pygame.transform.scale(n_image_1, (100, 100))
    n_image_2 = pygame.transform.scale(n_image_2, (100, 100))
    n_image_3 = pygame.transform.scale(n_image_3, (100, 100))
    s_image = pygame.image.load(address_p)
    s_image = pygame.transform.scale(s_image, (100, 100))
    screen.blit(n_image_1, (200, 625))
    screen.blit(n_image_2, (400, 625))
    screen.blit(n_image_3, (600, 625))
    screen.blit(s_image, (800, 625))


def stones_need_fun(screen, elem, boss):
    address_e = "icons/" + elem + ".png"
    address1 = "Stones/" + elem + "1.png"
    address2 = "Stones/" + elem + "2.png"
    address3 = "Stones/" + elem + "3.png"
    address4 = "Stones/" + elem + "4.png"
    element = pygame.image.load(address_e)
    stone_1 = pygame.image.load(address1)
    stone_2 = pygame.image.load(address2)
    stone_3 = pygame.image.load(address3)
    stone_4 = pygame.image.load(address4)
    element = pygame.transform.scale(element, (130, 130))
    stone_1 = pygame.transform.scale(stone_1, (100, 100))
    stone_2 = pygame.transform.scale(stone_2, (100, 100))
    stone_3 = pygame.transform.scale(stone_3, (100, 100))
    stone_4 = pygame.transform.scale(stone_4, (100, 100))
    screen.blit(element, (540, 160))
    screen.blit(stone_1, (100, 500))
    screen.blit(stone_2, (300, 500))
    screen.blit(stone_3, (500, 500))
    screen.blit(stone_4, (700, 500))
    if boss == 1:
        address_boss_m = "boss_materials/" + elem + "_boss.png"
        boss_m = pygame.image.load(address_boss_m)
        boss_m = pygame.transform.scale(boss_m, (100, 100))
        screen.blit(boss_m, (900, 500))
    if boss == 2:
        boss_m = pygame.image.load("boss_materials/longxi_boss.png")
        boss_m = pygame.transform.scale(boss_m, (100, 100))
        screen.blit(boss_m, (900, 500))


def char_image_load_final(screen, elem, num, wh, x, y):
    char_dic = {"fire": ["d", "keli", "bannite", "hutao", "anbo", "xianglin", "yanfei", "xinyan"],
                "water": ["mona", "gongzi", "xingqiu", "babala"],
                "wind": ["wendi", "xiao", "qin", "shatang"],
                "elec": ["keqing", "leize", "beidou", "feixieer", "lisha"],
                "ice": ["ganyu", "qiqi", "diaona", "chongyun", "luoshaliya", "kaiya"],
                "stone": ["zhongli", "abeiduo", "ningguang", "noaier"]}
    materials_match = {"d": [2, 14, 1], "keli": [5, 8, 1], "bannite": [7, 3, 1], "hutao": [1, 9, 2], "anbo": [3, 14, 1],
                       "xianglin": [6, 5, 1], "yanfei": [7, 16, 2], "xinyan": [7, 6, 1],
                       "mona": [1, 8, 1], "gongzi": [2, 15, 1], "xingqiu": [4, 9, 1], "babala": [5, 8, 1],
                       "wendi": [6, 12, 1], "xiao": [6, 11, 2], "qin": [4, 10, 1], "shatang": [1, 3, 1],
                       "keqing": [1, 13, 1], "leize": [4, 4, 1], "beidou": [7, 16, 1], "feixieer": [3, 14, 1],
                       "lisha": [6, 7, 1],
                       "ganyu": [1, 11, 1], "qiqi": [5, 6, 1], "diaona": [3, 2, 1], "chongyun": [4, 13, 1],
                       "luoshaliya": [2, 7, 1], "kaiya": [7, 2, 1],
                       "zhongli": [6, 13, 1], "abeiduo": [5, 12, 1], "ningguang": [2, 1, 1], "noaier": [4, 7, 1]}

    address = "cha icons/" + char_dic[elem][num-1] + ".png"
    char_image = pygame.image.load(address)
    if wh == 0:
        screen.blit(char_image, (700, 150))
    if wh == 1:
        char_image = pygame.transform.scale(char_image, (170, 170))
        screen.blit(char_image, (350, 150))
        materials_need_fun(screen, materials_match[char_dic[elem][num-1]][0], materials_match[char_dic[elem][num-1]][1])
        stones_need_fun(screen, elem, materials_match[char_dic[elem][num-1]][2])
    if wh == 2:
        char_image = pygame.transform.scale(char_image, (150, 150))
        screen.blit(char_image, (x, y))
        if x != 900:
            x += 200
            num += 1
            if num <= len(char_dic[elem]):
                char_image_load_final(screen, elem, num, 2, x, y)
            if num == len(char_dic[elem])+1:
                kleeee = pygame.image.load("emotes/kleeee.png")
                screen.blit(kleeee, (x, y))
        if x == 900:
            x = 100
            y = 600
            num += 1
            if num <= len(char_dic[elem]):
                char_image_load_final(screen, elem, num, 2, x, y)
            if num == len(char_dic[elem])+1:
                kleeee = pygame.image.load("emotes/kleeee.png")
                screen.blit(kleeee, (x, y))


def elem_image_load(screen):
    fire = pygame.image.load(r"icons/fire.png")
    fire = pygame.transform.scale(fire, (100, 100))
    screen.blit(fire, (85, 220))
    water = pygame.image.load(r"icons/water.png")
    water = pygame.transform.scale(water, (100, 100))
    screen.blit(water, (270, 220))
    wind = pygame.image.load(r"icons/wind.png")
    wind = pygame.transform.scale(wind, (100, 100))
    screen.blit(wind, (455, 220))
    elec = pygame.image.load(r"icons/elec.png")
    elec = pygame.transform.scale(elec, (100, 100))
    screen.blit(elec, (640, 220))
    ice = pygame.image.load(r"icons/ice.png")
    ice = pygame.transform.scale(ice, (100, 100))
    screen.blit(ice, (825, 220))
    stone = pygame.image.load(r"icons/stone.png")
    stone = pygame.transform.scale(stone, (100, 100))
    screen.blit(stone, (1010, 220))


def materials_load(screen, run_name, elem_name, num, level, level_str):
    while run_name:
        title_bg_page(screen, elem_name)
        screen.blit(drawText1("-------------------------------------------------------------------------------------",
                              "bradleyhandbold", 35, color(elem_name)), (40, 115))
        screen.blit(drawText1("--------------------------------------Materials--------------------------------------",
                              "bradleyhandbold", 35, color(elem_name)), (40, 320))
        screen.blit(drawText1("Character", "bradleyhandbold", 40, color(elem_name)), (150, 200))
        screen.blit(drawText1("Level", "bradleyhandbold", 40, color(elem_name)), (850, 200))
        char_image_load_final(screen, elem_name, num, 1, 0, 0)
        screen.blit(drawText1(level_str, "bradleyhandbold", 60, color(elem_name)), (980, 185))

        mora_image = pygame.image.load(r"money_exp/mora.png")
        mora_image = pygame.transform.scale(mora_image, (150, 150))
        screen.blit(mora_image, (200, 350))
        exp_image = pygame.image.load(r"money_exp/EXP.png")
        exp_image = pygame.transform.scale(exp_image, (100, 100))
        screen.blit(exp_image, (700, 375))
        t_num = character(level)
        mora_num = t_num.money_need_fun()
        exp_num = t_num.exp_need_fun()
        t_num.stones_boss_need_fun()
        t_num.materials_need_fun()
        screen.blit(drawText1(mora_num, "arialroundedbold", 40, color(elem_name)), (350, 400))
        screen.blit(drawText1(exp_num, "arialroundedbold", 40, color(elem_name)), (800, 400))
        screen.blit(drawText1(stones_need_1, "arialroundedbold", 40, color(elem_name)), (200, 525))
        screen.blit(drawText1(stones_need_2, "arialroundedbold", 40, color(elem_name)), (400, 525))
        screen.blit(drawText1(stones_need_3, "arialroundedbold", 40, color(elem_name)), (600, 525))
        screen.blit(drawText1(stones_need_4, "arialroundedbold", 40, color(elem_name)), (800, 525))
        screen.blit(drawText1(boss_need, "arialroundedbold", 40, color(elem_name)), (1000, 525))
        screen.blit(drawText1(materials_normal_need_1, "arialroundedbold", 40, color(elem_name)), (300, 650))
        screen.blit(drawText1(materials_normal_need_2, "arialroundedbold", 40, color(elem_name)), (500, 650))
        screen.blit(drawText1(materials_normal_need_3, "arialroundedbold", 40, color(elem_name)), (700, 650))
        screen.blit(drawText1(materials_special_need, "arialroundedbold", 40, color(elem_name)), (900, 650))

        for event_materials in pygame.event.get():
            if event_materials.type == pygame.QUIT:
                run_name = False
                running = False
            if event_materials.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                # QUIT
                if x > 1130 and y < 25:
                    run_name = False
                    running = False
                    exit()
                # GUIDE
                if 950 < x < 1020 and y < 25:
                    run_name = False
                    draw_page("guide", screen)
                # HOME
                if 1040 < x < 1105 and y < 25:
                    run_name = False
        pygame.display.update()


def level_load(screen, run_name, elem_name, num, klee):
    global level
    global level_str
    global running_klee
    running_klee = True
    if klee == 0:
        while run_name:
            title_bg_page(screen, elem_name)
            screen.blit(drawText1("Character  You  Chose", "bradleyhandbold", 36, color(elem_name)), (250, 300))
            screen.blit(drawText1("--------------------------------------------------------------------------------------",
                                  "bradleyhandbold", 36, color(elem_name)), (40, 430))
            screen.blit(drawText1("Please  Choose  the  Level", "bradleyhandbold", 36, color(elem_name)), (420, 460))
            screen.blit(drawText1("You  Want  to  Upgrade  to", "bradleyhandbold", 36, color(elem_name)), (405, 500))
            screen.blit(drawText1("20", "bradleyhandbold", 60, color(elem_name)), (90, 580))
            screen.blit(drawText1("40", "bradleyhandbold", 60, color(elem_name)), (250, 580))
            screen.blit(drawText1("50", "bradleyhandbold", 60, color(elem_name)), (410, 580))
            screen.blit(drawText1("60", "bradleyhandbold", 60, color(elem_name)), (570, 580))
            screen.blit(drawText1("70", "bradleyhandbold", 60, color(elem_name)), (730, 580))
            screen.blit(drawText1("80", "bradleyhandbold", 60, color(elem_name)), (890, 580))
            screen.blit(drawText1("90", "bradleyhandbold", 60, color(elem_name)), (1050, 580))
            char_image_load_final(screen, elem_name, num, 0, 0, 0)
            for event_level in pygame.event.get():
                if event_level.type == pygame.QUIT:
                    run_name = False
                    running = False
                if event_level.type == pygame.MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.get_pos()
                    # QUIT
                    if x > 1130 and y < 25:
                        run_name = False
                        running = False
                        exit()
                    # GUIDE
                    if 950 < x < 1020 and y < 25:
                        run_name = False
                        draw_page("guide", screen)
                    # HOME
                    if 1040 < x < 1105 and y < 25:
                        run_name = False
                    # LEVEL_CHECK
                    if 90 < x < 160 and 580 < y < 630:
                        level = 20
                        level_str = "20"
                        materials_load(screen, run_name, elem_name, num, level, level_str)
                        run_name = False
                    if 250 < x < 320 and 580 < y < 630:
                        level = 40
                        level_str = "40"
                        materials_load(screen, run_name, elem_name, num, level, level_str)
                        run_name = False
                    if 410 < x < 480 and 580 < y < 630:
                        level = 50
                        level_str = "50"
                        materials_load(screen, run_name, elem_name, num, level, level_str)
                        run_name = False
                    if 570 < x < 640 and 580 < y < 630:
                        level = 60
                        level_str = "60"
                        materials_load(screen, run_name, elem_name, num, level, level_str)
                        run_name = False
                    if 730 < x < 800 and 580 < y < 630:
                        level = 70
                        level_str = "70"
                        materials_load(screen, run_name, elem_name, num, level, level_str)
                        run_name = False
                    if 890 < x < 960 and 580 < y < 630:
                        level = 80
                        level_str = "80"
                        materials_load(screen, run_name, elem_name, num, level, level_str)
                        run_name = False
                    if 1050 < x < 1120 and 580 < y < 630:
                        level = 90
                        level_str = "90"
                        materials_load(screen, run_name, elem_name, num, level, level_str)
                        run_name = False
            pygame.display.update()
    if klee == 1:
        while running_klee:
            title_bg_page(screen, elem_name=" ")
            klee = pygame.image.load("emotes/kleeee.png")
            screen.blit(klee, (0, 0))
            screen.blit(klee, (160, 0))
            screen.blit(klee, (320, 0))
            screen.blit(klee, (480, 0))
            screen.blit(klee, (640, 0))
            screen.blit(klee, (800, 0))
            screen.blit(klee, (0, 160))
            screen.blit(klee, (160, 160))
            screen.blit(klee, (320, 160))
            screen.blit(klee, (480, 160))
            screen.blit(klee, (640, 160))
            screen.blit(klee, (800, 160))
            screen.blit(klee, (960, 160))
            screen.blit(klee, (1120, 160))
            screen.blit(klee, (0, 320))
            screen.blit(klee, (160, 320))
            screen.blit(klee, (320, 320))
            screen.blit(klee, (480, 320))
            screen.blit(klee, (640, 320))
            screen.blit(klee, (800, 320))
            screen.blit(klee, (960, 320))
            screen.blit(klee, (1120, 320))
            screen.blit(klee, (0, 480))
            screen.blit(klee, (160, 480))
            screen.blit(klee, (320, 480))
            screen.blit(klee, (480, 480))
            screen.blit(klee, (640, 480))
            screen.blit(klee, (800, 480))
            screen.blit(klee, (960, 480))
            screen.blit(klee, (1120, 480))
            screen.blit(klee, (0, 640))
            screen.blit(klee, (160, 640))
            screen.blit(klee, (320, 640))
            screen.blit(klee, (480, 640))
            screen.blit(klee, (640, 640))
            screen.blit(klee, (800, 640))
            screen.blit(klee, (960, 640))
            screen.blit(klee, (1120, 640))

            for event_klee in pygame.event.get():
                if event_klee.type == pygame.QUIT:
                    running_klee = False
                    running = False
                if event_klee.type == pygame.MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.get_pos()
                    # QUIT
                    if x > 1130 and y < 25:
                        running_klee = False
                        running = False
                        exit()
                    # GUIDE
                    if 950 < x < 1020 and y < 25:
                        running_klee = False
                        draw_page("guide", screen)
                    # HOME
                    if 1040 < x < 1105 and y < 25:
                        running_klee = False
            pygame.display.update()


def elem_click(screen, run_name, elem_name):
    while run_name:
        title_bg_page(screen, elem_name)
        home_page(screen, elem_name)
        char_image_load_final(screen, elem_name, 1, 2, 100, 400)
        for event_elem in pygame.event.get():
            if event_elem.type == pygame.QUIT:
                run_name = False
                running = False
            if event_elem.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                # QUIT
                if x > 1130 and y < 25:
                    run_name = False
                    running = False
                    exit()
                # GUIDE
                if 950 < x < 1020 and y < 25:
                    run_name = False
                    draw_page("guide", screen)
                # HOME
                if 1040 < x < 1105 and y < 25:
                    run_name = False
                # Fire
                if 90 < x < 180 and 220 < y < 320:
                    run_name = False
                    draw_page("fire", screen)
                # WATER
                if 270 < x < 370 and 220 < y < 320:
                    run_name = False
                    draw_page("water", screen)
                # WIND
                if 455 < x < 555 and 220 < y < 320:
                    run_name = False
                    draw_page("wind", screen)
                # ELEC
                if 640 < x < 740 and 220 < y < 320:
                    run_name = False
                    draw_page("elec", screen)
                # ICE
                if 825 < x < 925 and 220 < y < 320:
                    run_name = False
                    draw_page("ice", screen)
                # STONE
                if 1010 < x < 1100 and 220 < y < 320:
                    run_name = False
                    draw_page("stone", screen)

                if 100 < x < 250 and 400 < y < 550:
                    num = 1
                    level_load(screen, run_name, elem_name, num, 0)
                    run_name = False
                if 300 < x < 450 and 400 < y < 550:
                    num = 2
                    level_load(screen, run_name, elem_name, num, 0)
                    run_name = False
                if 500 < x < 650 and 400 < y < 550:
                    num = 3
                    level_load(screen, run_name, elem_name, num, 0)
                    run_name = False
                if 700 < x < 850 and 400 < y < 550:
                    num = 4
                    level_load(screen, run_name, elem_name, num, 0)
                    run_name = False
                if 900 < x < 1050 and 400 < y < 550 and \
                        (elem_name == "fire" or elem_name == "elec" or  elem_name =="ice"):
                    num = 5
                    level_load(screen, run_name, elem_name, num, 0)
                    run_name = False
                if 100 < x < 250 and 600 < y < 750 and (elem_name == "fire" or elem_name == "ice"):
                    num = 6
                    level_load(screen, run_name, elem_name, num, 0)
                    run_name = False
                if 300 < x < 450 and 600 < y < 750 and elem_name == "fire":
                    num = 7
                    level_load(screen, run_name, elem_name, num, 0)
                    run_name = False
                if 500 < x < 650 and 600 < y < 750 and elem_name == "fire":
                    num = 8
                    level_load(screen, run_name, elem_name, num, 0)
                    run_name = False
                # KLEE PAGE
                if 900 < x < 1050 and 400 < y < 550 and \
                    (elem_name == "water" or elem_name == "wind" or elem_name == "stone"):
                    level_load(screen, run_name, elem_name, 0, 1)
                    run_name = False
                if 100 < x < 250 and 600 < y < 750 and elem_name == "elec":
                    level_load(screen, run_name, elem_name, 0, 1)
                    run_name = False
                if 300 < x < 450 and 600 < y < 750 and elem_name == "ice":
                    level_load(screen, run_name, elem_name, 0, 1)
                    run_name = False
                if 700 < x < 850 and 600 < y < 750 and elem_name == "fire":
                    level_load(screen, run_name, elem_name, 0, 1)
                    run_name = False
        pygame.display.update()


def home_page(screen, elem_name):
    title_bg_page(screen, elem_name)
    screen.blit(drawText1("--------------------------------------Elements--------------------------------------",
                          "bradleyhandbold", 35, color(elem_name)), (40, 170))
    screen.blit(drawText1("-------------------------------------Characters-------------------------------------",
                          "bradleyhandbold", 35, color(elem_name)), (40, 330))
    elem_image_load(screen)


def draw_page(page_name, screen):
    global running
    if page_name == "guide":
        running_guide = True
        while running_guide:
            title_bg_page(screen, elem_name=" ")
            screen.blit(drawText1("Hello, traveler!", "bradleyhandbold", 28, (0, 0, 0)), (130, 200))
            screen.blit(drawText1("Maybe you found it's hard to count how many materials you need to upgrade",
                                  "bradleyhandbold", 28, (0, 0, 0)), (130, 240))
            screen.blit(drawText1("your characters. Don't worry! This calculator can help you!",
                                  "bradleyhandbold", 28, (0, 0, 0)), (100, 280))
            screen.blit(drawText1("First, please choose the element and the character you want to upgrade.",
                                  "bradleyhandbold", 28, (0, 0, 0)), (130, 320))
            screen.blit(drawText1("e.g.     CLICK                THEN  FIND  THE  CHARACTER  YOU  WANT",
                                  "bradleyhandbold", 28, (240, 80, 57)), (130, 400))
            screen.blit(drawText1("Second, please choose the level you want to upgrade to.",
                                  "bradleyhandbold", 28, (0, 0, 0)), (130, 500))
            screen.blit(drawText1("e.g.     I  WANT  TO  UPGRADE  TO                     SO  I  CLICK  IT.",
                                  "bradleyhandbold", 28, (240, 80, 57)), (130, 580))
            screen.blit(drawText1("90",
                                  "bradleyhandbold", 60, (240, 80, 57)), (600, 550))
            screen.blit(drawText1("Finally, you can get the result, including mora, exp, and materials.",
                                  "bradleyhandbold", 28, (0, 0, 0)), (130, 630))
            screen.blit(drawText1("You can go back to homepage whenever you click HOME in the upper right corner.",
                                  "bradleyhandbold", 28, (0, 0, 0)), (130, 670))
            screen.blit(drawText1("Also, you can check this guide by clicking ",
                                  "bradleyhandbold", 28, (0, 0, 0)), (130, 710))
            screen.blit(drawText1("                                                                             GUIDE.",
                                  "bradleyhandbold", 28, (255, 0, 0)), (130, 710))
            screen.blit(drawText1("(TAKE CARE OF KLEE !!!)",
                                  "bradleyhandbold", 20, (0, 0, 0)), (800, 750))
            ex_1 = pygame.image.load("icons/fire.png")
            ex_2 = pygame.image.load("cha icons/d.png")
            ex_1 = pygame.transform.scale(ex_1, (100, 100))
            ex_2 = pygame.transform.scale(ex_2, (100, 100))
            KLEE = pygame.image.load("emotes/kleeee.png")
            KLEE = pygame.transform.scale(KLEE, (50, 50))
            screen.blit(ex_1, (300, 360))
            screen.blit(ex_2, (1000, 360))
            screen.blit(KLEE, (1050, 730))
            for event_guide in pygame.event.get():
                if event_guide.type == pygame.QUIT:
                    running_guide = False
                    running = False
                if event_guide.type == pygame.MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.get_pos()
                    if x > 1130 and y < 25:
                        running_guide = False
                        running = False
                        exit()
                    if 1040 < x < 1105 and y < 25:
                        running_guide = False
            pygame.display.update()

    if page_name == "fire":
        global running_fire
        running_fire = True
        elem_click(screen, running_fire, "fire")

    if page_name == "water":
        global running_water
        running_water = True
        elem_click(screen, running_water, "water")

    if page_name == "wind":
        global running_wind
        running_wind = True
        elem_click(screen, running_wind, "wind")

    if page_name == "elec":
        global running_elec
        running_elec = True
        elem_click(screen, running_elec, "elec")

    if page_name == "ice":
        global running_ice
        running_ice = True
        elem_click(screen, running_ice, "ice")

    if page_name == "stone":
        global running_stone
        running_stone = True
        elem_click(screen, running_stone, "stone")


def title_bg_page(screen, elem_name):
    bg = pygame.image.load("bg_image/bg22.jpg")
    bg = pygame.transform.scale(bg, (1200, 800))
    screen.blit(bg, (0, 0))
    logo = pygame.image.load("emotes/Genshin-Impact-Logo.png")
    logo = pygame.transform.scale(logo, (200, 76))
    screen.blit(logo, (500, 0))
    emote1 = pygame.image.load("emotes/paimeng?.png")
    emote1 = pygame.transform.scale(emote1, (80, 80))
    emote2 = pygame.image.load("emotes/paimeng_home.png")
    emote2 = pygame.transform.scale(emote2, (100, 100))
    emote3 = pygame.image.load("emotes/paimeng_quit.png")
    emote3 = pygame.transform.scale(emote3, (80, 80))
    screen.blit(emote1, (950, 35))
    screen.blit(emote2, (1025, 27))
    screen.blit(emote3, (1120, 33))
    hutao = pygame.image.load("emotes/hutao.png")
    hutao = pygame.transform.scale(hutao, (140, 140))
    screen.blit(hutao, (150, 0))
    screen.blit(drawText1("Quit", "bradleyhandbold", 28, (0, 0, 0)), (1130, 0))
    screen.blit(drawText1("Home", "bradleyhandbold", 28, (0, 0, 0)), (1040, 0))
    screen.blit(drawText1("Guide", "bradleyhandbold", 28, (255, 0, 0)), (950, 0))
    screen.blit(drawText1("Genshin Impact Calculator", "arialroundedbold", 48, color(elem_name)), (300, 70))


def main():
    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("Genshin Impact Calculator")
    icon = pygame.image.load(r"icons/ice.png")
    pygame.display.set_icon(icon)
    global running
    running = True

    while running:
        title_bg_page(screen, elem_name=" ")
        home_page(screen, elem_name=" ")

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                if x > 1130 and y < 25:
                    running = False
                if 950 < x < 1020 and y < 25:
                    draw_page("guide", screen)
                if 90 < x < 180 and 220 < y < 320:
                    draw_page("fire", screen)
                if 270 < x < 370 and 220 < y < 320:
                    draw_page("water", screen)
                if 455 < x < 555 and 220 < y < 320:
                    draw_page("wind", screen)
                if 640 < x < 740 and 220 < y < 320:
                    draw_page("elec", screen)
                if 825 < x < 925 and 220 < y < 320:
                    draw_page("ice", screen)
                if 1010 < x < 1100 and 220 < y < 320:
                    draw_page("stone", screen)

        pygame.display.update()


if __name__ == '__main__':
    main()
