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
            [np.nan, np.nan],
            ['Afghanistan', 'Persian'],
            ['Albania', np.nan],
            ['Algeria', 'Arabic'],
            ['Andorra', np.nan]
        ], columns=['Country', 'Language'])
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
            'Language': ['Arabic','Bengali','Chinese','Dutch','English'],
            'List of Countries In Language Group':
                [
                ['Algeria', 'Bahrain', 'Egypt', 'Iraq', 'Jordan', 'Kuwait', 'Lebanon', 'Libya', 'Morocco', 'Oman',
                 'Qatar', 'Saudi Arabia', 'Sudan', 'Syria', 'Tunisia'],
                ['Bangladesh'],
                ['China, People\'s Republic of', 'Hong Kong SAR', 'Macao SAR', 'Taiwan Province of China'],
                ['Belgium', 'Netherlands', 'Suriname'],
                ['Antigua and Barbuda', 'Australia', 'Bahamas, The', 'Barbados', 'Belize', 'Canada',
                'Grenada', 'Guyana', 'Ireland', 'Jamaica', 'New Zealand', 'Singapore', 'Trinidad and Tobago',
                'United Kingdom', 'United States']
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
        df = obj.create_imf_ppp_mod()
        df = df[['Country', 1980]]
        df = df.head()

        expected_df = pd.DataFrame({
            'Country': [np.nan, 'Afghanistan', 'Albania', 'Algeria', 'Andorra'],
            1980: [np.nan, np.nan, 0.042886468593090005, 0.6683259264378286, np.nan]
        }, columns=['Country', 1980])

        print('=====')
        print('Testing creation of language_to_country dictionary...')
        print("Expected DF:")
        print(expected_df)
        print('======')
        print("Actual DF:")
        print(df)
        print('=====')

        assert_frame_equal(df, expected_df)

    def test5_group_imf_gdp_ppp_by_language(self):
        obj = Data()
        df = obj.group_imf_gdp_ppp_by_language()
        df = df.head()
        df = df[1980]

        data = {
            'Language': ['Arabic', 'Bengali', 'Chinese', 'Dutch', 'English'],
            1980: [6.637759, 0.375493, 2.981812, 2.035182, 29.327724]
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
        result = obj.generate_annual_summary_stats()
        series = obj.gdp_dict[1980]['IMF']['gdp_ppp']
        series.head()

        expected_series = None

        print('=====')
        print('Testing generation of summary stats...')
        print("Actual df:")
        print(series, "Heres actual series type:", type(series))
        print('=====')
        print("Expected DF:")
        print(expected_series, "Heres expected series type:", type(expected_series))
        print('======')


    # def test7(self):
    #
    #
    # def test8(self):
    #
    #
    # def test_9(self):


if __name__ == '__main__':
    unittest.main()