# Lab 4: Two Laps of the Track

## Grading for the rest of the term

**Read this section carefully. The attendance rules are strict.**

| Component                                     | When                             | Weight                    |
| --------------------------------------------- | -------------------------------- | ------------------------- |
| Attendance                                    | every lab                        | **50%** of your lab grade |
| Lab 4 task: two laps of the track             | this week and next week (2 labs) | **15%** of your lab grade |
| Final assessment                              | the 3 labs after Lab 4           | **35%** of your lab grade |
| Bonus: shape task during your laps (optional) | during Lab 4                     | **+1%** to your lab grade |

**Attendance (50%).** If you have attended every lab so far, you have not lost
any marks.

**Lab 4 task (15%), over 2 weeks.** If you miss **either** week, you lose 2/3 of
this mark automatically, so the most you can score is **5/15**. If you miss
**both** weeks, you get **0/15**.

**Final assessment, over 3 weeks.** You lose **1/2** of the final assessment
mark for **each** lab you miss in that period. Miss 1 lab and the most you can
score is 1/2 of the mark; miss 2 and the most you can score is 0.
The final assessment uses the green robot, the **Hiwonder JetRover**.

> **There are no exceptions for missed attendance.** This is strict because
> from now on you work in groups, and when you miss a lab your group members
> lose your help.

### Groups

From now on you work in **pairs**. Groups of three are allowed only when the
numbers require it. You may also choose to work **alone**.

### Using AI tools (ChatGPT, Claude, Copilot, ...)

You **may** use LLM tools. Keep a short note of when you used one and what for
(for example, a comment in your code or a `NOTES.md` file in your folder).

This is meant to reflect a real setting: at work or at home you will have
these tools available, and we want you to practise using them responsibly.
You are still responsible for understanding what your code does.

---

## Today's task

**Get your robot to complete two full laps of the track, fully autonomously.**
No one may touch the robot or the controls (joystick, buttons, keyboard) once
it has started.

A lap counts when your robot goes around the track and crosses one of the
**white lines** on it. Our track is not a perfect circuit, so a lap does not
have to finish exactly where it started.

A TA must watch **both** laps to give you the mark.

### 💡 Hint: the line sensor is tuneable

The line sensor is not fixed. Each of its 4 channels has a small
**potentiometer** (a tiny screw on the sensor board under the front bumper)
that sets how bright the floor must be before that channel switches between
"line" and "no line".

Out of the box it is set to tell **black from white**. Our track is **grey and
white**. With the right adjustment, the sensor can tell those apart too.

To tune it:

1. Run `python tools/line_sensor.py --watch` (or open the window and look at the
   **Line sensors** panel).
2. Place one sensor over grey, then over white, and watch its reading.
3. Turn that channel's potentiometer **gently**, a little at a time, with a
   small screwdriver, until the reading changes between grey and white.
4. Repeat for each of the 4 channels.

### There is no right way to do this

You have every tool from the previous labs available to you. Use whichever
approach you like. Some ideas:

- **The line sensor and the Lab 2 line follower.** The track is grey and white,
  not black tape on a light floor. Inverting the Lab 2 line-following system is
  one viable approach (see `LINE_INVERT` in `turbopi/config.py`, or change the
  logic in your own code).
- **Tuning the line sensor's potentiometers** (see the hint above).
- **The camera.** If you can get around the track using the camera instead,
  that's good too.
- **Anything else** you can make work.

### Optional bonus (+1% to your lab grade)

Use the **coloured shapes** in the lab to make your robot perform a task while
it runs its laps. It can be as simple as: see a shape, do a 360° spin on the
spot, then carry on with the lap.

This needs computer vision. You should already have that from Lab 3; if you
don't, ask a TA. You do **not** need computer vision for the main task.

---

## What you're given

This folder contains the **complete Lab 2 solution** as your starting point.

```
Lab_4/
├── README.md               ← you are here
├── requirements.txt        ← Python packages to install
├── run_robot.py            ← opens the window and connects to the robot
├── line_follower.py        ← the Lab 2 line follower (complete)
├── turbopi/
│   ├── config.py           ← every setting: speeds, tuning values, LINE_INVERT, ...
│   ├── rosbridge_client.py ← talks to the robot (cmd_vel, servos, sonar, line sensor)
│   ├── gui.py              ← the window, with the line sensor panel and Line Follow button
│   └── ...
└── tools/
    ├── line_sensor.py      ← watch the 4 line sensors live
    └── list_topics.py      ← lists the robot's ROS topics
```

### Quick reference

```bash
pip install -r requirements.txt     # once per computer
python run_robot.py                 # open the window and connect to the robot
python tools/line_sensor.py --watch # print the 4 line sensors live (Ctrl+C to stop)
```

Connect to the robot's Wi-Fi first, exactly as in the previous labs.

### Reminders from Lab 2

- **Watching the sensors:** the **Line sensors** panel in the window and
  `tools/line_sensor.py --watch` both show what each of the 4 sensors sees, live.
  Use them while you slide the robot over the track by hand.
- **Tuning values** (`FOLLOW_SPEED`, `TURN_GAIN`, `SEARCH_TURN`) are in
  `turbopi/config.py`. Change one at a time and write down what happened.
  After editing `config.py`, close the window and run the program again.
- **After editing `line_follower.py`**, click **Stop Line Follow**, then
  **Start Line Follow** again. The file is reloaded each time.
- **Stopping the robot:** the **space bar**, the **STOP** button, touching the
  joystick, or closing the window all stop it.
- `python run_robot.py --check` still runs the **Lab 2** tests. It does not
  grade this lab, so it is fine if your changes make some of them fail.
