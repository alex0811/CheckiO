class Warrior:
    hp = 50
    at = 5
    is_alive = True

class Knight(Warrior):
    at = 7
    pass

def fight(unit_1: Warrior, unit_2: Warrior):
    while unit_1.hp > 0:
        unit_2.hp = unit_2.hp - unit_1.at
        unit_2.is_alive = unit_2.hp > 0
        if unit_2.is_alive == False:
            return True
        unit_1.hp = unit_1.hp - unit_2.at
        unit_1.is_alive = unit_1.hp > 0
    # 1 能坚持几个回合
    # u1_round = unit_1.hp // unit_2.at
    # u2_round = unit_2.hp // unit_1.at
    # u1_round = u1_round - 1

    # u1_remainder_hp = unit_1.hp - u1_round * unit_2.at
    # u2_remainder_hp = unit_2.hp - u2_round * unit_1.at
    
    # print('双方坚持回合数：', u1_round, u2_round)
    # print('剩余生命值', u1_remainder_hp, u2_remainder_hp)
    # # u2_round = u2_round - 1 # 由于是后手，所以生存回合少一个
    # unit_1.hp = u1_remainder_hp
    # unit_2.hp = u2_remainder_hp
    # unit_1.is_alive = unit_1.hp > 0
    # unit_2.is_alive = unit_2.hp > 0

    # if u1_round == u2_round:
    #     return True
    # if u2_round > u1_round:
    #     return False
    return False

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing

    chuck = Warrior()
    bruce = Warrior()
    carl = Knight()
    dave = Warrior()
    mark = Warrior()

    assert fight(chuck, bruce) == True
    assert fight(dave, carl) == False
    assert chuck.is_alive == True
    assert bruce.is_alive == False
    assert carl.is_alive == True
    assert dave.is_alive == False
    assert fight(carl, mark) == False
    assert carl.is_alive == False

    print("Coding complete? Let's try tests!")
