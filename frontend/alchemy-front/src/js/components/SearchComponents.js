import React, { useState } from 'react';
// import '../../css/Report.css';
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

class SearchBar extends React.Component {

    constructor(props) {
        super(props);
        this.items = this.props.items;
        this.state = {
            suggestions: this.props.items,
            buffer: '',
        }
    }

    onSearch = (e) => {
        const value = e.target.value;
        let suggestions = [];
        if (!this.items.includes(value) || this.props.emptyOnClick) {
            suggestions = this.items.filter(keyphrase => keyphrase.includes(value)); 
        }
        this.setState(() => ({ suggestions, buffer: value }))
    }

    clickItem = (value) => {
        this.setState(() => ({
            buffer: '' ? this.props.emptyOnClick : value,
            suggestions: []
        }));
    }

    renderSuggestions() {
        const { suggestions } = this.state;
        if (suggestions.length === 0) {
            return null;
        }

        return (
            <ul>
                {suggestions.map((item) => <li onClick={() => {
                    this.clickItem(item);
                    if(this.props.onclick) {
                        this.props.onclick(item);
                    }
                }}>{item}</li>)}
            </ul>
        )
    }

    render() {
        return (
            <div>
                <input value={ this.state.buffer } onChange={this.onSearch} className="input" type="text"/>
                <div className='search-box'>
                    {this.renderSuggestions()}
                </div>
            </div>
        );
    }
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
                    <div>
                        <input
                        type='checkbox'
                        id={`checkbox-${item}`}
                        onClick={() => props.setResults(item)}/>
                        <label for={`checkbox-${item}`} >{item}</label>
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
                    <div>
                        <input type='radio' value={item} name={props.name}/> {item}
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
            }} className="input" type="text"/>
        </div>
    )
}

class SearchList extends React.Component {
    constructor(props) {
        super(props);
    }

    addItem(item) {
        if (!this.props.items.includes(item)){
            this.props.setItems([...this.props.items, item]);
        }
    }
    
    removeItem(item) {
        if (this.props.items.includes(item)){
            const newItems = this.props.items.filter(key => key !== item);
            this.props.setItems(newItems);
        }
    }

    render() {
        return (
            <div>
                <LabeledElement label={this.props.label}>
                        <SearchBar items={this.props.choices} onclick={this.addItem.bind(this) } emptyOnClick={true}/>
                </LabeledElement>
                {this.props.children}
            </div>
        )
    }
}

const DisplayFilter = (props) => {
    const filteredItems = props.data.filter(this.props.filter);
    return (<div>{filteredItems.map(props.display)}</div>);
}

export {LabeledElement, SearchBar, NameTagList, DynamicMultipleChoice, DynamicRadioList, ListBarController, SearchList, DisplayFilter, InputController}