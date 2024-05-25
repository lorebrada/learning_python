motorcycles = ['Honda', 'Yamaha', 'Suzuki', 'Pagani']
print(motorcycles)

motorcycles[0] = 'Ducati'
print(motorcycles)

motorcycles[3] = "Kawasaki"
print(motorcycles)

motorcycles = ['Honda', 'Yamaha', 'Ducati']
print(motorcycles)
motorcycles.append('Suzuki')
print(motorcycles)

motorcycles = []

motorcycles.append('Honda')
motorcycles.append('Yamaha')
motorcycles.append('Suzuki')
print(motorcycles)


motorcycles = ['Honda', 'Yamaha', 'Suzuki']
motorcycles.insert(0, 'Ducati')
print(motorcycles)


motorcycles = ['Honda', 'Yamaha', 'Ducati']
print(motorcycles)

del motorcycles[0]
print(motorcycles)

motorcycles = ['Honda', 'Yamaha', 'Ducati']
print(motorcycles)

del motorcycles[1]
print(motorcycles)

motorcycles = ['Honda', 'Ducati', 'Suzuki']
print(motorcycles)

popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

motorcycles = ['Honda', 'Yamaha', 'Suzuki']
print(motorcycles)
last_owned = motorcycles.pop()
print(f"The last motorcycle I owned was a {last_owned.title()}.")
first_owned = motorcycles.pop(0)
print(f"The last motorcycle I owned was a {first_owned.title()}.")

motorcycles = ['Honda', 'Ducati', 'Suzuki', 'Yamaha']
print(motorcycles)
motorcycles.remove('Ducati')
print(motorcycles)

motorcycles = ['Honda', 'Ducati', 'Suzuki', 'Yamaha']
print(motorcycles)

too_expensive = 'Ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"\nA {too_expensive.title()} is too expensive for me.")
