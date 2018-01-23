.. TrajTracker Paradigms documentation master file, created by
   sphinx-quickstart on Wed Jul  5 00:26:03 2017.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

TrajTracker Paradigms |version|
===============================

TrajTracker offers two ready-to-use experimental paradigms - number-to-position mapping and discrete-choice
(two buttons forced choice). Each of them is a set of functions that allow
creating your own experiment with almost no programming.

For each of the two paradigms, you can create your own experiment in two ways:

* For most common features, you will only have to change the program configuration.

* If your experiment requires features that are not directly supported by the configuration offered,
  you can change the python code. To help you in that, see below the documentation of the functions
  that implement each of the two paradigms.

The list of trial is defined in a CSV file. The format of this files, including the
possible things you can configure via this file, are explained :doc:`here <input_data_format>`.

The results of each experiment session are saved in 3 files: a file with general data, a file with
trials information, and a trajectory file. See details :doc:`here <results>`.

Supported paradigms
-------------------

Number-to-position mapping
++++++++++++++++++++++++++

This paradigm shows a number line and various possible stimuli. The response is indicated by
dragging the finger to a location on the number line.

For an overview of this paradigm under TrajTracker, see
`the number-to-position page <https://trajtracker.wixsite.com/trajtracker/ttrk-exp-num2pos>`_.

.. toctree::
   :maxdepth: 1
   :glob:

   Configuration: the Config class <num2pos/Config>
   Technical: the software design <num2pos/num2pos_design>
   Technical: the ExperimentInfo class <num2pos/ExperimentInfo>
   Technical: the TrialInfo class <num2pos/TrialInfo>


Discrete choice
+++++++++++++++

This paradigm shows two response buttons (in the top corners of the screen) and various possible stimuli.
The response is indicated by dragging the finger to one of the buttons.

.. toctree::
   :maxdepth: 1
   :glob:

   Configuration: the Config class <dchoice/Config>
   Technical: the software design <dchoice/dchoice_design>
   Technical: the ExperimentInfo class <dchoice/ExperimentInfo>
   Technical: the TrialInfo class <dchoice/TrialInfo>


How to use these paradigms
--------------------------

Creating a simple experiment (that uses only the supported features)
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

Several features are already supported by the paradigm we wrote. These features can be used
with almost no programming. To use them, you should:

- Create your main program by copy one of the existing sample scripts. The simplest ones are
  `number_to_position_1 <https://github.com/trajtracker/trajtracker/tree/master/samples/number_to_position_1>`_
  for number-to-position experiments and
  `dchoice_1 <https://github.com/trajtracker/trajtracker/tree/master/samples/dchoice_1>`_
  for discrete-choice experiments.
- In your script, set the experiment's general configuration parameters.
  This is done by updating the **Config** object (see here its documentation for
  :doc:`number-to-position <num2pos/Config>` and
  :doc:`discrete-choice <num2pos/Config>` experiments.
- Create a CSV file with the per-trial data. See :doc:`here <input_data_format>`
  a detailed description of this file format.

Even in this experiment, you may need to write minimal code - e.g., if you use non-text stimuli,
you would have to create them yourself (e.g., see the
`quantity_to_position <https://github.com/trajtracker/trajtracker/tree/master/samples/quantity_to_position>`_
sample experiment we created, where the stimuli are sets of dots).


Making advanced changes by modifying the code
+++++++++++++++++++++++++++++++++++++++++++++

If your experiment requires features that are not supported via the above configuration, you can modify
the relevant python functions. To help you on this, the following pages describe how the experiment
software is designed: for :doc:`number-to-position <num2pos/num2pos_design>` experiments
and for :doc:`discrete-choice <dchoice/dchoice_design>` experiments.

The simplest way to do such modifications is to copy the relevant functions into your own script.
You can see an example for the way it is done in the
`number_to_position_2 <https://github.com/trajtracker/trajtracker/tree/master/samples/number_to_position_2>`_
sample script.

Events
++++++

*TrajTracker Paradigms* works with events, which help you run your custom code at predefined times.
To learn how to plug your code to run when specific events occur, please read the
`events <http://www.trajtracker.com/apiref/events/events_overview>`_ and check out
the :func:`EventManager.register_operation <trajtracker:trajtracker.events.EventManager.register_operation>` method.

*TrajTracker Paradigms* supports the following events per trial:

- **trajtracker.events.TRIAL_INITIALIZED**: Dispatched when the trial information is initalized. This typically happens
  right after the previous trial has ended.

- **trajtracker.events.TRIAL_STARTED**: Dispatched when the trial starts, which is when the finger touches the screen.

  when :attr:`Config.stimulus_then_move <trajtrackerp.num2pos.Config.stimulus_then_move>` = *True*,
  the timing of target onset/offset is specified relatively to this event.

- **trajtracker.events.TRIAL_SUCCEEDED**: Dispatched when the trial ends successfully. If the trial required an additional task
  after the main task (e.g., confidence rating), the event will be dispatched after the additional tasks
  are completed too.

- **trajtracker.events.TRIAL_FAILED**: Dispatched when an error occurs. "An error" does not mean an incorrect response,
  but that the subject did not comply with one of the experiment rules (e.g. lifted the finger, moved too slowly,
  etc.).

- **trajtracker.events.TRIAL_ENDED**: This event dispatched both with TRIAL_SUCCEEDED and with TRIAL_FAILED.

- **trajtrackerp.common.FINGER_STARTED_MOVING**: Dispatched when the finger leaves the start point.

  when :attr:`Config.stimulus_then_move <trajtrackerp.num2pos.Config.stimulus_then_move>` = *False*,
  the timing of target onset/offset is specified relatively to this event.

  In such case, if you set the target's onset_time to be 0, it will be presented right after this event.
  The delay between the event and the target onset may vary within the range of 1 frame (delay <= 17 ms for
  a 60Hz monitor). If you want to write a custom function that is very accurately syhcoronized with the
  target's onset, it is better to register the function to FINGER_STARTED_MOVING with delay.
  For example, registering your function to FINGER_STARTED_MOVING+0.1 will make it run 100 ms after the target's onset,
  and registering it to FINGER_STARTED_MOVING+0.001 will make your function run in the frame immediately following
  the target's onset.


Resource files
++++++++++++++

TrajTracker includes the source code for the two paradigms above, and also some resource files:

- Sounds (to indicate successful / incorrect trial)
- Images for simple stimuli

These files are in the `trajtrackerp_res <https://github.com/trajtracker/trajtrackerp/tree/master/src/trajtrackerp_res>`_
directory (if your installed with *pip*, find this directory in your *site-packages* folder).


Indices and tables
==================

* :ref:`genindex`
* :ref:`search`
