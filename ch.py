import torch 
print(torch.__version__) 
print(torch.cuda.is_available())

# # import logging as lg
# from dataclasses import dataclass


# @dataclass
# class Bauwerk:
#     x: float = 0.0
#     y: float = 0.0
#     z: float = 0.0
#     btype: str = 'h'

#     def __str__(self):
#         if self.btype == 'h':
#             out = f'Haus\n {self.x= }\n {self.y= }'
#         elif self.btype == 'w':
#             out = f'Windrad\n {self.x= }\n {self.y= }\n {self.z= }'
#         else:
#             out = "?"
#         out = out.replace('self', 'k')
#         return out


# h = Bauwerk(1, 2, 3, 'w')

# bauwerke = []
# # bauwerke = list([Bauwerk(1, 2, 3), Bauwerk(7, 8, 9)])
# # bauwerke.append(h)
# # for h in bauwerke:
# #     print(h)

# bauwerke.append(Bauwerk(1, 2, 3, 'w'))
# bauwerke.append(h)
# bauwerke.append(Bauwerk(7, 8, 9, 'h'))
# for h in bauwerke:
#     print(h)

# list1 = ["uu", "jjkk", "uoo"]
# list2 = ["uk", "ölkk", "pppo", "222"]

# list3 = list1 + list2
# print(list3)