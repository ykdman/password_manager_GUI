# # FileNotFound, KeyError
#
# try:
#     file = open("a_file.txt")  # FileNotFound, 개체 파일이 존재 하지 않을때 에러
#
#     a_dictionary = {"key": "value"}  # KeyError, 저장되지 않은 Key를 호출할때 에러
#     print(a_dictionary["key"])
# except FileNotFoundError:
#     file = open("a_file.txt", "w")
#     file.write("Something")
# except KeyError as error_message:  # Error Message 를 가져온다
#     print(f"The Key {error_message} does not exist.")
#     # The key 'asdasdas' does not exist.
# else:
#     content = file.read()
#     print(content)
# finally:
#     raise TypeError("This is an error that i made up")
#     raise KeyError
#     raise FileNotFoundError

height = float(input("Height:"))  # M 단위
weight = int(input("Weight:"))

if height > 3:
    raise ValueError("Human Height should not be 3 Meters")

bmi = weight / height ** 2  # 체중 / 키의 제곱

print(bmi)