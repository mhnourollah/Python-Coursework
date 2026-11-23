midterm_scores = [99.5, 78.25, 76, 58.5, 100, 87.5, 91, 68, 100]
final_scores = [55, 62, 100, 98.75, 80, 76.5, 85.25]

print("Lowest midterm:", min(midterm_scores))
print("Highest midterm:", max(midterm_scores))

print("Lowest final:", min(final_scores))
print("Highest final:", max(final_scores))

print("Average midterm:",
      sum(midterm_scores) / len(midterm_scores))

print("Average final:",
      sum(final_scores) / len(final_scores))
