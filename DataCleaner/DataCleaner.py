class Data:
    def __init__(self):
        # Current dataframes
        self.wb_ppp = None
        self.wb_nom = None
        self.imf_ppp = None
        self.imf_nom = None

        # Dictionaries
        self.lang_to_country = {}
        self.country_to_lang = {}
