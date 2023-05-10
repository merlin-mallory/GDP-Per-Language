from DataCleaner import *
class Data:
    def __init__(self):
        # Dictionaries
        self.country_to_lang = self.import_country_to_lang()
        self.lang_to_country = self.create_lang_to_country()
        self.export_lang_to_country_to_xls()

