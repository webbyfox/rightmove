import csv


class ParseCSV(object):

    def __init__(self, data):
        self.data = data

    def read_data(self):
        with open(self.data, 'r') as f:
            parsed_data = [row for row in csv.reader(f.read().splitlines())]
        return parsed_data

    
    def get_mean_value_for_postcode_outward(self, parsed_data, postcode_outward):
        parsed_data.pop(0)
        prices = [x[1] for x in parsed_data if x[7].startswith(postcode_outward)]
        return prices


    def sort_property_by_proce(self, parsed_data):
        parsed_data.pop(0)
        properties = parsed_data.sort(lambda x: x[1])
        return properties        
