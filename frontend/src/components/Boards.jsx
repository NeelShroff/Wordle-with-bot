import React, { useState } from 'react'

import Letter from './Letter';

function Boards() {
  
  return (
    <div className='board'>
        <div className='row'>
          <Letter letterPos={0} attemptval={0}/>
          <Letter letterPos={1} attemptval={0}/>
          <Letter letterPos={2} attemptval={0}/>
          <Letter letterPos={3} attemptval={0}/>
          <Letter letterPos={4} attemptval={0}/>
        </div>
        <div className='row'> 
          <Letter letterPos={0} attemptval={1}/>
          <Letter letterPos={1} attemptval={1}/>
          <Letter letterPos={2} attemptval={1}/>
          <Letter letterPos={3} attemptval={1}/>
          <Letter letterPos={4} attemptval={1}/>
        </div>
        <div className='row'> 
          <Letter letterPos={0} attemptval={2}/>
          <Letter letterPos={1} attemptval={2}/>
          <Letter letterPos={2} attemptval={2}/>
          <Letter letterPos={3} attemptval={2}/>
          <Letter letterPos={4} attemptval={2}/>
        </div>
        <div className='row'> 
          <Letter letterPos={0} attemptval={3}/>
          <Letter letterPos={1} attemptval={3}/>
          <Letter letterPos={2} attemptval={3}/>
          <Letter letterPos={3} attemptval={3}/>
          <Letter letterPos={4} attemptval={3}/>
        </div>
        <div className='row'> 
          <Letter letterPos={0} attemptval={4}/>
          <Letter letterPos={1} attemptval={4}/>
          <Letter letterPos={2} attemptval={4}/>
          <Letter letterPos={3} attemptval={4}/>
          <Letter letterPos={4} attemptval={4}/>
        </div>
        <div className='row'> 
          <Letter letterPos={0} attemptval={5}/>
          <Letter letterPos={1} attemptval={5}/>
          <Letter letterPos={2} attemptval={5}/>
          <Letter letterPos={3} attemptval={5}/>
          <Letter letterPos={4} attemptval={5}/>
        </div>
    </div>
  );
}


export default Boards