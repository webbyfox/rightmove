# CSV parser

Written code with Python3.6

### Unit test
Run unit test via
```
>>>python test.py -v
test_csv_read_data_property_postcode (__main__.CSVTest) ... ok
test_csv_read_data_property_price (__main__.CSVTest) ... ok
test_for_average_diff_between_house_vs_flat (__main__.CSVTest) ... ok
test_for_top_ten_most_expensive_properties (__main__.CSVTest) ... ok
test_property_mean_value_for_postcode_outward (__main__.CSVTest) ... ok

----------------------------------------------------------------------
Ran 6 tests in 0.025s

```

### Running Code  
```
>>>python main.py
----------------------------------------------------------------------------------------------------
Mean value of properties: 1158750.0
Average diff value between house vs flat : 39687.25
Top 10 % of expansive properties: [['12', '7500000', '11', '4', '', 'Brighton Road ', 'Surrey', 'GU13 4DD', 'Mansion'], ['13', '2500000', '7', '2', '1', 'Station Road', 'London', 'W1F 3UT', 'Mansion']]
----------------------------------------------------------------------------------------------------
```
