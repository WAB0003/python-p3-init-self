#!/usr/bin/env python3
import ipdb

class Dog:
    def __init__(self,name, breed="Mutt"):
        self.name = name
        self.breed = breed
        print(f'{name} is born! They are a {breed}')
