import './App.css'
import Boards from './components/Boards'
import Keyboard from './components/Keyboard'
import { boardDefault } from './Words'
import { createContext, useEffect, useState } from 'react';
import axios from "axios";
import GameOver from './components/GameOver';


export const AppContext = createContext();

function App() {
   const [board, setBoard] = useState(boardDefault);
   const [currAttempt, setCurrAttempt] = useState({ attempt: 0, letterPos: 0 });
   const [disabledLetters, setDisabledLetters] = useState([]);
   const [botGuess, setBotGuess] = useState("");
   const [correctWord, setCorrectWord] = useState("");
   const [gameOver, setGameOver] = useState({ gameOver: false, wordGuessedByHuman: false, wordGuessedByBot: false });

   const [currWord, setCurrWord] = useState(""); 

   const onSelectLetter = (keyVal) => {
     if (currAttempt.letterPos > 4) return;
     const newBoard = [...board];
     newBoard[currAttempt.attempt][currAttempt.letterPos] = keyVal;
     setBoard(newBoard);
     setCurrAttempt({ ...currAttempt, letterPos: currAttempt.letterPos + 1 });
   }

   const onDelete = () => {
     if (currAttempt.letterPos === 0) return;
     const newBoard = [...board];
     newBoard[currAttempt.attempt][currAttempt.letterPos - 1] = "";
     setBoard(newBoard);
     setCurrAttempt({ ...currAttempt, letterPos: currAttempt.letterPos - 1 });
   }

   const handleSubmit = async (currWord) => {
    try {
      const response = await axios.post(
        "http://127.0.0.1:5000/validate_word",
        {
          word: currWord, 
        },
        {
          headers: {
            "Content-Type": "application/json", 
          },
        }
      );
      const { exists_in_list } = response.data;
      return exists_in_list;
    } catch (error) {
      console.error("Error submitting the word", error);
      return false;
    }
  };

  const GetMachineGuess = async () => {
    try {
      const response = await axios.get("http://127.0.0.1:5000/machine_guess");
      const { bot_guess } = response.data;
      console.log("Bot's Guess:", bot_guess); 
      setBotGuess(bot_guess.toUpperCase())
    } catch (error) {
      console.error("Error fetching machine guess:", error);
      alert("Something Went Wrong");
    }
  };

  const GetWord = async () => {
    try {
      const response = await axios.get("http://127.0.0.1:5000/word");
      const { wordle_guess } = response.data;
      console.log("wordle word:", wordle_guess); 
      setCorrectWord(wordle_guess.toUpperCase());
    } catch (error) {
      console.error("Error fetching machine guess:", error);
      alert("Something Went Wrong");
    }
  }

  useEffect(() => {
    GetWord()
  }, []);

  const onEnter = async () => {
    if (currAttempt.letterPos !== 5) return;

    let word = "";
    for (let i = 0; i < 5; i++) {
      word += board[currAttempt.attempt][i];
    }
    setCurrWord(word);
    const word_present = await handleSubmit(word.toLowerCase());

    if (word_present) {
      setCurrAttempt({ attempt: currAttempt.attempt + 1, letterPos: 0 });
      await GetMachineGuess();
    } else {
      alert("Word Not Found");
    }

    if (currAttempt.attempt === 5) {
      setGameOver({ gameOver: true, wordGuessedByHuman: false, wordGuessedByBot: false });
      return;
    }
  };

  
  useEffect(() => {
    if (botGuess && correctWord && currWord) {
      if (botGuess === correctWord && currWord === correctWord) {
        setGameOver({ gameOver: true, wordGuessedByHuman: true, wordGuessedByBot: true });
        return;
      } else if (currWord === correctWord) {
        setGameOver({ gameOver: true, wordGuessedByHuman: true, wordGuessedByBot: false });
        return;
      } else if (botGuess === correctWord) {
        setGameOver({ gameOver: true, wordGuessedByHuman: false, wordGuessedByBot: true });
        return;
      }
    }
  }, [botGuess, correctWord, currWord]);

  return (
    <div className='App'>
      <div>
        <nav>
          <h1>Wordle</h1>
        </nav>
      </div>
      <div className='game'>
        <AppContext.Provider value={{
          board,
          setBoard,
          currAttempt,
          setCurrAttempt,
          onSelectLetter,
          onDelete,
          onEnter,
          correctWord,
          setCorrectWord,
          disabledLetters,
          setDisabledLetters,
          botGuess,
          gameOver,
          setGameOver
        }}>
          <Boards />
          {gameOver.gameOver ? <GameOver /> : <Keyboard />}
        </AppContext.Provider>
      </div>
    </div>
  );
}

export default App;
