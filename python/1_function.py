#call by value
def func(input_string):
    input_string+="_test"
    print(f"inside function,input_string={input_string}; address={id(input_string)}")

print("********CALL BY VALUE*****")
input_string="input"
print(f"before function,input_string={input_string}; address={id(input_string)}")
func(input_string)

#NOTE: "input": actual parameter; variable which is passed:
#input_string: formal parameter; variable used inside function

#call by reference
def func(input_list):
    input_list+=["test"]
    print(f"inside function,input_string={input_list}; address={id(input_list)}")

print("********CALL BY REFERENCE*****")
input_list=[2,3,4]
print(f"before function,input_list={input_list}; address={id(input_list)}")
func(input_list) 

#ANSWER::

# ********CALL BY VALUE*****
# before function,input_string=input; address=2191863136304
# inside function,input_string=input_test; address=2191872299568
# ********CALL BY REFERENCE*****
# before function,input_list=[2, 3, 4]; address=2191863866752
# inside function,input_string=[2, 3, 4, 'test']; address=2191863866752