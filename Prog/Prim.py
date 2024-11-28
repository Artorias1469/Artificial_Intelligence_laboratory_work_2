#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Рассмотрим реализацию алгоритма поиска в ширину на практике, в программном коде.

class Node:
    def __init__(self, state, parent=None):
        self.state = state
        self.parent = parent


class FIFOQueue:
    def __init__(self, initial=None):
        self.queue = initial or []

    def pop(self):
        return self.queue.pop(0) if self.queue else None

    def appendleft(self, item):
        self.queue.insert(0, item)

    def __bool__(self):
        return len(self.queue) > 0


def expand(problem, node):
    # Предполагается, что функция expand генерирует дочерние узлы для узла.
    # Это нужно реализовать в зависимости от вашего конкретного случая.
    pass


class Problem:
    def __init__(self, initial):
        self.initial = initial

    def is_goal(self, state):
        # Это условие определения цели нужно реализовать накладывая на вашу задачу.
        pass


failure = None  # или любое другое значение, которое вы хотите использовать для обозначения неудачи.


def breadth_first_search(problem):
    node = Node(problem.initial)
    if problem.is_goal(problem.initial):
        return node

    frontier = FIFOQueue([node])
    reached = {problem.initial}

    while frontier:
        node = frontier.pop()
        for child in expand(problem, node):
            s = child.state
            if problem.is_goal(s):
                return child
            if s not in reached:
                reached.add(s)
                frontier.appendleft(child)

    return failure