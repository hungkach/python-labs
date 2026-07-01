# Lift Volume Session Calculator

A Python tool that calculates per-set and session-total training volume from rep and weight inputs.

## Why this exists
In Strength and Conditioning (S&C), monitoring total session volume is a primary metric for quantifying training stress and ensuring properly managed athletic adaptation. Calculating these metrics manually across multiple parallel data points introduces calculation lag and human error. This utility automates the calculation process to provide practitioners and athletes with an immediate, accurate volumetric breakdown of their training sessions.

## What it does
- Pairs parallel sequences of repetitions and weights into ordered, chronological sets.
- Computes exact training volume for each individual set (reps × weight).
- Accumulates a progressive running total of training stress throughout the session.
- Handles and outputs sequential summary tracking for multiple training bouts.

##
```
[5, 5, 5, 3, 3]
[135, 155, 175, 185, 195]

Set 1: 8 X 95 = 760 pounds | Running total 760 pounds
Set 2: 8 X 115 = 920 pounds | Running total 1680 pounds
Set 3: 8 X 135 = 1080 pounds | Running total 2760 pounds
Session total: 2760 lbs

Set 1: 5 X 135 = 675 pounds | Running total 675 pounds
Set 2: 5 X 155 = 775 pounds | Running total 1450 pounds
Set 3: 5 X 175 = 875 pounds | Running total 2325 pounds
Set 4: 3 X 185 = 555 pounds | Running total 2880 pounds
Set 5: 3 X 195 = 585 pounds | Running total 3465 pounds
Session total: 3465 lbs
```

# How to run
```
python main.py
```
## Built with 
Python 3.x, standard library only.

## Roadmap
- Implement threshold features to automatically classify warmup sets versus working sets.
- Support multi-exercise session architecture to aggregate total training stress across different movements.
- Integrate automated data ingestion capabilities via CSV or standard spreadsheet file structures.