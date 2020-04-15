class PyCharm:
    def excute(self):
        print("compile ")
        print("run")


class Intelij:
    def excute(self):
        print("spelling check")
        print("compile ")
        print("run")


class Programmer:
    def code(self, ide):  # ide argument should have execute method
        ide.excute()


p = Programmer()
p.code(PyCharm())
p.code(Intelij())