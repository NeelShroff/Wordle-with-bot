import React, { useContext } from 'react'
import { AppContext } from '../App'

function Key({keyVal,bigKey,disabled}) {
    const { onEnter,onSelectLetter,onDelete } = useContext(AppContext)
    const selectLetter  = () =>{
      if(keyVal === "Enter"){
           onEnter()
        }
       else if(keyVal === "Delete") {
         onDelete()
       }
      else{
        onSelectLetter(keyVal)
    }
  };
  return (
    <div className='key' id={ bigKey ? "big" :disabled && "disabled" } onClick={selectLetter}>
        {keyVal}
    </div>
  )
}

export default Key