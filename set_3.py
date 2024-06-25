def relationship_status (from_member, to_member, social_graph):
    '''Relationship Status'''
    from_member_following = (social_graph.get(from_member)).get("following")
    to_member_following = (social_graph.get(to_member)).get("following")

    follower = False
    followed_by = False
    friends = False
    no_relationship = False

    for username in from_member_following:
        if username == to_member:
            follower = True

    for username in to_member_following:
        if username== from_member:
            followed_by = True
    
    if follower== True and followed_by== True:
        return('friends')
    elif follower== False and followed_by== True:
        return('followed by')
    elif follower== True and followed_by== False:
        return('follower')
    else:
        return('no relationship')
    
def tic_tac_toe(board):
    '''Tic Tac Toe'''

    # Initializing variables
    caseholder = []
    boarddim = len(board)
    
    # Diagonals
    upper_left_to_lower_right = [board[i][i] for i in range(boarddim)]
    caseholder.append(upper_left_to_lower_right)
    
    lower_left_to_upper_right = [board[boarddim-1-i][i] for i in range(boarddim)]
    caseholder.append(lower_left_to_upper_right)

    # Columns
    columns = [list(col) for col in zip(*board)]
    for col in columns:
        caseholder.append(col)
    
    # Rows
    for row in board:
        caseholder.append(row)

    # Determining winner
    for case in caseholder:
        if all(j == case[0] and j != '' for j in case):
            winner = case[0]
            return winner

    return 'NO WINNER'

def eta(first_stop, second_stop, route_map):
    '''ETA'''
    # Initialize lists
    routes = []
    times = []
    # Populate the routes and times lists
    for key in route_map:
        routes.append(key[0])
        times.append(route_map[key]['travel_time_mins'])
    # Index of first and second stops
    i_1 = routes.index(first_stop)
    i_2 = routes.index(second_stop)
    total = 0
    # When first stop is less than the index of the second stop.                                     
    if i_1 < i_2:
        for i in range(i_1, i_2):
            total += times[i]
    # otherwise
    else:
        for i in range(i_1, len(routes)):
            total += times[i]
        for i in range(0, i_2):
            total += times[i]
    
    return total












