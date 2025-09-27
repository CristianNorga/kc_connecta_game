mi_juego/
├── main.py
├── game/
│   ├── engine.py          # Punto de arranque del bucle MVC
│   │
│   ├── models/
│   │   ├── player.py      # Clase Player
│   │   ├── oracle.py      # Clase Oracle
│   │   ├── linear_board.py   # Línea de fichas
│   │   └── square_board.py   # Tablero.
│   │
│   ├── views/
│   │   ├── terminal_view.py  # Renderizado en consola
│   │   ├── menu_view.py      # Menús y pantallas estáticas
│   │   └── input_handler.py     # Parsing de teclas / comandos
│   │
│   ├── controllers/
│   │   ├── game_controller.py   # Controlador principal
│   │   └── match_controller.py   # Controlador de partidas
│   │
│   └── utils/
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