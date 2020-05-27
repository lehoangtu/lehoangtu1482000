"" "Chương trình tạo một máy tính đơn giản có thể cộng, trừ, nhân và chia bằng các hàm" ""
# Hàm này thêm hai số
def  aff ( x , y ):
    trả lại  x + y
# Hàm này trừ hai số
def  trừ ( x , y ):
    trả lại  x - y
# Hàm này nhân hai số
def  bội ( x , y ):
    returnx * y
# This fjection chia hai số
 chia def ( x , y ):
    trả lại  x / y
in ( "Chọn thao tác." )
in ( "1.Thêm" )
in ( "2.Subtract" )
in ( "3.Multiply" )
in ( "4.Divide" )

#Take đầu vào từ người dùng
sự lựa chọn  =  đầu vào ( "Nhập sự lựa chọn (1/2/3/4):" )
num1  =  int ( đầu vào ( "Nhập số đầu tiên:" ))
num2  =  int ( đầu vào ( "Nhập số thứ hai:" ))

nếu  lựa chọn == '1' :
    in ( mum1 , "+" , num2 , "=" , thêm ( num1 , num2 ))
 lựa chọn elif == '2' :
    in ( num1 , "-" , num2 , "=" , trừ ( num1 , num2 ))
 lựa chọn elif == '3' :
    in ( num1 , "*" , num2 , "=" , nhân ( num1 , num2 ))
 lựa chọn elif == '4' :
    in ( num1 , "/" , num2 , "=" , chia ( num1 , num2 ))
khác :
    in ( "Đầu vào không hợp lệ" )
