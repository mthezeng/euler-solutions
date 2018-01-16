def month_len(mon, year):
    m_len = 0
    thirty_one = [1,3,5,7,8,10,12]
    thirty = [4,6,9,11]
    if mon in thirty_one:
        m_len = 31
    elif mon in thirty:
        m_len = 30
    elif mon == 2:
        if year % 100 == 0:
            if year % 400 == 0:
                m_len = 29
            else:
                m_len = 28
        if year % 4 == 0:
            m_len = 29
        else:
            m_len = 28
    return m_len

def next_dow(cur_dow):
    # 1 is Monday, 2 is Tuesday, ..., 6 is Saturday, 7 is Sunday
    if cur_dow < 7:
        return cur_dow + 1
    else:
        return 1

def counting_sundays(d, m, y, dow):
    #number of Sundays that fell on the first of the month in the 20th century
    sundays = 0
    while True:
        current_month_len = month_len(m, y)
        while d < current_month_len:
            d += 1
            dow = next_dow(dow)
        if m == 12:
            if y == 2000:
                break
            m, d = 1, 1
            y += 1
            dow = next_dow(dow)
        else:
            m += 1
            d = 1
            dow = next_dow(dow)
        if dow == 7:
            sundays += 1
    return sundays

day = 1
month = 1
year = 1901
day_of_week = 2
print(counting_sundays(day, month, year, day_of_week))
