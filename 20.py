Pascal  = [[ 1 ]]
num  =  int ( đầu vào ( "Nhap n:" ))
in ( Pascal [ 0 ])
cho  i  trong  phạm vi ( 1 , num + 1 ):
    Pascal . chắp thêm ([ 1 ])
    cho  j  trong  phạm vi ( len ( Pascal [ i - 1 ]) - 1 ):
        Pascal [ i ]. chắp thêm ( Pascal [ i - 1 ] [ j ] + Pascal [ i - 1 ] [ j + 1 ])
    Pascal [ i ]. nối ( 1 )
    in ( Pascal [ i ])
