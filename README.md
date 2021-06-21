# Self Tracking Health Test
Computer vision applied to your own behavior to detect low blinking ratio or bad ergonomic position and prevent future related diseases.


https://user-images.githubusercontent.com/4467437/122435994-15875c00-cf5e-11eb-869a-b61290394b1e.mp4



# Tracking functions supported
- Blinks per minute tracking.
- Average of ergonomic posture per minute in front of a screen.

# How it works
- inside your terminal go to project root and execute:
    ```
    python runner.py
    ```
- Press Esc key to end the test and see the report in your browser automatically.
- The tracking results will depend on how long you leave the script running (minutes measure).

# How to read the test results
It's recommended to use it for more than 30 minutes to have enough data and begin to see patterns.

- Blink section:
![test_results_blink](https://user-images.githubusercontent.com/4467437/122664925-eba28500-d169-11eb-9cb2-4c244857d5aa.png)

- Posture section:
![image](https://user-images.githubusercontent.com/4467437/122705564-a3dc3600-d21b-11eb-9ebf-b8539ba81b18.png)
for now it's pretty simple a linear graph that shows us a value between 1 and 0 if we have a good posture or not respectively

# Invite to colaborate
Anyone is free to collaborate with the current project.
