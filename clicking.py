import json
import mouse as m
import keyboard as k
import os
import time
import random
import math
from pyautogui import sleep
import bunghoe
import iodmiokf as iod

tax_rate = 0.01125
x_off = 5760
y_off = 1620

def buy_order(tag, quantity):
    order_coords = [[1544, 643], [1601, 647], [1430, 801], [1394, 645], [1447, 644]]
    os.chdir(r'C:\Users\TGSG\Desktop\mcbot')
    f = open('clicks.json',)
    clickmap = json.load(f)
    f.close()
    for item in clickmap[tag]:
        m.move(0, 0, absolute=True, duration=0)
        print(item)
        m.move(item[0]+x_off, item[1]+y_off, absolute=True, duration=0)
        time.sleep(random.random()*0.5+0.5)
        print(bunghoe.getpos())
        m.click(button='left')
        time.sleep(random.random()*0.5+0.5)
    index = 0
    for item in order_coords:
        m.move(item[0]+x_off, item[1]+y_off, absolute=True, duration=0)
        if index == 2:
            for char in str(quantity):
                k.send(char)
        time.sleep(random.random()*0.5+0.5)
        m.click(button='left')
        index += 1
        time.sleep(random.random()*0.5+0.5)
    
def flip_order(mprice):
    order_coords = [[1496, 791], [1277, 701], [1544,641], [1431, 801]]
    index = 0
    for item in order_coords:
        m.move(item[0]+x_off, item[1]+y_off, absolute=True, duration =0)
        time.sleep(random.random()*0.5+0.5)
        if index == 3:
            print(mprice)
            for char in str(mprice):
                k.send(char)
            time.sleep(0.5)
        if index != 1:
            m.click(button='left')
        if index == 1:
            m.click(button='right')
        index += 1
        time.sleep(random.random()*0.5+0.5)

def collect():
    order_coords = [[1487, 780], [1288, 634]]
    for item in order_coords:
        m.move(item[0]+x_off, item[1]+y_off, absolute=True, duration=0)
        time.sleep(random.random()*0.5+0.5)




def main():
    money = int(input('$: '))
    orders = []
    m.move(100+x_off, 100+y_off, absolute=True, duration=0)
    m.click(button='left')
    k.send('esc')
    while True:
        action = iod.get_action(orders)
        print(action)
        if action == 'buy':
            m.click(button='right')
            suggestions = iod.suggestions()
            for item in suggestions:
                if item['BuyIn'] <= money:
                    quantity = math.floor(money / item['BuyIn'] + 0.1)
                    tag = item['item']
                    orders.append([tag, quantity, item['BuyIn']+0.1, action])
                    buy_order(tag, quantity)
                    money -= orders[0][1]*orders[0][2]
                    jordel = True
                    while jordel:
                        suggestions = iod.suggestions()
                        for item in suggestions:
                            if item['item'] == tag:
                                print(item['BuyIn'],orders[0][2])
                                if item['BuyIn'] >= orders[0][2]:
                                    print('api updated lole')
                                    jordel = False
                                break
                        time.sleep(2)
                    break
        if action == 'flip':
            time.sleep(2)
            m.click(button='right')
            suggestions = iod.suggestions()
            for item in suggestions:
                if item['item'] == orders[0][0]:
                    sell_price = item['SellIn'] - 0.1
                    flip_order(sell_price)
                    orders[0][2] = sell_price
                    orders[0][3] = action
                    k.send('esc')
                    jordel = True
                    while jordel:
                        suggestions = iod.suggestions()
                        for item in suggestions:
                            if item['item'] == tag:
                                print(item['SellIn'],orders[0][2])
                                if item['SellIn'] <= orders[0][2]:
                                    print('api updated lole')
                                    jordel = False
                                break
                        time.sleep(2)
                    break
        if action == 'collect':
            m.click(button='right')
            collect()
            money += orders[0][1]*orders[0][2]*(1-tax_rate)
            orders.pop(0)
            k.send('esc')
            print(money)
        time.sleep(5)

if __name__ == '__main__':
    main()