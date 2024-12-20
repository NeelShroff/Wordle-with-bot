import React, { useContext } from 'react'
import { AppContext } from '../App'

function GameOver() {
    
    const {gameOver,correctWord} = useContext(AppContext)
    const win = () =>{
        if(gameOver.wordGuessedByHuman && gameOver.wordGuessedByBot){
            
            return "Both Of You Gussed At The Same Attempt"
        }
        else if(gameOver.wordGuessedByHuman){
            
            return "You Won The Game"
        }
        else if( gameOver.wordGuessedByBot){
            
            return "Machine Won the Game "
        }
        else {
            return "None Of You Won"
        }
    }
  return (
    <div className='gameOver' id='text'>
        <h2>{win()}</h2>
        <h3>Correct Word :{correctWord}</h3>
    </div>
  )
}
export default GameOver