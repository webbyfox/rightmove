import unittest
from main import ParseCSV


class CSVTest(unittest.TestCase):

    def setUp(self):
        """
        Setup for unit test
        """
        self.data = 'property-data.csv'
        self.propreties = ParseCSV(self.data)

    def test_csv_read_data_headers(self):
        """
        Test for CSV to have all required columns
        """
        self.assertEqual(
            self.propreties.read_data()[0],
            ['PROPERTY_REFERENCE', 'PRICE', 'BEDROOMS', 'BATHROOMS', 'HOUSE_NUMBER', 'ADDRESS', 'REGION', 'POSTCODE', 'PROPERTY_TYPE']
            )

    def test_csv_read_data_property_price(self):
        """
        Test for for column data
        """
        self.assertEqual(self.propreties.read_data()[1][1], '1000000')

    def test_csv_read_data_property_postcode(self):
        """
        Test for postcode column check
        """
        self.assertEqual(self.propreties.read_data()[1][7], 'W1F 3FT')

    def test_property_mean_value_for_postcode_outward(self):
        """
        Test for meanvalue check
        """
        mean_value = self.propreties.get_mean_value_for_postcode_outward(self.propreties.read_data(), 'W1F')
        self.assertEqual(mean_value, 1158750)

    def test_for_top_ten_most_expensive_properties(self):
        """
        Top ten percent of expansive property
        :return: 
        """
        properties = self.propreties.top_ten_expensive_properties(self.propreties.read_data())
        self.assertEqual(len(properties), 2)


    def test_for_average_diff_between_house_vs_flat(self):
        """
        Test for average price diff between house and flat
        :return:
        """
        avg_price = self.propreties.average_between_house_vs_flat(self.propreties.read_data())
        self.assertEqual(isinstance(avg_price, float), 1)
                          

if __name__ == '__main__':
    unittest.main()
