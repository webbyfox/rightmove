import csv
import statistics


class ParseCSV(object):

    def __init__(self, data):
        self.data = data

    def read_data(self):
        """
        Parsing CSV file
        :return: list of csv data
        """
        with open(self.data, 'r') as f:
            parsed_data = [row for row in csv.reader(f.read().splitlines())]
        return parsed_data

    def get_mean_value_for_postcode_outward(self, parsed_data, postcode_outward):
        """
        Return mean value of given postcode outward
        :param parsed_data: list
        :param postcode_outward: string
        :return: float
        """
        parsed_data.pop(0)
        prices = [float(x[1]) for x in parsed_data if x[7].lower().startswith(postcode_outward.lower())]
        return statistics.mean(prices)

    def average_between_house_vs_flat(self, parsed_data):
        """
        Return average value between house vs flat
        :param parsed_data: list
        :return: float
        """
        parsed_data.pop(0)
        flat_prices = [int(x[1]) for x in parsed_data if 'Flat' in x[8]]
        house_prices = [int(x[1]) for x in parsed_data if 'Flat' not in x[8]]
        return statistics.mean([float(x) - float(y) for x, y in zip(flat_prices, house_prices)])

    def top_ten_expensive_properties(self, parsed_data):
        """
        Return top ten percentage of expansive properties
        :param parsed_data: list
        :return: list
        """
        parsed_data.pop(0)
        sorted_data = list(reversed(sorted(parsed_data, key=lambda x: int(x[1]))))
        top_ten_percentage = sorted_data[:int(len(sorted_data)*.10)]
        return top_ten_percentage



if __name__ == '__main__':
   properties = ParseCSV('property-data.csv')
   properties_data = properties.read_data()
   print('-'*100)
   print("Mean value of properties: {0}".format(properties.get_mean_value_for_postcode_outward(properties_data, 'W1F')))
   print("Average diff value between house vs flat : {0}".format(properties.average_between_house_vs_flat(properties_data)))
   print("Top 10 % of expansive properties: {0}".format(properties.top_ten_expensive_properties(properties_data)))
   print('-'*100)
