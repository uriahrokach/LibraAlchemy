import React, { useState } from 'react';
// import '../../css/Report.css';

import '../../css/PotionComps.css'
import {ReactComponent as TrashIcon} from '../../icons/trash.svg';

const LabeledElement = (props) => {
    return (
        <div className="field">
            <label className="label">{props.label}</label>
            <br />
            <br />
            <div className="inputWrapper">
                {props.children}
            </div>
        </div>
    )
}

const NameTagList = (props) => {
    const [hover, setHover] = useState(false);

    return (
        <div>
            <ul className='name-tag'>
                {props.items.map((item) => 
                <li 
                    onMouseEnter={() => setHover(item)}
                    onMouseLeave={() => setHover('')}>
                        {item}
                        {hover == item && <TrashIcon className="trash-icon" onClick={() => props.onclick(item)}/>}
                </li>
                )}
            </ul>
        </div>
    )
}

const DynamicMultipleChoice = (props) => {
    return(
        <div>
            {props.choices.map(item => {
                return (
                    <div className='checkbox'>
                        <label>
                            <input type='checkbox' onClick={() => props.setResults(item)} checked={props.results.includes(item)}/> 
                            {`  ${item}`}
                        </label>
                    </div>
                )}
            )}
        </div>
    );
}

const DynamicRadioList = (props) => {
    return(
        <div onChange={(e) => props.setResults(e.target.value)}>
            {props.choices.map((item) => {
                return (
                    <div className='checkbox'>
                        <input type='radio' value={item} name={props.name} checked={props.result == item}/> {item}
                    </div>
                )
            })}
        </div>
    );
}

const ListBarController = (props) => {
    return (
        <div>
            <input 
            onChange={e => {
                const value = e.target.value;
                const newItems = props.items.filter(keyphrase => keyphrase.includes(value))
                props.setChoices(newItems); 
            }} className="input" type="text"/>
        </div>
    )
}

const InputController = (props) => {
    return (
        <div>
            <input 
            onChange={e => {
                props.setValue(e.target.value); 
            }} className="input" type="text" placeholder={props.placeholder ? props.placeholder : ''}/>
        </div>
    )
}

const TextAreaController = (props) => {
    return (
        <div>
            <textarea 
            onChange={e => {
                props.setValue(e.target.value); 
            }} className="text-area" cols="50" rows="3" placeholder={props.placeholder ? props.placeholder : ''}/>
        </div>
    )
}

const DisplayFilter = (props) => {
    const filteredItems = props.data.filter(this.props.filter);
    return (<div>{filteredItems.map(props.display)}</div>);
}

export {LabeledElement, NameTagList, DynamicMultipleChoice, DynamicRadioList, ListBarController, DisplayFilter, InputController, TextAreaController}