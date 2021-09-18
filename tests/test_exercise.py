import pytest
import src.perceptron


def test_perceptron1():
    assert src.perceptron.salida_neurona(
        [1, 3], [2, -4]) == 4.5397868702434395e-05


def test_perceptron2():
    assert src.perceptron.salida_neurona(
        [-1, 2], [-0.52, -.4]) == 0.43045377606077095


def test_perceptron3():
    assert src.perceptron.salida_neurona(
        [-1, 2], [-0.52, -.4, 1]) == "Error"
