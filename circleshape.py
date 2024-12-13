import pygame

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # print(f"Initializing CircleShape for {self.__class__.__name__}")

        # we will be using this later
        if hasattr(self, "containers"):
            # print(f"Found containers: {self.containers}")
            super().__init__(self.containers)
        else:
            # print("No containers found")
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # sub-classes must override
        pass

    def update(self, dt):
        # sub-classes must override
        pass

    def is_colliding_with(self, circleshape):
        obj_distance = pygame.math.Vector2.distance_to(
            self.position,
            circleshape.position
        )
        return obj_distance <= self.radius + circleshape.radius
