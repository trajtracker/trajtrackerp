"""

A simple version of the number-to-position experiment, which demonstrates how to use the events mechanism: 
it adds functions that run when various events occur (e.g. finger stars moving).
In this example, the functions only print things to log and display the event on screen; 
but you can use similar functions to do anything you want.

The functions are hooked into the program by registering them to specific events within the trial
(via the event manager). Here, the functions are registered to run immediately when the event occur. 
To make them run in certain delay after the event, add the delay (in seconds) to the event itself.
For example, try changing the registration of TRIAL_ENDED into:

exp_info.event_manager.register_operation(event=ttrk.events.TRIAL_ENDED + 0.5,
                                          operation=on_trial_ended,
                                          recurring=True,
                                          description="Custom on-ended operation")

@author: Dror Dotan
@copyright: Copyright (c) 2017, Dror Dotan
"""

import expyriment as xpy

import trajtracker as ttrk
import trajtrackerp as ttrkp
from trajtrackerp import num2pos, common


if not xpy.misc.is_android_running():
    xpy.control.defaults.window_mode = True
    ttrk.log_to_console = True

ttrk.env.default_log_level = ttrk.log_info


config = num2pos.Config("Num2Pos(D+U)",
                        max_movement_time=2,
                        max_numberline_value=100,
                        data_source=range(101) * 2,
                        text_target_height=0.5)

#=====================================================================

msg = xpy.stimuli.TextBox(text="", size=(200, 40), text_font="Arial", text_size=15,
                          text_colour=xpy.misc.constants.C_WHITE)

def on_finger_touched_screen(time_in_trial, time_in_session):
    print(">>>>>>> Finger touched screen")
    msg.text = "State: Starting"

def on_finger_started_moving(time_in_trial, time_in_session):
    print(">>>>>>> Finger started moving")
    msg.text = "State: Moving"

def on_finger_stopped_moving(time_in_trial, time_in_session):
    print(">>>>>>> Finger stopped moving")
    msg.text = "State: Stopped"

def on_trial_ended(time_in_trial, time_in_session):
    print(">>>>>>> Trial ended")
    msg.text = "State: Ended"

#=====================================================================

#-- Initialize & start the Expyriment
exp = ttrk.initialize()
xpy.control.start(exp)

if not xpy.misc.is_android_running():
    exp.mouse.show_cursor()

#-- Get subject info
(subj_id, subj_name) = ttrkp.common.get_subject_name_id()

#-- Initialize the experiment objects
exp_info = num2pos.ExperimentInfo(config, exp, subj_id, subj_name)
num2pos.create_experiment_objects(exp_info)
common.register_to_event_manager(exp_info)

#-- Set position of custom textboxes (this can only be done now, after the experiment was initialized)
msg.position = -exp_info.screen_size[0] / 2 + msg.size[0] / 2 + 10, -exp_info.screen_size[1] / 2 + msg.size[1] / 2 + 10

#-- Add custom objects
exp_info.stimuli.add(msg)   # So present() is repeatedly invoked for msg1

#-- Invoke custom operations when certain events occur

exp_info.event_manager.register_operation(event=ttrk.events.TRIAL_STARTED,
                                          operation=on_finger_touched_screen,
                                          recurring=True,
                                          description="Custom on-touch operation")

exp_info.event_manager.register_operation(event=ttrk.events.TRIAL_ENDED,
                                          operation=on_trial_ended,
                                          recurring=True,
                                          description="Custom on-ended operation")

exp_info.event_manager.register_operation(event=common.FINGER_STARTED_MOVING,
                                          operation=on_finger_started_moving,
                                          recurring=True,
                                          description="Custom on-move operation")

exp_info.event_manager.register_operation(event=common.FINGER_STOPPED_MOVING,
                                          operation=on_finger_stopped_moving,
                                          recurring=True,
                                          description="Custom on-stop operation")

exp_info.event_manager.log_level = ttrk.log_debug


#-- Run the experiment
num2pos.run_trials(exp_info)

#-- Shutdown Expyriment
xpy.control.end()
