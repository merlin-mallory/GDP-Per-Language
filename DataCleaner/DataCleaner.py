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

        # Dataframes containing all country, all year, modified data
        self.wb_ppp_mod = None
        self.wb_nom_mod = None
        self.imf_ppp_mod = self.create_imf_ppp_mod()
        self.imf_nom_mod = None

        # Dataframe that contains % of world GDP per language, for all years of data
        self.imf_ppp_full = self.group_imf_gdp_ppp_by_language()

        # Dictionary that will hold per language summary statistics, categorized by year/data source/data measure
        self.gdp_dict = {}
        for i in range(1980, 2029):
            self.gdp_dict[i] = {
                "World Bank": {
                    "gdp_ppp": None,
                    "gdp_nom": None
                },
                "IMF": {
                    "gdp_ppp": None,
                    "gdp_nom": None
                }
            }

    def import_country_to_lang(self):
        result = pd.read_excel('DataSource/Country_To_Lang.xls', sheet_name='Sheet1', engine='xlrd')
        return result

    def create_lang_to_country(self):
        new_df = self.country_to_lang.groupby('Language').agg({'Country': list})
        new_df = new_df.reset_index().rename(columns={'Language': 'Language',
                                                      'Country': 'List of Countries In Language Group'})
        return new_df

    def export_lang_to_country_to_xls(self):
        df = self.lang_to_country
        file_name = 'DataSource/Lang_To_Country.xlsx'
        with pd.ExcelWriter(file_name, engine='openpyxl') as writer:
            df.to_excel(writer, index=False, sheet_name='Sheet1')
        return

    def create_imf_ppp_mod(self):
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

        # Remove the World Data at the bottom of the frame
        row_to_remove = df[df['Country'] == 'World'].index
        df = df.drop(row_to_remove)

        # Write the data to the mod file
        file_name = 'DataSource/mod/imf_ppp_mod.xlsx'
        with pd.ExcelWriter(file_name, engine='openpyxl') as writer:
            df.to_excel(writer, index=False, sheet_name='Sheet1')

        return df

    def group_imf_gdp_ppp_by_language(self):
        # Import the relevant mod file and dictionary
        df1 = self.imf_ppp_mod
        df2 = self.country_to_lang

        # Merge the Country to Language info with the mod info
        df = pd.merge(df1, df2, on='Country', how='outer')

        # This will result in many rows of NaN, so lets drop them.
        cleaned_df = df.dropna(subset=['Country'])

        # Now lets group the data by language.
        grouped_by_language = df.groupby('Language')
        sum_by_language = grouped_by_language.sum()
        df = sum_by_language.reset_index()
        return df

    def generate_annual_summary_stats(self):
        # Grab the appropriate full data
        df = self.imf_ppp_full


        # Locate the starting and ending point of the loop
        starting_year = df.columns[1]
        ending_year = df.columns[-1]

        # Loop through every year of data, creating annual reports, and save them in the gdp_dict.
        for i in range(starting_year, ending_year+1):
            temp_df = df[['Language', i]]


