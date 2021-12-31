# import utils.length

# result = utils.length.get_length("Joseph")
# print("The length of the string is:", result)


# with terminal: $ export PYTHONPATH=$PYTHONPATH:$(pwd)/utls
# import length
# text = "Motherfucker"
# result_length = length.get_length(text)
# print("The length of the string is: ", result_length)


# import os
# import sys

# file_path = os.path.join(os.path.dirname(__file__), 'utils')
# sys.path.append(file_path)

# import length
# import upper
# import lower

# just_text = "Hello Motherfucker"

# res_len = length.get_length(just_text)
# print("The length of the string is: ", res_len)

# #        module_name.function or hopefully class also
# res_up = upper.to_upper(just_text)
# print("Uppercase test: ", res_up)

# res_low = lower.to_lower(just_text)
# print("Uppercase text: ", res_low)


# to understand with __init__.py
import utils

text = "Hello"
# res_len = utils.length.get_length(text)
# res_low = utils.lower.to_lower(text)
# res_up = utils.upper.to_upper(text)

# Now with the "BETTER CHOICE"
res_len = utils.get_length(text)
print(res_len)

res_up = utils.to_upper(text)
print(res_up)

res_low = utils.to_lower(text)
print(res_low)



