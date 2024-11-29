class Dictionary:
    def __init__(self):
        self.translations = {}

    def add_translation(self, word, translation):
        self.translations[word] = translation
        self.translations[translation] = word  # Allow reverse lookup

    def translate(self, word):
        return self.translations.get(word, "თარგმანი ვერ მოიძებნა")

    def load_from_file(self, filename):
        try:
            with open(filename, 'r', encoding='utf-8') as file:
                for line in file:
                    line = line.strip()
                    if ":" in line:
                        word, translation = line.split(":", 1)
                        self.add_translation(word.strip(), translation.strip())
            print(f"ლექსიკონი დატვირთულია ფაილიდან: {filename}.")
        except FileNotFoundError:
            print(f"ფაილი '{filename}' არ მოიძებნა. ახალი ლექსიკონის შეიქმნა.")
        except Exception as e:
            print(f"ფაილის დამუშავება ვერ მოხერხდა: {e}")

    def save_to_file(self, filename):
        unique_translations = set()
        try:
            with open(filename, 'w', encoding='utf-8') as file:
                for word, translation in self.translations.items():
                    if (word, translation) not in unique_translations and (translation, word) not in unique_translations:
                        file.write(f"{word}:{translation}\n")
                        unique_translations.add((word, translation))
            print(f"თარგმანი შენახულია ფაილში: {filename}.")
        except Exception as e:
            print(f"ფაილის შენახვა ვერ მოხერხდა: {e}")


class Translator:
    def __init__(self):
        self.dictionary = Dictionary()

    def add_translation(self):
        word = input("შეიყვანეთ სიტყვა: ")
        translation = input("შეიყვანეთ თარგმანი: ")
        self.dictionary.add_translation(word, translation)
        print("თარგმანი დამატებულია")

    def translate_word(self):
        word = input("შეიყვანეთ სიტყვა: ")
        translation = self.dictionary.translate(word)
        print(f"თარგმანი: {translation}")

    def save_translations(self):
        self.dictionary.save_to_file("translations.txt")


def main():
    translator = Translator()
    translator.dictionary.load_from_file("translations.txt")

    while True:
        print("\nთარჯიმანის მენიუ:")
        print("1. დაამატეთ თარგმანი")
        print("2. თარგმნეთ სიტყვა")
        print("3. შეინახეთ თარგმანი")
        print("4. გამოსვლა")

        choice = input("აირჩიეთ მოქმედება (1-4): ")

        if choice == "1":
            translator.add_translation()
        elif choice == "2":
            translator.translate_word()
        elif choice == "3":
            translator.save_translations()
        elif choice == "4":
            print("თქვენ გამოხვედით პროგრამიდან")
            break
        else:
            print("შესაძლებელია მხოლოდ 1-4 შეყვანა")


if __name__ == "__main__":
    main()
