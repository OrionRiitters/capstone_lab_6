import sqlite3

db_url = 'mileage.db'   # Assumes the table miles have already been created.

"""
    Before running this test, create test_miles.db
    Create expected miles table
    create table miles (vehicle text, total_miles float);
"""

class MileageError(Exception):
    pass

def add_miles(vehicle, new_miles):
    '''If the vehicle is in the database, increment the number of miles by new_miles
    If the vehicle is not in the database, add the vehicle and set the number of miles to new_miles

    If the vehicle is None or new_miles is not a positive number, raise MileageError
    '''

    if not vehicle:
        raise MileageError('Provide a vehicle name')
    if not isinstance(new_miles, (int, float))  or new_miles < 0:
        raise MileageError('Provide a positive number for new miles')

    conn = sqlite3.connect(db_url)
    cursor = conn.cursor()
    rows_mod = cursor.execute('UPDATE MILES SET total_miles = total_miles + ? WHERE vehicle = ?', (new_miles, vehicle))
    if rows_mod.rowcount == 0:
        cursor.execute('INSERT INTO MILES VALUES (?, ?)', (vehicle, new_miles))
    conn.commit()
    conn.close()


def main():
    while True:
        vehicle = input('Enter vehicle name or enter to quit:')
        if not vehicle:
            break
        miles = float(input('Enter new miles for %s: ' % vehicle)) ## TODO input validation

        add_miles(vehicle, miles)


if __name__ == '__main__':
    main()
