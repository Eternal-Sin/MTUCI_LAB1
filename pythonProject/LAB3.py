def ExampleTextFunc():

    try:
        with open("example.txt","r") as exampleFile:
            if(input("Введите S для вывода построчно/Любой другой символ для вывода целиком: ") == "S"):
                for line in exampleFile:
                    print(line)

            else:
                print(exampleFile.read())
            return

    except FileNotFoundError:
        print("Файл не найден!")
        if (input("Введите Y для перезапуска/Любой другой символ для окончания: ") == "Y"):
            ExampleTextFunc()
        else:
            return


def UserTextFunc(userText):

    try:
        with open("user_input.txt", "a") as userInputFile:
            userInputFile.write(userText)
            return

    except FileNotFoundError:
        print("Файл не найден!")
        if(input("Введите Y для перезапуска/Любой другой символ для окончания: ") == "Y"):
            UserTextFunc(input("Введите текст: "))
        else:
            return


ExampleTextFunc()

UserTextFunc(input("Введите текст: "))