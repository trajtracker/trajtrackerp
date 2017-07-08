"""

A simple version of the number-to-position experiment, which adds an object that is continuously fed
with the finger trajectory information.

To create such an object, you should:
1. Create a class with the reset() and update_xyt() methods, each getting the same parameters
   as in the example below.
2. Create an object of this class and register it as a trajectory-sensitive object:
   exp_info.add_trajectory_sensitive_object(tso)
   
reset() will be called when the trial is initialized (finger touches screen).
update_xyt() will be repeatedly called when the finger moves (between the FINGER_STARTED_MOVING 
and FINGER_STOPPED_MOVING events). 

@author: Dror Dotan
@copyright: Copyright (c) 2017, Dror Dotan
"""

import numpy as np

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
                          text_colour=xpy.misc.constants.C_GREEN)

class TrajectorySensitiveObject(object):

    def reset(self, time0):
        self._trajectory = []

    def update_xyt(self, position, time_in_trial, time_in_session):
        self._trajectory.append(position)

    def calc_trajectory_length(self):
        dx = np.diff([pos[0] for pos in self._trajectory])
        dy = np.diff([pos[1] for pos in self._trajectory])
        segments = np.sqrt(dx ** 2 + dy ** 2)
        return sum(segments)

tso = TrajectorySensitiveObject()

def on_finger_stopped_moving(time_in_trial, time_in_session):
    print(">>>>>>> Finger stopped moving")
    length = tso.calc_trajectory_length()
    print("Trajectory length: {:}".format(length))
    msg.text = "Length: {:}".format(int(length))

#===========================================================================================

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
msg.position = -exp_info.screen_size[0]/2 + msg.size[0]/2 + 10, -exp_info.screen_size[1]/2 + msg.size[1]/2 + 10

#-- Add custom objects
exp_info.stimuli.add(msg)   # So present() is repeatedly invoked for msg2
exp_info.add_trajectory_sensitive_object(tso)  # So tso.reset() and tso.update_xyt() are called


#-- When the finger stopped moving, update the trajectory information
exp_info.event_manager.register_operation(event=common.FINGER_STOPPED_MOVING,
                                          operation=on_finger_stopped_moving,
                                          recurring=True,
                                          description="Show trajectory data")

#-- Run the experiment
num2pos.run_trials(exp_info)

#-- Shutdown Expyriment
xpy.control.end()
