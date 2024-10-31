import string
import re

class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        for file_name in self.file_names:
            try:
                with open(file_name, 'r', encoding='utf-8') as file:
                    text = file.read().lower()
                    words = re.findall(r"\b\w+'?\w*|\w+\b", text)
                    all_words[file_name] = words
            except FileNotFoundError:
                print(f"Файл {file_name} не найден.")
        return all_words

    def find(self, target_word):
        all_words = self.get_all_words()
        results = {}
        for file_name, words in all_words.items():
            if target_word.lower() in words:
                results[file_name] = words.index(target_word.lower()) + 1
        return results

    def count(self, target_word):
        all_words = self.get_all_words()
        results = {}
        for file_name, words in all_words.items():
            results[file_name] = words.count(target_word.lower())
        return results

finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())
print(finder2.find('text'))
print(finder2.count('text'))
