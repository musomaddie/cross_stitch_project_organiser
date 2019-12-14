import sqlite3


MY_DATABASE = "db/Cross_Stitch_Supplies.db"


def _dmc_compare(v1, v2):
    """ Compares the two dmc numbers, returns true if the first is smaller
    then the second. TESTED!
    """
    if v1 == "5200":
        return True
    elif v2 == "5200":
        return False
    if v1 == v2:
        return True

    try:
        n1, n2 = int(v1), int(v2)
        return n1 < n2

    except ValueError:
        if v1 == "BLANC":
            return True
        elif v2 == "BLANC":
            return False
        elif v1 == "ECRU":
            return True
        else:
            return False


def _dmc_sort(threads):
    # INPUT: list of tuples, 0 index in tuple is dmc name
    # Merge sort implementation using special sorting rules
    if len(threads) == 0:
        return []

    if len(threads) == 1:
        return threads
    elif len(threads) == 2:
        if _dmc_compare(threads[0][0], threads[1][0]):
            return [threads[0], threads[1]]
        return [threads[1], threads[0]]

    middle = int(len(threads) / 2)
    left_list = _dmc_sort(threads[:middle])
    right_list = _dmc_sort(threads[middle:])
    left_index = 0
    right_index = 0
    sorted_list = []

    while True:
        if left_index == len(left_list):
            while right_index < len(right_list):
                sorted_list.append(right_list[right_index])
                right_index += 1
            return sorted_list
        elif right_index == len(right_list):
            while left_index < len(left_list):
                sorted_list.append(left_list[left_index])
                left_index += 1
            return sorted_list

        if _dmc_compare(left_list[left_index][0], right_list[right_index][0]):
            sorted_list.append(left_list[left_index])
            left_index += 1
        else:
            sorted_list.append(right_list[right_index])
            right_index += 1


def _read_all_threads_db():
    conn = sqlite3.connect(MY_DATABASE)
    cur = conn.cursor()
    try:
        cur.execute(""" SELECT * FROM threads """)
        result = cur.fetchall()
        cur.close()
        conn.close()
        return result
    except Exception:
        cur.close()
        conn.close()
        return []


def _check_number(n):
    try:
        float(n)
        return True
    except ValueError:
        return False


def add_new_thread(thread_name, amount_have, update=False):
    # TODO: add documentation
    conn = sqlite3.connect(MY_DATABASE)
    cur = conn.cursor()
    if not _check_number(amount_have):
        return False
    try:
        if update:
            cur.execute(""" UPDATE threads
                            SET amount_have=?
                            WHERE colour==?;""",
                        (amount_have, thread_name))
        else:
            cur.execute(""" INSERT INTO threads
                            VALUES (?, ?);""", (thread_name, amount_have))
    except Exception:
        return False
    conn.commit()
    cur.close()
    conn.close()
    return True


def get_all_threads():
    """ For use inside the view table. Displays all threads.

        Returns list<dict<??>>
    """
    all_threads = []
    threads = _read_all_threads_db()

    # Put them in sorted order before adding to list
    threads_sorted = _dmc_sort(threads)
    for thread in threads_sorted:
        all_threads.append({"dmc": thread[0],
                            "amount have": thread[1]})
    return all_threads




if __name__ == "__main__":
    import doctest
    doctest.testmod()
