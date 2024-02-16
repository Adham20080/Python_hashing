import hashlib
from UserData import users_info


# 1

# for i in users_info.values():
#     b = hashlib.sha256(str(i["Password"]).encode("utf-8")).hexdigest()
#     print(b)

# 2

# def hashing_func(abcde: str):
#     sha256 = hashlib.sha256(str(abcde).encode("utf-8")).hexdigest()
#     print(sha256)
#
#
# hashing_func(input("Hashlash uchun ma'lumot kiriting: "))

# 3

# class Hashing:
#     def __init__(self, info_h: str):
#         self.ih = info_h
#
#     def with_open(self):
#         with open("user.txt", 'w') as f:
#             f.write(hashlib.sha256(str(self.ih).encode("utf-8")).hexdigest())
#
#
# obj = Hashing("Hello World")
# obj.with_open()
