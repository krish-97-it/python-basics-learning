#   void - dont have any return type
def dollarToRupee(amount):
    conversion_rate     =   82.62  #    1 Us dollar = 82.62 as per current date
    converted_result    =   amount*conversion_rate
    print("(by void function call)",amount," dollar = ",converted_result," in Indian rupees.")
    

#   non-void - should have a return type
def returnDollarToRupee(amount):
    conversion_rate     =   82.62  #    1 Us dollar = 82.62 as per current date
    return amount*conversion_rate

#main body
dollar_input    =   float(input("Enter dollar: "))
void_fn = dollarToRupee(dollar_input)     #   void form
print (void_fn)
get_res         =   returnDollarToRupee(dollar_input)  #    non-void form
print(get_res)
print("(by non-void function call)",dollar_input," dollar = ",get_res," in Indian rupees.")

