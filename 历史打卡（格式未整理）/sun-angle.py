def sun_angle(time):
    s0 = 6 * 3600
    h, m = time.split(":")
    s1 = int(h) * 3600 + int(m) * 60
    s_e = 64800
    return "I don't see the sun!" if s1 < s0 or s1 > s_e else (s1 - s0) / (s_e - s0) * 180.0

if __name__ == '__main__':
    print("Example:")
    print(sun_angle("07:00"))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert sun_angle("07:00") == 15
    assert sun_angle("01:23") == "I don't see the sun!"
    print("Coding complete? Click 'Check' to earn cool rewards!")

