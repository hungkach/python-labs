# Lift volume session calculator
# Mark Hung, 5/19/2026
# Calculates per-set and total session volume from rep and weight inputs.


# Define the session data
reps = [5, 5, 5, 3, 3]
weights = [135, 155, 175, 185, 195]
reps_b = [8, 8, 8]
weights_b = [95, 115, 135]

#Print reps and weights of the first pair of lists
print(reps)
print(weights)

# Define the function
def print_session_summary(reps, weights):

    total_volume = 0

    for index, (rep, weight) in enumerate(zip(reps, weights),start=1):
        volume = rep * weight
        total_volume += volume
        print(f"Set {index}: {rep} X {weight} = {volume} pounds | Running total {total_volume} pounds")

    print(f"Session total: {total_volume} lbs")

# Call the functions and print the summaries

print()
print_session_summary(reps_b, weights_b)

print()
print_session_summary(reps, weights)