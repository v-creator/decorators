import os
import datetime

def my_logger(old_function):
    def new_function(*args, **kwargs):
        date_and_time = datetime.datetime.now()
        result = old_function(*args, **kwargs)
        if old_function.__name__ == 'get_article':
            log_result = 'html_code'
        elif old_function.__name__ == 'read_article':
            log_result = 'html_code'
            args = {'article_args': 'html_code'}
        else:
            log_result = result
        with open('scrapping.log', 'a', encoding='utf-8') as f:
            text = f'{date_and_time} {old_function.__name__} {tuple(args)} {tuple(kwargs.values())} {log_result}'
            f.write(text)
            f.write('\n')
        return result
    return new_function