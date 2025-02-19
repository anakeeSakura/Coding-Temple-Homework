# Chapter 2.3: The Pass Statement:
''' Pass statement does nothing but serves as a place holder for code. It's no operation statement no action 
is desired or nessary. You can use the pass statement 
to avoid syntex errors and keeps your code running smoothly.'''

# Example 1. The unfinished Function

def to_be_define():
    pass
to_be_defined() # No Output and no error

# Example 2. the silent Exception Handler

try: 
    x = 1 / 0
except ZeroDivisionError:
    pass
print("The script continues!")


# Example 3. The Placeholder Loop

for i in range(5):
    #0, 1, 2, 3, 4
    pass
print("Loop completed!")


# Example 4. The Yet-To-Be- Defined Class

class FutureImplementation:
    def method_one(self):
        pass
    def methon_two(self):
        pass
obj= FutureImplementation()
obj.method_one() # No output and no error


# Example 5. The conditional Placeholder

Value = 10
if Value > 5:
  pass  #Will implement this later
else:
    print("Value is not greater than 5.")