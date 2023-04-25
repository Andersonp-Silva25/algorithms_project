def study_schedule(permanence_period, target_time):
    if not target_time:
        return None
    
    counter = 0

    for entry_period, leave_period  in permanence_period:
        if isinstance(entry_period, int) and isinstance(leave_period, int):
            if entry_period <= target_time <= leave_period:
                counter += 1
        else:
            return None
    return counter
