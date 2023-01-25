if player == computer:
    print('its a tie!')
elif player == 'rock' and computer == 'scissors':
    print('Player wins!')
elif player == 'paper' and computer == 'rock':
    print('Player wins!')
elif player == 'scissors' and computer == 'paper':
    print('Player wins!')
else:
    print('Computer wins!')