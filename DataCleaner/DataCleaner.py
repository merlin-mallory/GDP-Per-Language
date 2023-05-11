import pandas as pd
import numpy as np
import xlwt
from openpyxl import Workbook, load_workbook

class Data:
    def __init__(self):
        # Dictionaries
        self.country_to_lang = self.import_country_to_lang()
        self.lang_to_country_imf = self.create_lang_to_country()
        self.export_lang_to_country_to_xls()
        #
        # # Dataframes containing all country, all year, modified data
        # self.imf_ppp_mod = self.create_mod('imf', 'ppp')
        # self.imf_nom_mod = self.create_mod('imf', 'nom')
        self.wb_ppp_mod = self.create_mod('wb', 'ppp')
        # self.wb_nom_mod = None
        #
        # # Dataframe that contains % of world GDP per language, for all years of data
        # self.imf_ppp_full = self.group_by_language('imf', 'ppp')
        # self.imf_nom_full = self.group_by_language('imf', 'nom')
        # self.wb_ppp_full = None
        # self.wb_nom_full = None
        #
        # # Dictionary that will hold per language summary statistics, categorized by [year][data source][data measure]
        # self.gdp_dict = {}
        # for i in range(1960, 2029):
        #     self.gdp_dict[i] = {
        #         "wb": {
        #             "ppp": None,
        #             "nom": None
        #         },
        #         "imf": {
        #             "ppp": None,
        #             "nom": None
        #         }
        #     }
        #
        # self.generate_annual_summary_stats('imf', 'ppp')
        # self.generate_annual_summary_stats('imf', 'nom')

    def import_country_to_lang(self):
        result = pd.read_excel('DataSource/CountryNameLanguageMap.xls', sheet_name='Sheet1', engine='xlrd')
        return result

    def create_lang_to_country(self):
        new_df = self.country_to_lang
        columns_to_drop = ['IMF Name', 'WB Name', 'WB Code']
        new_df = new_df.drop(columns_to_drop, axis=1)
        new_df = self.country_to_lang.groupby('Language').agg({'PowerBI Name': list})
        new_df = new_df.reset_index().rename(columns={'Language': 'Language',
                                                      'PowerBI Name': 'List of Countries In Language Group'})
        return new_df

    def export_lang_to_country_to_xls(self):
        df = self.lang_to_country_imf
        file_name = 'DataSource/Lang_To_Country.xlsx'
        with pd.ExcelWriter(file_name, engine='openpyxl') as writer:
            df.to_excel(writer, index=False, sheet_name='Sheet1')
        return

    def create_mod(self, data_source, data_measure):
        # Import the file
        if data_source == 'imf' and data_measure == 'ppp':
            my_sheet_name = 'PPPGDP'
        elif data_source == 'imf' and data_measure == 'nom':
            my_sheet_name = 'NGDPD'
        elif data_source == 'wb' and data_measure == 'ppp':
            my_sheet_name = 'Data'
        else: # datasource == 'wb' and data_measure == 'nom'
            my_sheet_name = 'Data'

        path = 'DataSource/raw/' + data_source + '_' + data_measure + '.xls'
        df = pd.read_excel(path, sheet_name=my_sheet_name, engine='xlrd')

        # print('DF before first 3 drop:')
        # print(df.head())
        # Initialize the top rows
        if data_source == 'wb':
            # Drop the first 3 rows of the header, should be 'Data Source', 'Last Updated Date', and 'Header'
            df = df.iloc[2:]
            # Next, reassign the column names
            df.reset_index(drop=True, inplace=True)
            df.columns = df.iloc[0]
            df = df.iloc[1:]
            df.reset_index(drop=True, inplace=True)
            # Adjust the country's name column
            df.rename(columns={'Country Name': 'Country'}, inplace=True)
            df.columns = df.columns.astype(str)
            df.columns = df.columns.str.replace(r'\.0$', '', regex=True)
        # print('DF after first 3 drop:')
        # print(df.head())

        # Continue here...

        # Convert names to PowerBI Names
        if data_source == 'imf':
            names_to_change = {
                'Bahamas, The': 'Bahamas',
                'Brunei Darussalam': 'Brunei',
                'Cabo Verde': 'Cape Verde',
                'China, People\'s Republic of': 'China',
                'Congo, Dem. Rep. of the': 'Democratic Republic of the Congo',
                'Congo, Republic of': 'Republic of the Congo',
                'Czech Republic': 'Czechia',
                'Gambia, The': 'The Gambia',
                'Hong Kong SAR': 'Hong Kong',
                'Korea, Republic of': 'South Korea',
                'Kyrgyz Republic': 'Kyrgyzstan',
                'Macao SAR': 'Macao',
                'Micronesia, Fed. States of': 'Federated States of Micronesia',
                'Russian Federation': 'Russia',
                'South Sudan, Republic of': 'South Sudan',
                'Taiwan Province of China': 'Taiwan',
                'Türkiye, Republic of': 'Turkey',
                }
        else:   # data_source = 'wb'
            names_to_change = {
                'Bahamas, The': 'Bahamas',
                'Brunei Darussalam': 'Brunei',
                'Cabo Verde': 'Cape Verde',
                'Congo, Dem. Rep.': 'Democratic Republic of the Congo',
                'Congo, Rep.': 'Republic of the Congo',
                'Cote d\'Ivoire': 'Côte d\'Ivoire',
                'Egypt, Arab Rep.': 'Egypt',
                'Gambia, The': 'The Gambia',
                'Hong Kong SAR, China': 'Hong Kong',
                'Iran, Islamic Rep.': 'Iran',
                'Korea, Rep.': 'South Korea',
                'Kyrgyz Republic': 'Kyrgyzstan',
                'Lao PDR': 'Lao P.D.R.',
                'Macao SAR, China': 'Macao',
                'Micronesia, Fed. Sts.': 'Federated States of Micronesia',
                'Russian Federation': 'Russia',
                'St. Kitts and Nevis': 'Saint Kitts and Nevis',
                'St. Lucia': 'Saint Lucia',
                'St. Vincent and the Grenadines': 'Saint Vincent and the Grenadines',
                'Syrian Arab Republic': 'Syria',
                'Turkiye': 'Turkey',
                'Venezuela, RB': 'Venezuela',
                'Yemen, Rep.': 'Yemen'
                }

        df['Country'] = df['Country'].replace(names_to_change)

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
        file_name = 'DataSource/mod/' + data_source + '_' + data_measure + '_' + 'mod' + '.xlsx'
        with pd.ExcelWriter(file_name, engine='openpyxl') as writer:
            df.to_excel(writer, index=False, sheet_name='Sheet1')

        return df

    def group_by_language(self, data_source, data_measure):
        # Import the relevant mod file and dictionary
        if data_source == 'imf' and data_measure == 'ppp':
            df1 = self.imf_ppp_mod
        elif data_source == 'imf' and data_measure == 'nom':
            df1 = self.imf_nom_mod
        elif data_source == 'wb' and data_measure == 'ppp':
            df1 = self.wb_ppp_mod
        else: # data_source == 'wb and data_measure == 'nom'
            df1 = self.wb_nom_mod

        df2 = self.country_to_lang

        # Merge the Country to Language info with the mod info
        df = pd.merge(df1, df2, on='Country', how='outer')

        # This will result in many rows of NaN, so lets drop them.
        cleaned_df = df.dropna(subset=['Country'])

        # Now lets group the data by language.
        grouped_by_language = df.groupby('Language')
        sum_by_language = grouped_by_language.sum()
        sum_by_language.reset_index()

        # Drop the country column
        sum_by_language = sum_by_language.drop('Country', axis='columns')

        # Write the dataframe to the appropriate "full" file
        file_name = 'DataSource/full/' + data_source + '_' + data_measure + '_' + 'full' + '.xlsx'
        with pd.ExcelWriter(file_name, engine='openpyxl') as writer:
            sum_by_language.to_excel(writer, index=True, sheet_name='Sheet1')

        return sum_by_language

    def generate_annual_summary_stats(self, data_source, data_measure):
        # Grab the appropriate full data
        if data_source == 'imf' and data_measure == 'ppp':
            df = self.imf_ppp_full
        elif data_source == 'imf' and data_measure == 'nom':
            df = self.imf_nom_full
        elif data_source == 'wb' and data_measure == 'ppp':
            df = self.wb_ppp_full
        else: # data_source == 'wb' and data_measure == 'ppp'
            df = self.wb_nom_full

        # Locate the starting and ending point of the loop
        starting_year = df.columns[0]
        ending_year = df.columns[-3]

        # Loop through every year of data, creating annual reports, and save them in the gdp_dict.
        for i in range(starting_year, ending_year+1):
            if i in df.columns:
                # Grab the appropriate [year][data_source][data_measure] dataframe
                temp_df = df[i].copy()
                temp_df.columns = ['Language', '% of world GDP PPP']
                # Sort this slice's data according to % of world GDP
                sorted_df = temp_df.sort_values(ascending=False)
                # Cut down to top 20
                culled_df = sorted_df.iloc[:20]
                self.gdp_dict[i][data_source][data_measure] = culled_df

                file_name = 'DataSource/final/' + data_source + '_' + data_measure + '/' + str(i) + '.xlsx'
                with pd.ExcelWriter(file_name, engine='openpyxl') as writer:
                    culled_df.to_excel(writer, index=True, sheet_name='Sheet1')


