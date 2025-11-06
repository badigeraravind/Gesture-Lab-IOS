import random
import time

def test_drag_drop(driver):
    driver.find_element('accessibility id','nav_Drag_and_Drop').click()

    for _ in range(1,4):
        nail = driver.find_element('accessibility id','wooden_nail').rect
        nailx = int(nail['x'] + nail['width'] / 2)
        naily = int(nail['y'] + nail['height'] / 2)

        endx = random.randint(30,350)
        endy = random.randint(150, 750)

        driver.execute_script('mobile: dragFromToForDuration',{'fromX':nailx , 'fromY':naily, 'toX': endx, 'toY':endy, 'duration': 5.0})       # drag for 5 seconds.
        print(f'Drag#{_} Dragged the wooden nail from ({nailx}, {naily}) to ({endx}, {endy})')

        time.sleep(3)
        driver.find_element('accessibility id','Home').click()

        # if an object/element to be dragged from one element to other element
        # driver.execute_script('mobile: dragFromToForDuration',{'fromElement':a.id, 'toElement':z.id, 'duration':7.5})



