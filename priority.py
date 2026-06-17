# Priority Score = User Tier + Urgency + Fairness Credits
from config import user_tier

def time_remaining(ev, current_hour):
    if ev.departure < current_hour:
        return 24 + ev.departure - current_hour
    else:
        return ev.departure - current_hour
    
def urgency(ev, current_hour):
    return ev.energy_req/time_remaining(ev, current_hour)

def priority_score(ev, current_hour):
    return user_tier[ev.user_pref]["priority"] + urgency(ev, current_hour) + 0.5*ev.v2g