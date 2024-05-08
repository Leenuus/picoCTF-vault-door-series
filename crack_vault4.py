#!/usr/bin/env python

def main():
    my_bytes = [106 , 85  , 53  , 116 , 95  , 52  , 95  , 98  ,
            0x55, 0x6e, 0x43, 0x68, 0x5f, 0x30, 0x66, 0x5f,
            0o142, 0o131, 0o164, 0o63 , 0o163, 0o137, 0o146, 0o64 ,
            'a' , '8' , 'c' , 'd' , '8' , 'f' , '7' , 'e' ,
                ]
    chars =  list(b if isinstance(b, str) else chr(b) for b in my_bytes)
    print(''.join(chars))


if __name__ == '__main__':
    main()
