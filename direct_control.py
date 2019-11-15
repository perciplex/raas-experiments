import curses
import time
import numpy as np

import gym
import gym_raas
'''
'''

class curses_env:

    def __init__(self):

        self.env = gym.make('raaspendulum-v0')
        self.env.reset()


    def DCloop(self, stdscr):
        #https://docs.python.org/3/howto/curses.html
        #https://docs.python.org/3/library/curses.html#curses.window.clrtobot
        print('Size of curses window: LINES={}, COLS={}'.format(curses.LINES, curses.COLS), 1)
        delay_time = 0.05

        torque = 0.0
        torque_incr = 0.1

        last_action_str_pos = [0, 10]
        torque_str_pos = [0, 6]

        x_str_pos = [0, 2]
        y_str_pos = [0, 3]
        thetadot_str_pos = [0, 4]

        self.drawStandard(stdscr)

        while True:
            c = stdscr.getch()

            if c == curses.KEY_LEFT:
                torque += torque_incr
                obs, reward, done, info = self.env.step([torque])
                x, y, thetadot = obs

                time.sleep(delay_time)
                self.drawStandard(stdscr)

                stdscr.addstr(x_str_pos[1], x_str_pos[0], 'x = {:.2f}'.format(x))
                stdscr.addstr(y_str_pos[1], y_str_pos[0], 'y = {:.2f}'.format(y))
                stdscr.addstr(thetadot_str_pos[1], thetadot_str_pos[0], 'thetadot = {:.2f}'.format(thetadot))

                stdscr.addstr(torque_str_pos[1], torque_str_pos[0], 'Current torque = {:.2f}'.format(torque))

                stdscr.addstr(last_action_str_pos[1], last_action_str_pos[0], 'Pressed Left key, incrementing torque')
                self.moveCursorRefresh(stdscr)


            if c == curses.KEY_RIGHT:
                torque -= torque_incr
                obs, reward, done, info = self.env.step([torque])
                x, y, thetadot = obs

                time.sleep(delay_time)
                self.drawStandard(stdscr)

                stdscr.addstr(x_str_pos[1], x_str_pos[0], 'x = {:.2f}'.format(x))
                stdscr.addstr(y_str_pos[1], y_str_pos[0], 'y = {:.2f}'.format(y))
                stdscr.addstr(thetadot_str_pos[1], thetadot_str_pos[0], 'thetadot = {:.2f}'.format(thetadot))

                stdscr.addstr(torque_str_pos[1], torque_str_pos[0], 'Current torque = {:.2f}'.format(torque))

                stdscr.addstr(last_action_str_pos[1], last_action_str_pos[0], 'Pressed Right key, decrementing torque')
                self.moveCursorRefresh(stdscr)

            if c == ord('r'):

                torque = 0.0
                obs, reward, done, info = self.env.step([torque])
                x, y, thetadot = obs

                time.sleep(delay_time)
                self.drawStandard(stdscr)

                stdscr.addstr(x_str_pos[1], x_str_pos[0], 'x = {:.2f}'.format(x))
                stdscr.addstr(y_str_pos[1], y_str_pos[0], 'y = {:.2f}'.format(y))
                stdscr.addstr(thetadot_str_pos[1], thetadot_str_pos[0], 'thetadot = {:.2f}'.format(thetadot))

                stdscr.addstr(torque_str_pos[1], torque_str_pos[0], 'Current torque = {:.2f}'.format(torque))

                stdscr.addstr(last_action_str_pos[1], last_action_str_pos[0], 'Pressed r, refreshing')
                self.moveCursorRefresh(stdscr)


            elif c == ord('q'):
                print('you pressed q! exiting', 1)
                break  # Exit the while loop


    def moveCursorRefresh(self, stdscr):
        stdscr.move(curses.LINES - 1, curses.COLS - 1)
        stdscr.refresh() #Do this after addstr


    def directControl(self):
        print('entering curses loop', 1)
        curses.wrapper(self.DCloop)
        print('exited curses loop.', 1)
        self.env.reset()



    def drawStandard(self, stdscr):
        stdscr.erase()

        stdscr.addstr(curses.LINES - 1, 0,  'Press q or Esc to quit')

        stdscr.refresh() #Do this after addstr


if __name__ == '__main__':


    ce = curses_env()

    ce.directControl()

    print('Size of curses window: LINES={}, COLS={}'.format(curses.LINES, curses.COLS), 1)
