import time

def date_time(t: str) -> str:
    t_time = time.strptime(t, "%d.%m.%Y %H:%M")
    return f"{t_time.tm_mday} {time.strftime('%B', t_time)} {t_time.tm_year} year {t_time.tm_hour} " + ("hour" if t_time.tm_hour == 1 else "hours") + f" {t_time.tm_min} " + ("minute" if t_time.tm_min == 1 else "minutes")

if __name__ == '__main__':
    print("Example:")
    print(date_time('01.01.2000 00:00'))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert date_time("01.01.2000 00:00") == "1 January 2000 year 0 hours 0 minutes", "Millenium"
    assert date_time("09.05.1945 06:30") == "9 May 1945 year 6 hours 30 minutes", "Victory"
    assert date_time("20.11.1990 03:55") == "20 November 1990 year 3 hours 55 minutes", "Somebody was born"
    # print("Coding complete? Click 'Check' to earn cool rewards!")
