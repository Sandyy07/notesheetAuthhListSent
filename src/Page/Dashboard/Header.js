import React from 'react'

function Header({ setIsCreating }){
    return (
        <header>
            <div>
                <button onClick={() => setIsCreating(true)} className='round-button'>Create Notesheet</button>
              
            </div>
            <h1>Recieved Notesheets</h1>
            
        </header>
    )
}

export default Header








