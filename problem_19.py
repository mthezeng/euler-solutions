def month_len(mon, year):
    m_len = 0
    if mon == 1 or mon == 3 or mon == 5 or mon == 7 or mon == 8 or mon == 10 or mon == 12:
        m_len = 31
    elif mon == 4 or mon == 6 or mon == 9 or mon == 11:
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
    if cur_dow == 'Monday': return 'Tuesday'
    elif cur_dow == 'Tuesday': return 'Wednesday'
    elif cur_dow == 'Wednesday': return 'Thursday'
    elif cur_dow == 'Thursday': return 'Friday'
    elif cur_dow == 'Friday': return 'Saturday'
    elif cur_dow == 'Saturday': return 'Sunday'
    elif cur_dow == 'Sunday': return 'Monday'

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
        if dow == 'Sunday':
            sundays += 1
    return sundays

day = 1
month = 1
year = 1901
day_of_week = 'Tuesday'
print(counting_sundays(day, month, year, day_of_week))
