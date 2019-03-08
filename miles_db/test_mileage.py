
import mileage
from mileage import MileageError
import sqlite3
from unittest import TestCase

class TestMileageDB(TestCase):

    test_db_url = 'test_miles.db'

    """
    Before running this test, create test_miles.db
    Create expected miles table
    create table miles (vehicle text, total_miles float);
    """

    # The name of this method is important - the test runner will look for it
    def setUp(self):
        # Overwrite the mileage
        mileage.db_url = self.test_db_url
        # drop everything from the DB to always start with an empty database
        conn = sqlite3.connect(self.test_db_url)
        conn.execute('DELETE FROM miles')
        conn.commit()
        conn.close()


    def test_add_new_vehicle(self):
        mileage.add_miles('Blue Car', 100)
        expected = { 'BLUE CAR': 100 }
        self.compare_db_to_expected(expected)

        mileage.add_miles('Green Car', 50)
        expected['GREEN CAR'] = 50
        self.compare_db_to_expected(expected)


    def test_increase_miles_for_vehicle(self):
        mileage.add_miles('Red Car', 100)
        expected = { 'RED CAR': 100 }
        self.compare_db_to_expected(expected)

        mileage.add_miles('Red Car', 50)
        expected['RED CAR'] = 100 + 50
        self.compare_db_to_expected(expected)


    def test_add_new_vehicle_no_vehicle(self):
        with self.assertRaises(Exception):
            mileage.addMiles(None, 100)


    def test_add_new_vehicle_invalid_new_miles(self):
        with self.assertRaises(MileageError):
            mileage.add_miles('Car', -100)
        with self.assertRaises(MileageError):
            mileage.add_miles('Car', 'abc')
        with self.assertRaises(MileageError):
            mileage.add_miles('Car', '12.def')


    # This is not a test method, instead, it's used by the test methods
    def compare_db_to_expected(self, expected):

        conn = sqlite3.connect(self.test_db_url)
        cursor = conn.cursor()
        all_data = cursor.execute('SELECT * FROM MILES').fetchall()

        # Same rows in DB as entries in expected dictionary
        self.assertEqual(len(expected.keys()), len(all_data))

        for row in all_data:
            # Vehicle exists, and mileage is correct
            self.assertIn(row[0], expected.keys())
            self.assertEqual(expected[row[0]], row[1])

        conn.close()

    def test_vehicle_upper(self):
        mileage.add_miles('yes', 34)
        expected = {'YES': 34}
        self.compare_db_to_expected(expected)


class TestSearchVehicle(TestCase):

    test_db_url = 'test_miles.db'

    """
    Before running this test, create test_miles.db
    Create expected miles table
    create table miles (vehicle text, total_miles float);
    """

    # The name of this method is important - the test runner will look for it
    def setUp(self):
        # Overwrite the mileage
        mileage.db_url = self.test_db_url
        # drop everything from the DB to always start with an empty database
        conn = sqlite3.connect(self.test_db_url)
        conn.execute('DELETE FROM miles')
        conn.execute('INSERT INTO miles values ("ORANGE CAR", 45)')
        conn.execute('INSERT INTO miles values ("BAD TRUCK", 49)')
        conn.commit()
        conn.close()


    def test_search_vehicle_found(self):
        conn = sqlite3.connect(self.test_db_url)
        conn.execute('INSERT INTO miles values ("COOL VAN", 73)')
        conn.commit()
        van_mileage = mileage.search_vehicle('Cool Van')
        self.assertEqual(73, van_mileage)
        conn.close()

    def test_search_vehicle_not_found(self):
        conn = sqlite3.connect(self.test_db_url)
        van_mileage = mileage.search_vehicle('bop')
        self.assertEqual(None, van_mileage)
        conn.close()
