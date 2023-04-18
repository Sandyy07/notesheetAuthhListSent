import React, { useEffect, useState } from 'react';
import Dashboard from "../Page/Dashboard/index.js";
// import Home from "./pages/Home";

const Home = (props) => {

let p;
    if(props.name) {
        // console.log(props.name)
        p=(
            
            <Dashboard/>
        )
    }
    else { 
        // console.log(props.name)
        p=(
            
            'Currently You are not Logged In'
        )
    }
    return (
       
        <div>
        
           {p}
           {/* {props.name ? <List/> : "Currently You are not Logged In"} */}
        </div>
        
        
       
    );
};

export default Home;