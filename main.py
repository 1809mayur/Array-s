# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

class Computer:
    def __init__(self,processor,cores):
        self.processor = processor
        self.cores = cores#those variable which depends on instances(each object) (specific to their object) are instance variable.
        self.RAM = 16
    def config (self):#thoase variable which are independent from an instance(object) are class variable.
        return (self.processor,self.cores,self.RAM)

com1 = Computer("ryzen5","6cores")
first = Computer.config(com1)
sec = Computer("ryzen3","4cores").config()
print(com1)
print(sec)
print(first)
