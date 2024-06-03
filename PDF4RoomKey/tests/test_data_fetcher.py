import unittest
from unittest.mock import patch, Mock
from PDF4RoomKey import DataFetcher

class TestDataFetcher(unittest.TestCase):
    def setUp(self):
        self.generator = DataFetcher(api_url='http://example.com/api', api_key='your_api_key')

    @patch('requests.get')
    def test_fetch_data(self, mock_get):
        mock_response = Mock()
        expected_data = [{'key': 'value'}]
        mock_response.json.return_value = expected_data
        mock_response.status_code = 200
        mock_get.return_value = mock_response

        data = self.generator.fetch_data('2022-01-01')
        self.assertEqual(data, expected_data)

    @patch('builtins.open', new_callable=unittest.mock.mock_open)
    @patch('csv.writer')
    def test_write_to_csv(self, mock_csv_writer, mock_open):
        data = [{'key': 'value'}]
        self.generator.write_to_csv(data, 'test.csv')
        mock_open.assert_called_once_with('test.csv', 'w', newline='')
        mock_csv_writer().writerow.assert_called()

    @patch('builtins.open', new_callable=unittest.mock.mock_open)
    @patch('json.dump')
    def test_write_to_json(self, mock_json_dump, mock_open):
        data = [{'key': 'value'}]
        self.generator.write_to_json(data, 'test.json')
        mock_open.assert_called_once_with('test.json', 'w')
        mock_json_dump.assert_called_once_with(data, mock_open(), indent=4)

    @patch('PDF4RoomKey.DataFetcher.fetch_data')
    @patch('PDF4RoomKey.DataFetcher.write_to_csv')
    @patch('PDF4RoomKey.DataFetcher.write_to_json')
    def test_generate(self, mock_write_to_json, mock_write_to_csv, mock_fetch_data):
        mock_fetch_data.return_value = [{'key': 'value'}]
        self.generator.generate('2022-01-01', 'test.csv', 'csv')
        mock_write_to_csv.assert_called_once()
        self.generator.generate('2022-01-01', 'test.json', 'json')
        mock_write_to_json.assert_called_once()
        
    def test_check_name_length(self):
        case1 = ''
        case2 = 'wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww'
        case3 = 'Stauss, Maximilian'
        
        # error cases
        self.assertRaises(ValueError,self.generator.check_name_length,case1)
        self.assertRaises(ValueError,self.generator.check_name_length,case2)
        
        # success cases
        self.assertEqual(self.generator.check_name_length(case3),True)

    def test_check_dates(self):
        case1 = {'arrival':'','departure':''}
        case2 = {'arrival':'','departure':'2024-01-09'}
        case3 = {'arrival':'2024-01-10','departure':''}
        case4 = {'arrival':'2024-01-10','departure':'2024-01-09'}
        case5 = {'arrival':'2024-01-09','departure':'2024-01-10'}

        # error cases
        self.assertRaises(ValueError,self.generator.check_dates,case1['arrival'],case1['departure'])
        self.assertRaises(ValueError,self.generator.check_dates,case2['arrival'],case2['departure'])
        self.assertRaises(ValueError,self.generator.check_dates,case3['arrival'],case3['departure'])
        self.assertRaises(ValueError,self.generator.check_dates,case4['arrival'],case4['departure'])

        # success cases
        self.assertEqual(self.generator.check_dates(case5['arrival'],case5['departure']),True)

if __name__ == '__main__':
    unittest.main()