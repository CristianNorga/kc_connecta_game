mi_juego/
├── main.py
├── game/
│   ├── __init__.py
│   ├── engine.py          # Punto de arranque del bucle MVC
│   │
│   ├── models/
│   │   ├── __init__.py
│   │   ├── player.py      # Clase Player
│   │   ├── oracle.py      # Clase Oracle
│   │   ├── linear_board.py   # Línea de fichas
│   │   └── square_board.py   # Tablero.
│   │
│   ├── views/
│   │   ├── __init__.py
│   │   ├── terminal_view.py  # Renderizado en consola
│   │   ├── menu_view.py      # Menús y pantallas estáticas
│   │   └── input_handler.py     # Parsing de teclas / comandos
│   │
│   ├── controllers/
│   │   ├── __init__.py
│   │   ├── game_controller.py   # Controlador principal
│   │   └── match_controller.py   # Controlador de partidas
│   │
│   └── utils/
│       ├── __init__.py
│       ├── constants.py
│       └── helpers.py
│
├── data/
│   ├── maps/
│   ├── texts/
│   └── settings.py
├── assets/
│   └── sounds/
└── tests/