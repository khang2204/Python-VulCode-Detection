def main():...
pygame.init()
screen_width = 1360
screen_height = 760
screen = pygame.display.set_mode((screen_width, screen_height))
screen.fill((0, 0, 0))
grid = Graph(34, 19)
visual_graph = GraphVisual(grid, 40, screen)
start_square = pygame.rect.Rect(3, 363, 36, 36)
goal_square = pygame.rect.Rect(1323, 363, 36, 36)
start_node = Node(Vector2(0, 9))
goal_node = Node(Vector2(33, 9))
astar = AStar(grid, start_node, goal_node)
drawn_path = []
path = []
dragging_start = False
dragging_goal = False
mouse_is_down = False
pressed_enter = False
while True:
screen.fill((0, 0, 0))
visual_graph = GraphVisual(grid, 40, screen)
for event in pygame.event.get():
if event.type == pygame.QUIT:
pygame.event.pump()
return
if event.type == pygame.MOUSEBUTTONDOWN:
pressed_enter = False
if event.type == pygame.MOUSEBUTTONUP:
if event.button == 1:
mouse_is_down = False
if event.type == pygame.MOUSEMOTION:
if start_square.collidepoint(event.pos):
if pygame.key.get_pressed()[pygame.K_RETURN]:
if event.button == 1:
if dragging_start:
dragging_start = True
if goal_square.collidepoint(event.pos):
pressed_enter = True
if pressed_enter:
count = 0
mouse_x, mouse_y = event.pos
if dragging_goal:
mouse_x, mouse_y = event.pos
dragging_goal = True
count = 0
if not path:
count = 0
pygame.draw.rect(screen, (0, 255, 0), start_square)
if dragging_start is True or dragging_goal is True:
start_square.x = mouse_x + offset_x
mouse_x, mouse_y = event.pos
if mouse_is_down:
offset_x = start_square.x - mouse_x
mouse_x, mouse_y = event.pos
for node in visual_graph.node_visual_colliders:
path = astar.find_path()
astar = AStar(grid, start_node, goal_node)
count_two = 1
pygame.draw.rect(screen, (255, 0, 0), goal_square)
for collider in visual_graph.node_visual_colliders:
start_square.y = mouse_y + offset_y
goal_square.x = mouse_x + offset_x
count = 0
offset_y = start_square.y - mouse_y
offset_x = goal_square.x - mouse_x
if node.collidepoint(event.pos) and mouse_is_down is False:
path = astar.find_path()
while count_two <= len(path) - 1:
count = 0
if start_square.colliderect(collider):
astar = AStar(grid, start_node, goal_node)
goal_square.y = mouse_y + offset_y
for node in visual_graph.node_visual_colliders:
offset_y = goal_square.y - mouse_y
current_state = grid.nodes[count].is_traversable
count += 1
line_start = Vector2(path[count].get_x() * 40, path[count].get_y() * 40)
for node in grid.nodes:
start_square.left = visual_graph.node_visual_colliders[count].left
if goal_square.colliderect(collider):
if node.collidepoint(event.pos) and grid.nodes[count
mouse_is_down = True
line_end = Vector2(path[count_two].get_x() * 40, path[count_two].get_y() * 40)
if node.is_traversable is False:
pygame.display.flip()
start_square.top = visual_graph.node_visual_colliders[count].top
goal_square.left = visual_graph.node_visual_colliders[count].left
count += 1
grid.nodes[count].toggle_state('wall')
count += 1
drawn_path.append(Line(screen, (0, 0, 255), Vector2(line_start.x_pos + 20, 
    line_start.y_pos + 20), Vector2(line_end.x_pos + 20, line_end.y_pos + 
    20), 5))
pygame.draw.rect(screen, (0, 0, 0), visual_graph.node_visual_colliders[count])
count += 1
dragging_start = False
goal_square.top = visual_graph.node_visual_colliders[count].top
count += 1
start_node = Node(Vector2(visual_graph.node_visuals[count].node.get_x(),
    visual_graph.node_visuals[count].node.get_y()))
dragging_goal = False
count_two += 1
goal_node = Node(Vector2(visual_graph.node_visuals[count].node.get_x(),
    visual_graph.node_visuals[count].node.get_y()))
