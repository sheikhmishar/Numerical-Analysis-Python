import matplotlib.pyplot as plt
import numpy as np

userinput = input("Enter a string: ")
binstring = (" ".join(f"{ord(i):08b}" for i in userinput))
binstream = binstring.replace(" ","")

print(f"Encoded Stream Divided in Octets:\n{binstring}")
print(f"Raw Data Stream:\n{binstream}")

def my_lines(axis, positions, *arguments, **kwarguments):
    if axis == 'x':
        for position in positions:
            plt.axvline(position, *arguments, **kwarguments)
    else:
        for position in positions:
            plt.axhline(position, *arguments, **kwarguments)

bitdata = np.array([int(i) for i in binstream]).repeat(2)
clockspeed = 1 - np.arange(len(bitdata)) % 2
manchester = np.logical_xor(clockspeed, bitdata)
timeinterval = 0.5 * np.arange(len(bitdata))

my_lines('x', range(len(binstream)), color = 'grey', linewidth = .5)
my_lines('y', [.5, 2, 4], color = 'grey', linewidth = .5)
plt.step(timeinterval, clockspeed + 4, 'r', linewidth = 1, where = 'post')
plt.step(timeinterval, bitdata + 2, 'g', linewidth = 1, where = 'post')
plt.step(timeinterval, manchester, 'b', linewidth = 1, where = 'post')
plt.ylim(-1, 6)

for timebit, bitchar in enumerate(binstream):
    plt.text(timebit + .25, 1.5, bitchar)

plt.title(f"Simulation of Raw Data Manipulation of Text : '{userinput}'")
plt.text(0, -.5, "Manchester")
plt.text(0, 3.5, "Clock")
plt.gca().axis('off')
plt.show()
