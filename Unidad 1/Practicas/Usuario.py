class Usuario:
    def __init__(self,usuario,contraseña,rol,Nombre,CURP,ciudad) -> None:
        self._usuario = usuario
        self._contraseña = contraseña
        self._rol = rol
        self._Nombre = Nombre
        self.CURP = CURP
        self.ciudad = ciudad