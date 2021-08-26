import sys
import re

if __name__ == '__main__':
    # Compruebo si obtengo al menos un argumento a parte del propio porgrama.
    if len(sys.argv) < 2:
        sys.stderr.write('Error: falta el nombre del archivo con el texto a procesar\n')
        exit(1)

    # Obtengo el argumento que puede ser una IP o una URL
    ip_o_url = sys.argv[1]

    # Compruebo si es una dirección IP, si no es, entra en el if.
    if  re.search('^(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$',
                ip_o_url) == None:

        # Compruebo si es una URL, si no lo es, entra en el if.
        m = re.search('^https?:\/\/[\w\-]+(\.[\w\-]+)+[/#?]?.*$', ip_o_url)
        if  re.search('^https?:\/\/[\w\-]+(\.[\w\-]+)+[/#?]?.*$', ip_o_url) == None:

            # # Compruebo si es una URL en otro formato
            # p =re.search("^[\w~]+([-+.'][\w~]+)*", ip_o_url)
            # if re.search("[\w~]+([-+.'][\w~]+)*", ip_o_url) == None:
            #     sys.stderr.write("No corresponde a una ip/url válidas")
            #     # return False
            exit(0)
        print("url correcta")
        exit(0)
        # return True       # Si que es una URL válida.
    print("dirección ip correcta")
    exit(0)

#    jjjjjjjj  oooo       aaa      nnn    nn 
#       jj    oo  oo     aa aa     nn nn  nn
#       jj   oo    oo   aa   aa    nn  nn nn
#  jj   jj    oo  oo   aaaaaaaaa   nn   nnnn
#    jjjj      oooo   aa       aa  nn    nnn