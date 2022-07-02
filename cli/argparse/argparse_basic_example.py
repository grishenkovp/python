from argparse import ArgumentParser


def main(my_str1, my_str2, my_str3):
    my_string = f"{my_str1} {my_str2} {str(my_str3)}"
    print(my_string)


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("--arg1", dest="str1", help="This is str1", type=str)
    parser.add_argument("--arg2", dest="str2", help="This is str2", type=str)
    parser.add_argument("--arg3", dest="str3", help="This is str3", type=int, choices=[0, 1, 2, 3, 4, 5], default=1)
    args = parser.parse_args()

    # Запуск в терминале: python test.py --arg1 "Тест" --arg2 "номер" --arg3 3
    main(args.str1, args.str2, args.str3)
