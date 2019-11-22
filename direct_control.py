import curses
import time
import numpy as np

import gym
import gym_raas
'''
'''

stdscr = curses.initscr()
curses.halfdelay(1)
curses.noecho()


class curses_env:

    def __init__(self):

        self.env = gym.make('raaspendulum-v0')
        self.env.reset()


    def DCloop(self, stdscr):
        #https://docs.python.org/3/howto/curses.html
        #https://docs.python.org/3/library/curses.html#curses.window.clrtobot

        curses.halfdelay(1)

        #print('Size of curses window: LINES={}, COLS={}'.format(curses.LINES, curses.COLS), 1)
        delay_time = 0.05

        torque = 0.0
        torque_incr = 0.1
        max_torque = 2.0

        last_action_str_pos = [0, 8]
        waiting_str_pos = [0, 10]
        torque_str_pos = [0, 6]

        x_str_pos = [0, 2]
        y_str_pos = [0, 3]
        thetadot_str_pos = [0, 4]


        stay_on = False


        self.drawStandard(stdscr)

        while True:
            c = stdscr.getch()

            #_, _, _ = self.env._get_obs()

            if c != curses.ERR:

                if c == curses.KEY_LEFT:
                    curses.flushinp()

                    torque = min(max_torque, torque + torque_incr)
                    obs, reward, done, info = self.env.step([torque])
                    x, y, thetadot = obs

                    stay_on = True

                    time.sleep(delay_time)
                    self.drawStandard(stdscr)

                    stdscr.addstr(x_str_pos[1], x_str_pos[0], 'x = {:.2f}'.format(x))
                    stdscr.addstr(y_str_pos[1], y_str_pos[0], 'y = {:.2f}'.format(y))
                    stdscr.addstr(thetadot_str_pos[1], thetadot_str_pos[0], 'thetadot = {:.2f}'.format(thetadot))

                    stdscr.addstr(torque_str_pos[1], torque_str_pos[0], 'Current torque = {:.2f}'.format(torque))

                    stdscr.addstr(last_action_str_pos[1], last_action_str_pos[0], 'Pressed Left key, incrementing torque')
                    self.moveCursorRefresh(stdscr)


                if c == curses.KEY_RIGHT:
                    curses.flushinp()

                    torque = max(-max_torque, torque - torque_incr)
                    obs, reward, done, info = self.env.step([torque])
                    x, y, thetadot = obs

                    stay_on = True

                    time.sleep(delay_time)
                    self.drawStandard(stdscr)

                    stdscr.addstr(x_str_pos[1], x_str_pos[0], 'x = {:.2f}'.format(x))
                    stdscr.addstr(y_str_pos[1], y_str_pos[0], 'y = {:.2f}'.format(y))
                    stdscr.addstr(thetadot_str_pos[1], thetadot_str_pos[0], 'thetadot = {:.2f}'.format(thetadot))

                    stdscr.addstr(torque_str_pos[1], torque_str_pos[0], 'Current torque = {:.2f}'.format(torque))

                    stdscr.addstr(last_action_str_pos[1], last_action_str_pos[0], 'Pressed Right key, decrementing torque')
                    self.moveCursorRefresh(stdscr)





                if c == curses.KEY_UP:
                    curses.flushinp()

                    torque = 2
                    obs, reward, done, info = self.env.step([torque])
                    x, y, thetadot = obs

                    stay_on = False

                    time.sleep(delay_time)
                    self.drawStandard(stdscr)

                    stdscr.addstr(x_str_pos[1], x_str_pos[0], 'x = {:.2f}'.format(x))
                    stdscr.addstr(y_str_pos[1], y_str_pos[0], 'y = {:.2f}'.format(y))
                    stdscr.addstr(thetadot_str_pos[1], thetadot_str_pos[0], 'thetadot = {:.2f}'.format(thetadot))

                    stdscr.addstr(torque_str_pos[1], torque_str_pos[0], 'Current torque = {:.2f}'.format(torque))

                    stdscr.addstr(last_action_str_pos[1], last_action_str_pos[0], 'Pressed Down key, applying momentary max torque')
                    self.moveCursorRefresh(stdscr)


                if c == curses.KEY_DOWN:
                    curses.flushinp()

                    torque = -2
                    obs, reward, done, info = self.env.step([-2])
                    x, y, thetadot = obs

                    stay_on = False

                    time.sleep(delay_time)
                    self.drawStandard(stdscr)

                    stdscr.addstr(x_str_pos[1], x_str_pos[0], 'x = {:.2f}'.format(x))
                    stdscr.addstr(y_str_pos[1], y_str_pos[0], 'y = {:.2f}'.format(y))
                    stdscr.addstr(thetadot_str_pos[1], thetadot_str_pos[0], 'thetadot = {:.2f}'.format(thetadot))

                    stdscr.addstr(torque_str_pos[1], torque_str_pos[0], 'Current torque = {:.2f}'.format(torque))

                    stdscr.addstr(last_action_str_pos[1], last_action_str_pos[0], 'Pressed Up key, applying momentary -max torque')
                    self.moveCursorRefresh(stdscr)



                if c == ord('r'):
                    curses.flushinp()
                    
                    torque = 0.0
                    obs, reward, done, info = self.env.step([torque])
                    x, y, thetadot = obs

                    stay_on = False

                    time.sleep(delay_time)
                    self.drawStandard(stdscr)

                    stdscr.addstr(x_str_pos[1], x_str_pos[0], 'x = {:.2f}'.format(x))
                    stdscr.addstr(y_str_pos[1], y_str_pos[0], 'y = {:.2f}'.format(y))
                    stdscr.addstr(thetadot_str_pos[1], thetadot_str_pos[0], 'thetadot = {:.2f}'.format(thetadot))

                    stdscr.addstr(torque_str_pos[1], torque_str_pos[0], 'Current torque = {:.2f}'.format(torque))

                    stdscr.addstr(last_action_str_pos[1], last_action_str_pos[0], 'Pressed r, refreshing')
                    self.moveCursorRefresh(stdscr)


                if c == ord('q') or c == 27:
                    stdscr.addstr(last_action_str_pos[1], last_action_str_pos[0], 'You pressed q! exiting.')
                    print('you pressed q! exiting', 1)
                    break  # Exit the while loop


            else:

                x, y, thetadot = self.env._get_obs()

                self.drawStandard(stdscr)

                if not stay_on:
                    torque = 0
                    obs, reward, done, info = self.env.step([torque])
                    stdscr.addstr(torque_str_pos[1], torque_str_pos[0], 'Current torque = {:.2f}'.format(torque))
                    curses.flushinp()


                stdscr.addstr(x_str_pos[1], x_str_pos[0], 'x = {:.2f}'.format(x))
                stdscr.addstr(y_str_pos[1], y_str_pos[0], 'y = {:.2f}'.format(y))
                stdscr.addstr(thetadot_str_pos[1], thetadot_str_pos[0], 'thetadot = {:.2f}'.format(thetadot))

                stdscr.addstr(waiting_str_pos[1], waiting_str_pos[0], 'Waiting for next command...')
                self.moveCursorRefresh(stdscr)



    def draw_directions(self, stdscr):

        stdscr.addstr(curses.LINES - 4, 0, '--Press Up and Down for momentary max torque')
        stdscr.addstr(curses.LINES - 3, 0, '--Press Left and Right to adjust permanent applied torque')
        stdscr.addstr(curses.LINES - 2, 0, '--Press r to refresh')
        stdscr.addstr(curses.LINES - 1, 0, '--Press q to quit')


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

        self.draw_directions(stdscr)

        stdscr.refresh() #Do this after addstr


if __name__ == '__main__':


    ce = curses_env()

    ce.directControl()

    print('Size of curses window: LINES={}, COLS={}'.format(curses.LINES, curses.COLS), 1)
