#!/usr/bin/env python
# encoding: utf-8

from abc import ABCMeta, abstractmethod
import itertools


class Zoo:
    def __init__(self, name):
        self.name = name
        self.animals = set()

    def add_animal(self, animal):
        if animal not in self.animals:
            self.animals.add(animal)


class Animal(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self, type_, feeding, size, disposition):
        self.type = type_
        self.feeding = feeding
        self.size = size
        self.disposition = disposition

    @property
    def is_ferocious(self):
        return self.feeding == '食肉' and self.size != '小型' and self.disposition == '性格凶猛'


class Cat(Animal):
    sound = '喵'

    def __init__(self, name, type_, feeding, size, disposition):
        super().__init__(type_, feeding, size, disposition)
        self.name = name

    @property
    def is_pet(self):
        return not self.is_ferocious

    def __str__(self):
        return f'{self.name}, {self.type}, {self.feeding}, {self.size}, {self.disposition}, {"凶猛动物" if self.is_ferocious else "温顺动物"}, {"适合作宠物" if self.is_pet else "不适合作宠物"}'


if __name__ == '__main__':
    try:
        Animal('猫', '食肉', '小型', '性格凶猛')
    except Exception as e:
        print(e)

    zoo = Zoo('geektime')

    types = ('大橘', '美短', '缅因')
    feedings = ('食肉', '杂食')
    sizes = ('小型', '中型', '大型')
    dispositions = ('性格温顺', '性格凶猛')

    for idx, cat in enumerate(itertools.product(types, feedings, sizes, dispositions)):
        zoo.add_animal(Cat(cat[0]+str(idx), *cat))

    for animal in zoo.animals:
        print(animal)

