'''
# Trip Cost Calculator

Create a python script that asks a user questions in the command line. The script should follow the outlined specs.

## Specs

Receive the following arguments from the user:

- kilometers to drive
- liters-per-kilometer usage of the car
- price per liter of fuel

Calculate the cost of the trip and display it to the user in the console.

'''

distance = float(input('Kilometres to drive: '))
litres_per_km = float(input('Litres-per-kilometre usage of the car: '))
price_per_litre = float(input('Price per litre of fuel: '))

total_cost = distance * litres_per_km * price_per_litre

print('The cost of fuel for your trip is expected to be: ' + str(total_cost))
