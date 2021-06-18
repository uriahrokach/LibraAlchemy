import React, {useState} from 'react';
import { SearchList } from '../components/SearchComponents';

const Potion = (props) => {
    return (
        <div>
            <h3>{props.name}</h3>
            <h5>{props.technic}</h5>
            <p>{props.description}</p>
        </div>
    )
}

export {Potion};