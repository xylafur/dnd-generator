#!/usr/bin/env python3

from util.shell_util import move_cursor 

def health_print(to_print, noncanonical=True, lineno=0):
    if noncanonical:
        move_cursor(0, lineno)
    print(to_print)
    return lineno + 1

class HealthTable:
    def __init__(self, n, noncanonical=False):
        assert(n>0)
        self.HT = {}
        self.total_max_hp = 0
        for i in range(n):
            name = input('Enter entity'+ str(i+1) +' name : ')
            hp = int(input('Enter entity max hp : '))
            chp = input('Enter current hp : ')
            chp = int(chp) if len(chp) else hp
            assert(chp and hp)

            self.HT[name] = [chp, hp]
            self.total_max_hp += hp
        print()

    def print_health_table(self):
        total_curr_hp = 0
        print('{:17s}{:13s}{:14s}{}'.format('NAME', '%HP', 'HP/MAX', 'STATUS'))
        for s in self.HT:
            p = self.HT[s]

            status = 'ALIVE'
            if p[0] <= 0:
                status = 'DEAD'
            elif p[0] <= p[1] // 2:
                status = 'BLOODIED'

            print(  ' {:12s} -> [{:6.2f} %hp] ({} / {}) , status : {}'.format(
                    s, (100 * p[0]/p[1]), p[0], p[1], status
                 ))
            total_curr_hp += p[0]

        status = 'ALIVE'
        if total_curr_hp <= 0:
            status = 'DEAD'
        elif total_curr_hp <= self.total_max_hp // 2:
            status = 'BLOODIED'
        print(' TOTAL        -> [{:6.2f} %hp] ({} / {}) , status : {}'.format(
                (100 * total_curr_hp/self.total_max_hp),
                total_curr_hp, self.total_max_hp, status))

def Main():
    ht = HealthTable(2)
    ht.print_health_table()

if __name__=='__main__':
    Main()

