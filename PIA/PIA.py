
import cv2
import time
import mediapipe as mp

# Inicializar el detector de manos
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(static_image_mode=False, max_num_hands=1, min_detection_confidence=0.5)

# Inicializar el tablero
board = [[' ', ' ', ' '],
         [' ', ' ', ' '],
         [' ', ' ', ' ']]

# Variable para almacenar el turno actual
current_turn = 'X'


# Función para dibujar el tablero en el marco
def draw_board(image):
    height, width, _ = image.shape
    cell_width = width // 3
    cell_height = height // 3

    for i in range(1, 3):
        # Dibujar líneas horizontales
        cv2.line(image, (0, i * cell_height), (width, i * cell_height), (255, 0, 0), 2)

        # Dibujar líneas verticales
        cv2.line(image, (i * cell_width, 0), (i * cell_width, height), (255, 0, 0), 2)

    # Dibujar las "X" y "O" en el tablero
    for i in range(3):
        for j in range(3):
            if board[i][j] == 'X':
                cv2.putText(image, 'X', (j * cell_width + 30, i * cell_height + 60), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 2)
            elif board[i][j] == 'O':
                cv2.putText(image, 'O', (j * cell_width + 30, i * cell_height + 60), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 2)
            else:
                cv2.putText(image, ' ', (j * cell_width + 30, i * cell_height + 60), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 2)

# Función para actualizar el tablero con la posición detectada
def update_board(row, col, player):
    if row >= 0 and row < 3 and col >= 0 and col < 3:
        if board[row][col] == ' ':
            board[row][col] = player
            return True
        else:
            return False

# Función para cambiar el turno de los jugadores
def change_turn():
    global current_turn
    if current_turn == 'X':
        current_turn = 'O'
    else:
        current_turn = 'X'

# Función para reiniciar el juego
def restart_game():
    global current_turn
    current_turn = 'X'
    for i in range(3):
        for j in range(3):
            board[i][j] = ' '

# Función para verificar si hay un ganador
def check_winner():
    # Verificar filas
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != ' ':
            return True

    # Verificar columnas
    for j in range(3):
        if board[0][j] == board[1][j] == board[2][j] != ' ':
            return True

    # Verificar diagonales
    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return True
    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return True

    return False

# Función para verificar si el tablero está lleno
def check_full_board():
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                return False
    return True

# Inicializar la cámara
cap = cv2.VideoCapture(1)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Voltear el marco horizontalmente
    frame = cv2.flip(frame, 1)

    # Convertir el marco BGR a RGB
    image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Detección de manos
    results = hands.process(image)

    # Convertir el marco RGB de nuevo a BGR
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

    # Dibujar el tablero en el marco
    draw_board(image)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            for idx, landmark in enumerate(hand_landmarks.landmark):
                
                # Obtener la posición normalizada de los puntos de referencia de la mano
                x = int(landmark.x * image.shape[1])
                y = int(landmark.y * image.shape[0])

                # Calcular la celda correspondiente en el tablero
                row = y // (image.shape[0] // 3)
                col = x // (image.shape[1] // 3)
                
                # Obtener el índice y pulgar de la mano
                index_finger = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
                thumb = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]

                # Calcular la distancia entre el índice y el pulgar
                distance = ((index_finger.x - thumb.x) ** 2 + (index_finger.y - thumb.y) ** 2) ** 0.5

                # Actualizar el tablero solo si el dedo índice y pulgar se tocan
                if distance < 0.05:
                    is_touching = True
                    
                    # Actualizar el tablero con la posición seleccionada si es una casilla vacía y no se ha seleccionado ninguna otra casilla antes
                    if update_board(row, col, current_turn):
                        
                        # Verificar si hay un ganador
                        if check_winner():
                            print("¡Jugador", current_turn, "ha ganado!")
                            restart_game()
                        elif check_full_board():
                            print("El juego ha terminado en empate.")
                            restart_game()
                        else:
                            # Cambiar el turno
                            change_turn()


    cv2.imshow('Tic Tac Toe', image)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

