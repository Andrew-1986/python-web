import asyncio
from aiopath import AsyncPath
from asyncio import run, gather
import os
import shutil
import re


def normalize(text):
    symbols = ("абвгдеёзийклмнопрстуфхъыьэАБВГДЕЁЗИЙКЛМНОПРСТУФХЪЫЬЭ",
               "abvgdeezijklmnoprstufh'y'eABVGDEEZIJKLMNOPRSTUFH'Y'E")

    compare_symbols = {ord(a):ord(b) for a, b in zip(*symbols)}

    translated = text.translate(compare_symbols)
    translated = re.sub(r'\W', '_', text)

    return translated


async def file_handler(path, param):
    imgs_extension = ['jpeg', 'png', 'jpg', 'psd']
    imgs_list = []
    docs_extension = ['doc', 'docx', 'txt', 'pdf', 'xlsx', 'xls', 'pptx']
    docs_list = []
    video_extension = ['avi', 'mp4', 'mov']
    video_list = []
    music_extension = ['mp3', 'ogg', 'wav', 'amr']
    music_list = []
    archive_extension = ['zip', 'gz', 'tar']
    archive_list = []
    folders = []
    files = os.listdir(path)
    
    if files:
        for file in files:
            new_element = file.split('.')
            
            if new_element[-1] in imgs_extension:
                imgs_list.append(file)
            elif new_element[-1] in docs_extension:
                docs_list.append(file)
            elif new_element[-1] in video_extension:
                video_list.append(file)
            elif new_element[-1] in music_extension:
                music_list.append(file)
            elif new_element[-1] in archive_extension:
                archive_list.append(file)
            elif os.path.isdir(path + f'\{file}') and len(os.listdir(path + f'\{file}')) != 0:
                folders.append(file)
            elif os.path.isdir(path + f'\{file}') and len(os.listdir(path + f'\{file}')) == 0:
                os.removedirs(path + f'\{file}')
                
        if param == "imgs":
            return imgs_list
        elif param == "docs":
            return docs_list
        elif param == "video":
            return video_list
        elif param == "music":
            return music_list
        elif param == "archive":
            return archive_list
        elif param == "folders":
            return folders
        else:
            return None
    else:
        os.removedirs(path)


async def imgs_handle(path):
    files_list = await file_handler(path, 'imgs')
    folders = await file_handler(path, 'folders')
    os.makedirs(f'{path}\images')
    
    for file in files_list:
        if os.path.isfile(f'{path}\{file}'):
            shutil.copyfile(f'{path}\{file}', f'{path}\images\{normalize(file)}')
            
    await asyncio.sleep(2)
    
    for folder in folders:
        if folder not in ['images', 'documents', 'music', 'video', 'archives']:
            await picture_handle(f'{path}\{folder}')
    

async def docs_handle(path):
    files_list = await file_handler(path, 'docs')
    folders = await file_handler(path, 'folders')  
    os.makedirs(f'{path}\documents')
    
    for file in files_list:
        if os.path.isfile(f'{path}\{file}'):
            shutil.copyfile(f'{path}\{file}', f'{path}\documents\{normalize(file)}')
            
    await asyncio.sleep(2)
    
    for folder in folders:
        if folder not in ['images', 'documents', 'music', 'video', 'archives']:
            await document_handle(f'{path}\{folder}')
            

async def video_handle(path):
    files_list = await file_handler(path, 'video')
    folders = await file_handler(path, 'folders')   
    os.makedirs(f'{path}\video')
    
    for file in files_list:
        if os.path.isfile(f'{path}\{file}'):
            shutil.copyfile(f'{path}\{file}', f'{path}\video\{normalize(file)}')
            
    await asyncio.sleep(2)
    
    for folder in folders:
        if folder not in ['images', 'documents', 'music', 'video', 'archives']:
            await video_handle(f'{path}\{folder}')


async def music_handle(path):
    files_list = await file_handler(path, 'music')
    folders = await file_handler(path, 'folders')   
    os.makedirs(f'{path}\music')
    
    for file in files_list:
        if os.path.isfile(f'{path}\{file}'):
            shutil.copyfile(f'{path}\{file}', f'{path}\music\{normalize(file)}')
            
    await asyncio.sleep(2)
    
    for folder in folders:
        if folder not in ['images', 'documents', 'music', 'video', 'archives']:
            await music_handle(f'{path}\{folder}')
            

async def archive_handle(path):
    files_list = await file_handler(path, 'archive')
    folders = await file_handler(path, 'folders')
    os.makedirs(f'{path}\archives')
    
    for file in files_list:
        if os.path.isfile(f'{path}\{file}'):
            shutil.unpack_archive(f'{path}\{file}', f'{path}\archives\{normalize(file)}')
            
    await asyncio.sleep(2)
    
    for folder in folders:
        if folder not in ['images', 'documents', 'music', 'video', 'archives']:
            await archive_handle(f'{path}\{folder}')


async def main():
    path = input("Choose directory: ")
    tasks = [imgs_handle(path), docs_handle(path), music_handle(path), video_handle(path), archive_handle(path)]
    await gather(*tasks)


if __name__ == "__main__":
    run(main())
