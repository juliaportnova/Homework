#№1
# С матрицами что-то не разобралась.
#№2
# from abc import ABC, abstractmethod
# class AbstractClothes(ABC):
#     @abstractmethod
#     def palto(self):
#         pass
#     @abstractmethod
#     def costume(self):
#         pass
#
# class Clothes(AbstractClothes):
#  def __init__(self,V,H):
#   self.V=V
#   self.H=H
#  @property
#  def palto(self):
#   return self.V/6.5+0.5
#  @property
#  def costume(self):
#   return self.H*2+0.3
# ex = Clothes(25,1.65)
# print(f'Для пальто необходимо {ex.palto:2f} м ткани')
# print(f'Для костюма необходимо {ex.costume:2f} м ткани')
#№3
# class Kletka:
#  def __init__(self,kolvo):
#   self.kolvo=int(kolvo)
#  def __add__(self,nov):
#   return self.kolvo + nov.kolvo
#  def __sub__(self,nov):
#   if self.kolvo > nov.kolvo:
#    return self.kolvo - nov.kolvo
#   else:
#    print('Операция не может быть выполнена')
#  def __mul__(self,nov):
#   return self.kolvo * nov.kolvo
#  def __truediv__(self, nov):
#   return self.kolvo // nov.kolvo
#  def make_order(self,kol_r):
#   r = ''
#   for i in range(int(self.kolvo / kol_r)):
#    r += f'{"*" * kol_r} \n'
#   r += f'{"*" * (self.kolvo % kol_r)}'
#   return r
#
# kl1 = Kletka(33)
# kl2 = Kletka(11)
# print(kl1)
# print(kl1 + kl2)
# print(kl1 - kl2)
# print(kl1 * kl2)
# print(kl1 / kl2)
# print(kl1.make_order(11))
# print(kl2.make_order(3))