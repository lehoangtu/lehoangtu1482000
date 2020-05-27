nhập  môn toán
đặt ra = [ 0 , 0 ]
trong khi  Đúng :
    s = đầu vào ()
    nếu  không  s :
        phá vỡ
    chuyển động =  s . chia ( "" )
    hướng = chuyển động [ 0 ]
    bước = int ( chuyển động [ 1 ])
    nếu  hướng == "LÊN" :
        pos [ 0 ] + = bước
     hướng elif == "XUỐNG" :
        pos [ 0 ] - = bước
     hướng elif == "TRÁI" :
        pos [ 1 ] - = bước
     hướng elif == "QUYỀN" :
        pos [ 1 ] + = bước
    khác :
        vượt qua
##############################
in ( int ( vòng ( toán học . sqrt ( pos [ 1 ] ** 2 + pos [ 0 ] ** 2 ))))
