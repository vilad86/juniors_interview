import asyncio
import csv
import os
import time

import aiohttp
from bs4 import BeautifulSoup, Tag

async def grab_page_content(url: str) -> str:
    """Grab page content.

    Args:
        url (str): url page.

    Returns:
        str: Page content.
    """
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            response.raise_for_status()
            content = await response.text()
            return content

async def сount_all_animals_category(url: str, category: str) -> int:
    """Count all animals from the specified category

    Returns:
        int: Number of animals in the category.
    """

    count_animals_category = 0

    #: Делаем первый запрос, чтобы узнать какое животное расположено в конце списка...
    #: Чтобы отталкиваться от него в дальнейшем.
    animals: list[str] = await grab_animals_from(url, category)

    if (not animals):
        print(f'[~] Категория - {category} | животных: {count_animals_category}')
        return count_animals_category

    count_animals_category += len(animals)
    
    while (len(animals := await grab_animals_from(url, category, animals[-1])) > 1):
        count_animals_category += len(animals) - 1

    print(f'[~] Категория - {category} | животных: {count_animals_category}')

    return count_animals_category

async def grab_animals_from(url: str, category: str, from_: str = None) -> list[str]:
    r"""Grab all animals from the category on this page.

    Args:
        url (str): URL wikipedia:category
        category (str): Column name\category. Example: 'А' or 'Б' or 'В' ...
        from (str, optional): Where to start, for example, it can be the category itself, or the name of one of the elements in the column\category. Defaults to None, and used :param:`category`.

    Returns:
        list[str]: List animals: [Бабизяна, Курва бобир, Китик, ...]
    """
    
    if (from_ is None): from_ = category
    url_category = url + f'?from={from_}'

    content: str = await grab_page_content(url_category)
    soup = BeautifulSoup(content, 'html.parser')
    category_columns_content: Tag = soup.find('div', {'class': 'mw-category mw-category-columns'})
    category_columns: list[Tag] = category_columns_content.find_all('div', {'class': 'mw-category-group'})
    
    if (not category_columns): return []
    
    category_name: str = category_columns[0].find('h3').text
    if (category_name.upper() != category.upper()): return []
    
    category_element: Tag = category_columns[0]

    animals: list[str] = [animal_element.text for animal_element in category_element.find_all('a')]
    return animals

async def main():
    #: ------------------------------------- CONST -------------------------------------
    ALF = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя".upper()

    CURRENT_DIR = os.path.abspath(os.path.dirname(__file__))
    FILENAME = 'beasts.csv'
    FULL_PATH = os.path.join(CURRENT_DIR, FILENAME)

    URL = "https://ru.wikipedia.org/wiki/Категория:Животные_по_алфавиту"
    #: ---------------------------------------------------------------------------------
    
    print(f'[+][START] Запуск подсчета животных в категориях от "{ALF[0]}" до "{ALF[-1]}".')
    start = time.time()
    results: list[int] = await asyncio.gather(*[сount_all_animals_category(URL, category) for category in ALF])
    end = time.time()
    print(f'[+][  END] Подсчет закончен. Это заняло: {round(end-start, 2)} сек.')
    print(f'[+] Запись результата в файл "{FILENAME}".')
    
    data = [[category, count] for category, count in zip(ALF, results)]

    #: Запись в файл
    with open(FULL_PATH, mode="w", encoding="utf-8", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(data)

    print(f'[+] Результат записан!')
    print(f'[~] Путь до файла: "{FULL_PATH}".')

    #: Вот бы консольку расскрасить :\

if (__name__ == '__main__'):
    asyncio.run(main())


