import json

async def increase_points(points, user_id):
    #increase points in gambling.json by points for user
    #if user doesn't exist, create a new entry for them
    #if user exists, add points to their current points
    with open('modules/gambling/gambling.json') as f:
        data = json.load(f)
        if user_id in data['users']:
            data['users'][user_id]['balance'] += points
        else:
            data['users'][user_id] = {"balance": points}
    with open('modules/gambling/gambling.json', 'w') as f:
        json.dump(data, f, indent=4)