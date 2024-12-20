import React ,{useContext,useEffect,useState} from 'react'
import { AppContext } from '../App'


function Letter({ letterPos,attemptval }) {

    const { board , correctWord,currAttempt,disabledLetters,setDisabledLetters } = useContext(AppContext) ;
    const letter  = board[attemptval][letterPos];
    const correct = correctWord[letterPos] === letter;
    const almost = !correct && letter !== "" && correctWord.includes(letter);
    const color = () =>{
      if(correct){
        return "correct"
      }
      else if(almost){
        return "almost"
      }
      else{
        return "error"
      }
    }

    const [isBounced, setIsBounced] = useState(false);

  
  useEffect(() => {
    if (currAttempt.letterPos === letterPos+1 && currAttempt.attempt === attemptval) {
      setIsBounced(true); 
      setTimeout(() => setIsBounced(false), 400); 
    }
  }, [currAttempt.letterPos, letterPos]);

    const letterState = currAttempt.attempt > attemptval && color() ;
    useEffect(()=>{
      if(letter != "" && !correct && !almost ){
        setDisabledLetters((prev) => [...prev,letter]);
      }
    },[currAttempt.attempt]);
  return (
    <div className={`letter ${letterState} ${isBounced ? 'bounce' : ''}`}>
    {letter}
  </div>
  )
}

export default Letter
