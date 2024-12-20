import React, { useContext } from 'react'
import { AppContext } from '../App'

function MachineGuessed() {
    const {botGuess} = useContext(AppContext)
  return (
    <div ><h2> Machine Guessed The Word : {botGuess}</h2></div>
  )
}

export default MachineGuessed