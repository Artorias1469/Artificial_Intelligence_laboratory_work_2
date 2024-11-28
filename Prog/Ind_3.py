#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from collections import deque

class Node:
    def __init__(self, state, parent=None):
        self.state = state  # текущий город/узел
        self.parent = parent  # предыдущий узел в пути

    def path(self):
        # Восстанавливает путь, идя от конечного узла к начальному
        node, path_back = self, []
        while node:
            path_back.append(node.state)
            node = node.parent
        return path_back[::-1]  # Путь в прямом порядке

class FIFOQueue:
    def __init__(self, initial=None):
        self.queue = deque(initial) if initial else deque()

    def pop(self):
        return self.queue.popleft() if self.queue else None

    def appendleft(self, item):
        self.queue.append(item)

    def __bool__(self):
        return len(self.queue) > 0

def expand(graph, node):
    """Генерирует дочерние узлы для текущего узла."""
    for neighbor, _ in graph.get(node.state, []):
        yield Node(neighbor, node)

class Problem:
    def __init__(self, initial, goal):
        self.initial = initial
        self.goal = goal

    def is_goal(self, state):
        return state == self.goal

failure = None  # Значение для обозначения неудачи

def breadth_first_search(problem, graph):
    node = Node(problem.initial)
    if problem.is_goal(node.state):
        return node.path(), 0  # Если начальная точка уже является целью

    frontier = FIFOQueue([node])
    reached = {problem.initial: 0}  # Хранит минимальные расстояния до узлов

    while frontier:
        node = frontier.pop()
        current_distance = reached[node.state]

        for child in expand(graph, node):
            s = child.state
            if problem.is_goal(s):
                # Вычисление общей стоимости пути
                total_distance = current_distance + next(weight for neighbor, weight in graph[node.state] if neighbor == s)
                return child.path(), total_distance

            # Добавляем в очередь только непосещенные или если найден более короткий путь
            if s not in reached:
                edge_weight = next(weight for neighbor, weight in graph[node.state] if neighbor == s)
                reached[s] = current_distance + edge_weight
                frontier.appendleft(child)

    return failure, float('inf')  # если пути не существует

# Пример использования
if __name__ == "__main__":
    # Граф представлен в виде списка смежности
    graph = {
        1: [(2, 219), (3, 488), (4, 314), (5, 462)],
        2: [(1, 219), (6, 287), (7, 365)],
        3: [(1, 488), (4, 334), (8, 226), (9, 217)],
        4: [(1, 314), (3, 334), (5, 192)],
        5: [(1, 462), (4, 192), (8, 424)],
        6: [(2, 287), (10, 354)],
        7: [(2, 365), (11, 214), (12, 354), (9, 219)],
        8: [(3, 226), (5, 424), (14, 291)],
        9: [(3, 217), (7, 219), (15, 211), (16, 222), (20, 460), (14, 360)],
        10: [(6, 354), (11, 124)],
        11: [(7, 214), (10, 124), (12, 146)],
        12: [(7, 354), (11, 146), (13, 153)],
        13: [(12, 153), (19, 188), (20, 192)],
        14: [(8, 291), (9, 360), (15, 164), (16, 148), (17, 68)],
        15: [(9, 211), (14, 164)],
        16: [(9, 222), (14, 148), (17, 110)],
        17: [(14, 68), (16, 110), (18, 381)],
        18: [(17, 381), (20, 148)],
        19: [(13, 188), (20, 112)],
        20: [(9, 460), (13, 192), (18, 148), (19, 112)],
        21: [(16, 344)],
    }

    # Задача: найти кратчайший путь от узла 1 до узла 14
    start = 1
    goal = 11
    problem = Problem(start, goal)
    path, distance = breadth_first_search(problem, graph)
    print("Кратчайший путь:", path)
    print("Длина пути:", distance)

