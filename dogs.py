# Эта программа позволяет определить породу собаки (операторы if, else)

answer = input("Собака короткошерстной породы? ")
if answer.lower().strip() == "да":
    answer = input("У собаки рост менее 50 см? ")
    if answer.lower().strip() == "да":
        answer = input("У собаки короткий хвост? ")
        if answer.lower().strip() == "да":
            print("Английский бульдог")
        else:
            answer = input('У собаки длинные уши? ')
            if answer.lower().strip() == "да":
                print("Гончая")
            else:
                answer = input('У собаки короткое тело? ')
                if answer.lower().strip() == "да":
                    print("Мопс")
                else:
                    print("Чихуахуа")
    else:
        answer = input("Собака весит более 50 кг? ")
        if answer.lower().strip() == "да":
            print("Датский дог")
        else:
            print("Фоксхаунд")
else:
    answer = input("У собаки рост менее 50 см? ")
    if answer.lower().strip() == "да":
        answer = input("У собаки доброжелательный характер? ")
        if answer.lower().strip() == "да":
            print("Кокер-спаниэль")
        else:
            print("Ирландский сеттер")
    else:
        answer = input("У собаки рост менее 70 см? ")
        if answer.lower().strip() == "да":
            answer = input("У собаки длинные уши? ")
            if answer.lower().strip() == "да":
                print("Большой вандейский грифон")
            else:
                print("Колли")
        else:
            answer = input("Окрас с белыми отметинами? ")
            if answer.lower().strip() == "да":
                print("Сенбирнар")
            else:
                answer = input("Белоснежный окрас? ")
                if answer.lower().strip() == "да":
                    print("Ирландский волкодав")
                else:
                    print("Ньюфаундленд")