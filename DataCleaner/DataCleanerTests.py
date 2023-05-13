import unittest
from DataCleaner import *
import pandas as pd
import numpy as np
from pandas.testing import assert_frame_equal, assert_series_equal
import xlwt

class TestProgram(unittest.TestCase):

    def test1_import_country_to_lang_dict(self):
        """Tests importing the Country-To-Lang dictionary"""
        obj = Data()
        df = obj.import_country_to_lang()
        df = df.head()
        expected_df = pd.DataFrame([
            ['Afghanistan', 'Afghanistan','Afghanistan', 'AFG', 'Persian'],
            ['Albania', 'Albania', 'Albania', 'ALB', np.nan],
            ['Algeria', 'Algeria', np.nan, np.nan, 'Arabic'],
            ['Andorra', 'Andorra', 'Andorra', 'AND', np.nan],
            ['Angola', 'Angola', 'Angola', 'AGO', 'Portuguese']
        ], columns=['PowerBI Name', 'IMF Name', 'WB Name', 'WB Code', 'Language'])
        print('=====')
        print('Testing import of country-to-lang dictionary...')
        print("Expected DF:")
        print(expected_df)
        print('======')
        print("Actual DF:")
        print(df)
        print('=====')

        assert_frame_equal(df, expected_df)

    def test2_create_lang_to_country(self):
        obj = Data()
        df = obj.create_lang_to_country()
        df = df.head()

        expected_df = pd.DataFrame({
            'Language': ['Arabic','Bengali','Chinese','Danish','Dutch'],
            'List of Countries In Language Group':
                [
                ['Algeria', 'Bahrain', 'Egypt', 'Iraq', 'Jordan', 'Kuwait', 'Lebanon', 'Libya', 'Morocco', 'Oman',
                 'Qatar', 'Saudi Arabia', 'Sudan', 'Syria', 'Tunisia', 'United Arab Emirates'],
                ['Bangladesh'],
                ['China', 'Hong Kong', 'Macao', 'Taiwan'],
                ['Denmark'],
                ['Belgium', 'Netherlands', 'Suriname']
                ]
        }, columns=['Language', 'List of Countries In Language Group'])

        print('=====')
        print('Testing creation of language_to_country dictionary...')
        print("Expected DF:")
        print(expected_df)
        print('======')
        print("Actual DF:")
        print(df)
        print('=====')

        assert_frame_equal(df, expected_df)

    # Commenting out this test because the xlsx file includes the quotes in array elements, but my test data didn't.
    # I can come back to it later, maybe try with " / ' later.
    #def test3_export_lang_to_country_to_xls(self):
        # obj = Data()
        # obj.export_lang_to_country_to_xls()
        #
        # df = pd.read_excel('DataSource/Lang_To_Country.xlsx', index_col=0)
        # df = df.head()
        #
        # expected_df = pd.DataFrame({
        #     'Language': ['Arabic', 'Bengali', 'Chinese', 'Dutch', 'English'],
        #     'List of Countries In Language Group':
        #         [
        #             ['Algeria', 'Bahrain', 'Egypt', 'Iraq', 'Jordan', 'Kuwait', 'Lebanon', 'Libya', 'Morocco', 'Oman',
        #              'Qatar', 'Saudi Arabia', 'Sudan', 'Syria', 'Tunisia'],
        #             ['Bangladesh'],
        #             ['China, People\'s Republic of', 'Hong Kong SAR', 'Macao SAR', 'Taiwan Province of China'],
        #             ['Belgium', 'Netherlands', 'Suriname'],
        #             ['Antigua and Barbuda', 'Australia', 'Bahamas, The', 'Barbados', 'Belize', 'Canada',
        #              'Grenada', 'Guyana', 'Ireland', 'Jamaica', 'New Zealand', 'Singapore', 'Trinidad and Tobago',
        #              'United Kingdom', 'United States']
        #         ]
        # }, columns=['Language', 'List of Countries In Language Group'])
        #
        # print('=====')
        # print('Testing export of lang_to_country...')
        # print("Expected DF:")
        # print(expected_df)
        # print('======')
        # print("Actual DF:")
        # print(df)
        # print('=====')
        #
        # assert_frame_equal(df, expected_df)


    def test4_import_imf_ppp(self):
        obj = Data()
        df = obj.create_mod('imf', 'ppp')
        df = df[['Country', 1980]]
        df = df.head()

        expected_df = pd.DataFrame({
            'Country': [np.nan, 'Afghanistan', 'Albania', 'Algeria', 'Andorra'],
            1980: [np.nan, np.nan, 0.042886468593090005, 0.6683259264378286, np.nan]
        }, columns=['Country', 1980])

        print('=====')
        print('Testing creation of imf ppp mod file...')
        print("Expected DF:")
        print(expected_df)
        print('======')
        print("Actual DF:")
        print(df)
        print('=====')

        assert_frame_equal(df, expected_df)

    def test5_group_imf_gdp_ppp_by_language(self):
        obj = Data()
        df = obj.group_by_language('imf', 'ppp')
        df = df.head()
        df = df[1980]

        data = {
            'Language': ['Arabic', 'Bengali', 'Chinese', 'Danish', 'Dutch'],
            1980: [7.307723, 0.375493, 2.981812, 0.452762, 2.035182]
        }
        expected_df = pd.DataFrame(data)
        expected_df.set_index('Language', inplace=True)
        expected_df = expected_df.squeeze()

        print('=====')
        print('Testing grouping of language data int...')
        print("Expected DF:")
        print(expected_df, "Heres expected series type:", type(expected_df))
        print('======')
        print("Actual df:")
        print(df, "Heres actual series type:", type(df))
        print('=====')

        assert_series_equal(df, expected_df)

    def test6_generate_annual_summary_stats(self):
        obj = Data()
        result = obj.generate_annual_summary_stats('imf', 'ppp')
        series = obj.gdp_dict[1980]['imf']['ppp']
        series = series.head()
        df = series.to_frame()
        df = df.reset_index()

        data = {
            'Language': ['English', 'Spanish', 'Japanese', 'German', 'Arabic'],
            1980: [29.327724, 9.798936, 7.953924, 7.849050, 7.307723]
        }
        expected_df = pd.DataFrame(data)


        print('=====')
        print('Testing generation of summary stats...')
        print("Actual df:")
        print(df, "Heres actual df type:", type(df))
        print('=====')
        print("Expected DF:")
        print(expected_df, "Heres expected df type:", type(expected_df))
        print('======')

        assert_frame_equal(df, expected_df)


    def test7_wb_ppp_create_mod(self):
        obj = Data()
        df = obj.create_mod('wb', 'ppp')
        df = df[['Country', '2020']]
        df = df.head()
        df = df.reset_index(drop=True)
        df.columns = ['Country', '2020']

        expected_df = pd.DataFrame({
            'Country': ['Aruba', 'Afghanistan', 'Angola', 'Albania', 'Andorra'],
            '2020': [0.0027790922850847435, 0.06032679578746639, 0.15858149066833638, 0.02969400031277929, np.nan]
            }, columns=['Country', '2020'])

        print('=====')
        print('Testing creation of World Bank PPP mod...')
        print("Expected DF:")
        print(expected_df)
        print('======')
        print("Actual DF:")
        print(df)
        print('=====')

        assert_frame_equal(df, expected_df)

    def test8_wb_nom_create_mod(self):
        obj = Data()
        df = obj.create_mod('wb', 'nom')
        df = df[['Country', '2020']]
        df = df.head()
        df = df.reset_index(drop=True)
        df.columns = ['Country', '2020']

        expected_df = pd.DataFrame({
            'Country': ['Aruba', 'Afghanistan', 'Angola', 'Albania', 'Andorra'],
            '2020': [0.0030664371130266163, 0.023665776669792787, 0.06299504371216032, 0.017777863637857775, 0.0033965539229652317]
            }, columns=['Country', '2020'])

        print('=====')
        print('Testing creation of World Bank Nom mod...')
        print("Expected DF:")
        print(expected_df)
        print('======')
        print("Actual DF:")
        print(df)
        print('=====')

        assert_frame_equal(df, expected_df)

    def test_9_group_by_lang_wb_ppp(self):
        obj = Data()
        df = obj.group_by_language('wb', 'ppp')
        df = df.head()
        df = df[2000]

        data = {
            'Language': ['Arabic', 'Bengali', 'Chinese', 'Danish', 'Dutch'],
            2000: [5.635107789618117, 0.41349639715083003, 7.90116159609634, 0.311137777211474, 1.618435033271701]
            }
        expected_df = pd.DataFrame(data)
        expected_df.set_index('Language', inplace=True)
        expected_df = expected_df.squeeze()

        print('=====')
        print('Testing grouping of language data int...')
        print("Expected DF:")
        print(expected_df, "Heres expected series type:", type(expected_df))
        print('======')
        print("Actual df:")
        print(df, "Heres actual series type:", type(df))
        print('=====')

        assert_series_equal(df, expected_df)

    def test10_generate_annual_summary_stats_wb_ppp(self):
        obj = Data()
        result = obj.generate_annual_summary_stats('wb', 'ppp')
        series = obj.gdp_dict[2000]['wb']['ppp']
        series = series.head()
        df = series.to_frame()
        df = df.reset_index()

        data = {
            'Language': ['English', 'Chinese', 'Spanish', 'Japanese', 'Arabic'],
            2000: [27.74113666619502, 7.90116159609634, 7.549588191980197, 7.036586638441318, 5.635107789618117]
            }
        expected_df = pd.DataFrame(data)

        print('=====')
        print('Testing generation of summary stats...')
        print("Actual df:")
        print(df, "Heres actual df type:", type(df))
        print('=====')
        print("Expected DF:")
        print(expected_df, "Heres expected df type:", type(expected_df))
        print('======')

        assert_frame_equal(df, expected_df)

if __name__ == '__main__':
    unittest.main()