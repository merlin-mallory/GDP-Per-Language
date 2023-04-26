import pandas as pd
import numpy as np
import xlwt
from openpyxl import Workbook, load_workbook

class Data:
    def __init__(self):
        # Dictionaries
        self.country_to_lang = self.import_country_to_lang()
        self.lang_to_country = self.create_lang_to_country()
        self.export_lang_to_country_to_xls()

        # Current dataframes
        self.wb_ppp = None
        self.wb_nom = None
        self.imf_ppp = self.import_imf_ppp()
        self.imf_nom = None
    def import_country_to_lang(self):
        result = pd.read_excel('DataSource/Country_To_Lang.xls', sheet_name='Sheet1', engine='xlrd')
        return result

    def create_lang_to_country(self):
        new_df = self.country_to_lang.groupby('Language').agg({'Country Name': list})
        new_df = new_df.reset_index().rename(columns={'Language': 'Language',
                                                      'Country Name': 'List of Countries In Language Group'})
        return new_df

    def export_lang_to_country_to_xls(self):
        df = self.lang_to_country
        file_name = 'DataSource/Lang_To_Country.xlsx'
        with pd.ExcelWriter(file_name, engine='openpyxl') as writer:
            df.to_excel(writer, index=False, sheet_name='Sheet1')
        return

    def import_imf_ppp(self):
        # Import the file
        sheet_name = 'PPPGDP'
        df = pd.read_excel('DataSource/raw/imf_ppp.xls', sheet_name='PPPGDP', engine='xlrd')

        # Rename the first column as "Country"
        target_column_index = 0
        old_column_name = df.columns[target_column_index]
        new_column_name = 'Country'
        df = df.rename(columns={old_column_name: new_column_name})

        # Grab the world GDP row
        world_data = df[df["Country"] == "World"]

        # Locate Zimbabwe's index, we want to delete all the rows after Zimbabwe
        mask = df["Country"] == "Zimbabwe"
        index_of_zimbabwe = df.loc[mask].index
        print("index of z:", index_of_zimbabwe)

        # Delete all of the rows after Zimbabwe's index
        df = df.iloc[:index_of_zimbabwe[0]+1]

        # Add back in the world data
        df = pd.concat([df, world_data], ignore_index=True)

        # Replace all of the values that says "no data" with "NaN"
        df = df.replace('no data', float('nan'))

        def calculate_percentage(row):
            world_data = df[df["Country"] == "World"]
            for year in df.columns[1:]:
                row[year] = (row[year] / world_data[year].values[0]) * 100
            return row

        # Calculate percent of global GDP for each country and year
        df = df.apply(calculate_percentage, axis=1)

        return df

