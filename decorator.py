from datetime import datetime
import os

def Logger(file_name:str):
    def new_function(function):
        def log_maker(*args, **kwargs):
            BASE = f'{os.getcwd()}\\'
            start = datetime.now()
            result = function(*args, **kwargs)
            with open(f'{BASE+file_name}', 'a', encoding='utf-8') as file:
                file.write(f'{start}: Функция - {function.__name__}, аргументы - {args}{kwargs}, результат - {result}\n')
            return result
        return log_maker
    return(new_function)