from PyQt5.QtWidgets import QGraphicsScene, QGraphicsRectItem, QGraphicsPathItem, QMessageBox
from PyQt5.QtGui import QBrush, QColor, QPen, QPainterPath
from PyQt5.QtCore import QObject, QTimer, QPropertyAnimation, QEasingCurve, QRectF, pyqtProperty, QPointF

class EventHandler(QObject):
    def __init__(self, main_window, dispenser_controller):
        super().__init__()
        self.main_window = main_window
        self.dispenser_controller = dispenser_controller
        self.scene = QGraphicsScene()
        self.main_window.candyDispenser.setScene(self.scene)
        
        # Set initial spring properties
        self._spring_y = 550  # Adjusted initial spring top position
        self.spring_height = 500  # Adjusted initial spring height
        self.spring_width = 150
        self.num_coils = 12
        
        self.candy_items = []
        self.spring_item = None
        self.container_item = None

        # Set container properties
        self.container_width = 300
        self.container_height = 450
        self.container_x = 100  # Centered horizontally
        self.container_y = 50

        self.setup_connections()
        self.update_dispenser_view()

    def setup_connections(self):
        # Connect UI buttons to their respective functions
        self.main_window.pushButton.clicked.connect(self.push_candy)
        self.main_window.popButton.clicked.connect(self.pop_candy)
        self.main_window.peekButton.clicked.connect(self.peek_candy)
        self.main_window.sizeButton.clicked.connect(self.check_size)
        self.main_window.ifEmptyButton.clicked.connect(self.check_if_empty)

    def push_candy(self):
        result = self.dispenser_controller.push()
        if isinstance(result, str):
            self.show_message("Error", result)
        else:
            self.animate_spring_down()
            self.show_message("Push", f"Added a {result.color} candy successfully")

    def pop_candy(self):
        result = self.dispenser_controller.pop()
        if isinstance(result, str):
            self.show_message("Error", result)
        else:
            self.animate_spring_up()
            self.show_message("Pop", f"Removed a {result.color} candy")

    def peek_candy(self):
        result = self.dispenser_controller.peek()
        if isinstance(result, str):
            self.show_message("Error", result)
        else:
            self.show_message("Peek", f"Top candy is {result.color}")

    def check_size(self):
        size = self.dispenser_controller.get_candy_count()
        self.show_message("Dispenser Size", f"The dispenser contains {size} candies")

    def check_if_empty(self):
        is_empty = self.dispenser_controller.is_dispenser_empty()
        status = "empty" if is_empty else "not empty"
        self.show_message("Dispenser Status", f"The dispenser is {status}")

    def show_message(self, title, message):
        QMessageBox.information(self.main_window, title, message)

    def update_dispenser_view(self):
        self.scene.clear()
        self.candy_items.clear()

        # Draw spring
        self.draw_spring()

        # Draw container
        self.draw_container()

        # Draw candies
        self.draw_candies()

    def draw_container(self):
        # Create a rounded rectangle for the candy container
        container = QPainterPath()
        container.addRoundedRect(QRectF(self.container_x, self.container_y, self.container_width, self.container_height), 30, 30)
        self.container_item = QGraphicsPathItem(container)
        self.container_item.setBrush(QBrush(QColor(200, 200, 200, 100)))
        self.scene.addItem(self.container_item)

    def draw_spring(self):
        path = QPainterPath()
        x = 250  # Center of the scene
        y = self._spring_y
        coil_height = self.spring_height / self.num_coils

        # Starting point (connect to the bottom of the container)
        path.moveTo(x, self.container_y + self.container_height - 5)  
        # Draw coils
        for i in range(self.num_coils):
            direction = -1 if i % 2 == 0 else 1
            path.cubicTo(
                x + direction * self.spring_width / 2, y + coil_height / 4,
                x + direction * self.spring_width / 2, y + coil_height * 3 / 4,
                x, y + coil_height
            )
            y += coil_height

        pen = QPen(QColor("gray"), 5)
        self.spring_item = self.scene.addPath(path, pen)

        
        bottom_line = QGraphicsPathItem()
        bottom_path = QPainterPath()
        bottom_path.moveTo(x, y)
        bottom_path.lineTo(x, 600)  
        bottom_line.setPath(bottom_path)
        bottom_line.setPen(pen)
        self.scene.addItem(bottom_line)

    def draw_candies(self):
        count = self.dispenser_controller.get_candy_count()
        candy_width = 60
        candy_height = 30
        for i in range(count):
            candy = self.dispenser_controller.candy_stack.items[i]
            x = self.container_x + (self.container_width - candy_width) / 2
            y = self.container_y + self.container_height - (i + 1) * (candy_height + 10)
            candy_item = QGraphicsRectItem(x, y, candy_width, candy_height)
            candy_item.setBrush(QBrush(QColor(candy.color)))
            self.scene.addItem(candy_item)
            self.candy_items.append(candy_item)

    def animate_spring_down(self):
        candy_count = self.dispenser_controller.get_candy_count()
        max_compression = 100  # Maximum compression in pixels
        compression = min(candy_count * 10, max_compression)  # 10 pixels per candy, up to max_compression
        target_y = min(550 + compression, 650)  # Start from 550 and compress downwards
        self.animate_spring(target_y)

    def animate_spring_up(self):
        candy_count = self.dispenser_controller.get_candy_count()
        max_compression = 100  # Maximum compression in pixels
        compression = min(candy_count * 10, max_compression)  # 10 pixels per candy, up to max_compression
        target_y = max(550, self._spring_y - 10)  # Move up by 10 pixels, but not above 550
        self.animate_spring(target_y)

    def animate_spring(self, target_y):
        self.spring_animation = QPropertyAnimation(self, b"spring_y")
        self.spring_animation.setStartValue(self._spring_y)
        self.spring_animation.setEndValue(target_y)
        self.spring_animation.setDuration(200)
        self.spring_animation.setEasingCurve(QEasingCurve.OutBounce)
        self.spring_animation.finished.connect(self.update_dispenser_view)
        self.spring_animation.start()

    def get_spring_y(self):
        return self._spring_y

    def set_spring_y(self, value):
        self._spring_y = value
        candy_count = self.dispenser_controller.get_candy_count()
        max_compression = 100
        compression = min(candy_count * 10, max_compression)
        self.spring_height = 500 - compression
        self.container_y = 50 + compression  # Adjust container position based on compression
        self.update_dispenser_view()

    spring_y = pyqtProperty(float, get_spring_y, set_spring_y)

