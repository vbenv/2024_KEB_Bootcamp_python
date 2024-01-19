import random

# numbers = list()
# for i in range(5):
#     numbers.append(random.randint(1,100))
# print(numbers)

numbers = [random.randint(1,100) for i in range(5)]
print(numbers)

try:
    pick = int(input(f"Input index (0 ~ {len(numbers)-1}) : "))
    print(numbers[pick])
    print(5/0)
except ValueError as err:
    print(f"Input Only Number~\n{err}")
except IndexError as err:
    print(f"Out of range : Wrong index number\n{err}")
except ZeroDivisionError as err:
    try:
        pick = int(input(f"Input index (0 ~ {len(numbers) - 1}) : "))
        print(numbers[pick])
    except ValueError as err:
        print(f"Input Only Number~\n{err}")
    except IndexError as err:
        print(f"Out of range : Wrong index number\n{err}")
    except Exception:
        print(f"The denominator cannot be 0\n{err}")
except Exception:
    print("Error occurs")