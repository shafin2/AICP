# Task 1: Start of the day
train_schedule = {
    '09:00': {'available_seats': 480, 'total_money': 0, 'passengers': 0},
    '10:00': {'available_seats': 560, 'total_money': 0, 'passengers': 0},
    '11:00': {'available_seats': 480, 'total_money': 0, 'passengers': 0},
    '12:00': {'available_seats': 560, 'total_money': 0, 'passengers': 0},
    '13:00': {'available_seats': 480, 'total_money': 0, 'passengers': 0},
    '14:00': {'available_seats': 560, 'total_money': 0, 'passengers': 0},
    '15:00': {'available_seats': 480, 'total_money': 0, 'passengers': 0},
    '16:00': {'available_seats': 560, 'total_money': 0, 'passengers': 0},
}

# Task 2: Purchasing tickets
def purchase_tickets(train_time, num_tickets):
    if train_schedule[train_time]['available_seats'] >= num_tickets:
        ticket_price = num_tickets * 25
        if num_tickets >= 10:
            free_tickets = num_tickets // 10
            ticket_price -= free_tickets * 25
        train_schedule[train_time]['available_seats'] -= num_tickets
        train_schedule[train_time]['total_money'] += ticket_price
        train_schedule[train_time]['passengers'] += num_tickets
        print(f"Tickets purchased successfully for {num_tickets} passengers at {train_time}.")
    else:
        print(f"Sorry, not enough seats available for {num_tickets} passengers at {train_time}.")

# Task 3: End of the day
def end_of_day():
    total_passengers = 0
    total_money = 0
    max_passengers_train = None
    max_passengers = 0

    for time, data in train_schedule.items():
        total_passengers += data['passengers']
        total_money += data['total_money']

        if data['passengers'] > max_passengers:
            max_passengers = data['passengers']
            max_passengers_train = time

    print("\nEnd of the day summary:")
    print(f"Total passengers: {total_passengers}")
    print(f"Total money collected: ${total_money}")
    print(f"The train with the most passengers today is at {max_passengers_train} with {max_passengers} passengers.")

# Task 4: Keep the booking running until all tickets are sold
while any(data['available_seats'] > 0 for data in train_schedule.values()):
    for time in train_schedule.keys():
        num_tickets = min(train_schedule[time]['available_seats'], 5)  # You can adjust the number of tickets per purchase
        purchase_tickets(time, num_tickets)

end_of_day()

# suggestions