from config import user_tier

# Calculate hours remaining before the EV leaves
def time_remaining(ev, current_hour):
    if ev.departure < current_hour:
        return 24 + ev.departure - current_hour
    else:
        return ev.departure - current_hour
    
# More energy needed in less time = higher urgency
def urgency(ev, current_hour):
    return ev.energy_req/time_remaining(ev, current_hour)

# Final priority combines:
# User tier + urgency + small V2G bonus
def priority_score(ev, current_hour):
    return user_tier[ev.user_pref]["priority"] + urgency(ev, current_hour) + 0.5*ev.v2g