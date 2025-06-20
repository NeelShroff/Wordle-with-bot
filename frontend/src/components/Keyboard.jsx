import React, { useEffect,useContext, useCallback } from 'react'
import Key from './Key';
import { AppContext } from '../App'
import MachineGuessed from './MachineGuessed';

function Keyboard() {
  const keys1 = ["Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P"];
  const keys2 = ["A", "S", "D", "F", "G", "H", "J", "K", "L"];
  const keys3 = ["Z", "X", "C", "V", "B", "N", "M"];
  const {onEnter,onSelectLetter,onDelete,disabledLetters} = useContext(AppContext)

  const handleKeyboard = useCallback(
    (event) => {
    if (event.key === "Enter") {
      onEnter();
    } else if (event.key === "Backspace") {
      onDelete();
    } else {
      keys1.forEach((key) => {
        if (event.key.toLowerCase() === key.toLowerCase()) {
          onSelectLetter(key);
        }
      });
      keys2.forEach((key) => {
        if (event.key.toLowerCase() === key.toLowerCase()) {
          onSelectLetter(key);
        }
      });
      keys3.forEach((key) => {
        if (event.key.toLowerCase() === key.toLowerCase()) {
          onSelectLetter(key);
        }
  })
}});
useEffect(() => {
  document.addEventListener("keydown", handleKeyboard);

  return () => {
    document.removeEventListener("keydown", handleKeyboard);
  };
}, [handleKeyboard]);
 

  return (
    <div className='keyboard' >
      <div className='bot'id='h22'>
        <MachineGuessed/>
      </div >
      <div>
      <div className='line1'> 
        {keys1.map((key) => {
          return <Key keyVal={key} disabled={disabledLetters.includes(key)}/>
        })}
      </div>
      <div className='line2'> 
        {keys2.map((key) => {
          return <Key keyVal={key} disabled={disabledLetters.includes(key)} />
        })}
      </div>
      <div className='line3'> 
      <Key keyVal={"Enter"} bigKey/>
        {keys3.map((key) => {
          
          return <Key keyVal={key} disabled={disabledLetters.includes(key)}/>
        })}
      <Key keyVal={"Delete"} bigKey/>
      </div>
    </div>
    </div>
  );
}

export default Keyboard