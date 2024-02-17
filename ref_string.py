class GenRefString:
    
    def __init__(self, path) -> None:
        self.__trace_list = self.__load(path)
        self.__clean_trace_list = []

    def __load(self,path) -> list:
        with open(path) as trace_file:
            trace_list = trace_file.readlines()
            for i in range(len(trace_list)):
                trace_list[i] = trace_list[i].strip()
        
        return trace_list
    
    def __addres2page(self):
        for i in range(len(self.__trace_list)):
            if len(self.__trace_list[i]) <= 3:
                self.__trace_list[i] = 0
            else:
                self.__trace_list[i] = int(self.__trace_list[i][:-3], 16)

        return
    
    def __clean_rept(self):
        self.__clean_trace_list.append(self.__trace_list[0])
        previous_trace = self.__trace_list[0]

        for i in range(1, len(self.__trace_list)):
            if (self.__trace_list[i] != previous_trace):
                self.__clean_trace_list.append(self.__trace_list[i])
            previous_trace = self.__trace_list[i]
        
        return

    def gen_ref_string(self):
        self.__addres2page()
        self.__clean_rept()

        return self.__clean_trace_list
    
    def get__reduction(self):
        return 1- len(self.__clean_trace_list) / len(self.__trace_list)
    
    def get__sizes(self):
        return len(self.__clean_trace_list), len(self.__trace_list)
    
    def get__address(self):
        return self.__trace_list