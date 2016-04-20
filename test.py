

import times
try:
    A = times.Time(6,15,30,5)
    B = times.Time( 8, 9, 15, -4)
    C = times.Time( 14, 20, 25 )
    D = times.Time( 23, 59 )
    E = times.Time( 12 )
    F = times.Time( )
    G = times.Time(15)
except ValueError:
    print("The time you entered is in wrong format")
    
print()
print("A", str(A))
print("B", repr(B))
print("C", str(C))
print("D", repr(D))
print("E", str(E))
print("F", repr(F))
print("G", repr(G))
print(60 * "-")
print()

print("A: {}; A.get_as_local(): {}".format( A, A.get_as_local()))
print("B: {}; B.get_as_local(): {}".format( B, B.get_as_local()))
print("C: {}; C.get_as_local(): {}".format( C, C.get_as_local()))
print("D: {}; D.get_as_local(): {}".format( D, D.get_as_local()))
print("E: {}; E.get_as_local(): {}".format( E, E.get_as_local()))
print("F: {}; F.get_as_local(): {}".format( F, F.get_as_local()))
print("F: {}; F.get_as_local(): {}".format( G, G.get_as_local()))

print(60 * "-")
print()
try:
    T=times.Time()
    T.from_str("06:15:30+05")
    print("After T.from_str( '06:15:30+05' ), T is", T)
    T.from_str("06:79:30+05")
    print("After T.from_str( '06:79:30+05' ), T is", T)
except ValueError:
    print(T, "raised a ValueError")
print(60 * "-")
def display( arg1, arg2 ):
    try:
        print("T1, T2:", T1, ",", T2)
        print("T1 == T2 is ", T1 == T2)
        print("T1 != T2 is ", T1 != T2 )
        print("T1 < T2 is ", T1 < T2) 
        print("T1 <= T2 is ", T1 <= T2)
        print("T1 > T2 is ", T1 >T2) 
        print("T1 >= T2 is ", T1>= T2) 
        print(60 * "-")
        print()
    except TypeError:
        print(arg2, "raised a TypeError")
        
T1 = times.Time( 23, 15, 0, 5 )
print("T1", T1)
try:
    T2 = T1 + 300 
    print("T2 = T1 + 300", " ",T2)
    T3 = T1 + 3600
    print("T3 = T1 + 3600"," ", T3) 
    T4 = T1 + -90000
    print( "T4 = T1 + -90000"," ", T4)
except TypeError:
    print("second parameter not an int")
print(60 * "-")
print()

T1 = times.Time( 14, 20, 45 ) 
T2 = times.Time( 14, 18, 15 ) 
print("T1 , T2", T1, T2)
try:
    print("T1 – T2", T1 - T2) 
    print("T2 – T1", T2 - T1)
except TypeError:
    print("wrong time format")
print(60 * "-")
print()
 
T1 = times.Time( 7, 35, 15, -6 ) 
T2 = times.Time( 7, 21, 30, -5 ) 
print("T1 , T2", T1, T2)
try:
    print("T1 – T2", T1 - T2) 
    print("T2 – T1", T2 - T1)
except TypeError:
    print("wrong time format")
print(60 * "-")
def main():
    A = times.Time( 7, 35, 15, -6 )
    B = times.Time( 7, 21, 30, -5 )
    display( A, B )

main()