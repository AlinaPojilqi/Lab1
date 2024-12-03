import functools
from datetime import datetime
def performance_log(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f'{datetime.now().strftime("[%d.%m.%Y %H:%M:%S]")} Обновлён параметр {args[1]} на значение {args[2]}')
        return result
    return wrapper

class ComputerExtended:
    __slots__ = ['_cpu', '_ram', '_storage', '_gpu', '_vram', 'id']
    computer_count = 0
    def __init__(self, cpu, ram, storage, gpu, vram):
        self._cpu = cpu
        self._ram = ram
        self._storage = storage
        self._gpu = gpu
        self._vram = vram
        ComputerExtended.computer_count += 1
        self.id = f"PC_{ComputerExtended.computer_count}"
    @property    
    def cpu(self):
        return self._cpu
    @cpu.setter
    def cpu(self, value):
        if not isinstance(value, str):
            raise ValueError("CPU долженбыть строкой")
        self._cpu = value
    @property 
    def ram(self):
        return self._ram
    @ram.setter
    def ram(self, value):
        if not isinstance(value, int) or value <= 0:
            raise ValueError("RAM должен быть положительным целым числом")
        self._ram = value
    @property 
    def vram(self):
      return self._vram
    @vram.setter
    def vram(self, value):
        if not isinstance(value, int) or value <= 0:
          raise ValueError("VRAM должен быть положительным числом")
        self._vram = value
    @property 
    def storage(self):
        return self._storage
    @storage.setter
    def storage(self, value):
        if not isinstance(value, int) or value <= 0:
            raise ValueError("Объем хранилища должен быть положительным целым числом")
        self._storage = value
    @property 
    def gpu(self):
        return self._gpu
    @gpu.setter
    def gpu(self, value):
        if not isinstance(value, str):
            raise ValueError("GPU долженбыть строкой")
        self._gpu = value
    @performance_log    
    def upgrade_component(self, component, new_value):
        if component == 'cpu':
            self._cpu = new_value
        elif component == 'ram':
            self._ram = new_value
        elif component == 'storage':
            self._storage = new_value
        elif component == 'gpu':
            self._gpu = new_value
        elif component == 'vram':
            self._vram = new_value
        else:
            raise ValueError(f"Компонент {component} не существует.")
    @staticmethod
    def is_high_performance(computer):
         if not isinstance(computer, ComputerExtended):
            raise ValueError("Переданный объект не является экземпляром Computer.")
         return (computer._ram > 14 and computer._storage > 256 and computer._vram > 15)

    def __eq__(self, other):
        if not isinstance(other, ComputerExtended):
            raise ValueError("Нет такого компонента")
        return (self.cpu == other.cpu and self.ram == other.ram and self.storage == other.storage and self.gpu == other.gpu and self.vram == other.vram)
    def __str__(self):
        return f"Computer {self.id}: CPU: {self.cpu}, RAM: {self.ram}GB, Storage: {self.storage}GB, GPU: {self.gpu}"
    @property
    def total_memory(self):
        return self._ram + self._vram
    
computer1 = ComputerExtended('Intel i5', 16, 512, 'NVIDIA GTX 1650', 16)
print(computer1)
computer2 = ComputerExtended('Intel i7', 16, 1024, 'RADEON RX 580', 32)
print(computer2)
computer3 = ComputerExtended('Intel i5', 16, 512, 'NVIDIA GTX 1650', 16)
print(computer3)
print(f"Computer1 and computer2 same: {computer1.__eq__(computer2)}")
print(f"Computer1 and computer3 same: {computer1.__eq__(computer3)}")
print(f"compliance with {computer1.id} parameters: {ComputerExtended.is_high_performance(computer1)}")
print(f"ram + vram for Computer1: {computer1.total_memory}GB")
computer1.upgrade_component('ram','32')
print(f"upgrade {computer1}")






print("Hello")