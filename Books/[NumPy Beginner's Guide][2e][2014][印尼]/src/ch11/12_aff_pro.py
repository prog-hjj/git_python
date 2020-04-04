import numpy as np
import sklearn.cluster
import pygame, sys
from pygame.locals import *

positions = np.random.randint(0, 400, size=(30, 2))

# 欧氏距离（Euclidean distance）
positions_norms = np.sum(positions ** 2, axis=1)
S = - positions_norms[:, np.newaxis] - positions_norms[np.newaxis, :] + 2 * \
    np.dot(positions, positions.T)

# 为每一个数据点标记合适的聚类编号
aff_pro = sklearn.cluster.AffinityPropagation().fit(S)
labels = aff_pro.labels_

polygon_points = []

for i in range(max(labels) + 1):
    polygon_points.append([])

# 对数据点进行聚类
for i in range(len(labels)):
    polygon_points[labels[i]].append(positions[i])

pygame.init()
screen = pygame.display.set_mode((400, 400))

while True:
    for i in range(len(polygon_points)):
        # 为每一个聚类绘制多边形
        pygame.draw.polygon(screen, (255, 0, 0), polygon_points[i])

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
