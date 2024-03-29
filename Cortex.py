from enum import Enum


class LayerType(Enum):
    INPUT = 1
    HIDDEN = 2
    OUTPUT = 3


class NeuronType(Enum):
    Sigmoid = 1
