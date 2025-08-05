def plot(name, win, attack, relaunch, die_list, pro_die):

    ###-----------Códigos_de_color_ANSI-------------###
    RESET       = "\033[0m"
    BLACK       = "\033[30m"
    ROJO        = "\033[31m"
    VERDE       = "\033[32m"
    AMARILLO    = "\033[33m"
    AZUL        = "\033[34m"
    MAGENTA     = "\033[35m"
    CYAN        = "\033[36m"
    WHITE       = "\033[37m"
    NEGRITA     = "\033[1m"

    ###----------------Print_info-------------------###
    print(str("\n") + f"{NEGRITA}{MAGENTA}" + str(name) + f"{RESET}")
    print(f" -- Probability win: {round((1-win)*100, 4)}%")
    print(f" -- Probability attack true: {round(attack*100, 4)}%")
    print(f" -- Probability relaunch attack: {round(relaunch*100, 4)}%")
    print(str("\n") + str(f"{CYAN} ----------- Blows to die ------------ {RESET}"))
    for i   in  range(len(die_list)):
        n   =   int(pro_die[i]*10)
        print(f"{die_list[i]} {"::"*n} {round((pro_die[i])*100)}%")

