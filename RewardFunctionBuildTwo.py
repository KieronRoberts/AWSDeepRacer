def reward_function(params):
    #Reads all needed input parameters
    track_width = params['track_width']
    distance_from_center = params['distance_from_center']
    speed = params['speed']
    steering = abs(params['steering_angle'])
    progress = params['progress']
    all_wheels_on_track = params['all_wheels_on_track']
    waypoints = params['waypoints']
    closest_waypoints = params['closest_waypoints']

    #Initialise reward and penalties
    reward = 0.0
    off_track_reward = -1e5

    #Gives a high reward if the car completes a lap
    if progress == 100:
        reward += 1e5

    # Penalising if the car goes off track
    if not all_wheels_on_track:
        reward += off_track_reward

    #Calculating the optimal speed based on the distance from the center of the track
    optimal_speed = speed / (1 + 0.25 * abs(distance_from_center))

    #Rewarding the car for traveling fast
    reward += speed ** 2 / track_width

    #Rewarding the car for staying close to the center of the track
    reward += (1 - (steering / 30)) * (1 - (distance_from_center / (track_width/2))) ** 2

    # Rewarding the car for following all waypoints
    next_point = waypoints[closest_waypoints[1]]
    prev_point = waypoints[closest_waypoints[0]]
    track_direction = math.atan2(next_point[1] - prev_point[1], next_point[0] - prev_point[0])
    direction_diff = abs(params['heading'] - track_direction)
    reward += (1 - direction_diff / math.pi) * 10

    #Rewarding the car for minimising the distance to the next waypoint
    reward += (1 - distance_from_center / (track_width/2)) ** 2

    #Reward the car for traveling further along the track
    reward += progress / 10 ** 6

    return float(reward)
    print(reward)
    


