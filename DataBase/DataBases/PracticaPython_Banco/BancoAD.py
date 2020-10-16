
class BancoAD:

    def capturar(self, datos):
        
        # 1. Abrir el archivo Clientes.txt
        archivoOut = open("Clientes.txt", "a")
        
        # 2. Almacenar los datos en el archivo
        archivoOut.write(datos+"\n")
        
        # 3. Cerrar el archivo
        archivoOut.close()
        
        return "Datos capturados: "+datos

    def consultar(self):
        # 1. Abrir el archivo para leer
        archivoIn = open("Clientes.txt","r")
        
        # 2. Leer los datos del archivo
        datos=""
        cliente = archivoIn.readline()
        while cliente != "":
            #datos = datos + cliente + "\n"
            datos = datos + cliente
            cliente = archivoIn.readline()
        
        # 3. Cerrar el archivo
        archivoIn.close()
        
        return datos

    def consultarTipo(self,tipo):
        # 1. Abrir el archivo
        archivoIn = open("Clientes.txt","r")

        # 2. Procesar datos del archivo
        datos = ""
        encontrado = False
        cta=""
        nom=""
        tcta=""
        saldo=""
        
        cliente = archivoIn.readline()
        while cliente != "":
            st    = cliente.split("_")
            cta   = st[0]
            nom   = st[1]
            tcta  = st[2]
            saldo = st[3]
            
            if tcta == tipo:
                datos = datos + cliente
                encontrado = True
        
            cliente = archivoIn.readline()
        
        # 3. Cerrar el archivo
        archivoIn.close
        
        #if encontrado == False:
        if (not encontrado):
            datos = "No se localizo el Tipo de cuenta "+tipo

        return datos

    def consultarCta(self,ncta):
        # 1. Abrir el archivo
        archivoIn = open("Clientes.txt","r")
        
        # 2. Procesar datos del archivo
        datos = ""
        encontrado = False
        cta=""
        nom=""
        tcta=""
        saldo=""
        
        cliente = archivoIn.readline()
        while (cliente != "" and not encontrado):
            st = cliente.split("_")
            cta = st[0]
            nom = st[1]
            tcta= st[2]
            saldo = st[3]
            
            if cta == ncta:
                datos = datos + cliente
                encontrado = True
            
            cliente = archivoIn.readline()
        
        # 3. Cerrar el archivo
        archivoIn.close
        
        #if encontrado == False:
        if (not encontrado):
            datos = "No se localizo el Cliente con Cuenta "+ncta
        
        return datos
