import sys
class BitsManipulation(object):
    def sum(self, a, b,):
      mask = 0xffffffff

    # in Python, every integer is associated with its two's complement and its sign.
    # However, doing bit operation "& mask" loses the track of sign.
    # Therefore, after the while loop, a is the two's complement of the final result as a 32-bit unsigned integer.
      while b != 0:
          print ("a = ", a, "bin(a)=", bin(a))
          print("b = " , b, "bin(b)=", bin(b))
          carry = a & b
          a= a ^ b & mask
          b = carry << 1 & mask
          print("carry = ",bin(carry))
      # print ("a = ", a, "bin(a)=", bin(a))
      # print("b = " , b, "bin(b)=", bin(b))
      # a = 16
      # b = ~a
      # c = (~a & 0xF)
      # print(c)
      # print(bin(a))
      # print(bin(b))
      # print(bin(c))
      # mask = 0xFFFFFFFF
      # mask2 = 0xFFF
      # print(mask)
      # print (mask2)
      # print(bin(mask2))
      # a=-15
      # print (bin(a))
      # b = a >> 31
      # print (bin (b))
      # print(b)
      # a=15
      # print (bin(a))
      # b = a >> 31
      # print (bin (b))
      # print(b)
      # print(mask)
      # print(bin(mask))


if __name__ == "__main__":
    x = BitsManipulation()
    x.sum(1,-1)