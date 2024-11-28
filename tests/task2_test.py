import unittest
from unittest.mock import patch
from aioresponses import aioresponses

from task2.solution import (grab_page_content, 
                            grab_animals_from, 
                            сount_all_animals_category)

class Task2_Test(unittest.IsolatedAsyncioTestCase):

    async def test_grab_page_content(self):
        url = "https://example_url.com"
        content = "<html><body>Test</body></html>"
        
        with aioresponses() as mocked:
            mocked.get(url, status = 200, body = content)
            result = await grab_page_content(url)
            self.assertEqual(result, content)

    async def test_grab_page_content_raises(self):
        url = "https://example_url.com"
        
        with aioresponses() as mocked:
            mocked.get(url, status = 404)
            with self.assertRaises(Exception):
                await grab_page_content(url)

    async def test_grab_animals_from(self):
        url = 'https://example_url.com'
        category = 'А' 
        page_content = """
        <div class="mw-category mw-category-columns">
            <div class="mw-category-group">
                <h3>А</h3>
                <ul>
                    <li><a href="/link1">Китик</a></li>
                    <li><a href="/link2">Курва бобир</a></li>
                </ul>
            </div>
        </div>
        """
        
        with patch('task2.solution.grab_page_content', return_value = page_content):
            result = await grab_animals_from(url, category)
            self.assertEqual(result, ["Китик", "Курва бобир"])

    async def test_grab_animals_from_empty(self):
        url = 'https://example_url.com'
        category = 'А'
        page_content = """
        <div class="mw-category mw-category-columns">
        </div>
        """
        
        with patch('task2.solution.grab_page_content', return_value=page_content):
            result = await grab_animals_from(url, category)
            self.assertEqual(result, [])

    async def test_count_all_animals_category(self):
        url = 'https://example_url.com'
        category = 'А'

        def castom_grab_animals(url, category, from_=None):
            if from_ is None:
                return ["Китик", "Козлик", "Кукушка"]
            elif from_ == "Кукушка":
                return ["Кукушка", "Куница"]
            else:
                return []

        with patch('task2.solution.grab_animals_from', side_effect=castom_grab_animals):
            result = await сount_all_animals_category(url, category)
            self.assertEqual(result, 4)