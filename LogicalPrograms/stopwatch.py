import time

def stopwatch_simulation():
    """
    Simulates a stopwatch to measure elapsed time between start and end clicks.
    
    Returns:
    float: The elapsed time in seconds.
    """
    input("Press Enter to start the stopwatch")
    start_time = time.time()
    
    input("Press Enter to stop the stopwatch")
    end_time = time.time()
    
    elapsed_time = end_time - start_time
    return elapsed_time

# Main
print("Stopwatch simulation started. Follow instructions:")
elapsed_time = stopwatch_simulation()
print(f"Elapsed time: {elapsed_time} seconds")
