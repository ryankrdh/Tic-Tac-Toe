let playerText = document.getElementById('playerText');
let restartBtn = document.getElementById('restartBtn');
let boxes = Array.from(document.getElementsByClassName('box'));

let winnerIndicator = getComputedStyle(document.body).getPropertyValue(
  'winning-blocks'
);

const O_TEXT = 'O';
const X_TEXT = 'X';
const HUMAN_PLAYER = X_TEXT;
const AI_PLAYER = O_TEXT;

let currentPlayer = HUMAN_PLAYER;
let spaces = Array(9).fill(null);

const startGame = () => {
  boxes.forEach((box) => box.addEventListener('click', boxClicked));
};

function boxClicked(e) {
  const id = e.target.id;

  if (!spaces[id] && currentPlayer === HUMAN_PLAYER) {
    spaces[id] = currentPlayer;
    // e.target.innerText = currentPlayer;
    e.target.innerHTML =
      '<img src="assets/melo.png" alt="AI player" style= "width: 60px; height: 60px">';
    if (playerHasWon(currentPlayer)) {
      playerText.innerHTML = `Melo(You) Win!`;
      highlightWinningCombination(getWinningCombination(currentPlayer));
    } else if (checkTie()) {
      playerText.innerHTML = "It's a Tie!";
    } else {
      currentPlayer = AI_PLAYER;
      makeAIMove();
    }
  }
}

function checkTie() {
  return spaces.every((cell) => cell !== null);
}

function makeAIMove() {
  let bestMove = findBestMove();
  spaces[bestMove] = AI_PLAYER;

  boxes[bestMove].innerHTML =
    '<img src="assets/boba.png" alt="AI player" style= "width: 60px; height: 60px">';
  //   boxes[bestMove].innerText = AI_PLAYER;

  if (playerHasWon(AI_PLAYER)) {
    playerText.innerHTML = `Boba(AI) Wins!`;
    highlightWinningCombination(getWinningCombination(AI_PLAYER));
  } else if (checkTie()) {
    playerText.innerHTML = "It's a Tie!";
  } else {
    currentPlayer = HUMAN_PLAYER;
  }
}

// AI using minimax algorithm

function findBestMove() {
  let bestScore = -Infinity;
  let bestMove = null;

  for (let i = 0; i < spaces.length; i++) {
    if (!spaces[i]) {
      spaces[i] = AI_PLAYER;
      let score = minimax(spaces, 0, false);
      spaces[i] = null;

      if (score > bestScore) {
        bestScore = score;
        bestMove = i;
      }
    }
  }

  return bestMove;
}

function minimax(board, depth, isMaximizing) {
  if (playerHasWon(AI_PLAYER)) return 10 - depth;
  if (playerHasWon(HUMAN_PLAYER)) return depth - 10;
  if (checkTie()) return 0;

  if (isMaximizing) {
    let bestScore = -Infinity;
    for (let i = 0; i < board.length; i++) {
      if (!board[i]) {
        board[i] = AI_PLAYER;
        let score = minimax(board, depth + 1, false);
        board[i] = null;
        bestScore = Math.max(bestScore, score);
      }
    }
    return bestScore;
  } else {
    let bestScore = Infinity;
    for (let i = 0; i < board.length; i++) {
      if (!board[i]) {
        board[i] = HUMAN_PLAYER;
        let score = minimax(board, depth + 1, true);
        board[i] = null;
        bestScore = Math.min(bestScore, score);
      }
    }
    return bestScore;
  }
}

function playerHasWon(player) {
  for (const combination of getWinningCombination(player)) {
    const [a, b, c] = combination;
    if (spaces[a] === player && spaces[b] === player && spaces[c] === player) {
      return true;
    }
  }
  return false;
}

function getWinningCombination(player) {
  const winningCombinations = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6],
  ];
  return winningCombinations.filter((combination) =>
    combination.every((index) => spaces[index] === player)
  );
}

function highlightWinningCombination(winningCombination) {
  const [a, b, c] = winningCombination[0];
  [a, b, c].forEach(
    (index) => (boxes[index].style.backgroundColor = winnerIndicator)
  );
}

restartBtn.addEventListener('click', () => {
  spaces.fill(null);
  boxes.forEach((box) => {
    box.innerText = '';
    box.style.backgroundColor = '';
  });
  playerText.innerHTML = 'Tic Tac Toe';
  currentPlayer = HUMAN_PLAYER;
});

startGame();
