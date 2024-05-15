import time
from colorama import Fore, Back, Style

start = time.time()

# Do something

end = time.time()

print(Fore.BLACK + f'Time spent: {end - start:.2f} seconds')
