import unittest
from main import ParseCSV


class CSVTest(unittest.TestCase):

    def setUp(self):
        self.data = 'property-data.csv'
        self.parsed_data = [
            ['PROPERTY_REFERENCE','PRICE','BEDROOMS','BATHROOMS','HOUSE_NUMBER','ADDRESS','REGION','POSTCODE','PROPERTY_TYPE'],
            ['1','1000000','7','2','12','Richard Lane','London','W1F 3FT','Mansion'],
            ['24','755000','5','5','122','Jeff Street','Surrey','GU13 9OB','Mansion'],
        ]
        self.propreties = ParseCSV(self.data)

    def test_csv_read_data_headers(self):
        self.assertEqual(
            self.propreties.read_data()[0],
            ['PROPERTY_REFERENCE','PRICE','BEDROOMS','BATHROOMS','HOUSE_NUMBER','ADDRESS','REGION','POSTCODE','PROPERTY_TYPE']
            )

    def test_csv_read_data_property_price(self):
        self.assertEqual(self.propreties.read_data()[1][1], '1000000')

    def test_csv_read_data_property_postcode(self):
        self.assertEqual(self.propreties.read_data()[1][7], 'W1F 3FT')

    def test_property_mean_value_for_postcode_outward(self):
        mean_value = self.propreties.get_mean_value_for_postcode_outward(self.propreties.read_data(), 'W1F')
        self.assertEqual(mean_value,2323)

    # def test_get_min_score_difference(self):
    #     self.assertEqual(self.football.get_min_score_difference(self.parsed_data), 1)

    # def test_get_team(self):
    #     index_value = self.football.get_min_score_difference(self.parsed_data)
    #     self.assertEqual(self.football.get_team(index_value, self.parsed_data), 'Liverpool')


if __name__ == '__main__':
    unittest.main()