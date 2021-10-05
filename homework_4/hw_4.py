import os
import sys
from pathlib import Path
import shutil
from threading import Thread
import re


def normalize(text):
    symbols = ("абвгдеёзийклмнопрстуфхъыьэАБВГДЕЁЗИЙКЛМНОПРСТУФХЪЫЬЭ",
               "abvgdeezijklmnoprstufh'y'eABVGDEEZIJKLMNOPRSTUFH'Y'E")

    compare_symbols = {ord(a):ord(b) for a, b in zip(*symbols)}

    translated = text.translate(compare_symbols)
    translated = re.sub(r'\W', '_', text)

    return translated


def sort_files(path):
    images = ['jpeg', 'png', 'jpg', 'psd']
    docs = ['doc', 'docx', 'txt', 'pdf', 'xlsx', 'xls', 'pptx']
    video = ['avi', 'mp4', 'mov']
    music = ['mp3', 'ogg', 'wav', 'amr']
    archives = ['zip', 'gz', 'tar']
    files = os.listdir(path)

    if files:
        os.makedirs(f'{path}\images')
        os.makedirs(f'{path}\documents')
        os.makedirs(f'{path}\\video')
        os.makedirs(f'{path}\music')
        os.makedirs(f'{path}\\archives')

        for element in files:
            new_element = element.split('.')
            new_element_str = '.'.join(new_element[0:-1])
            if new_element[-1].lower() in images:
                if os.path.isfile(f'{path}\{element}'):
                    shutil.copyfile(f'{path}\{element}', f'{path}\images\{normalize(new_element_str)}.{new_element[-1]}')
            if new_element[-1].lower() in docs:
                if os.path.isfile(f'{path}\{element}'):
                    shutil.copyfile(f'{path}\{element}', f'{path}\documents\{normalize(new_element_str)}.{new_element[-1]}')
            if new_element[-1].lower() in video:
                if os.path.isfile(f'{path}\{element}'):
                    shutil.copyfile(f'{path}\{element}', f'{path}\video\{normalize(new_element_str)}.{new_element[-1]}')
            if new_element[-1].lower() in music:
                if os.path.isfile(f'{path}\{element}'):
                    shutil.copyfile(f'{path}\{element}', f'{path}\music\{normalize(new_element_str)}.{new_element[-1]}')
            if new_element[-1].lower() in archives:
                if os.path.isfile(f'{path}\{element}'):
                    shutil.unpack_archive(f'{path}\{element}', f'{path}\archives\{normalize(new_element_str)}')

    files = os.listdir(path)

    for element in files:
        if os.path.isdir(path + f'\{element}') and len(os.listdir(path + f'\{element}')) == 0:
            os.removedirs(path + f'\{element}')


def deep_sort_files(path):
    files = os.listdir(path)
    
    if files:
        for element in files:
            if os.path.isdir(f'{path}\{element}') and element not in ['images', 'documents', 'video', 'music', 'archives']:
                    sort_files(f'{path}\{element}')
    

def main():
    path = input("Choose directory: ")

    sort_files(path)

    t1 = Thread(target=deep_sort_files, args=(fr'{path}', ))
    t1.start()


if __name__ == "__main__":
    main()
